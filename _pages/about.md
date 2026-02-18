---
permalink: /
title: "Hello, I'm Minhyuk!"
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<div class="intro-section">
  <p class="intro-title"> I'm a Ph.D. student at UIUC Mechanical Science and Engineering, passionate about all kinds of robotics and learning-based control. I bring an interdisciplinary background in AI and mechanical engineering, grounded in strong mathematics in control theory and hands-on hardware experience that gives me system-level insight. I believe researchers who understand the full system architecture can make the greatest impact! <a href="/files/minhyukjang_CV.pdf" target="_blank" class="cv-link">[CV]</a>
</p>

  <h3>🔬 Research Interests</h3>
  <div class="research-pills">
    <span class="research-pill">Learning-Based Control</span>
    <span class="research-pill">Robotics</span>
    <span class="research-pill">AI Safety</span>
    <span class="research-pill">Multi-Agent Systems</span>
  </div>
</div>

<div class="content-section">
  <h2 class="section-title">
    <span class="section-icon">🎓</span>
    Education
  </h2>
  <div class="education-list">
    <div class="edu-entry">
      <img src="/images/illinois_logo.png" alt="UIUC" class="edu-logo">
      <div class="edu-body">
        <div class="edu-degree">Ph.D. student in Mechanical Science and Engineering</div>
        <div class="edu-detail"><strong>University of Illinois Urbana-Champaign (UIUC), Aug 2025 – Present · GPA: 4.0 / 4.0</strong></div>
        <div class="edu-detail"><a href="https://naira.mechse.illinois.edu/">Advanced Controls Research Laboratory</a> · Advisor: Prof. Naira Hovakimyan</div>
      </div>
    </div>
    <div class="edu-entry">
      <img src="/images/SNU.svg" alt="SNU" class="edu-logo">
      <div class="edu-body">
        <div class="edu-degree">B.S. in Mechanical Engineering, Interdisciplinary Major in AI</div>
        <div class="edu-detail"><strong>Seoul National University, 2025 · GPA: 3.99 / 4.0</strong></div>
        <div class="edu-detail">College of Engineering Outstanding Graduate Award</div>
      </div>
    </div>
  </div>
</div>

<div class="content-section">
  <h2 class="section-title">
    <span class="section-icon">📄</span>
    Publications
  </h2>
  <div class="publications-list">
    <div class="publication-item">
      <h4 class="paper-title">Distributionally Robust Kalman Filter</h4>
      <p class="paper-authors"><em>Minhyuk Jang</em>*, Astghik Hakobyan*, and Insoon Yang · <span class="paper-note">* Equal contribution</span></p>
      <a href="https://arxiv.org/abs/2512.06286" target="_blank" class="paper-link">arXiv</a>
    </div>

    <div class="publication-item">
      <h4 class="paper-title">On the Steady-State Distributionally Robust Kalman Filter</h4>
      <p class="paper-authors"><em>Minhyuk Jang</em>*, Astghik Hakobyan*, and Insoon Yang · <span class="paper-note">* Equal contribution</span></p>
      <p class="paper-venue">IEEE Control and Decision Conference 2025</p>
      <a href="https://arxiv.org/abs/2503.23742" target="_blank" class="paper-link">arXiv</a>
    </div>

    <div class="publication-item">
      <h4 class="paper-title">Wasserstein Distributionally Robust Control and State Estimation for Partially Observable Linear Systems</h4>
      <p class="paper-authors"><em>Minhyuk Jang</em>, Astghik Hakobyan, and Insoon Yang</p>
      <a href="https://arxiv.org/abs/2406.01723" target="_blank" class="paper-link">arXiv</a>
    </div>

    <div class="publication-item">
      <h4 class="paper-title">Stability Analysis of Disturbance Observer under Model Uncertainty with Different System Degrees between True and Nominal Systems</h4>
      <p class="paper-authors"><em>Minhyuk Jang</em></p>
      <p class="paper-venue">Institute of Control, Robotics and Systems (ICROS), 2024</p>
    </div>
  </div>
