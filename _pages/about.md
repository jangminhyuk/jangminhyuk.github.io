---
permalink: /
title: "Hello, I'm Minhyuk!"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<div class="hero-section">
  <div class="hero-content">
    <div class="hero-text">
      <h2>PhD Student in Mechanical Science & Engineering</h2>
      <p class="affiliation">University of Illinois Urbana-Champaign | <a href="https://naira.mechse.illinois.edu/" target="_blank">Advanced Controls Research Lab</a></p>
      <p class="background">I earned my bachelor's degree in Mechanical Engineering and Artificial Intelligence at Seoul National University.</p>
    </div>
    <div class="research-highlights">
      <h3>Research Focus</h3>
      <div class="research-grid">
        <div class="research-item">
          <div class="research-icon">⚙️</div>
          <span><strong>Control Theory</strong><br>Robust, Optimal, Adaptive, Learning-Based Control</span>
        </div>
        <div class="research-item">
          <div class="research-icon">🛡️</div>
          <span><strong>Safety-Critical Systems</strong><br>Multirotor, VTOL, Robotics</span>
        </div>
        <div class="research-item">
          <div class="research-icon">🤝</div>
          <span><strong>Multi-agent Systems</strong><br>Distributed Control & Coordination</span>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="cta-section">
  <a href="https://jangminhyuk.github.io/portfolio/" target="_blank" class="portfolio-button">
    <span class="button-text">View My Portfolio</span>
    <span class="button-arrow">→</span>
  </a>
</div>

<div class="carousel">
  <div class="carousel-images">
    <div class="carousel-item">
      <img src="/images/portfolio_img/Foamboard_transition.gif" alt="Foamboard Transition">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/VTOL2_SNU_photo.jpg" alt="VTOL SNU">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/awesome_takeoff.gif" alt="Awesome Takeoff">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/cart_system.jpg" alt="Cart System">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/awesome_transition.gif" alt="Awesome Transition">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/0.005_MPPI_MJPC.gif" alt="MPPI MJPC">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/landinggearexpanding.gif" alt="Landing Gear Expanding">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/BNB3403_0627.jpg" alt="BNB3403">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/drone_outdoor.jpg" alt="Drone Outdoor">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/nearthlab.jpg" alt="Nearth Lab">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/preflight.jpg" alt="Preflight">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/WDRCE_qq.jpg" alt="WDRCE">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/drone_seminar_3.jpg" alt="Drone Seminar">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/tau_0.001_ani.gif" alt="Tau Animation">
    </div>
  </div>
  <button class="carousel-button left">&#10094;</button>
  <button class="carousel-button right">&#10095;</button>
</div>
<div class="carousel-dots">
  <span class="dot" onclick="moveToSlide(0)"></span>
  <span class="dot" onclick="moveToSlide(1)"></span>
  <span class="dot" onclick="moveToSlide(2)"></span>
  <span class="dot" onclick="moveToSlide(3)"></span>
  <span class="dot" onclick="moveToSlide(4)"></span>
  <span class="dot" onclick="moveToSlide(5)"></span>
  <span class="dot" onclick="moveToSlide(6)"></span>
  <span class="dot" onclick="moveToSlide(7)"></span>
  <span class="dot" onclick="moveToSlide(8)"></span>
  <span class="dot" onclick="moveToSlide(9)"></span>
  <span class="dot" onclick="moveToSlide(10)"></span>
  <span class="dot" onclick="moveToSlide(11)"></span>
  <span class="dot" onclick="moveToSlide(12)"></span>
  <span class="dot" onclick="moveToSlide(13)"></span>
</div>

