---
layout: default
title: NCAR Dog Protocols
---
<style>
  .index-header {
    margin-bottom: 2.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 3px solid #2c2c2c;
  }

  .index-header h1 {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 2rem;
    font-weight: bold;
    margin: 0 0 0.5rem;
  }

  .index-header p {
    color: #555;
    font-size: 1rem;
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
  }

  .protocol-list {
    list-style: none;
    padding: 0;
    margin: 0;
    counter-reset: protocol-counter;
  }

  .protocol-list li {
    counter-increment: protocol-counter;
    border-bottom: 1px solid #ddd;
  }

  .protocol-list li:first-child {
    border-top: 1px solid #ddd;
  }

  .protocol-list a {
    display: flex;
    align-items: center;
    gap: 1.25rem;
    padding: 1.25rem 0.5rem;
    text-decoration: none;
    color: #1a1a1a;
    transition: background 0.15s;
  }

  .protocol-list a:hover {
    background: #f0ede8;
  }

  .protocol-list a::before {
    content: counter(protocol-counter);
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 2.25rem;
    height: 2.25rem;
    background: #2c2c2c;
    color: #fff;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 0.95rem;
    font-weight: bold;
    border-radius: 50%;
    flex-shrink: 0;
  }

  .protocol-list .title {
    font-family: Arial, Helvetica, sans-serif;
    font-weight: bold;
    font-size: 1.1rem;
  }

  .dogs-nav {
    margin-top: 2rem;
    border-top: 1px solid #ddd;
    padding-top: 1.5rem;
  }

  .dogs-nav-label {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 0.75rem;
    font-weight: bold;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #888;
    margin: 0 0 0.75rem;
  }

  .dogs-nav-link {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 1rem 1rem 1rem 1.25rem;
    background: #fff;
    border: 1px solid #e0ddd9;
    border-radius: 8px;
    text-decoration: none;
    color: #1a1a1a;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    transition: background 0.15s;
  }

  .dogs-nav-link:hover {
    background: #f0ede8;
  }

  .dogs-nav-link .title {
    font-family: Arial, Helvetica, sans-serif;
    font-weight: bold;
    font-size: 1.1rem;
  }

  .dogs-nav-link .subtitle {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 0.85rem;
    color: #777;
    margin-top: 0.15rem;
  }

  .dogs-nav-link .arrow {
    font-size: 1.25rem;
    color: #aaa;
    flex-shrink: 0;
  }
</style>

<div class="index-header">
  <h1>Dog Protocols</h1>
  <p>Staff and volunteer handling protocols</p>
</div>

<ul class="protocol-list">
  {% assign posts = site.posts | sort: 'order' %}
  {% for post in posts %}
    <li>
      <a href="{{ post.url | relative_url }}">
        <span class="title">{{ post.title }}</span>
      </a>
    </li>
  {% endfor %}
</ul>

<div class="dogs-nav">
  <p class="dogs-nav-label">Quick Reference</p>
  <a href="{{ '/dogs/' | relative_url }}" class="dogs-nav-link">
    <div>
      <div class="title">Dogs for Adoption</div>
      <div class="subtitle">Breed, age, sex and notes for all current dogs</div>
    </div>
    <span class="arrow">&#8594;</span>
  </a>
</div>
