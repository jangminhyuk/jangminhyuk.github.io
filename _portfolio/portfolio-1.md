---
title: "A Practical Implementation of Model Predictive Path Integral(MPPI) Control Using MuJoCo MPC(MJPC) framework"
excerpt: "MPPI-MJPC <br/><img src='/images//portfolio_img/MPPIMJPC_quad.jpg' alt="drawing" width="80">"
collection: portfolio
---

# Empowering Complex Robotic Tasks with MPPI-MJPC

**Project Duration : SEP '23 - Present**

(Last update : 2023-12-24)

This reserach project is mainly focused on solving complex robotic tasks with MPPI control law by utilizing [MuJoCo MPC](https://github.com/google-deepmind/mujoco_mpc) Framework. The code for this project can be found in [HERE](https://github.com/jangminhyuk/MPPI_in_MJPC).

### Model Predictive Path Integral(MPPI)

The Model Predictive Path Integral(MPPI) control method has evolved significantly and has exhibited its efficacy in various autonomous driving experiments. These sampling-based MPC techniques are rooted in an Information-Theoretic approach, leveraging information derived from randomly generated simple policies. Control inputs are determined by the cost associated with each of these policies. Unlike traditional optimal control problems(e.g., MPC), this approach doesn’t require objective function to be differentiable, allowing the use of complex dynamical models without approximation. Moreover, MPPI can be computed efficiently, with each rollout parallelized. These characteristics makes MPPI able to handle complex, contact-rich environments involving high-DOF robotics. Recent work has demonstrated the effectiveness of MPPI in various complex contact-rich tasks, such as collision avoidance with robot arms in Isaac Gym environments, leveraging GPU acceleration. [Ref] (https://proceedings.mlr.press/v164/bhardwaj22a.html)

### MuJoCo MPC(MJPC)

An open source framework named MuJoCo MPC [(MJPC)](https://github.com/google-deepmind/mujoco_mpc) offers various tasks and provides a user-friendly environment for testing sampling based control algorithms. MJPC supports controllers based on trivial sampling-based methods, generating samples and computing costs using the dynamic model of the MuJoCo environment. This approach streamlines the controller design process and simplifies the computation of multiple trajectories in a single-CPU environment, without using GPU resources. The sampling controller provided in MJPC is straightforward, by selecting the lowest-cost policy. **However, due to the lack of a robust theoretical background and some undesired fluctuations with this lowest-cost selection method, we decided to incorporate the Information-Theoretic approach of MPPI into the MJPC framework.**

### MPPI-MJPC

