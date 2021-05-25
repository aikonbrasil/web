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

![\mathcal{\tau;t}=\sum_n \alpha_n(t)e^{-j2\pi f_c\tau_n(t)} \delta[\tau-\tau_n(t)]](https://latex.codecogs.com/svg.latex?\Large&space; \mathcal{\tau;t}=\sum_n \alpha_n(t)e^{-j2\pi f_c\tau_n(t)} \delta[\tau-\tau_n(t)])


Creating the DB platform
-------
