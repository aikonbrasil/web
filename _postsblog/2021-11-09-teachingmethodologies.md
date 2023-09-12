---
title: 'Teaching Methodologies'
date: 2021-11-09
permalink: /tips/2021/11/teaching/
author_profile: false
read_more: enabled
tags:
  - Teaching Methodologies
  - Bachelor Students


---

***Abstract:*** Some key ideas of a short course about teaching methodologies



Learning theories
=======
between many options the most popular in the discussion constructive learning theory mixed with humanistic can be an interesting approach. Constructive provides the ground based on self-learning and guidance, and humanistic provides freedom and flexibility to use the technical knowledge to create and innovate. 

Esperience of experts: 
-----------
It is up to the type of participants (bachelors, PhD students, subject type, etc). It is important to concider that the audience is always different. As professor, we should avoid monologs. As teacher you should admit that you are not in front of your audience showing your own goodness. At the end teacher will use a mix of these theoretic learning methodologies. It is more important what the students are doing compared to what teacher is doing. Teachers always should be able to use a flexible and dynamic approach.


Paper discussion about preconcepts and missconceptios:
=================

Title: "Students presisted preconception and learing economic principles"

Suggestion: It is very important to be aware of preconceptios and missconceptions that students can show in classes. The comparison was done based on the gain for each student (difference between pre-test and post-test).

Anonymous polls are used to check pre-conceptions or initial intuitions of what they think is correct or not. It is a kind of constructivism approach.


Group discussion:
=============


I usually ask them a simple question: How they think that a whatsapp message achieve its final destination on any spot in the world?
Based on their answers (sometimes is preconcept or missconception).As professors, we try to construct a proper answer based on the information used in the initial answer and complementing it with key insights to get the correct answer formation.


Education activities, miss... pre... 

starting to draw by themselfs, general tolerances and compare this results with standar techniques.

TASK:
=====
Try an experiment with current students.

1.- Start planning your development work:
    * Describe what you are developing? why you have chosen just that?
    * What is the new method/idea/way of doing that you are aiming at?
    * is there something you could do in collcaboration with our colleagues? what would be the benefits ?
    * How are you planning to evaluate the success of ....

2.-  What should be the length of the manuscript: 6-8 pages. 

6520 ROOM


Creating of Digital Learning Materials and Video and Sharing Tools:
============

www.toptools4learning.com/


USE ICE BREAKER : annonymous polls, 1.5 hours of conference and use a text wall to answer questions

AUDIENCE ACTIVATION:

Question and ANSWERS


REMINDER TASK:
============

Development plan length = FREE

WHAT?
WHAT METHODOLOGY?
WHAT ARE THE METHODS?
WHAT ARE YOU GOING TO DEVELOP?




EXAMPLE PLAN FROM TAMK:




BONUS IDEA:
=======

SEFI BARCELONA 
19-22 September 2022

ENGINEERING EDUCATION in EUROPE





Keynote 02
=======
FUAVE – Finnish UAV Ecosystem

Eija Honkavaara, FGI

what is FUAVE?, the idea is to create a bridge between academy and society

Hanny Karvonen
fn.sn@vtt.fi

Juha Roning
fn.sn@oulu.fi

FUAVE Temp D-Areas available/planned (interesting to test drones with all lay concerns and permissions to fly)

FUAVE Multidiscplinary disruptive Research

www.fuave.fi/research

Keynote 03
=======
Europe and Finland in the revolution of unmanned electrified aviation

Petri Mononen, VTT

UTM & U.Space: enabling complex drone operations

Funding from SESAR JU, H2020, Horizon Europe 2021 (not an specific topic for UAVs)

Drones4safety, rapid, 5Daerosafe, ..., TINDAIR, ...

P2P collab in drones: UIC2, SESAR JU VLDs, Intelligent transportation systems, 

VTT + UAVs:
AirMOUR: 
DROLO:  RDI

Keynote 04
======
UAV Projects: 5G!Drones, HYFLIERS, DroneMaster, RoboMesh, FF2020

