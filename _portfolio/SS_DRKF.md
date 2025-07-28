---
title: "On the Steady-State Distributionally Robust Kalman Filter"
excerpt: On the Steady-State Distributionally Robust Kalman Filter <br/> IEEE CDC 2025  <br/><img src='/images/portfolio_img/violin_lqr.jpeg' width='500'>
order: 1
---

**Duration : OCT '24 - MAR '25**

([arXiv](https://arxiv.org/abs/2503.23742))


## Abstract

State estimation in the presence of uncertain or data-driven noise distributions remains a critical challenge in control and robotics. Although the Kalman filter is the most popular choice, its performance degrades significantly when distributional mismatches occur, potentially leading to instability or divergence. To address this limitation, we introduce a novel steady-state distributionally robust (DR) Kalman filter that leverages Wasserstein ambiguity sets to explicitly account for uncertainties in both process and measurement noise distributions. Our filter achieves computational efficiency by requiring merely the offline solution of a single convex semidefinite program, which yields a constant DR Kalman gain for robust state estimation under distributional mismatches. Additionally, we derive explicit theoretical conditions on the ambiguity set radius that ensure the asymptotic convergence of the time-varying DR Kalman filter to the proposed steady-state solution. Numerical simulations demonstrate that our approach outperforms existing baseline filters in terms of robustness and accuracy across both Gaussian and non-Gaussian uncertainty scenarios, highlighting its significant potential for real-world control and estimation applications.