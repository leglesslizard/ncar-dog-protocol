---
layout: default
title: Dog Protocols
permalink: /protocols/
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

  .back-link {
    display: inline-block;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 0.875rem;
    color: #555;
    text-decoration: none;
    margin-bottom: 1.5rem;
  }

  .back-link:hover { color: #1a1a1a; }

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
</style>

<a class="back-link" href="{{ '/' | relative_url }}">&#8592; Home</a>

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
