---
title: "System Level Simulation on Cellular Networks"
collection: teaching
type: "Post graduate Course"
permalink: /teaching/2020-autumn -teaching-1
venue: "LUT University, Energy Systems"
date: 2020-09-01
location: "Lappeenranta, Finland"
---

This is an introductory course on simulation of cellular networks using ns3

Pre-installation and ns3 environment
======

(1) Installing the environment: As it was indicated in the reference lectures,  ns3 can be installed in any Linux Distribution, such as Ubuntu. However, in this course, we advice to use ArchLinux, which enables a transparent installation of ns3. We indicate to install this Linux distribution (ArchLinux) in a Virtual Machine, such as VirtualBox. To do it, you can use the diversity of tutorials in Youtube or you can follow the step-by-step tutorial indicated in the following video 

[Environment](https://www.youtube.com/watch?v=dr9ghhDZVVA)

(Note: Use the playback option on 0.25 to check details).

This step is fundamental for the next activities. So, please feel free to contact me to the E-mail: dick.carrillo.melgarejo@lut.fi. I will be able to assist you by zoom, the idea is to solve any potential issue.


(2) Installing ns3:

    Create an account in https://bitbucket.org
    Send your account login to the following E-mail: dick.carrillo.melgarejo@lut.fi using the subject: "bitbucket-ns3-login".
    After you receive the confirmation of the access, you should run the following command in the Linux Console.
    $ git clone https://dcarrillom@bitbucket.org/dcarrillom/lut2020ns3.git
    Install some dependencies, such as Python and Python-matplotlib. In the particular case of ArchLinux, to install them you should run the following in the command line:
    $ sudo pacman -S python python-matplotlib
    In the Linux console, you should write the following:
    $ cd lut2020ns3
    $ ./waf clean
    $ ./waf configure --build-profile=debug --enable-examples --enable-tests
    $ ./waf build
    As initial delivery, which should be added to the task of Sec. 5.1, please run the following and indicate the output message.
    $ ./waf --run first

    Use the following video as reference to install ns3: 

[ns3 installation](https://www.youtube.com/watch?v=HT8vE9yatIg)

(Note: Use the playback option on 0.25 to check details).

General Concepts of Wireless Communication
======
<div style="text-align: justify"> 
The impact of cellular networks on society has been defined by the evolution of technologies that were used in each generation. Between 1G to 2G,  there was a transition from analog to digital communications. In 3G, the frequency spectrum efficiency was improving based on techniques that compressed the audio signal during a call. The 4G revolutionized the cellular network industry because it was the first system supporting an end-to-end packet-switched network; for instance, voice calls can be done using a full IP network. Other important difference with previous generations was that data speed achieved 100 Mbps for devices in movement and 1 Gps for devices on fixed positions. Finally, the 5G (the generation that is being deployed now) aims to support not only human demands, but also vertical (machine-type) applications, such as control and automation targeting latency as low as 5 ms. 5G is currently introduced on commercial applications and the most significant feature is the increased data rate when compared with the previous generation, which is expected to achieve 10 Gbps.
</div>


<div style="text-align: justify"> 
There are a variety of options to study and analyze cellular networks. Academic institutions usually prioritize communication theory frameworks, focusing on specific network layer features, such as physical layer considering only symbol level analyses, usually this mathematical framework is compared with Monte Carlo simulation to validate results. In the case of industry, it mostly prioritizes complex simulator that aims to reproduce real scenarios with a protocol stack that is complain with the current cellular network standard. So, in general simulation of digital communication systems has a fundamental importance because it enables the design of specific scenarios and constraints using only computational resources, avoiding the high cost on development of the same scenario in a real environment.
</div>


<div style="text-align: justify"> 
In both, academy and industry, there are a diversity of simulators and tools. For instance, at link level simulation is common to consider Matlab to support specific physical layer and MAC features; in the system level simulation, Matlab can be also used; however, it presents some computational limitations by the amount of routines. For this reason, most of the system level simulators consider to use high performance programming languages, such as C++.
</div>


<div style="text-align: justify"> 
The nature of full packet-switched network of cellular networks since 4G development provides flexibility to simulate the protocol stack in specialized software. One of these tools is ns-3, which is an open-source discrete-event network simulator. It can be used to prove fundamental features on communication and also to test new features without investing in a real network deployment. Furthermore, reproducing a similar protocol stack that has been implemented on real devices.
</div>

If you are interested in details, please check the following [wireless communication](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-452-principles-of-wireless-communications-spring-2006/) reference.


Hands on with ns3 environment
======


point-to-point simulation
======

point-to-multipoint simulation
======

Advanced scenarios on 4G/5G
======