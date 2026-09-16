---
title: "WRAP: Wasserstein-Robust Adaptive Plug-in for Robot Localization"
research_id: wrap
home_order: -2
topics: [robotics, learning, estimation]
card_title: "WRAP: robust robot localization"
card_summary: "Adaptive noise models, including learned adapters, with Wasserstein-robust EKF/ESKF updates."
permalink: /portfolio/wrap/
excerpt: "Adaptive, distributionally robust state estimation for changing sensing conditions."
order: -1
---

## Overview

Robot localization becomes less reliable when sensing conditions change: GNSS can suffer from multipath, UWB links can become non-line-of-sight, and nominal noise models can become inaccurate.

WRAP adds an adaptive, Wasserstein-robust update to existing extended Kalman filter and error-state Kalman filter pipelines. An adaptive module supplies effective noise statistics; a robust local update accounts for remaining covariance uncertainty. The baseline propagation model, residual, and state representation remain intact.

## Evaluation

The paper evaluates UWB–IMU localization on held-out sequences, studies GNSS–INS behavior, and reports embedded runtime on a Jetson Orin Nano. See the linked preprint for the experimental setup, results, and limitations.
