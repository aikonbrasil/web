---
title: 'Python for Computer Science - Introduction'
date: 2021-12-10
permalink: /tips/2021/10/i2cs/
author_profile: true
read_more: enabled
tags:
  - Python
  - Teaching
  - MiniConda
  - Docker
  - Containers
  - Computer Science

---

***Abstract:*** A short screenshot of the current teaching activity that I am doing at LUT University. It is a introduction to computer science course in which Python is used as primary language programming.

Most of the environment is builded in Linux (Ubuntu, ArchLinux). However, most of student still prefer to use Windows. So, here I add some tips to do it using VirtualBox, MiniConda, etc.

As a complement, I highlight critical tips based on tools, such as Docker and Containers. 



Building the Development environment in Windows
=======

<ol>
  <li>Installing VirtualBox and MiniConda:</li>


 Installing [VirtualBox](https://www.virtualbox.org/wiki/Downloads).

 Installing [MiniConda](https://docs.conda.io/en/latest/miniconda.html).

  <li>Installing Jupyter in Miniconda Console</li>

> ``` conda install -c conda-forge jupyterlab```

  <li>Third item</li>
  <li>Fourth item</li>
</ol> 


Keynote: What is CE marking?

Jukka Vuorinen, Director, Global Key Accounts at Intertek Finland

Efficiency Energy usage, Nano materials, etc in many potential technologies, for instance in UAVs. It will provide big business opportunities, but with risks.

What are the typical markets were you can see in the label of products.Risk analysis: (Documentation, artificial intelligence, etc.)

www.dedrone.com --> incidents with Drones and challenges with them.

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