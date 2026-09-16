---
title: "Uncertainty-Aware Vision-Based Autonomous Aerial Refueling"
research_id: aerial-refueling
permalink: /portfolio/aerial-refueling/
excerpt: "Vision-based docking with uncertainty-aware planning margins."
order: -3
---

## Overview

Autonomous probe-and-drogue refueling requires a receiver aircraft to align its probe with a moving drogue. The controller uses margins derived from uncertainty in relative-state estimation and aircraft motion.

The architecture combines vision-based drogue measurements, differential GPS, and avionics in an extended Kalman filter. Conformal calibration characterizes near-contact estimation error, while an offline covariance design assesses position dispersion and corrective-command budgets. Together, they configure an online model predictive controller.

## Demonstration

The video shows simulated docking approaches in FlightGear / JSBSim. The study evaluates how geometric and command margins affect crossing accuracy and control effort.