Juha Röning, University of Oulu


megatronic devices (uavs)

ADRA???

5G!Drones

HYFLIERS: oil Industry, uAVs should inspect the . Satellite , some videos are available...

ROboMESH: UAVs to collaborate

MRAT-SafeDrone: 

DroneMaser: www.dronemaster.fi


Keynote 05
======
UAV Projects: VED, UCNDrones, UAM Oulu

Vadim Kramar, Oulu University of Applied Sciences

UCN DRONES: www.UAS-Finland.eu


BREAK:
=====

SPS members are not receiving the EMAIL broadcasting ...


Keynote 06
=====
AFDA Keynote

Tuija Karanko, Association of Finnish Defence and Aerospace Industries

Are there restriction to provide Passport to researchers onit?
It depends of the nature of the nature of research project. 

Keynote 07
=====
Drone applications in mineral exploration

Ari Saarteenoja, Radai Ltd

Geophysical Surveys with Drones

measurement of magnetic with ANTENNAS OMNI and other specialized for mineral exploration.

50 min. of flying 

getting access from them: it is possible to do it. 

Challenges???

DATASET of SIGNAL Straingt *******


Keynote 08
=====
Geodrone6 in professional data collecting and surveying

Eero Vihavainen, Geotrim Ltd

Agriculture applications: Fast, flexible and easy to use.

hovering vs operating speed
without payload vs with Payload


GEOTRIM - Nordic Drones - 

corridor mission 8.5 km.

other: 10 m/s  -- 20 km

Other corridor
32 min
8 m/s
15 km
terrain follow


Keynote 09
=====
Nokia’s recent contribution in drone ecosystem

Juha Hannula, Nokia

Radio developing Oulu

DroLo: www.drolo.fi



Keynote 10
======
Wrap Up

Kimmo Paajanen, Oulu University of Applied Sciences







Embedded System on Pandaboard
=======

The Pandaboard is running the ARM version of ArchLinux, the installation is detailed in [ArchLinux Installation](https://archlinuxarm.org/platforms/armv7/ti/pandaboard).


Softwares and Setup on ArchLinux
=======

+ ***INSTALLING  hostapd:***

    ```pacman -S hostapd```  


    Adjust the options in hostapd configuration file if necessary. Especially, change the ssid and the wpa_passphrase. See hostapd Linux documentation page for more information.

    /etc/hostapd/hostapd.conf

    ```sh
    ssid=COVID19
    country_code=FI
    interface=wlan0_ap
    bridge=br0
    ssid=YourWiFiName
    country_code=US
    hw_mode=g
    channel=7
    max_num_sta=5
    wpa=2
    auth_algs=1
    wpa_pairwise=CCMP
    wpa_key_mgmt=WPA-PSK
    wpa_passphrase=Somepassphrase
    logger_stdout=-1
    logger_stdout_level=2
    ```

+ ***INSTALLING dhcp***


    ```pacman -S dhcp```


    adjust the configuration file: /etc/dhcpd.conf


    ```sh
    option domain-name-servers 8.8.8.8, 8.8.4.4;
    subnet 192.168.123.0 netmask 255.255.255.0{
    }

    subnet 192.168.123.0 netmask 255.255.255.0{
    range 192.168.123.150 192.168.123.160;
    }
    ```

+ ***Getting default initialization to WiFi Interface***


    Create a static configuration for WLAN doing the following:


    Board $> cat /lib/systemd/network/hostapd.network

    ```sh
    [Match]
    Name=wlan0

    [Network]
    Address=192.168.72.1/24
    DHCPServer=yes
    IPForward=ipv4
    IPMasquerade=yes
    ```


+ ***CONFIGURING IPTABLES (NAT)***


    NOTE: it should be done after the WLAN interface got an IP.

    ```sh
    sysctl net.ipv4.ip_forward=1
    iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
    iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT 
    ```

+ ***Enabling Daemons***

    ```sh
    systemctl enable dhcpd4.service
    systemctl enable hostapd.service
    ```