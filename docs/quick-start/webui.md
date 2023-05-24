---
template: main.html
description: The ExpressLRS Web UI is an essential part of the ExpressLRS ecosystem. WiFi Updates and Configuration can be done through it.
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/quick-start.png)

## The ExpressLRS Web UI

The ExpressLRS Web UI is an essential part of the ExpressLRS ecosystem. In earlier versions of the project, its main use is for updating the ExpressLRS firmware and logging or debugging (on select hardware).

ExpressLRS 3.0 has further expanded the capabilities of the ExpressLRS Web UI. It is now capable of changing Firmware Parameters, including the Binding Phrase, Regulatory Domain  (for the 900MHz devices), UART Inversion and more.

### The Banner

<figure markdown>
![Web UI Banner](../assets/images/web-banner.png)
<figcaption>The ExpressLRS Web UI Banner </figcaption>
</figure>

### The Options Tab

This tab allows users to change firmware options without reflashing their devices. It also allows the import and export of the Configuration from one device to another, useful for setting up backup equipment.

Options common to both Receivers and TX Modules:

- Binding Phrase: Type in your Binding Phrase here if you want to update it from either the factory setting or from an earlier flashed setting.

    !!! abstract "It's Blank!"
        This field doesn't store the plain text Binding Phrase. If you see it blank like shown, do not worry. The next field, UID, has the information.

- UID: As you type in your Binding Phrase in the field above, this read-only field will update with the UID translation. This is what actually gets saved in your device.

- Regulatory Domain: This only applies to the 900MHz system. This field allows users to change the Regulatory Domain for their device.

    !!! abstract "What about 2.4GHz?"
        The EU_CE Regulatory Domain setting is a Compile-time option and the LBT code needs to be baked in for it to work properly.
    
- WiFi "Auto On" Interval (in seconds): This field allows you to change how soon WiFi automatically activates when the device is powered up and it's not getting a valid CRSF signal (for TX Modules) or sync packets (for Receivers).

=== "Receiver Options"

    <figure markdown>
    ![Web UI Banner](../assets/images/web-options-rx.png)
    <figcaption>ExpressLRS Receiver Options Tab</figcaption>
    </figure>

    - UART Baud: The baud rate to which the receiver will send and receive signals to or from a Flight Controller, or any device. Under normal circumstances, this setting should be left at the default 420000 setting.
        - KISS V1 requires this setting to be set to 400000 because that's the baud rate the CRSF protocol is configured on this particular Flight Controller firmware.

    - Invert TX Pin: This setting should also be left disabled or unchecked under normal circumstances. It inverts the CRSF signal coming out of the TX pin of the receiver.
        - Receivers that will be connected to an SBUS pad on Flight Controllers without extra uninverted RX pads should enable this setting. Additionally the command `set serialrx_inverted = on` will be needed in the Flight Controller configuration.

    - Lock on First Connection: This setting speeds up the reconnection of a Receiver and TX Module if you don't ever change your RF Mode/Packet Rate.

=== "TX Module Options"

    <figure markdown>
    ![Web UI Banner](../assets/images/web-options-tx.png)
    <figcaption>ExpressLRS TX Module Options Tab</figcaption>
    </figure>

    - TLM Report Interval: This setting controls how often Telemetry packets are sent back to the radio. 240LU is the default setting and is already fast for EdgeTX or OpenTX.

    - UART Inverted: Keep this enabled or checked if you're using your TX module on an OpenTX or EdgeTX Radio. The S.Port pins in External Module bays are inverted bidirectional pins.

    - Fan Runtime (in seconds): This setting controls how long the fan on the TX Module will keep spinning even after the current Transmit Power of the module is already Lower than the Fan Threshold Lua Script setting.

### The WiFi Tab

<figure markdown>
![Web UI Banner](../assets/images/web-homenetwork.png)
<figcaption>ExpressLRS WebUI WiFi Tab</figcaption>
</figure>

### The Model Tab

<figure markdown>
![Web UI Banner](../assets/images/web-rxmodel.png)
<figcaption>ExpressLRS Receiver Model Tab</figcaption>
</figure>

<figure markdown>
![Web UI Banner](../assets/images/web-pwmoutput.png)
<figcaption>ExpressLRS PWM Receiver Output Settings</figcaption>
</figure>

### The Buttons Tab

This section is currently only available for the RadioMaster Ranger module.

<figure markdown>
![Web UI Banner](../assets/images/web-buttonsTX.png)
<figcaption>ExpressLRS TX Module Buttons Tab</figcaption>
</figure>

### The Update Tab

