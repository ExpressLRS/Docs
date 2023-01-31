---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

!!! danger "Advisory"
    1. If flashing/updating for the first time from the factory firmware or an older firmware, flash the module to version 2.5.1.
    2. Once it has the 2.5.1 flashed, update to 3.x.

    !!! info "If you've flashed it straight to 3.x and you're getting "Not Enough Space" popup during WiFi flashing, flash the receiver to 2.5.1 first,  and then flash it to 3.x. The Repartitioner is for TX only."

## Wiring up your receiver

!!! attention "Note"
    There are Flight Controllers that will pull the RX pads `LOW` which will put the ESP-based receivers into `Bootloader Mode` unintentionally. A solid LED light on these receivers even with the TX module off is a sign they are in Bootloader Mode. If this is the case, rewire the receiver to a different UART.

<figure markdown>
![BetaFPV RX connection](../../assets/images/betaFPVrx2400.png)
<figcaption>BetaFPV Nano</figcaption>
</figure>

<figure markdown>
![BetaFPV RX Lite connection](../../assets/images/betaFPVrxLite.png)
<figcaption>BetaFPV Lite (Flat & Tower)</figcaption>
</figure>

The images above show the receiver pinouts and their connections. As we're dealing with UART connection, Rx on receiver goes to a TX pad on the FC, and Tx on the receiver goes to an uninverted Rx pad on the FC.

There are Flight Controllers that put their Receiver UART's RX pads Low, which in turn, puts the ESP-based (e.g. EP1 and EP2) receivers to Bootloader mode unintentionally. One remedy is to wire them into a different UART, or wire a pull-up resistor (300-1k ohm) between the Rx pad of the FC and a 3.3v or 5v pad, as shown below.

<figure markdown>
![pull up](../../assets/images/pull-up.png)
<figcaption>Wiring up receiver</figcaption>
</figure>

## Configuring your Flight Controller

To configure your flight controller properly, please go through [Configure FC page](configuring-fc.md). These settings apply on INAV, Betaflight and other flight controller software.

Ports Tab should be setup so that Serial RX is on the UART where you have soldered the receiver.

Receiver protocol is `CRSF` with `serialrx_inverted = off` and `serialrx_halfduplex = off`.

The next step will not be able to proceed properly and you'll have issues later if any of these are set differently. Once you have configured your Flight Controller software, close its Configurator and unplug-replug the USB cable from the FC or your computer. This will refresh the connection and you'll be ensured that the port is not busy (of high importance with the Passthrough Flashing Method).

## <span class="custom-heading" data-id="1">Flashing via WiFi</span>

