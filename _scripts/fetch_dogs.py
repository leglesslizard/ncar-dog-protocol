#!/usr/bin/env python3
"""
Scrapes current dogs for adoption from ncar.org.uk and saves to _data/dogs.json.
Run via GitHub Actions on a daily schedule, or manually.
"""
import json
import os
import sys
import time

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://ncar.org.uk"
ARCHIVE_URL = f"{BASE_URL}/animal_categories/dogs/"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; NCARStaffTool/1.0)"}
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "_data", "dogs.json")


def get_soup(url):
    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def get_archive_dogs():
    """Return list of {name, url} dicts from all paginated archive pages."""
    dogs = []
    page = 1

    while True:
        url = ARCHIVE_URL if page == 1 else f"{ARCHIVE_URL}page/{page}/"
        print(f"  Archive page {page}: {url}")

        try:
            soup = get_soup(url)
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                break
            raise

        articles = soup.find_all("article")
        if not articles:
            break

        for article in articles:
            link = article.find("a", class_="kt-imageoverlay-link")
            name_el = article.find("h2", class_="image-overlay-title")
            if link and link.get("href") and name_el:
                dogs.append({
                    "name": name_el.get_text(strip=True),
                    "url": link["href"],
                })

        next_link = soup.find("a", class_="next")
        if not next_link:
            break

        page += 1
        time.sleep(0.5)

    return dogs


def parse_dog_page(url):
    """Return detailed dog info from an individual dog page."""
    soup = get_soup(url)

    # Image — first kt-img-overlay on the page
    image = None
    img = soup.find("img", class_="kt-img-overlay")
    if img and img.get("src"):
        image = img["src"]

    # Status — paragraph styled with the palette accent colour class
    status = None
    status_p = soup.find("p", class_="has-palette-color-1-color")
    if status_p:
        status = status_p.get_text(strip=True).title()

    # Age, Sex, Breed — located by their <strong> label
    age = sex = breed = None
    for p in soup.find_all("p"):
        strong = p.find("strong")
        if not strong:
            continue
        label = strong.get_text(strip=True).rstrip(":")
        value = p.get_text(strip=True)
        value = value[len(strong.get_text(strip=True)):].lstrip(":").strip()
        if label == "Age":
            age = value
        elif label == "Sex":
            sex = value
        elif label == "Breed":
            breed = value

    # Notes — all kb-dynamic-list-item elements (covers positive and negative lists)
    notes = []
    for li in soup.find_all("li", class_="kb-dynamic-list-item"):
        text = li.get_text(strip=True)
        if text:
            notes.append(text)

    return {
        "image": image,
        "status": status,
        "age": age,
        "sex": sex,
        "breed": breed,
        "notes": notes,
    }


def main():
    print("Fetching archive pages...")
    dogs = get_archive_dogs()
    print(f"Found {len(dogs)} dogs\n")

    for i, dog in enumerate(dogs):
        print(f"[{i + 1}/{len(dogs)}] {dog['name']} — {dog['url']}")
        try:
            details = parse_dog_page(dog["url"])
            dog.update(details)
        except Exception as e:
            print(f"  Error fetching dog page: {e}", file=sys.stderr)
            dog.update({
                "image": None,
                "status": None,
                "age": None,
                "sex": None,
                "breed": None,
                "notes": [],
            })
        time.sleep(0.5)

    output = os.path.normpath(OUTPUT_PATH)
    with open(output, "w", encoding="utf-8") as f:
        json.dump(dogs, f, indent=2, ensure_ascii=False)

    print(f"\nSaved {len(dogs)} dogs to {output}")


if __name__ == "__main__":
    main()
