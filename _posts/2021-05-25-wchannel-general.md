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

when the equivalent low-pass received signal, is analyzed as a tropospheric scatter channel, the previous model is replicated, but in the continuum multipath domain. It is expected  that ![\alpha](https://latex.codecogs.com/svg.latex?\; \alpha_n(t)) and ![\tau](https://latex.codecogs.com/svg.latex?\; \tau_n(t)) change sufficiently at different rates and in an unpredictable manner. When there are a large number of paths, the central limit theorem can be applied. That is, the equivalent low-pass received signal (![r_l(t)](https://latex.codecogs.com/svg.latex?\;r_l(t))) may be modeled as a complex-valued Gaussian random process. This means that the time-variant impulse response ![c(tau,t)](https://latex.codecogs.com/svg.latex?\;\mathcal{C}(\tau, t)) is a complex-valued Gaussian random process in the ![tau](https://latex.codecogs.com/svg.latex?\; t) variable.

As a consequence on signal ![r_l(t)](https://latex.codecogs.com/svg.latex?\;r_l(t)), the multiplath propagation model will result in signal fading. The fading phenomenon is a result of time variant of the phase and in the amplitude (<em> signal fading </em>). Which are due to the time-variant multipath characteristics of the channel.

When the impulse response ![c(tau,t)](https://latex.codecogs.com/svg.latex?\;\mathcal{C}(\tau, t)) aims to model  a moving scattererers scenario, it is modeled as a zero-mean complex-valued Gaussian process, the envelope ![c(tau,t)](https://latex.codecogs.com/svg.latex?\;Abs(\mathcal{C}(\tau,t))) is Rayleigh-distributed (<em> Rayleigh fading channel</em>). In the event that there are fixed scatterers or signal reflectors in the medium, in addition to randomly moving scatterers, the envelope ![c(tau,t)](https://latex.codecogs.com/svg.latex?\;Abs(\mathcal{C}(\tau, t))) has a Rice distribution (<em> Ricean fading channel</em>).

It is important to remark that these distribution functions aims to model the envelope of fading signals



Creating the DB platform 
-------
