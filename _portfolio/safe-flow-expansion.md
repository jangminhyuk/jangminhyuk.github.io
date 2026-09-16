---
title: "Safe Flow Expansion: Discovering Safe Robot Behaviors in Out-of-Distribution Motion Planning"
research_id: safe-flow-expansion
permalink: /portfolio/safe-flow-expansion/
excerpt: "Discovering new safe robot behaviors with an expanded generative policy."
order: -2
---

## Overview

Safe Flow Expansion trains generative motion policies and expands their coverage in unfamiliar environments. Sampling-based predictive control supplies safe demonstrations for conditional flow matching. The policy then generates additional actions, checks them for safety, and uses the verified actions for further training.

## Safety conditions

Individual safe action samples do not necessarily remain safe when averaged. The method uses finite-horizon discrete-time control barrier function conditions that preserve one-step safety under weighted averaging.

The same conditions support policy expansion, allowing new safe modes to be discovered in previously unseen environments. The work includes simulations and hardware experiments across planar robots, quadrotors, and manipulators.

The video above shows quadrotor hardware trajectories after safe flow expansion.
