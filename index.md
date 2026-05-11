---
layout: default
title: NCAR Information
---
<style>
  .home-header {
    margin-bottom: 2.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 3px solid #2c2c2c;
  }

  .home-header h1 {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 2rem;
    font-weight: bold;
    margin: 0 0 0.4rem;
  }

  .home-header p {
    color: #555;
    font-size: 1rem;
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
  }

  .home-nav {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.25rem;
  }

  @media (max-width: 560px) {
    .home-nav { grid-template-columns: 1fr; }
  }

  .home-nav-card {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 1.75rem 1.5rem;
    background: #fff;
    border: 1px solid #e0ddd9;
    border-radius: 10px;
    text-decoration: none;
    color: #1a1a1a;
    box-shadow: 0 1px 4px rgba(0,0,0,0.07);
    transition: background 0.15s, box-shadow 0.15s;
    min-height: 160px;
  }

  .home-nav-card:hover {
    background: #f0ede8;
    box-shadow: 0 3px 10px rgba(0,0,0,0.1);
  }

  .home-nav-card-title {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 1.3rem;
    font-weight: bold;
    margin: 0 0 0.5rem;
  }

  .home-nav-card-desc {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 0.9rem;
    color: #666;
    margin: 0;
    line-height: 1.4;
  }

  .home-nav-card-arrow {
    font-size: 1.4rem;
    color: #aaa;
    margin-top: 1.25rem;
    align-self: flex-end;
  }
</style>

<div class="home-header">
  <h1>NCAR Information</h1>
  <p>Staff and volunteer reference</p>
</div>

<nav class="home-nav">
  <a href="{{ '/protocols/' | relative_url }}" class="home-nav-card">
    <div>
      <div class="home-nav-card-title">Dog Protocols</div>
      <p class="home-nav-card-desc">Handling protocols for dog fights, loose dogs, vet visits, behaviour assessments and more.</p>
    </div>
    <span class="home-nav-card-arrow">&#8594;</span>
  </a>
  <a href="{{ '/dogs/' | relative_url }}" class="home-nav-card">
    <div>
      <div class="home-nav-card-title">Dogs for Adoption</div>
      <p class="home-nav-card-desc">Quick reference for all current dogs — breed, age, sex and key notes.</p>
    </div>
    <span class="home-nav-card-arrow">&#8594;</span>
  </a>
</nav>
