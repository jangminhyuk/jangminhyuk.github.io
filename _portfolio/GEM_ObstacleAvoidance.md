---
title: "Autonomous Obstacle Avoidance on the GEM e4"
excerpt: "Obstacle-aware planning and control on a full-scale autonomous vehicle (Polaris GEM e4)"
collection: portfolio
order: 0
preview_layout: stacked
preview_images:
  - /images/portfolio_img/thumbs/gem_outdoor.gif
  - /images/portfolio_img/thumbs/gem_gazebo.gif
  - /images/portfolio_img/thumbs/gem_passenger.gif
---

**CS588: Autonomous Vehicle System Engineering**

A Highbay navigation framework for the **Polaris GEM e4** that performs obstacle-aware planning and control. An **RGB-D + YOLO** perception module estimates obstacle positions, a **hierarchical Frenet-frame replanner** samples safe detours, and a low-level **Stanley controller** tracks the chosen path. The system is validated first in high-fidelity simulation and then on the physical GEM e4.

### Simulation

In simulation, obstacles (including a pedestrian added to the scene) are detected from the front-camera stream and avoided in closed loop, with a mean tracking error of 0.41&nbsp;m (RMSE 0.66&nbsp;m).

<center>
  <video src='/images/portfolio_img/gem_gazebo.mp4' width='600' autoplay loop muted playsinline></video>
  <figcaption>Closed-loop obstacle avoidance in the Highbay simulator</figcaption>
</center>

### Hardware Deployment

The same planning and tracking pipeline transfers to the physical GEM e4: the vehicle follows the reference, executes a lateral detour around the obstacle, and returns to path with a minimum clearance of 1.84&nbsp;m (lateral RMSE 0.38&nbsp;m).

<center>
  <video src='/images/portfolio_img/gem_outdoor.mp4' width='600' autoplay loop muted playsinline></video>
  <figcaption>Hardware deployment on the GEM e4 in the Highbay environment (3&times; speed)</figcaption>
</center>

<center>
  <video src='/images/portfolio_img/gem_passenger.mp4' width='600' autoplay loop muted playsinline></video>
  <figcaption>Onboard view during an autonomous detour maneuver (3&times; speed)</figcaption>
</center>