</div>

<div class="content-section">
  <h2 class="section-title">
    <span class="section-icon">🛠️</span>
    Projects
  </h2>
  <div class="project-grid">
    {% assign sorted_projects = site.portfolio | sort: 'order' %}
    {% for project in sorted_projects %}
      {% assign img_count = project.preview_images | size %}
      {% if img_count == 4 %}
        {% assign span_class = "project-card project-card--span2" %}
      {% elsif img_count == 2 %}
        {% assign span_class = "project-card project-card--span2" %}
      {% else %}
        {% assign span_class = "project-card" %}
      {% endif %}
      <div class="{{ span_class }}">
        <a href="{{ project.url }}" class="project-card__link">
          <h3 class="project-card__title">{{ project.title }}</h3>
        </a>
        {% if img_count == 4 %}
          <div class="project-card__images project-card__images--grid4">
            {% for img in project.preview_images %}
              <div class="project-card__img-wrap project-card__img-wrap--small">
                <img src="{{ img }}" alt="{{ project.title }}" loading="lazy">
              </div>
            {% endfor %}
          </div>
        {% elsif img_count == 2 %}
          <div class="project-card__images project-card__images--side">
            {% for img in project.preview_images %}
              <div class="project-card__img-wrap">
                <img src="{{ img }}" alt="{{ project.title }}" loading="lazy">
              </div>
            {% endfor %}
          </div>
        {% elsif img_count == 1 %}
          <div class="project-card__images project-card__images--single">
            <div class="project-card__img-wrap">
              <img src="{{ project.preview_images[0] }}" alt="{{ project.title }}" loading="lazy">
            </div>
          </div>
        {% endif %}
        <p class="project-card__excerpt">{{ project.excerpt }}</p>
      </div>
    {% endfor %}
  </div>
</div>

<div class="content-section">
  <h2 class="section-title">
    <span class="section-icon">🚁</span>
    Beyond Research: FPV Piloting
  </h2>
  <div class="fpv-section">
    <div class="video-container">
      <iframe src="https://www.youtube.com/embed/WPttdZw-E_8?si=gXVi6KftqGTxxWPf" title="FPV Flight Video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
  </div>
</div>

