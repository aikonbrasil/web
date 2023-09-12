---
title: 'Custom Access Point with PandaBoard'
date: 2021-07-03
permalink: /tips/2021/07/accesspoint/
author_profile: false
read_more: enabled
tags:
  - Access Point WiFi
  - Embbedded Systems
  - WiFi
  - Pandaboard
---

***Abstract:*** A traditional board that was very used 10 years ago is Pandaboard, which is an OMAP4430 platform designed to provide access to as many of the powerful features of the OMAP4430 Multimedia Processor as possible, while maintaining a low cost. This will allow the user to develop software to utilize the features of the powerful OMAP4430 processor. In addition, by providing expandability via onboard connectors, the PandaBoard supports development of additional capabilities/functionality. This embedded system can be set up to run as an WiFi Access Point. This short post aims to provide a step by step receipt of the technical procedure.



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