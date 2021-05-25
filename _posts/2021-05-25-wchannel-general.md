---
title: 'Fading Multipath Channels'
date: 2021-05-25
permalink: /tips/2021/05/fading/
author_profile: false
read_more: enabled
tags:
  - Wireless Communication
  - Theory
  - Fading
  - Multipath
---

***Abstract:*** Most of the edge research in wireless communication is based on theory studies. It is extremely difficult to model a truly wireless communication as it is happening in the real world. However, there are very well accurated mathematical models that aims to represent some specific scenarios. 

Fading Multipath Channels
=======

To characterize the time-variant multipath channel statistically. So, let us examine the effects of the channel on a transmitted signal that is represented as


![s(t)=Re\left[s_l(t)e^{j2\pi f_ct}\right]](https://latex.codecogs.com/svg.latex?\Large&space;s(t)=Re\left[s_l(t)e^{j2\pi f_ct}\right]) 

Assuming a multiple propagation paths, a propagation delay and an attenuation factor is considered for each path, both are time-variant because the changes in the medium. For this reason, the received band-pass may be expressed as

![x(t)=\sum_n \alpha_n(t) s[t-\tau_n(t)]](https://latex.codecogs.com/svg.latex?\Large&space; x(t)=\sum_n \alpha_n(t) s[t-\tau_n(t)] )

it follows that the equivalent low-pass received signal is 

![\mathcal{c}(\tau;t)=\sum_n \alpha_n(t)e^{-j2\pi f_c\tau_n(t)} \delta[\tau-\tau_n(t)]](https://latex.codecogs.com/svg.latex?\Large&space; \mathcal{C}(\tau;t)=\sum_n \alpha_n(t)e^{-j2\pi f_c\tau_n(t)} \delta[\tau-\tau_n(t)])

when the equivalent low-pass received signal, is analyzed as a tropospheric scatter channel, the previous model is replicated, but in the continuum multipath domain. It is expected  that ![\alpha](https://latex.codecogs.com/svg.latex?\; \alpha_n(t)) and ![\tau](https://latex.codecogs.com/svg.latex?\; \tau_n(t)) change sufficiently at different rates and in an unpredictable manner. When there are a large number of paths, the central limit theorem can be applied. That is, the equivalent low-pass received signal may be modeled as a complex-valued Gaussian random process. This means that the time-variant impulse response ![c(tau,t)](https://latex.codecogs.com/svg.latex?\; \mathcal{c}(\tau, t)) is a complex-valued Gaussian random process in the ![tau](https://latex.codecogs.com/svg.latex?\; t) variable.


Creating the DB platform
-------
