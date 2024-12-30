---
title: 'Started kit Nvidia-Nano-2GB'
date: 2024-10-21
permalink: /knowhow/nvidianano/
author_profile: false
read_more: enabled
tags:
  - machine learning
  - hardware
  - started Kit
---

***Abstract:*** In the last years many AIML applications are getting popular, most of them are constrained to computer simulations without any hardware implication. In this case, the target is to get in touch with Nvidia hardware for a potential run-up on real applications, for example robotics. 

Resources
======

By now, the Nvidia-Nano-2B is already waiting for the next components, such as cooler and a microSD-card. In addition, the plan is to buy a raspberry cam (Raspberry Pi Camera Module 2) to do an basic image application. 

[Nvidia-Nano-2G](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit) outdated information, but still valid. The hardware is not anymore available, but the intention is to buy later an advanved version, such as these new [Nano boards](https://developer.nvidia.com/buy-jetson?product=all&location=FI).

[Reference Video](https://www.youtube.com/watch?v=1BneqPdEhMM) here there is a basic good reference to follow.

[Getting Nvidia certificate](https://developer.nvidia.com/embedded/learn/jetson-ai-certification-programs#jetson_ai_ambassador) is a good chance to use the Jetson Nano 2GB to get a certificate.


List
=====

1. item 1
2. item 2



To make FAN to work
======

1. go and follow the instructions defined in this repo: [Jetson Fan CTL](https://github.com/pyrestone/jetson-fan-ctl)
2. Extra: editing FAN configuration: ```edit /etc/automagic-fan/config.json```




TO UPGRADE THE JETSON
======

1. edit ```etc/apt/sources.list.d/nvidia-l4t-apt-source.list``` to point to the 35.1 repo. To do it just change the version to r35.1 in both lines.
2. use the following command: ```sudo apt update```
3. use the following command: ```sudo apt dist-upgrade```

Example:
```
*****@jetson:~$ cat /etc/apt/sources.list.d/nvidia-l4t-apt-source.list
deb https://repo.download.nvidia.com/jetson/common r35.1 main
deb https://repo.download.nvidia.com/jetson/t210 r35.1 main
```


TO INSTALL JTOP
================

Another important tool is to install the JTOP tool. It is used to monitor the system statistics, including CPU and GPU. Details are provided in the following link [Installing JTOP](https://jetsonhacks.com/2023/02/07/jtop-the-ultimate-tool-for-monitoring-nvidia-jetson-devices/)

