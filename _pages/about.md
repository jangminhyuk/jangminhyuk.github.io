---
layout: research-site
permalink: /
title: "Minhyuk Jang"
excerpt: "Robotics, learning-based control, and safe autonomy. Ph.D. student at the University of Illinois Urbana-Champaign."
redirect_from:
  - /about/
  - /about.html
---
<section class="intro" aria-labelledby="intro-title">
  <div class="intro-copy">
    <h1 id="intro-title">Minhyuk Jang<span class="name-period">.</span></h1>
    <p class="intro-bio">My research is in robotics, with a focus on robust state estimation, learning-based control, and safe motion planning. I work with Prof. Naira Hovakimyan at the <a href="https://naira.mechse.illinois.edu/">Advanced Controls Research Laboratory</a>.</p>
    <div class="education-brief" aria-label="Education">
      <div><strong>University of Illinois Urbana-Champaign</strong><p>Ph.D. student, Mechanical Science & Engineering · 2025–present <span class="gpa">GPA: 4.0 / 4.0</span></p></div>
      <div><strong>Seoul National University</strong><p>B.S., Artificial Intelligence & Mechanical Engineering · 2025 <span class="gpa">GPA: 3.99 / 4.0</span></p><p class="education-awards">College of Engineering Outstanding Graduate Award<br>Outstanding B.S. Thesis Presentation Award</p></div>
    </div>
    <div class="intro-actions">
      <a class="text-link intro-cv" href="{{ '/files/Minhyuk_Jang_CV.pdf' | relative_url }}">View CV <span aria-hidden="true">↗</span></a>
      <div class="contact-links"><a href="mailto:{{ site.author.email }}">Email <span aria-hidden="true">↗</span></a><a href="{{ site.author.googlescholar }}">Google Scholar <span aria-hidden="true">↗</span></a><a href="https://github.com/{{ site.author.github }}">GitHub <span aria-hidden="true">↗</span></a><a href="https://www.linkedin.com/in/{{ site.author.linkedin }}/">LinkedIn <span aria-hidden="true">↗</span></a></div>
    </div>
  </div>
  <figure class="portrait"><img src="{{ '/images/minhyuk-jang.jpg' | relative_url }}" alt="Minhyuk Jang" width="960" height="960" fetchpriority="high"></figure>
</section>

<section id="projects" class="research-section" aria-labelledby="projects-title">
  <span id="research" class="section-anchor" aria-hidden="true"></span>
  <div class="section-heading"><h2 id="projects-title">Research & Projects</h2><div class="section-actions"><button type="button" class="motion-toggle" hidden aria-pressed="false">Pause videos</button><a class="text-link" href="#publications">All publications <span aria-hidden="true">↓</span></a></div></div>
  <p class="section-intro">Research papers, robot systems, and experiments.</p>
  {% include project-browser.html grid_id="home-project-grid" grid_class="engineering-grid--featured" show_gallery=true %}
</section>

<section id="publications" class="section-block" aria-labelledby="publications-title">
  <div class="section-heading"><h2 id="publications-title">Publications</h2><a class="text-link" href="{{ '/publications/' | relative_url }}">Full citations <span aria-hidden="true">↗</span></a></div>
  <div class="publication-list--compact">
    {% for paper in site.data.research %}
    <article class="publication-compact">
      <div>
        <h3><a href="{{ paper.project | relative_url }}">{{ paper.title }}</a></h3>
        <p class="authors">{{ paper.authors | replace: 'Minhyuk Jang', '<strong>Minhyuk Jang</strong>' }}</p>
        <p class="venue">{{ paper.venue }}</p>
      </div>
      {% if paper.paper %}<a class="publication-paper" href="{{ paper.paper }}" aria-label="Read {{ paper.title | escape }}">{% if paper.paper contains 'arxiv.org' %}arXiv{% else %}Paper{% endif %} <span aria-hidden="true">↗</span></a>{% endif %}
    </article>
    {% endfor %}
  </div>
  <p class="publication-note small-note">* Equal contribution</p>
</section>

<section id="background" class="section-block background-section" aria-labelledby="background-title">
  <div class="section-heading"><h2 id="background-title">Experience & service</h2><a class="text-link" href="{{ '/files/Minhyuk_Jang_CV.pdf' | relative_url }}">Full CV <span aria-hidden="true">↗</span></a></div>
  <div class="background-grid">
    <div><h3>Research</h3><div class="background-entry"><span class="entry-date">2025 — Present</span><h4>Advanced Controls Research Laboratory</h4><p>Research Assistant · UIUC</p></div><div class="background-entry"><span class="entry-date">2023 — 2025</span><h4>Learning and Decision Systems Lab</h4><p>Research Intern · Seoul National University</p></div><div class="background-entry"><span class="entry-date">2024</span><h4>NEARTHLAB</h4><p>Aerospace Engineering Intern · GNC Team</p></div></div>
    <div><h3>Teaching & service</h3><div class="background-entry"><span class="entry-date">Spring & Fall 2026</span><h4>TAM 210/211 — Statics</h4><p>Teaching Assistant · UIUC</p></div><div class="background-entry"><h4>Reviewer</h4><p>IEEE Transactions on Signal Processing<br>IEEE Transactions on Control of Network Systems</p></div><div class="background-entry"><span class="entry-date">2023 — 2025</span><h4>Bulnabi — SNU Drone Club</h4><p>Team Leader · Quadrotor build/fly seminars<br>Korea Robot Aircraft Competition · Grand Award, 2024</p></div></div>
  </div>
</section>
<section class="fpv-section" aria-labelledby="fpv-title">
  <div class="section-heading"><h2 id="fpv-title">FPV flying</h2><a class="text-link" href="https://www.youtube.com/watch?v=WPttdZw-E_8">YouTube <span aria-hidden="true">↗</span></a></div>
  <iframe src="https://www.youtube-nocookie.com/embed/WPttdZw-E_8" title="FPV flight in Jeongseon, July 2025" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</section>
