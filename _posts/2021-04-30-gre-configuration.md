---
title: 'GRE simple configuration'
date: 2021-04-30
permalink: /tips/2021/04/gre/
author_profile: false
tags:
  - network
  - tunnel
  - L2
---

How to set up a L2 Tunnel ?
======

In every communication network, the transport layer plays a fundamental rule. Usually these communication networks are a conjunction of many networks. In parallel, some protocols, such as IEC-61850, transport specific messages with special requirements. For instance, sampled values (SV) message is transmitted over L2 in order to reduce latency using in most of the cases UDP packages. For this setup, it is mandatory to create specific tunnels at L2. One option to handle this type of tunnels is Generic Routing Encapsulation (GRE).

Here, the following configuration was used to deploy a GRE Tunnel:

First Router Configuration
------
![GRE Router 1](http://aikonbrasil.github.io/web/images/gre_1.png)

Second Router Configuration
------
![GRE Router 2](http://aikonbrasil.github.io/web/images/gre_2.PNG)