??? Note "Flashing via WiFi"

    - Target: `BETAFPV_Nano_2400_RX_via_WIFI`

    - Device Category: `BETAFPV 2.4 GHz`

    - Device: `BETAFPV Nano 2400 RX`, `BETAFPV Lite 2400 RX` (Tower & Flattie)

    <figure markdown>
    ![via WiFi](../../assets/images/Method_RX_WiFi.png)
    <figcaption>Flashing via WiFi</figcaption>
    </figure>

    ### <span class="custom-heading" data-id="2">Method 1</span>

    ??? Note "Method 1"

        1. [Wire] your receiver properly with FC.
        2. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
        3. Build the firmware, which will open the Target folder where the `BETAFPV_Nano_2400_RX-<version>.bin` file is located. Do not close this window so you can easily locate the correct file to upload to the module.

            <figure markdown>
            ![Build]
            </figure>

        4. Power your FC by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The receiver's LED will blink slowly at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi Hotspot Mode.

            <figure markdown>
            ![LEDSEQ_WIFI_UPDATE](https://cdn.discordapp.com/attachments/738450139693449258/921065813983760384/LEDSEQ_WIFI_UPDATE_2_3.gif)
            </figure>

        5. Connect to the Access Point created by the module, named `ExpressLRS TX`, using the password `expresslrs`.

            <figure markdown>
            ![WiFi Hotspot](../../assets/images/WifiHotspot.png)
            </figure>

        6. Open your browser and navigate to http://10.0.0.1/ to access the upload form. Scroll down to find the form.
        7. Drag and drop the firmware file, `BETAFPV_Nano_2400_RX-<version>.bin`, created by the ExpressLRS Configurator. Alternatively, use the `Choose File` button to select the file from the folder where the firmware was created.
        8. Ensure that you have selected the correct firmware file and click `Update`.
        9. A white page should load with the message "Update Success! Rebooting...."
        10. Wait until the LED on the Receiver starts to blink slowly again
        11. Receiver should be updated after waiting a little bit
        12. Power cycle the receiver
        13. Receiver should be able to bind with your TX module, if the Tx Module has also been updated and they have the same binding phrase and options.

        !!! info
            You can configure Home Network SSID and Password if you chose not to use ExpressLRS Configurator to set them. Once these are set, you can use the next two methods below.

        <figure markdown>
        ![JoinNetwork](../../assets/images/web-joinnetwork.png)
        </figure>

    ### <span class="custom-heading" data-id="3">Method 2</span>

    ??? Note "Method 2"

        !!! note "Note"
            This method will only work once the Home Network SSID and Password has been configured with the receiver.

        1. [Wire] your receiver properly with FC.
        2. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
        3. Build the firmware, which will open the Target folder where the `BETAFPV_Nano_2400_RX-<version>.bin` file is located. Do not close this window so you can easily locate the correct file to upload to the module.

            <figure markdown>
            ![Build]
            </figure>
        4. Power your FC by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The receiver's LED will blink slowly at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi AP Mode.
        5. The fast blink will pause and flash fast once again, indicating connection to your Home Network.

            <figure markdown>
            ![LEDSEQ_WIFI_UPDATE](https://cdn.discordapp.com/attachments/738450139693449258/921065813983760384/LEDSEQ_WIFI_UPDATE_2_3.gif)
            </figure>

        6. Open your browser and navigate to http://elrs_rx.local/ to access the upload form. It should show your device target along with the version of the firmware it currently has.
        7. Scroll down to the Firmware Update section, shown below:

            <figure markdown>
            ![Firmware Update](../../assets/images/web-firmwareupdate.png)
            </figure>

        8. Drag and drop the firmware file, `BETAFPV_Nano_2400_RX-<version>.bin`, created by the ExpressLRS Configurator. Alternatively, use the `Choose File` button to select the file from the folder where the firmware was created.

        9. Ensure that you have selected the correct firmware file and click `Update`.
        10. A white page should load with the message "Update Success! Rebooting...."
        11. Wait until the LED on the Receiver starts to blink slowly again
        12. Receiver should be updated after waiting a little bit
        13. Now power down your Flight Controller along with the receiver

    ### <span class="custom-heading" data-id="4">Method 3</span>

    ??? Note "Method 3"

        !!! note "Note"
            This method will only work once the Home Network SSID and Password has been configured with the receiver.

        1. [Wire] your receiver properly with FC.
        2. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
        3. Power your FC by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The receiver's LED will blink slowly at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi Mode.

            <figure markdown>
            ![LEDSEQ_WIFI_UPDATE](https://cdn.discordapp.com/attachments/738450139693449258/921065813983760384/LEDSEQ_WIFI_UPDATE_2_3.gif)
            </figure>


        4. **Build & Flash** the firmware using the ExpressLRS Configurator. 
            
            <figure markdown>
            ![Build & Flash]
            </figure>
        
        5. Wait for the process to complete, indicated by the "Success" prompt and the Receiver LED has gone back to the Slow Blink mode. You can now power down the Flight Controller.

            <figure markdown>
            ![RXUpload Log](../../assets/images/RXWifiUpdateLog.png)
            </figure>

## <span class="custom-heading" data-id="5">Flashing via Passthrough</span>

??? Note "Flashing via Passthrough"

    - Target: `BETAFPV_Nano_2400_RX_via_BetaflightPassthrough`

    - Device Category: `BETAFPV 2.4 GHz`

    - Device: `BETAFPV Nano 2400 RX`, `BETAFPV Lite 2400 RX` (Tower & Flattie)

    <figure markdown>
    ![via Passthrough](../../assets/images/Method_RX_Passthrough.png)
    <figcaption>Flashing via Passthrough</figcaption>
    </figure>

    1. [Wire] your receiver properly with FC.
    2. Connect the Rx pad on the Receiver to the Tx pad on the FC
    3. Connect the Tx pad on the Receiver to the Rx pad on the FC
    4. Make sure to set up the FC firmware to use CRSF Protocol
    5. Ensure UART is not inverted or running in half duplex
    6. Disconnect from Betaflight or INAV Configurator
    7. Close the FC Configurator and unplug the FC from USB
    8. Press and Hold the button on the receiver
    9. Connect USB or attach a LiPo (if necessary)
    10. Let go of the button once the LED in the receiver stopped blinking and goes SOLID
    11. Connect your FC to USB

        !!! attention "Note"
            If you powered the receiver and has solid LED light, your FC is probably pulling the current UART's RX pad `LOW` which will interfere with the normal and passthrough flashing of this receiver. Find another UART and wire your receiver there instead.

        !!! Info
            These procedures will not be needed in subsequent passthrough flashing. This is only needed on the first time you'd update the receiver from its factory firmware.

    12. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
    13. **Build & Flash** the firmware using the ExpressLRS Configurator. For first time flashing/updating, it would normally take a while.

        <figure markdown>
        ![Build & Flash]
        </figure>

    14. Wait for the process to complete, indicated by the "Success" prompt

## <span class="custom-heading" data-id="6">Flashing via FTDI</span>

??? Note "Flashing via FTDI"

    - Target: `BETAFPV_Nano_2400_RX_via_UART`

    - Device Category: `BETAFPV 2.4 GHz`

    - Device: `BETAFPV Nano 2400 RX`, `BETAFPV Lite 2400 RX` (Tower & Flattie)

    <figure markdown>
    ![via UART](../../assets/images/Method_RX_UART.png)
    <figcaption>Flashing via UART</figcaption>
    </figure>

    1. Wire the receiver into the FTDI

        - Connect the TX pad on receiver to the Rx on the FTDI
        - Connect the RX pad on receiver connected to the Tx of the FTDI. 
        - Wire 5V and GND of the FTDI to 5V and GND of the Receiver.
        - Press the button while powering the RX on, and release - the LED should now be solid.

        <figure markdown>
        ![FTDI Wiring](../../assets/images/FTDIConn.png)
        </figure>

    2. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
    3. **Build & Flash** the firmware using the ExpressLRS Configurator. 
            
        <figure markdown>
        ![Build & Flash]
        </figure>

[Build]: ../../assets/images/Build.png
[Build & Flash]: ../../assets/images/BuildFlash.png
[Firmware Options]: ../firmware-options.md
[Wire]: #wiring-up-your-receiver

<script src="../../../assets/javascripts/admonition-enhancement.js"></script>