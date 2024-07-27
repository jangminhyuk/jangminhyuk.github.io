---
permalink: /
title: "Hello, I'm Minhyuk!"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a student majoring in Mechanical Engineering and Artificial Intelligence at Seoul National University. My interests include 
- __Control Theory__ (Robust Control, Optimal Control, Adaptive Control, Nonlinear Control)
- Control and System Design for __Safety-Critical Systems__ (Multirotor, VTOL, Robotics, etc), __Multi-agent Systems__

<div class="carousel">
  <div class="carousel-images">
    <div class="carousel-item">
      <img src="/images/portfolio_img/Foamboard_transition.gif" alt="Photo 1">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/VTOL2_SNU_photo.jpg" alt="Photo 2">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/awesome_takeoff.gif" alt="Photo 3">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/cart_system.jpg" alt="Photo 4">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/awesome_transition.gif" alt="Photo 5">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/0.005_MPPI_MJPC.gif" alt="Photo 6">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/landinggearexpanding.gif" alt="Photo 7">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/BNB3403_0627.jpg" alt="Photo 8">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/drone_outdoor.jpg" alt="Photo 9">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/nearthlab.jpg" alt="Photo 10">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/preflight.jpg" alt="Photo 11">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/WDRCE_qq.jpg" alt="Photo 12">
    </div>
    <div class="carousel-item">
      <img src="/images/portfolio_img/drone_seminar_3.jpg" alt="Photo 13">
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
</div>

<style>
  .carousel {
    position: relative;
    width: 100%;
    max-width: 800px;
    height: 500px;
    margin: auto;
    overflow: hidden;
  }
  .carousel-images {
    display: flex;
    transition: transform 1s ease-in-out;
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
  }
  .carousel-button {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(0, 0, 0, 0.5);
    border: none;
    color: white;
    font-size: 18px;
    cursor: pointer;
    z-index: 10;
  }
  .carousel-button.left {
    left: 10px;
  }
  .carousel-button.right {
    right: 10px;
  }
  .carousel-dots {
    text-align: center;
    padding: 20px 0;
  }
  .dot {
    display: inline-block;
    width: 15px;
    height: 15px;
    margin: 5px;
    background-color: #bbb;
    border-radius: 50%;
    cursor: pointer;
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

    console.log("Document loaded");
    console.log(`Total images: ${totalImages}`);

    function showSlide(index) {
      console.log(`showSlide called with index: ${index}`);
      if (index >= totalImages) {
        currentIndex = 0;
      } else if (index < 0) {
        currentIndex = totalImages - 1;
      } else {
        currentIndex = index;
      }
      const offset = -currentIndex * 100;
      console.log(`Showing slide ${currentIndex}, offset: ${offset}%`);
      carouselImages.style.transform = `translateX(${offset}%)`;
      updateDots();
    }

    function moveSlide(step) {
      console.log(`moveSlide called with step: ${step}`);
      showSlide(currentIndex + step);
    }

    function moveToSlide(index) {
      console.log(`moveToSlide called with index: ${index}`);
      showSlide(index);
    }

    function autoSlide() {
      console.log("autoSlide called");
      moveSlide(1);
      autoSlideInterval = setTimeout(autoSlide, 5000);
    }

    function updateDots() {
      dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === currentIndex);
      });
    }

    document.querySelector('.carousel-button.left').addEventListener('click', function() {
      console.log("Left button clicked");
      clearTimeout(autoSlideInterval);
      moveSlide(-1);
      autoSlideInterval = setTimeout(autoSlide, 5000);
    });

    document.querySelector('.carousel-button.right').addEventListener('click', function() {
      console.log("Right button clicked");
      clearTimeout(autoSlideInterval);
      moveSlide(1);
      autoSlideInterval = setTimeout(autoSlide, 5000);
    });

    dots.forEach((dot, index) => {
      dot.addEventListener('click', function() {
        console.log(`Dot ${index} clicked`);
        clearTimeout(autoSlideInterval);
        moveToSlide(index);
        autoSlideInterval = setTimeout(autoSlide, 5000);
      });
    });

    autoSlide();
  });
</script>

## Check my Portfolio [HERE](https://jangminhyuk.github.io/portfolio/)

Education
======
* __B.S. in Mechanical Engineering, Interdisciplinary Major in Artificial Intelligence, Seoul National University, 2025 Feb__
  * GPA : __3.99 / 4.0__, Outstanding B.S. Thesis Presentation Award

Publications
======
* **Wasserstein Distributionally Robust Control and State Estimation for Partially Observable Linear Systems** 
  * *Minhyuk Jang*, Astghik Hakobyan, and Insoon Yang
  * Advances in Neural Information Processing Systems (NeurIPS), 2024. (submitted) ([arXiv](https://arxiv.org/abs/2406.01723))
* **Stability Analysis of Disturbance Observer under Model Uncertainty with Different System Degrees between True and Nominal Systems**
  * *Minhyuk Jang*
  * Institute of Control, Robotics and Systems (ICROS, Domestic Conference), 2024.

Experience
======
* Mar 2023 - Present : Control and Optimization Research ([CORE](http://coregroup.snu.ac.kr/)) Lab, SNU
  * Research Intern - Advisor : Prof. Insoon Yang
  * Developed unified algorithm for Wasserstein Distributionally Robust Control and State Estimation in partially observable linear stochastic systems, where the probability distributions of disturbances and measurement noises are unknown
  * Formulated a tractable semidefinite programming problem that iteratively determines the worst-case covariance matrices of all uncertainties, significantly enhancing the scalability and efficiency of the proposed algorithm

* Jan 2024 - Feb 2024: [NEARTHLAB](https://www.nearthlab.com/)
  * Aerospace Engineering Intern, GNC Team
  * Developed DOB and LQR based position/velocity controllers in C++ & ROS2 and tested through Gazebo simulation
  * Integrated the flight controller with a companion computer for offboard flight control of quadrotors, implemented DOB+LQR and DOB+PID controllers, and conducted extensive outdoor flight experiments

Leadership / Extracurricular
======
* Sep 2023 - Present : Bulnabi - SNU Drone Club
  * Team Leader
    * Led and developed over three Quadrotor Build/Fly seminars, teaching hardware assembly, sensor calibration, Ground Control Station usage, flight experiments, and flight log analysis
    * Directed a 25-member team for the Korea Robot Aircraft Competition, focusing on VTOL system design and autonomous flight missions, conducting extensive outdoor tests to stabilize all flight phases
* Sep 2021 -- Mar 2023
  * Senior KATUSA(Korean Augmentation to the United States Army)
    * Led and managed a 10-solider squad, ensuring their training, well-being, and mission preparedness
    * Operated within a U.S. Army office, collaborating extensively with American colleagues on a daily basis
    * Applied language proficiency to deliver crucial translation and interpretation support during Combined Exercises
  
Skills
======
* Programming : C/C++, Python, MATLAB
* Libraries/Softwares : PX4-Autopilot, ROS2, SolidWorks, MuJoCo, PyTorch, LaTeX
* Languagues : Korean, English (TOEFL 106)


  
<!-- Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul> -->
  
<!-- Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul> -->
  
Honors & Awards
======
* Outstanding B.S. Thesis Presentation Award (2024) : Automated Inverse Temperature Tuning Algorithm for MPPI Control
* Kwanjeong Scholarship (2021) : Recipient of a full tuition scholarship along with a stipend for two years, in recognition of outstanding academic achievement.
* ARCOM(Army Commendation Medal) (2022) : United States Department of the Army
