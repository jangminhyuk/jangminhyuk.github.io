---
permalink: /
title: "Hello, I'm Minhyuk!"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I will be joining the UIUC MechSE [Advanced Controls Research Lab](https://naira.mechse.illinois.edu/) as a PhD student in Fall 2025.

I earned my bachelor’s degree in Mechanical Engineering and Artificial Intelligence at Seoul National University. My interests include:

- **Control Theory** (Robust Control, Optimal Control, Adaptive Control, Nonlinear Control)
- **Safety Guarantee**, **Safety-Critical Systems** (Multirotor, VTOL, Robotics, etc.)
- **Multi-agent Systems**


<div align="center">
  <a href="https://jangminhyuk.github.io/portfolio/" target="_blank" style="text-decoration: none;">
    <button style="background-color: #4CAF50; color: white; padding: 15px 30px; font-size: 24px; border: none; border-radius: 8px; cursor: pointer;">
      Click HERE to Check My Portfolio
    </button>
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
  .carousel {
    position: relative;
    width: 100%;
    max-width: 800px;
    height: 500px;
    margin: 20px auto;
    overflow: hidden;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
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
    padding: 10px;
    border-radius: 50%;
    z-index: 10;
  }
  .carousel-button.left {
    left: 15px;
  }
  .carousel-button.right {
    right: 15px;
  }
  .carousel-dots {
    text-align: center;
    padding: 10px 0;
  }
  .dot {
    display: inline-block;
    width: 12px;
    height: 12px;
    margin: 5px;
    background-color: #bbb;
    border-radius: 50%;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  .dot.active {
    background-color: #717171;
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

## Education

- **B.S. in Mechanical Engineering, Interdisciplinary Major in Artificial Intelligence, Seoul National University, 2025 Feb**
  - **GPA: 3.99 / 4.0**, Outstanding B.S. Thesis Presentation Award
  - College of Engineering Outstanding Graduate Award, One of the Top 24 Graduates across the entire College of Engineering

## Publications
- **On the Steady-State Distributionally Robust Kalman Filter**, ([arXiv](https://arxiv.org/abs/2503.23742))
  - *Minhyuk Jang* **, Astghik Hakobyan **, and Insoon Yang
  - Submitted to *IEEE Control and Decision Conference* (submitted)
  - ** Equal contribution
- **Wasserstein Distributionally Robust Control and State Estimation for Partially Observable Linear Systems**, ([arXiv](https://arxiv.org/abs/2406.01723))
  - *Minhyuk Jang*, Astghik Hakobyan, and Insoon Yang
  - Submitted to *IEEE Transactions on Automatic Control* (under review)
- **Stability Analysis of Disturbance Observer under Model Uncertainty with Different System Degrees between True and Nominal Systems**
  - *Minhyuk Jang*
  - Institute of Control, Robotics and Systems (ICROS), 2024.

## I fly FPV drones too!

<iframe width="560" height="315" src="https://www.youtube.com/embed/qCGaa-OFfKE?si=3YpXTW-7aMHg-Lks" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

