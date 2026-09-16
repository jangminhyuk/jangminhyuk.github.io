---
title: "Safe Flow Expansion: Discovering Safe Robot Behaviors in Out-of-Distribution Motion Planning"
research_id: safe-flow-expansion
home_order: -3
topics: [robotics, control, learning]
card_title: "Safe Flow Expansion"
hide_research_media: true
permalink: /portfolio/safe-flow-expansion/
excerpt: "Discovering new safe robot behaviors with an expanded generative policy."
order: -2
---

## Abstract

Generative policies and sampling-based predictive control both plan robot motion by sampling candidate action sequences. However, the safety of individual samples does not guarantee safety when samples are combined to improve performance, and pretrained policy performance degrades rapidly in out-of-distribution environments, particularly under safety constraints. We address both of these concerns by presenting a unified framework that incorporates finite-horizon discrete-time control barrier function conditions into both online planning and generative policy learning. First, we develop a common convex safety condition that preserves one-step safety under weighted averaging of candidate action sequences. We then use these safe actions to train a conditional flow matching policy. Finally, we show that these same safety conditions allow us to expand the set of generated actions from a pretrained policy, allowing the system to discover new safe behaviors. We demonstrate the effectiveness of this approach in simulation and hardware experiments across a range of system scales, from planar robots to quadrotors to high-degree-of-freedom manipulators. Safe flow expansion improves coverage in out-of-distribution scenarios, while enabling 10× and 50× faster single-action generation than conventional sampling-based control and flow matching baselines.

<div class="comparison-heading">
  <h2>Videos</h2>
  <button type="button" class="motion-toggle" hidden aria-pressed="false">Pause videos</button>
</div>

<div class="video-comparison">
  <figure aria-labelledby="cfm-ball-title">
    <h3 id="cfm-ball-title">Pretrained CFM</h3>
    <video data-preview controls muted loop playsinline preload="none" poster="/assets/research/cfm-pretrained-ball.jpg" aria-label="Pretrained CFM trajectories around the ball obstacle, shown in red.">
      <source src="/assets/research/cfm-pretrained-ball.mp4" type="video/mp4">
      <a href="/assets/research/cfm-pretrained-ball.mp4">Watch pretrained CFM</a>
    </video>
  </figure>
  <figure aria-labelledby="sfe-ball-title">
    <h3 id="sfe-ball-title">After Safe Flow Expansion</h3>
    <video data-preview controls muted loop playsinline preload="none" poster="/assets/research/sfe-expanded-ball.jpg" aria-label="Trajectories after Safe Flow Expansion around the ball obstacle, shown in green.">
      <source src="/assets/research/safe-flow-expansion.mp4" type="video/mp4">
      <a href="/assets/research/safe-flow-expansion.mp4">Watch Safe Flow Expansion</a>
    </video>
  </figure>
</div>

<div class="video-comparison">
  <figure aria-labelledby="cfm-corridor-title">
    <h3 id="cfm-corridor-title">Pretrained CFM · Corridor</h3>
    <video data-preview controls muted loop playsinline preload="none" poster="/assets/research/cfm-pretrained-corridor.jpg" aria-label="Pretrained CFM quadrotor trajectories through a corridor of obstacles.">
      <source src="/assets/research/cfm-pretrained-corridor.mp4" type="video/mp4">
      <a href="/assets/research/cfm-pretrained-corridor.mp4">Watch pretrained CFM in the corridor</a>
    </video>
  </figure>
  <figure aria-labelledby="mppi-corridor-title">
    <h3 id="mppi-corridor-title">MPPI-DCBF · Corridor</h3>
    <video data-preview controls muted loop playsinline preload="none" poster="/assets/research/mppi-dcbf-corridor.jpg" aria-label="MPPI-DCBF quadrotor trajectories through a corridor of obstacles.">
      <source src="/assets/research/mppi-dcbf-corridor.mp4" type="video/mp4">
      <a href="/assets/research/mppi-dcbf-corridor.mp4">Watch MPPI-DCBF in the corridor</a>
    </video>
  </figure>
</div>
