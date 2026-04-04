---
title: "Distributionally Robust Extended Kalman Filter (DR-EKF)"
excerpt: "Target Tracking under inaccurate process and measurement noise distributions"
order: 0.8
preview_images:
  - /images/portfolio_img/traj_combined.jpg
  - /images/portfolio_img/thumbs/tracking_video_INSTANCE_4_ZOOMED_normal_fps15.gif
  - /images/portfolio_img/thumbs/tracking_video_MEAN_normal_fps15.gif
preview_layout: wide-top
---


Minhyuk Jang*, Jungjin Lee*, Astghik Hakobyan, Insoon Yang, Naira Hovakimyan.


<center>
  <img src='/images/portfolio_img/tracking_video_INSTANCE_1_quadratic_fps15.gif' width='500'/>
</center>
<center>
  <img src='/images/portfolio_img/tracking_video_INSTANCE_1_normal_fps15.gif' width='500'/>
</center>

## Abstract

The extended Kalman filter (EKF) is a cornerstone of nonlinear state estimation, yet its performance is fundamentally limited by noise-model mismatch and linearization errors. We develop a residual-aware distributionally robust EKF that addresses both challenges within a unified Wasserstein distributionally robust state estimation framework. The key idea is to treat linearization residuals as uncertainty and absorb them into an effective uncertainty model captured by a stage-wise ambiguity set, enabling noise-model mismatch and approximation errors to be handled within a single formulation. This approach yields a computable effective radius along with deterministic upper bounds on the prior and posterior mean-squared errors of the true nonlinear estimation error. The resulting filter admits a tractable semidefinite programming reformulation while preserving the recursive structure of the classical EKF. Simulations on coordinated-turn target tracking and uncertainty-aware robot navigation demonstrate improved estimation accuracy and safety compared to standard EKF baselines under model mismatch and nonlinear effects.