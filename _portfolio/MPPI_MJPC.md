---
card_video_alt: "Quadrotor hovering with MPPI control in MuJoCo simulation."
card_video: /assets/projects/mppi.mp4
card_image: /assets/projects/mppi.jpg
home_order: 4
featured_engineering: true
card_title: "Adaptive tuning for MPPI control"
card_label: "Sampling-based control"
card_summary: "Automatic inverse-temperature tuning for model predictive path integral control."
title: "Automated Inverse Temperature Tuning Algorithm for MPPI Control "
excerpt: "Automated Inverse Temperature Tuning for MPPI Control"
collection: portfolio
order: 2
preview_images:
  - /images/portfolio_img/thumbs/0.005_MPPI_MJPC.gif
---

**Project Duration : SEP '23 - JUN '24**

__Outstanding B.S. Thesis Presentation Award, Department of Mechanical Engineering, Seoul National University, 2024.__

(Last update : 2024-06-24)

This project implements automatic inverse-temperature tuning for MPPI in [MuJoCo MPC](https://github.com/google-deepmind/mujoco_mpc), with quadrotor hovering and path-tracking experiments.

### Model Predictive Path Integral(MPPI)

MPPI samples candidate control sequences, evaluates their rollout costs, and combines them using cost-based weights. It supports non-differentiable costs and parallel rollout evaluation. [Reference](https://proceedings.mlr.press/v164/bhardwaj22a.html)

### Inverse Temperature Tuning
The parameter **$\lambda$ (inverse temperature)** affects control cost and state fluctuation. This project updates $\lambda$ alongside the MPPI controller to reduce state fluctuations while maintaining low cost.

In the quadrotor experiments, $\lambda$ converged from different initial values, and adaptive tuning reduced fluctuations in hovering and path tracking.

## Experimental Results
Position tracking under different fixed values of $\lambda$:
<center>
  <img src='/images/portfolio_img/x_position_plot.png' width='500'/>
  <figcaption>X position with different inverse temperature</figcaption>
</center>
<center>
  <img src='/images/portfolio_img/y_position_plot.png' width='500'/>
  <figcaption>Y position with different inverse temperature</figcaption>
</center>
<center>
  <img src='/images/portfolio_img/z_position_plot.png' width='500'/>
  <figcaption>Z position with different inverse temperature</figcaption>
</center>

The above figures demonstrates the importance of selecting proper $\lambda$. ($\lambda=0.005$ shows small cost with small fluctuation in this case.)

Online updates from different initial values of $\lambda$:

<center>
  <img src='/images/portfolio_img/lambda_plot_fixed_0_005_sigma_0.005.png' width='500'/>
  <figcaption>Lambda update process with different initial condition</figcaption>
</center>

$\lambda$ starting from different initial condition converges.

<center>
  <img src='/images/portfolio_img/mppi_optimal_lambda.gif' width='700'/>
  <figcaption>Quadrotor Hovering task with MPPI (Goal Position : Green)</figcaption>
</center>
The results from MPPI with the properly tuned $\lambda$ showed reduced fluctuations compared to different selections of $\lambda$. Additionally, the optimal $\lambda$ values consistently converged to a specific range despite different initial values, underscoring the effectiveness of our approach. 
