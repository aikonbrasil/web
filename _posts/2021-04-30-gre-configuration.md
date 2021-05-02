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

What is a L2 Tunnel for ?
======
In every communication network, the transport layer plays a fundamental rule. Usually these communication networks are a conjunction of many networks. In parallel, some protocols, such as IEC-61850, transport specific messages with special requirements. For instance, sampled values (SV) message is transmitted over L2 in order to reduce latency using in most of the cases UDP packages. For this setup, it is mandatory to create specific tunnels at L2. One option to handle this type of tunnels is Generic Routing Encapsulation (GRE), other option is to use L2TP.


How to set up a L2 Tunnel ?
======

The main important thing is to get a good understanding of the networks that you are trying to connect through GRE. Usually the configuration is done between the routers (R1 and R2) that are connected in a specific WAN, the Tunnel will pass over this WAN in order to connect the respective LANs.

TO BE ADDED
------

Specific information of the layout used in the lab setup.

Here, the following configuration was used to deploy a GRE Tunnel:

First Router Configuration (R1)
------
![GRE Router 1](http://aikonbrasil.github.io/web/images/gre_1.png)
and the following routing police in R1
![routing policy in router 1](http://aikonbrasil.github.io/web/images/ssh_gre_1.PNG)

Second Router Configuration (R2)
------
![GRE Router 2](http://aikonbrasil.github.io/web/images/gre_2.PNG)
and the following routing police in R2
![routing policy in router 2](http://aikonbrasil.github.io/web/images/ssh_gre_2.PNG)

