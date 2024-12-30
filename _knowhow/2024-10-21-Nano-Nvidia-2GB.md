---
title: 'Started kit Nvidia-Nano-2GB'
date: 2024-12-30
permalink: /knowhow/nvidianano/
author_profile: false
read_more: enabled
tags:
  - machine learning
  - hardware
  - started Kit
  - nvidia
---

***Abstract:*** In the last years many AIML applications are getting popular, most of them are constrained to computer simulations without any hardware implication. In this case, the target is to get in touch with Nvidia hardware for a potential run-up on real applications, for example robotics. 

Resources
======

By now, the Nvidia-Nano-2B is already waiting for the next components, such as cooler and a microSD-card. In addition, the plan is to buy a raspberry cam (Raspberry Pi Camera Module 2) to do an basic image application. 

[Nvidia-Nano-2G](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit) outdated information, but still valid. The hardware is not anymore available, but the intention is to buy later an advanved version, such as these new [Nano boards](https://developer.nvidia.com/buy-jetson?product=all&location=FI).

[Reference Video](https://www.youtube.com/watch?v=1BneqPdEhMM) here there is a basic good reference to follow.

[Getting Nvidia certificate](https://developer.nvidia.com/embedded/learn/jetson-ai-certification-programs#jetson_ai_ambassador) is a good chance to use the Jetson Nano 2GB to get a certificate.


To make FAN to work
======

go and follow the instructions defined in this repo: [Jetson Fan CTL](https://github.com/pyrestone/jetson-fan-ctl)

1. Clone the repository.
2. run the following ```sudo ./install.sh```. The script will automatically run at boot time. It's a set-it-and-forget-it type thing, unless you want to mess with the fan speeds.

2. Customizing/setting the FAN: editing FAN configuration: ```vim /etc/automagic-fan/config.json```
   ```
   {
	"FAN_OFF_TEMP":20,
	"FAN_MAX_TEMP":50,
	"UPDATE_INTERVAL":2,
	"MAX_PERF":1
	}
   ```
   
   ```FAN_OFF_TEMP``` is the temperature (°C) below which the fan is turned off.
	```FAN_MAX_TEMP``` is the temperature (°C) above which the fan is at 100% speed.
	The script interpolates linearly between these two points.

	```UPDATE_INTERVAL``` tells the script how often to update the fan speed (in seconds).
	```MAX_PERF``` values greater than 0 maximize system performance by setting the CPU and GPU clock speeds to the maximum.

	You can use either integers (like 20) or floating point numbers (like 20.125) in each of these fields.
	The temperature precision of the thermal sensors is 0.5 (°C), so don't expect this to be too precise.

	Any changes in the script will be will be applied after the next reboot.
	You can run
	```sudo service automagic-fan restart```
	to apply changes immediately.

	If you suspect something went wrong, please check: ```sudo service automagic-fan status```



TO UPGRADE THE JETSON
======

1. edit ```etc/apt/sources.list.d/nvidia-l4t-apt-source.list``` to point to the 35.1 repo. To do it just change the version to r35.1 in both lines.
2. use the following command: ```sudo apt update```
3. use the following command: ```sudo apt dist-upgrade```

Example of the content of nvidia-14t-apt-source-list:
```
*****@jetson:~$ cat /etc/apt/sources.list.d/nvidia-l4t-apt-source.list
deb https://repo.download.nvidia.com/jetson/common r35.1 main
deb https://repo.download.nvidia.com/jetson/t210 r35.1 main
```


TO INSTALL JTOP
================

Another important tool is to install the JTOP tool. It is used to monitor the system statistics, including CPU and GPU. Details are provided in the following link [Installing JTOP](https://jetsonhacks.com/2023/02/07/jtop-the-ultimate-tool-for-monitoring-nvidia-jetson-devices/)

1. ```sudo apt update```
2. ```sudo apt install python3-pip```
3. ```sudo pip3 install -u jetson-stats```
4. rebooting the system.
5. ```jtop```