<style>
  /* Clean, minimal styling */
  .intro-section {
    margin-bottom: 40px;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
  }

  .intro-title {
    font-size: 1.3em;
    font-weight: 600;
    color: #333;
    margin-bottom: 15px;
    line-height: 1.4;
  }
  .cv-link {
    color: #2c3e50;
    text-decoration: underline;
    font-weight: 600;
  }
  .cv-link:hover {
    color: #34495e;
  }

  .intro-section p {
    font-size: 1.1em;
    color: #666;
    line-height: 1.6;
    margin-bottom: 10px;
  }

  .intro-section h3 {
    font-size: 1.3em;
    font-weight: 600;
    color: #333;
    margin: 25px 0 15px 0;
  }

  .research-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }
  .research-pill {
    display: inline-block;
    padding: 6px 16px;
    background: #f0f4f8;
    border: 1px solid #d0d7de;
    border-radius: 20px;
    font-size: 0.95em;
    font-weight: 600;
    color: #2c3e50;
  }

  /* Content sections */
  .content-section {
    margin: 50px auto;
    max-width: 800px;
  }

  .section-title {
    font-size: 1.6em;
    font-weight: 600;
    color: #333;
    margin-bottom: 25px;
    padding-bottom: 8px;
    border-bottom: 2px solid #ddd;
  }

  .section-icon {
    margin-right: 10px;
  }

  /* Education */
  .education-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .edu-entry {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 10px 16px;
    border-left: 4px solid #2c3e50;
    background: #fafbfc;
    border-radius: 0 4px 4px 0;
  }
  .edu-logo {
    width: 44px;
    height: 44px;
    object-fit: contain;
    flex-shrink: 0;
  }
  .edu-body {
    flex: 1;
    min-width: 0;
  }
  .edu-degree {
    font-size: 1.05em;
    font-weight: 600;
    color: #333;
    margin-bottom: 4px;
  }
  .edu-detail {
    font-size: 0.95em;
    color: #666;
    line-height: 1.5;
  }
  .edu-detail a {
    color: #2c3e50;
  }

  /* Publications */
  .publications-list {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .publication-item {
    padding: 10px 16px;
    border-left: 4px solid #2c3e50;
    background: #fafbfc;
    border-radius: 0 4px 4px 0;
  }

  .paper-title {
    font-size: 1em;
    font-weight: 600;
    color: #333;
    margin: 0 0 3px 0;
    line-height: 1.3;
  }

  .paper-authors {
    font-size: 0.9em;
    color: #666;
    margin-bottom: 3px;
  }

  .paper-venue {
    font-size: 0.85em;
    font-weight: 500;
    color: #888;
    margin-bottom: 4px;
  }

  .paper-links {
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }

  .paper-link {
    color: #333;
    text-decoration: none;
    padding: 4px 8px;
    border: 1px solid #ddd;
    border-radius: 3px;
    font-size: 0.9em;
    transition: background-color 0.3s ease;
  }

  .paper-link:hover {
    background-color: #f5f5f5;
    color: #333;
  }

  .paper-note {
    font-size: 0.9em;
    color: #999;
    font-style: italic;
  }

  /* ── Project Grid ── */
  .project-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-auto-flow: dense;
    gap: 20px;
  }

  .project-card {
    grid-column: span 1;
    border: 2px solid #ddd;
    border-radius: 6px;
    padding: 14px;
    transition: box-shadow 0.2s ease;
  }
  .project-card:hover {
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
  }

  .project-card--span2 {
    grid-column: span 2;
  }

  .project-card__link {
    text-decoration: none;
    color: inherit;
  }
  .project-card__title {
    font-size: 1.2em;
    font-weight: 600;
    color: #2c3e50;
    margin: 0 0 10px 0;
    line-height: 1.3;
  }
  .project-card__link:hover .project-card__title {
    color: #34495e;
    text-decoration: underline;
  }

  .project-card__excerpt {
    font-size: 0.9em;
    color: #777;
    margin: 8px 0 0 0;
    line-height: 1.4;
  }

  /* Image containers */
  .project-card__images--single .project-card__img-wrap,
  .project-card__images--side .project-card__img-wrap {
    background: #f5f6f7;
    border-radius: 4px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 220px;
  }

  .project-card__images--single {
    display: block;
  }

  .project-card__images--side {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }

  .project-card__images--grid4 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 8px;
  }
  .project-card__images--grid4 .project-card__img-wrap,
  .project-card__images--grid4 .project-card__img-wrap--small {
    background: #f5f6f7;
    border-radius: 4px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 180px;
  }

  .project-card__img-wrap img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  /* Simple FPV section */
  .fpv-section {
    text-align: center;
  }

  .video-container {
    position: relative;
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
    padding-bottom: 56.25%;
    height: 0;
    border-radius: 4px;
    overflow: hidden;
  }

  .video-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }

  /* Responsive */
  @media (max-width: 768px) {
    .intro-section h2 {
      font-size: 1.5em;
    }

    .section-title {
      font-size: 1.4em;
    }

    .project-grid {
      grid-template-columns: 1fr;
    }
    .project-card,
    .project-card--span2 {
      grid-column: span 1;
    }
    .project-card__images--single .project-card__img-wrap,
    .project-card__images--side .project-card__img-wrap {
      height: 200px;
    }
    .project-card__images--side {
      grid-template-columns: 1fr;
    }
    .project-card__images--grid4 {
      grid-template-columns: 1fr;
      grid-template-rows: auto;
    }
    .project-card__images--grid4 .project-card__img-wrap,
    .project-card__images--grid4 .project-card__img-wrap--small {
      height: 160px;
    }

    .video-container {
      max-width: 100%;
    }
  }
</style>
