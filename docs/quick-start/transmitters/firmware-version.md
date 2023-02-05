---
template: main.html
description: Get to know your ExpressLRS devices' Firmware Version.
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Why do you have to know the Firmware Version?

Knowing the ExpressLRS Firmware Version that's currently in your devices will determine whether there is a need to update to a newer version or whether you can simply get your devices bound together without updating. For newcomers in the hobby, or for those just starting with ExpressLRS, it can be a bit daunting to flash a new device. 

It is still recommended that you update your gear to the latest firmware version to ensure you have all the bugfixes and latest features.

## Transmitter Module Firmware Version

There's three methods to determine what firmware version you currently have on your Transmitter module

=== "via Lua Script"

    1. Press the ++"SYS"++ Key on your Radio.
    2. You are now in the Tools Menu where Lua Scripts can be found. Scroll down and select `ExpressLRS` Lua Script.
        - If the script is nowhere to be found, download it from [this page](../transmitters/lua-howto.md) and save it into your Radio SD Card Scripts/Tools/ folder.
    3. Press ++enter++ Key to activate the Script.
        - If the script is stuck on a "Loading..." screen, go back to the [Radio Preparation](../transmitters/tx-prep.md) Page and make sure you have configured your radio properly for ExpressLRS use.
    4. Scroll to the bottom of the page and you should see the Current Version flashed into your TX module.

    -insert image of Lua Script showing the version line-

=== "via OLED Screen"

    If your External TX module is equipped with a Screen, the Home Screen should show the different parameters currently configured on the module. It will also show the current firmware version flashed into the module.

    -insert OLED screen image with the version-

=== "via Web UI"

    1. Put your module into wifi mode.

        === "via ExpressLRS Lua Script" 

            1. Press the ++"SYS"++ Key on your Radio.
            2. You are now in the Tools Menu where Lua Scripts can be found. Scroll down and select `ExpressLRS` Lua Script.
                - If the script is nowhere to be found, download it from [this page](../transmitters/lua-howto.md) and save it into your Radio SD Card Scripts/Tools/ folder.
            3. Press ++enter++ to Load it.
                - If the script is stuck on a "Loading..." screen, go back to the [Radio Preparation](../transmitters/tx-prep.md) Page and make sure you have configured your radio properly for ExpressLRS use.
            4. Scroll down and select `Wifi Connectivity` and press ++enter++.
            5. Select `Enable WiFi` and press ++enter++.
            6. The `WiFi Running` screen will show up. Your TX module is now in WiFi mode.
                - If the Script stopped and is showing a Syntax Error, do not worry. The module is still in WiFi mode. The Syntax Error could be because you're on an older radio, older EdgeTX/OpenTX firmware or both. It could also be due to the fact your TX module is on an earlier firmware version and you're using a more recent Lua Script.

        === "External Module detached from Radio"

            1. With your Tx module disconnected from your Radio module bay, power it up either via an external power source (2S) or by plugging in a USB cable into its USB Port.
            2. Let it be for 60s and the RGB LED will turn into a Green Breathing LED pattern. This indicates it is now in WiFi Mode.
                - TX Modules with an OLED Screen will also show a message regarding WiFi mode.

    2. Scan for the `ExpressLRS TX` Access Point. 
        ![WiFi Hotspot](../../assets/images/WifiHotspotTX.png){ align=right }

        - If your TX Module is previously flashed with your Home WiFi SSID and Password, and it is able to connect to that WiFi Network, then the Access Point will not show up.
        - `expresslrs` is the Password for this Access Point.

        <br clear="right" />

    3. Load the Web UI on your browser using these addresses:
        - http://10.0.0.1/ -If you have connected to the `ExpressLRS TX` Access Point
            
            !!! Note
                This IP address is also often being used by some routers. Computers with an ethernet connection to their routers will find that this page doesn't load the ExpressLRS Web UI and instead loads their router or ISP modem configuration dashboards.

                We recommend disconnecting from the network first, or try a different device instead, e.g. smartphone or tablet.
        
        - http://elrs_tx.local - If you have previously set your Home WiFi SSID and Password into your TX Module when you flashed it.

            !!! Note
                Some computers and networks cannot resolve this address if MDNS is not working. 

            ??? tip "Use the IP Address instead!"
                === "The `arp` Command"

                    1. Open up a Command Prompt window on your computer.
                    2. Execute the command `arp -a` which will list all the devices in the Network.
                    3. Use each of the IP Addresses marked as `Dynamic` as URL into your Browser until you get to the ExpressLRS Web UI.

                === "Router DHCP List"
                    1. Log in into your Router dashboard.
                    2. Check the DHCP List and look for the "elrs" device.
                    3. Take note of the IP Address given by your router.
                    4. Use this IP address into your Browser as the URL.

    4. The Banner of the Web UI should tell you the firmware version flashed into your Tx module.

        -Insert Image of the new Web UI Banner for TX-

<hr />

Once you have determined the firmware version that's currently flashed into your Transmitter module, you can now decide to whether keep using it as is or update to the latest version. 

!!! Info "Versioning Scheme"
    The ExpressLRS Firmware Versioning scheme is based on the [semantic versioning scheme](https://semver.org/).

    A Version is defined or formatted as "Major.Minor.Patch"

        - major = major new feature and/or incompatible changes
        - minor = minor features or enhancements and/or new targets
        - patch = bug-fixes
    
    That first number in the Version string should match between a TX Module and a Receiver.
    Examples:

    - a TX Module with version string of 3.1.2 will sync and work with a Receiver with firmware version 3.0.1
    - a TX Module with version string of 3.2.0 will NOT sync or bind with a Receiver with firmware version 2.4.0


For the latest ExpressLRS firmware version, check the [Releases page in Git Hub](https://github.com/ExpressLRS/ExpressLRS/releases)

