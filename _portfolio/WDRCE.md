---
title: "Wasserstein Distributionally Robust Control and State Estimation for Partially Observable Linear Systems"
excerpt: Wasserstein Distributionally Robust Control and State Estimation(WDR-CE) <br/><img src='/images/portfolio_img/WDRCE_qq.jpg' width='500' height='500'> 
collection: portfolio
---

**Duration : MAR '23 - Present**

(Will be updated)

## Abstract

This paper presents a novel Wasserstein distributionally robust control and state estimation algorithm for partially observable linear stochastic systems, where the probability distributions of disturbances and measurement noises are unknown. Our method consists of the control and state estimation phases to handle distributional ambiguities of system disturbances and measurement noises, respectively. Leveraging tools from modern distributionally robust optimization, we consider an approximation of the control problem with an arbitrary nominal distribution and derive its closed-form optimal solution. We show that the separation principle holds, thereby allowing the state estimator to be designed separately. A novel distributionally robust Kalman filter is then proposed as an optimal solution to the state estimation problem with Gaussian nominal distributions. Our key contribution is the combination of distributionally robust control and state estimation into a unified algorithm. This is achieved by formulating a tractable semidefinite programming problem that iteratively determines the worst-case covariance matrices of all uncertainties, leading to a scalable and efficient algorithm. Our method is also shown to enjoy a guaranteed cost property as well as a probabilistic out-of-sample performance guarantee. The results of our numerical experiments demonstrate the performance and computational efficiency of the proposed method.