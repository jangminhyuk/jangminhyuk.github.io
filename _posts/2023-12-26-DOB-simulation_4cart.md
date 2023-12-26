---
title: 'DOB simulations (4-Cart System)'
date: 2023-12-26
permalink: /posts/2023/12/DOB/simulation_4cart
tags:
  - Control Theory
  - Disturbance Observer
  - DOB
  - Quadrotor Delivery
  - Unmodeled Dynamics
  - Parametric Uncertainty
  - 4 cart system
---

# DOB simulation

For this post, I'll introduce simulation results of 4-cart system. If you are not familiar with DOB, please check this [post](https://jangminhyuk.github.io/posts/2023/12/blog-post-2/)

## Relative degree

Before showing you the problem setting, I first want to explain about the concept of **relative degree**. If you have taken the undergraduate control courses, you might have heard about Relative degree. We can calculate relative degree of the system by looking at the degree of the transfer function's denomiantor and numerator.

**Relative degree : Degree of the denominator - Degree of the numerator**

I also recommend you to remember the following interpretation

**Relative degree : How many derivatives are needed to be applied to the output(y) until the input(u) becomes explicitly visible.**

Some of you might be unfamiliar with this interpretation. This concept came from the nonlinear system theory, but its extremely useful and will gave you a many insights while studying linear systems. Now, let's move on to the simulation setting.

## 1. 4-Cart system

Let's first look at the figure below
<center>
  <img src='/images/Blog_img/DOB_post/DOB_4cart.jpg' width='800' height='500' />
  <figcaption>Nominal system : 2-cart, True system : 4-cart</figcaption>
</center>
Assume that we have the nominal model consists of two cart(mass) with spring attached. However, imagine that the true(unknown) system was actually a 4-cart system. We can apply the force into the $m_1$ cart, and the output y of the cart is the position of the second cart. Let the nominal parameter $k=m_1=m_2=1$. Also let true(unknown) parameter as $m_1=1.05$, $m_2=0.95$, $m_3=1.2$, $k=0.5$, $k_1=0.5$, $k_2=0.5$. Additionally, assume sinusoidal disturbance $d=3 \sin{1.5t}$ is added to the input before fed into the true system.

### Control Objective : Starting from the origin, move the second cart($y=x_2$) to position $y=1m$ and stabilize the system.

This problems seems to to be extremely challenging because we do not have information of the true system dynamics(with additional 2-cart attached). Also, we do not have information of the true system parameters, such as mass or spring constants, which makes the problem even more challenging. Despite this unmodeled dynamics and parametric uncertainties with external disturbances, I will show how DOB could surprisingly help us to solve this challenging problem.

To check whether the DOB is appliable or not, we need to check the relative degree of the system. Remember the second definition I mentioned above. We can easily infer from the diagram that the relatively degree will remain the same between the nominal system and the true system. This is because the relative degree have the meaning of how many derivatives are needed to be applied to the output until the input u becomes explicitly visible. As the relative position of u and y remains consistent, the relative degree is conserved. 

For the readers, let's re-check whether the relative degree is conserved by deriving the transfer functions of both nominal and true systems.

Equation of the nominal system:
- $m_{1,n}\ddot{x}_1 = k_n (y-x_1)+u$
- $m_{2,n}\ddot{y} = k_n (x_1 -y)$

With the above equation, we can derive the transfer function of the nominal system:
- $P_n (s) = \frac{k_n}{ m_{1,n}m_{2,n}s^4 + k_n(m_{1,n}+m_{2,n})s^2 }$
where the relative degree is 4

For the true system, 
- $m_4 \ddot{x}_4 = k_2 (x_3-x_4)$
- $m_3 \ddot{x}_3 = k_1 (x_1-x_3)+k_2(x_4-x_3)$
- $m_1 \ddot{x}_1 = u + k(y-x_1) + k_1 (x_3-x_1)$
- $m_2 \ddot{y} = k(x_1-y)$

Obtaining transfer function of this true system are slight complicated. We finally get the transfer function $P(s)$

$\frac{Y}{U} = \frac{ k \left\{ m_3m_4s^4+(m_3k_2+m_4(k_1+k_2))s^2+k_1k_2 \right\} }{ D }$

where

$ D =(& m_1m_2s^4+(km_1+km_2+k_1m_2)s^2 + k k_1  )( m_3m_4s^4+(m_4k_1+m_4k_2+m_3k_2)s^2+k_1k_2 )-(m_2s^2+k)(k_2+m_4s^2)k_1^2 $.

For the true system, Relative degree = 8-4 = 4.

We can found out that the true system and the nominal system have the same relative degree of 4. 

Of course, for the real world applications, we couldn't get the relative degree of the true system by calculating the true transfer function as above. However, if the "relative position" between input and output remains the same, we can "claim" that the relative degree remains the same. As we have checked that the relative degree remains same for this 4-cart system, let's see how DOB can be applied.

## Q-filter

As the relative degree of the system = 4, let's use the Q-filter as

$Q(s)=\frac{a_0}{\tau^4s^4+a_3\tau^3s^3+a_2\tau^2s^2+a_1\tau+a_0}$

where $a_3=3$, $a_2=3$, $a_1=1$, $a_0=0.2$. If the DOB has been successfully applied, the system will behave just like the nominal 2-cart model.

For the nominal 2-cart problem, let's use basic lead-lag compensator $C(s)=-\frac{6.83s^2-1.84s-0.28}{s^2+4.27s+6.07}$, which was designed using the nominal parameters with 2-cart nominal dynamics.

Now, let's check the power of the DOB

## Simulation result

<img src='/images/Blog_img/DOB_post/DOB_2cart_4cart_m4_0.1_tau_0.025.jpg' width='500' height='300' />
<img src='/images/Blog_img/DOB_post/DOB_2cart_4cart_m4_0.1_tau_0.01.jpg' width='500' height='300' />
<img src='/images/Blog_img/DOB_post/DOB_2cart_4cart_m4_5_tau_0.025.jpg' width='500' height='300' />
<img src='/images/Blog_img/DOB_post/DOB_2cart_4cart_m4_5_tau_0.01.jpg' width='500' height='300' />

The red line indicates the output y(position of the second cart) for the ideal case when the controller is applied to the nominal system(2-cart). The blue line indicates the output y of the true 4-cart system. You can see that the output y is well stabilized to the position y = 1m. Also, you can see that the blue line get closer to the red line with smaller $\tau=0.01$. It is well-known that the performance of the DOB as we decreases the $\tau$. But, make sure you don't take "Too" small $\tau$ since it could increses the effect of the unmodeled fast-dynamics. For the real-world implementation, you should find proper $\tau$ and Q-filter coefficients by trial and error.

## Conclusion

Throughout this post, I've shown the simulation result for handling 4-cart sytem with the 2-cart nominal model using DOB. It is really surprising that DOB could stabilizes the system which is combined with parametric uncertainties + unmodeled dynamics + external disturbances. Imagine you are shaking a mass-spring cart without knowledge of the extra cart attached. It would be extremely hard, isn't it? 

I hope this simple magic-like-technology has attracted your mind. Next post will be about more complicated simulation using quadrotor-delivery dynamics with MPC. Stay tuned for the next post!