=== "Receiver Update Tab"
    <figure markdown>
    ![Web UI Banner](../assets/images/web-update-rx.png)
    <figcaption>ExpressLRS Receiver Update Tab</figcaption>
    </figure>

=== "TX Module Update Tab"
    <figure markdown>
    ![Web UI Banner](../assets/images/web-update-tx.png)
    <figcaption>ExpressLRS TX Module Update Tab</figcaption>
    </figure>

## How to get to the Web UI
=== "Receivers"
   
    1. Put your Receiver into WiFi Mode.

        === "Auto WiFi On"

            1. Make sure your Radio with your TX Module is Off.

            2. Power-cycle your receiver (turn it Off then turn it back On). The Receiver LED should be blinking slowly as shown below. 
        
                <figure markdown>
                ![RX Waiting](https://cdn.discordapp.com/attachments/738450139693449258/921065812985520268/LEDSEQ_DISCONNECTED_50_50.gif)
                </figure>

                ??? warning "Receiver LED not Blinking!"
                    If it has a Solid LED light, it may be in bootloader mode if you've only just wired it up. [Rewire](../quick-start/receivers/wiring-up.md) your receiver into a different uart. If you have attempted to update it before, then it could be soft-bricked. Follow the [Unbricking](../quick-start/unbricking.md) procedure to get it back into normal working condition.

            3. Wait for about 60 seconds or until the Receiver LED blinks rapidly indicating it is now in WiFi Mode.

                <figure markdown>
                ![RX WiFi](https://cdn.discordapp.com/attachments/738450139693449258/921065813983760384/LEDSEQ_WIFI_UPDATE_2_3.gif)
                </figure>


        === "via Lua Script"
            1. Make sure the Receiver and TX Module are in sync and bound. RSSI indicators on your Radio Home screen should be visible and the Receiver LED should be Solid as shown.

                <figure markdown>
                ![RX Bound](https://cdn.discordapp.com/attachments/738450139693449258/921065812507373568/LED_ON.gif)
                </figure>

            2. Press the ++"SYS"++ Key on your Radio.
                - Older Radios or those with only one Menu Key will need to long-press the ++context-menu++ Key to access the System Menu.
                - Consult your Radio User's Manual on how to access the System Menu.
            3. You are now in the Tools Menu where Lua Scripts can be found. Scroll down and select `ExpressLRS` Lua Script.

                <figure markdown>
                ![Lua Script]
                </figure>

                - If the script is nowhere to be found, download it from [this page](./transmitters/lua-howto.md) and save it into your Radio SD Card Scripts/Tools/ folder.
            4. Press ++enter++ to Load it.

                <figure markdown >
                ![Lua Running]
                </figure> 

                - If the script is stuck on a "Loading..." screen, go back to the [Radio Preparation](./transmitters/tx-prep.md) Page and make sure you have configured your radio properly for ExpressLRS use.
                - there should be a C in the top right corner of the Lua Script indicating TX Module and Receiver are Connected.
            5. Scroll down and select `Wifi Connectivity` and press ++enter++.
            6. Select `Enable RX WiFi` and press ++enter++.

                <figure markdown>
                ![Lua WiFi]
                </figure>

            7. The `WiFi Running` screen will briefly show up. Your Receiver is now in WiFi mode as indicated by the rapidly blinking LED.

                <figure markdown>
                ![RX WiFi](https://cdn.discordapp.com/attachments/738450139693449258/921065813983760384/LEDSEQ_WIFI_UPDATE_2_3.gif)
                </figure>

                !!! info "Note"
                    It is normal for the receiver will disconnect from the TX Module once it is in WiFi Mode. You will hear your radio announce "Telemetry Lost" if you have the sound pack on your Radio SD Card.

    4. Scan for the `ExpressLRS RX` Access Point. 
        ![WiFi Hotspot](../assets/images/WifiHotspot.png){ align=right }

        - If your Receiver is previously flashed with your Home WiFi SSID and Password, and it can connect to that WiFi Network, then the Access Point will not show up.
        - `expresslrs` is the Password for this Access Point.

        <br clear="right" />

    3. Load the Web UI on your browser using these addresses:
        - http://10.0.0.1/ - If you have connected to the `ExpressLRS RX` Access Point

            !!! Note
                This IP address is also often used by some routers. Computers with an ethernet connection to their routers will find that this page doesn't load the ExpressLRS Web UI and instead loads their router or ISP modem configuration dashboards.

                We recommend disconnecting from the network first or trying a different device instead, e.g. smartphone or tablet.

            !!! Note
                On some devices a network login prompt might pop up. Clicking this will often show an incomplete version of the webui that won't behave as expected. Please navigate to http://10.0.0.1/ manually in your browser instead.

        - http://elrs_rx.local - If you have previously set your Home WiFi SSID and Password into your Receiver when you flashed it.

            !!! Note
                If your browser cannot resolve this address, chances are MDNS is not set up and working on your computer or network.

            ??? tip "Use the IP Address instead!"
                === "The `arp` Command"

                    1. Open up a Command Prompt window on your computer.
                    2. Execute the command `arp -a` which will list all the devices in the Network.
                    3. Try each of the IP Addresses marked as `Dynamic` as a URL in your Browser until you get to the ExpressLRS Web UI.

                === "Router DHCP List"
                    1. Log in to your Router dashboard.
                    2. Check the DHCP List and look for the "elrs" device.
                    3. Take note of the IP Address given by your router.
                    4. Use this IP address in your Browser as the URL.
    
=== "TX Modules"

    1. Put your module into wifi mode.

        === "via ExpressLRS Lua Script" 

            1. Press the ++"SYS"++ Key on your Radio.
                - Older Radios or those with only one Menu Key will need to long-press the ++context-menu++ Key to access the System Menu.
                - Consult your Radio User's Manual on how to access the System Menu.
            2. You are now in the Tools Menu where Lua Scripts can be found. Scroll down and select `ExpressLRS` Lua Script.

                <figure markdown>
                ![Lua Script]
                </figure>

                - If the script is nowhere to be found, download it from [this page](./transmitters/lua-howto.md) and save it into your Radio SD Card Scripts/Tools/ folder.
            3. Press ++enter++ to Load it.

                <figure markdown >
                ![Lua Running]
                </figure> 

                - If the script is stuck on a "Loading..." screen, go back to the [Radio Preparation](./transmitters/tx-prep.md) Page and make sure you have configured your radio properly for ExpressLRS use.
            4. Scroll down and select `Wifi Connectivity` and press ++enter++.
            5. Select `Enable WiFi` and press ++enter++.

                <figure markdown>
                ![Lua WiFi]
                </figure>

            6. The `WiFi Running` screen will show up. Your TX module is now in WiFi mode.
                - If the Script stopped and is showing a Syntax Error, do not worry. The module is still in WiFi mode. The Syntax Error could be because you're on an older radio, older EdgeTX/OpenTX firmware or both. It could also be due to the fact your TX module is on an earlier firmware version and you're using a more recent Lua Script.

        === "External Module detached from Radio"

            1. With your Tx module disconnected from your Radio module bay, power it up either via an external power source (2S) or by plugging in a USB cable into its USB Port.
            2. Let it be for 60s and the RGB LED will turn into a Green Breathing LED pattern indicating it is now in WiFi Mode.
                - TX Modules with an OLED Screen will also show a message regarding WiFi mode.

    2. Scan for the `ExpressLRS TX` Access Point. 
        ![WiFi Hotspot](../assets/images/WifiHotspotTX.png){ align=right }

        - If your TX Module is previously flashed with your Home WiFi SSID and Password, and it can connect to that WiFi Network, then the Access Point will not show up.
        - `expresslrs` is the Password for this Access Point.

        <br clear="right" />

    3. Load the Web UI on your browser using these addresses:
        - http://10.0.0.1/ - If you have connected to the `ExpressLRS TX` Access Point

            !!! Note
                This IP address is also often used by some routers. Computers with an ethernet connection to their routers will find that this page doesn't load the ExpressLRS Web UI and instead loads their router or ISP modem configuration dashboards.

                We recommend disconnecting from the network first or trying a different device instead, e.g. smartphone or tablet.

            !!! Note
                On some devices a network login prompt might pop up. Clicking this will often show an incomplete version of the webui that won't behave as expected. Please navigate to http://10.0.0.1/ manually in your browser instead.

        - http://elrs_tx.local - If you have previously set your Home WiFi SSID and Password into your TX Module when you flashed it.

            !!! Note
                If your browser cannot resolve this address, chances are MDNS is not set up and working on your computer or network.

            ??? tip "Use the IP Address instead!"
                === "The `arp` Command"

                    1. Open up a Command Prompt window on your computer.
                    2. Execute the command `arp -a` which will list all the devices in the Network.
                    3. Try each of the IP Addresses marked as `Dynamic` as a URL in your Browser until you get to the ExpressLRS Web UI.

                === "Router DHCP List"
                    1. Log in to your Router dashboard.
                    2. Check the DHCP List and look for the "elrs" device.
                    3. Take note of the IP Address given by your router.
                    4. Use this IP address in your Browser as the URL.

[Lua Script]: ../assets/images/lua1.jpg
[Lua Running]: ../assets/images/lua/config-bw.png
[Lua WiFi]: ../assets/images/lua/wifi-bw.png