<style>
  /* Hero Section */
  .hero-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 60px 20px;
    margin: -20px -20px 40px -20px;
    border-radius: 0 0 20px 20px;
  }
  
  .hero-content {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    align-items: center;
  }
  
  .hero-text h2 {
    font-size: 2.5em;
    font-weight: 700;
    margin: 0 0 15px 0;
    line-height: 1.2;
  }
  
  .affiliation {
    font-size: 1.2em;
    margin: 15px 0;
    opacity: 0.9;
  }
  
  .affiliation a {
    color: #fff;
    text-decoration: underline;
  }
  
  .background {
    font-size: 1.1em;
    opacity: 0.85;
    line-height: 1.6;
  }
  
  .research-highlights h3 {
    font-size: 1.5em;
    margin-bottom: 20px;
    text-align: center;
  }
  
  .research-grid {
    display: grid;
    gap: 20px;
  }
  
  .research-item {
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    text-align: center;
    transition: transform 0.3s ease;
  }
  
  .research-item:hover {
    transform: translateY(-5px);
  }
  
  .research-icon {
    font-size: 2em;
    margin-bottom: 10px;
    display: block;
  }
  
  /* CTA Section */
  .cta-section {
    text-align: center;
    margin: 40px 0;
  }
  
  .portfolio-button {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    text-decoration: none;
    padding: 20px 40px;
    font-size: 1.3em;
    font-weight: 600;
    border-radius: 50px;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
    transition: all 0.3s ease;
  }
  
  .portfolio-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 35px rgba(102, 126, 234, 0.4);
    color: white;
  }
  
  .button-arrow {
    font-size: 1.2em;
    transition: transform 0.3s ease;
  }
  
  .portfolio-button:hover .button-arrow {
    transform: translateX(5px);
  }
  
  /* Content Sections */
  .section-divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, #667eea, transparent);
    margin: 60px 0 40px 0;
  }
  
  .content-section {
    margin: 50px 0;
    max-width: 1000px;
    margin-left: auto;
    margin-right: auto;
  }
  
  .section-title {
    display: flex;
    align-items: center;
    gap: 15px;
    font-size: 2.2em;
    font-weight: 700;
    color: #333;
    margin-bottom: 30px;
    border-bottom: 3px solid #667eea;
    padding-bottom: 10px;
  }
  
  .section-icon {
    font-size: 1em;
  }
  
  /* Education Timeline */
  .education-timeline {
    position: relative;
    padding-left: 30px;
  }
  
  .education-timeline::before {
    content: '';
    position: absolute;
    left: 15px;
    top: 0;
    bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, #667eea, #764ba2);
  }
  
  .education-item {
    position: relative;
    margin-bottom: 40px;
    background: white;
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
    border-left: 4px solid #667eea;
  }
  
  .education-item.current {
    border-left-color: #4CAF50;
    background: linear-gradient(135deg, #f0fff4 0%, #e8f8f5 100%);
  }
  
  .education-marker {
    position: absolute;
    left: -37px;
    top: 30px;
    width: 12px;
    height: 12px;
    background: #667eea;
    border-radius: 50%;
    border: 3px solid white;
    box-shadow: 0 0 0 3px #667eea;
  }
  
  .education-item.current .education-marker {
    background: #4CAF50;
    box-shadow: 0 0 0 3px #4CAF50;
  }
  
  .education-content h3 {
    font-size: 1.4em;
    font-weight: 700;
    color: #333;
    margin-bottom: 10px;
  }
  
  .institution {
    font-size: 1.2em;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 5px;
  }
  
  .duration {
    font-size: 1em;
    color: #666;
    margin-bottom: 10px;
  }
  
  .lab {
    font-size: 1em;
    color: #333;
  }
  
  .lab a {
    color: #667eea;
    text-decoration: none;
  }
  
  .achievements {
    margin-top: 15px;
    display: grid;
    gap: 8px;
  }
  
  .achievement-item {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  .achievement-label {
    font-weight: 600;
    color: #333;
  }
  
  .achievement-value {
    font-weight: 700;
    color: #4CAF50;
    font-size: 1.1em;
  }
  
  .achievement-badge {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 0.9em;
    font-weight: 600;
  }
  
  .achievement-note {
    font-style: italic;
    color: #666;
    font-size: 0.95em;
  }
  
  /* Publications */
  .publications-list {
    display: grid;
    gap: 25px;
  }
  
  .publication-item {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
    border-left: 4px solid #667eea;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  
  .publication-item:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
  }
  
  .paper-title {
    font-size: 1.3em;
    font-weight: 700;
    color: #333;
    margin-bottom: 10px;
    line-height: 1.4;
  }
  
  .paper-authors {
    font-size: 1.1em;
    color: #666;
    margin-bottom: 8px;
  }
  
  .paper-venue {
    font-size: 1em;
    font-weight: 600;
    color: #667eea;
    margin-bottom: 15px;
  }
  
  .paper-links {
    display: flex;
    align-items: center;
    gap: 15px;
    flex-wrap: wrap;
  }
  
  .paper-link {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: #667eea;
    color: white;
    text-decoration: none;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 0.9em;
    font-weight: 600;
    transition: background 0.3s ease;
  }
  
  .paper-link:hover {
    background: #5a67d8;
    color: white;
  }
  
  .paper-note {
    font-size: 0.9em;
    color: #666;
    font-style: italic;
  }
  
  /* FPV Section */
  .fpv-section {
    text-align: center;
  }
  
  .fpv-description {
    font-size: 1.2em;
    color: #666;
    margin-bottom: 30px;
    line-height: 1.6;
  }
  
  .video-container {
    position: relative;
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
    padding-bottom: 56.25%;
    height: 0;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  }
  
  .video-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
  
  /* Carousel Styles */
  .carousel {
    position: relative;
    width: 100%;
    max-width: 800px;
    height: 500px;
    margin: 40px auto;
    overflow: hidden;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  }
  
  .carousel-images {
    display: flex;
    transition: transform 0.5s ease-in-out;
  }
  
  .carousel-item {
    min-width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .carousel-item img {
    max-width: 100%;
    max-height: 500px;
    border-radius: 10px;
  }
  
  .carousel-button {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(0, 0, 0, 0.7);
    border: none;
    color: white;
    font-size: 18px;
    cursor: pointer;
    padding: 12px;
    border-radius: 50%;
    z-index: 10;
    transition: background-color 0.3s ease;
  }
  
  .carousel-button:hover {
    background-color: rgba(0, 0, 0, 0.9);
  }
  
  .carousel-button.left {
    left: 15px;
  }
  
  .carousel-button.right {
    right: 15px;
  }
  
  .carousel-dots {
    text-align: center;
    padding: 20px 0;
  }
  
  .dot {
    display: inline-block;
    width: 12px;
    height: 12px;
    margin: 5px;
    background-color: #ccc;
    border-radius: 50%;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .dot:hover {
    background-color: #999;
  }
  
  .dot.active {
    background-color: #667eea;
    transform: scale(1.2);
  }
  
  /* Responsive Design */
  @media (max-width: 768px) {
    .hero-content {
      grid-template-columns: 1fr;
      gap: 30px;
      text-align: center;
    }
    
    .hero-text h2 {
      font-size: 2em;
    }
    
    .section-title {
      font-size: 1.8em;
    }
    
    .portfolio-button {
      padding: 15px 30px;
      font-size: 1.1em;
    }
    
    .video-container {
      max-width: 100%;
    }
    
    .carousel {
      height: 300px;
      margin: 20px 10px;
    }
    
    .carousel-item img {
      max-height: 300px;
    }
  }
</style>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    let currentIndex = 0;
    const images = document.querySelectorAll('.carousel-item');
    const totalImages = images.length;
    const carouselImages = document.querySelector('.carousel-images');
    const dots = document.querySelectorAll('.dot');
    let autoSlideInterval;

    function showSlide(index) {
      if (index >= totalImages) {
        currentIndex = 0;
      } else if (index < 0) {
        currentIndex = totalImages - 1;
      } else {
        currentIndex = index;
      }
      const offset = -currentIndex * 100;
      carouselImages.style.transform = `translateX(${offset}%)`;
      updateDots();
    }

    function moveSlide(step) {
      showSlide(currentIndex + step);
    }

    function moveToSlide(index) {
      showSlide(index);
    }

    function autoSlide() {
      moveSlide(1);
      autoSlideInterval = setTimeout(autoSlide, 5000);
    }

    function updateDots() {
      dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === currentIndex);
      });
    }

    document.querySelector('.carousel-button.left').addEventListener('click', function() {
      clearTimeout(autoSlideInterval);
      moveSlide(-1);
      autoSlideInterval = setTimeout(autoSlide, 5000);
    });

    document.querySelector('.carousel-button.right').addEventListener('click', function() {
      clearTimeout(autoSlideInterval);
      moveSlide(1);
      autoSlideInterval = setTimeout(autoSlide, 5000);
    });

    dots.forEach((dot, index) => {
      dot.addEventListener('click', function() {
        clearTimeout(autoSlideInterval);
        moveToSlide(index);
        autoSlideInterval = setTimeout(autoSlide, 5000);
      });
    });

    autoSlide();
  });
