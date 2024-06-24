---
title: "Automated Inverse Temperature Tuning Algorithm for MPPI Control "
excerpt: Hovering Task using MPPI control <br/><img src='/images/portfolio_img/0.005_MPPI_MJPC.gif' width='500' height='300'>
collection: portfolio
order: 2
---

**Project Duration : SEP '23 - JUN '24**

__Outstanding B.S. Thesis Presentation Award, Department of Mechanical Engineering, Seoul National University, 2024.__

(Last update : 2024-06-24)

This reserach project is mainly focused on the automated selection of the hyperparameter named **Inverse Temperature** in MPPI control. Also, we implemented MPPI controller and our algorithm within [MuJoCo MPC](https://github.com/google-deepmind/mujoco_mpc) framework.

### Model Predictive Path Integral(MPPI)

The Model Predictive Path Integral(MPPI) control method has evolved significantly and has exhibited its efficacy in various autonomous driving experiments. These sampling-based MPC techniques are rooted in an Information-Theoretic approach, leveraging information derived from randomly generated simple policies. Control inputs are determined by the cost associated with each of these policies. Unlike traditional optimal control problems(e.g., MPC), this approach doesn’t require objective function to be differentiable, allowing the use of complex dynamical models without approximation. Moreover, MPPI can be computed efficiently, with each rollout parallelized. These characteristics makes MPPI able to handle complex, contact-rich environments involving high-DOF robotics. Recent work has demonstrated the effectiveness of MPPI in various complex contact-rich tasks, such as collision avoidance with robot arms in Isaac Gym environments, leveraging GPU acceleration. [Ref](https://proceedings.mlr.press/v164/bhardwaj22a.html)

### Inverse Temperature Tuning
In MPPI control theory, there is a crucial **hyperparameter** named **$\lambda$ (inverse temperature)**, which significantly impacts control performance. The choice of $\lambda$ affects both control cost and state fluctuation. However, there are no existing algorithms that automatically tune $\lambda$ for optimal performance. In this paper, we propose an adaptive algorithm for tuning $\lambda$ to minimize state fluctuation while maintaining low cost. We define an objective function with respect to $\lambda$ and update $\lambda$ to minimize this specific objective function, operating in parallel with the MPPI controller.

We demonstrated our algorithm using an open-source framework named MuJoCo MPC (MJPC), specifically in the quadrotor hovering and path tracking tasks. As we continuously update $\lambda$ at each time step, the $\lambda$ value starting from different initial values converges. Using the proposed algorithm with adpative $\lambda$, the quadrotor exhibits less fluctuation and improved control performance.

## Experimental Results
First, let's see the impact of $\lambda$ to the control performance.
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

The above figures demonstrates the importance of selecting proper $\lambda$.

Now, let's see the effect of our $\lambda$ tuning algorithm.

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

Our resulting algorithm is not only suitable for the quadrotor hovering task, but also adaptable to a variety of other robotic tasks that require smooth trajectory generation.