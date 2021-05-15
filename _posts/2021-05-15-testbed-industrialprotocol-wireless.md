---
title: 'IEC-61850 on a real cellular network - testbed'
date: 2021-05-15
permalink: /tips/2021/05/testbed/
author_profile: false
read_more: enabled
tags:
  - IEC-61850
  - 5G
  - 4G
  - LTE
  - Wireless
  - Real Networks
---

***Abstract:*** This is a short description of some technical issues that were used on the developing of a testbed. This testbed focused on analyze a network performance when an Industrial Protocol is used on it.

What is the main idea of the testbed ?
======

The application of wireless communication is increasing, specially in industries such as power systems. One of these protocols is IEC-61850, which was implemented mostly to support connectivity on sub-stations (power systems). This protocol is composed by many messages. SV message is one of the message that is inteded to enable connectivity between nodes that generate information from sensors and industrial end devices (IEDs). As this sensors generate critical information such as temperatura, voltage and current information, they should have a very short latency and simultaneously maintain a high reliability. 

[TBU] To Be updated ...

Physical Setup
======

The physical setup is composed by a typical cellular systems (UEs, eNBs, Core Network) and a micro grid network (inverter, rectifier, power storage, etc). Part of the development of this testbed is to develop a test system that generates IEC-61850 messages which are transmitted over the wireless network. Many issues were solved during the integration of this industrial standard that will be explained here. However, some important issues are shared in the following.


Embbeded Systems
=======

An embedded system was deployed on each node. Each embedded system is using Arch Linux as operative system and each of them is using a 1Tbyte of external hard drive to save the information that will be transmitted, processed and analyzed during the test bed. One key issue was the setup of this usbdrive on the embedded system. 

Setting up the external usb drive
-----

1. create a Linux filesystem (GPT) on the new hard drive and format it as VFAT.  


```sh
sudo mkfs.vfat /dev/sda1
```

2. edit the fstab configuration file  

```sh

sudo vim /etc/fstab
```

and edit the configuration file with the following setup

```

/dev/sda1	/home/lut/extdrive	vfat 	user,rw
```

Now the external hard drive can be used by any user with write and read rights, it can be mounted with a simple ´´´ mount extdrive  ´´´ (extdrive is a folder that you created in the path of your wish)