</script>

<div class="section-divider"></div>

<div class="content-section">
  <h2 class="section-title">
    <span class="section-icon">🎓</span>
    Education
  </h2>
  <div class="education-timeline">
    <div class="education-item current">
      <div class="education-marker"></div>
      <div class="education-content">
        <h3>Ph.D. in Mechanical Science and Engineering</h3>
        <p class="institution">University of Illinois Urbana-Champaign</p>
        <p class="duration">2025.Aug ~ Current</p>
        <p class="lab"><a href="https://naira.mechse.illinois.edu/" target="_blank">Advanced Controls Research Lab</a></p>
      </div>
    </div>
    <div class="education-item">
      <div class="education-marker"></div>
      <div class="education-content">
        <h3>B.S. in Mechanical Engineering, Interdisciplinary Major in AI</h3>
        <p class="institution">Seoul National University</p>
        <p class="duration">2025 Feb</p>
        <div class="achievements">
          <div class="achievement-item">
            <span class="achievement-label">GPA:</span>
            <span class="achievement-value">3.99 / 4.0</span>
          </div>
          <div class="achievement-item">
            <span class="achievement-badge">Outstanding B.S. Thesis Presentation Award</span>
          </div>
          <div class="achievement-item">
            <span class="achievement-badge">College of Engineering Outstanding Graduate Award</span>
          </div>
          <div class="achievement-item">
            <span class="achievement-note">Top 24 Graduates across the entire College of Engineering</span>
          </div>
        </div>
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
      <h4 class="paper-title">On the Steady-State Distributionally Robust Kalman Filter</h4>
      <p class="paper-authors"><em>Minhyuk Jang</em>*, Astghik Hakobyan*, and Insoon Yang</p>
      <p class="paper-venue">IEEE Control and Decision Conference 2025</p>
      <div class="paper-links">
        <a href="https://arxiv.org/abs/2503.23742" target="_blank" class="paper-link">📄 arXiv</a>
        <span class="paper-note">* Equal contribution</span>
      </div>
    </div>
    
    <div class="publication-item">
      <h4 class="paper-title">Wasserstein Distributionally Robust Control and State Estimation for Partially Observable Linear Systems</h4>
      <p class="paper-authors"><em>Minhyuk Jang</em>, Astghik Hakobyan, and Insoon Yang</p>
      <div class="paper-links">
        <a href="https://arxiv.org/abs/2406.01723" target="_blank" class="paper-link">📄 arXiv</a>
      </div>
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
    <span class="section-icon">🚁</span>
    Beyond Research: FPV Piloting
  </h2>
  <div class="fpv-section">
    <p class="fpv-description">When not working on control theory, I enjoy applying flight dynamics in practice through FPV drone piloting.</p>
    <div class="video-container">
      <iframe src="https://www.youtube.com/embed/WPttdZw-E_8?si=gXVi6KftqGTxxWPf" title="FPV Flight Video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
  </div>
</div>