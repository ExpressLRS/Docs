---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Check your Target

There are more `ESP8285` based RXes in the market due to massive shortage of `STM32` Chips. These support WiFi updating, and can be easily distinguished with a few tricks. The simplest way to tell is if on the rear of the RX (the side without the U.fl/SMD antenna) there is a large white component with the label **RainSun** (pictured below). If this is not there, you have an STM32 based target, if it is you have an `_ESP_` target, and can update using Wifi!

<figure markdown>
<img style="display: block; margin-left: auto; margin-right: auto;" src = "https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/antenna.jpg?raw=true" width = "30%">
<figcaption>RainSun Antenna</figcaption>
</figure>

!!! Note
    New versions of the receiver also have the PCB Wifi Antenna, and doesn't have the Rainsun SMD Antenna mentioned above. These will use the same ESP-based Target, not the STM-based target.

## Wiring up your receiver

!!! attention "Note"
    There are Flight Controllers that will pull the RX pads `LOW` which will put the ESP-based receivers into `Bootloader Mode` unintentionally. A solid LED light on these receivers even with the TX module off is a sign they are in Bootloader Mode. If this is the case, rewire the receiver to a different UART.

<figure markdown>
![NamimnoRC Voyager](../../assets/images/Pinout-Voyager.png)
</figure>

The image above show the receiver pinouts and their connections. As we're dealing with UART connection, Rx on receiver goes to a TX pad in the FC, and Tx on Receiver goes to an uninverted Rx pad on the FC.

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

## Flashing/Updating NamimnoRC Voyager

Following are the flashing and updating methods for NamimnoRC Voyager.

### <span class="custom-heading" data-id="1">Flashing via Passthrough</span>

??? Note "Flashing via Passthrough"

    - Targets:
        - `NamimnoRC_VOYAGER_900_ESP_RX_via_BetaflightPassthrough` 
        - `NamimnoRC_VOYAGER_900_RX_via_BetaflightPassthrough`

    - Device Category: 
        - `NamimnoRC VOYAGER 900 MHz`

    - Device:
        - `NamimnoRC VOYAGER 900 ESP RX`
        - `NamimnoRC VOYAGER 900 RX`

    <figure markdown>
    ![via Passthrough](../../assets/images/Method_RX_Passthrough.png)
    <figcaption>Flashing via Passthrough</figcaption>
    </figure>

    #### <span class="custom-heading" data-id="2">STM-based receivers</span>

    ??? Note "STM-based receivers"

        1. [Wire] up the receiver to FC.
        2. Plug in the flight controller to USB. If the receiver powers up too, with both LEDs lit, disconnect USB, hold the bind button on the receiver, and reconnect to USB. The LED should start alternating between green and red. Once it is alternating, you can release the bind button.
        3. If the receiver does not power up from USB, have a LiPo ready. On the ExpressLRS Configurator, set your firmware options, then click on "Build & Flash". The first time, it may take a while. Keep an eye out for the `Passthrough Init` stage, which will check your flight controller configuration for the correct Serial RX UART (Software Inversion via "set serialrx_inverted" and Half Duplex mode via "set serialrx_halfduplex" will be checked; both should be off.) 
            
            <figure markdown>
            ![Build & Flash]
            </figure>
        
        4. If `Retry...` lines appear, connect the LiPo to power up your flight controller and receiver.
        5. Wait until the flashing process is complete and the "Success" prompt is shown. On subsequent flashes, the LiPo can be plugged in and the receiver powered up before connecting the USB.

    #### <span class="custom-heading" data-id="3">ESP-based receivers</span>

    ??? Note "ESP-based receivers"

        1. For the ESP-based receivers, you can connect a LiPo during the `PASSTHROUGH DONE` section of the Log.
        2. Wait for the process to complete, indicated by the "Success" prompt

### <span class="custom-heading" data-id="4">Updating via WiFi (ESP Only - Recommended)</span>

??? Note "Updating via WiFi (ESP Only - Recommended)"

    - Target: `NamimnoRC_VOYAGER_900_ESP_RX_via_WIFI`

    - Device Category: `NamimnoRC VOYAGER 900 MHz`

    - Device: `NamimnoRC VOYAGER 900 ESP RX`

    <figure markdown>
    ![via WiFi](../../assets/images/Method_RX_WiFi.png)
    <figcaption>Updating via WiFi</figcaption>
    </figure>

    #### <span class="custom-heading" data-id="5">Method 1</span>

    ??? Note "Method 1"

        1. [Wire] your receiver properly with FC.
        2. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
        3. Build the firmware, which will open the Target folder where the `NamimnoRC_VOYAGER_900_ESP_RX-<version>.bin` file is located. Do not close this window so you can easily locate the correct file to upload to the module.

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
        7. Drag and drop the firmware file, `NamimnoRC_VOYAGER_900_ESP_RX-<version>.bin`, created by the ExpressLRS Configurator. Alternatively, use the `Choose File` button to select the file from the folder where the firmware was created.
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

    #### <span class="custom-heading" data-id="6">Method 2</span>

    ??? Note "Method 2"

        !!! note "Note"
            This method will only work once the Home Network SSID and Password has been configured with the receiver.

        1. [Wire] your receiver properly with FC.
        2. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
        3. Build the firmware, which will open the Target folder where the `NamimnoRC_VOYAGER_900_ESP_RX-<version>.bin` file is located. Do not close this window so you can easily locate the correct file to upload to the module.

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

        8. Drag and drop the firmware file, `NamimnoRC_VOYAGER_900_ESP_RX-<version>.bin`, created by the ExpressLRS Configurator. Alternatively, use the `Choose File` button to select the file from the folder where the firmware was created.

        9. Ensure that you have selected the correct firmware file and click `Update`.
        10. A white page should load with the message "Update Success! Rebooting...."
        11. Wait until the LED on the Receiver starts to blink slowly again
        12. Receiver should be updated after waiting a little bit
        13. Now power down your Flight Controller along with the receiver

    #### <span class="custom-heading" data-id="7">Method 3</span>

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


### <span class="custom-heading" data-id="8">Updating via FTDI (ESP Only)</span>

??? Note "Updating via FTDI (ESP Only)"

    - Target: `NamimnoRC_VOYAGER_900_ESP_RX_via_UART`

    - Device Category: `NamimnoRC VOYAGER 900 MHz`

    - Device: `NamimnoRC VOYAGER 900 ESP RX`

    <figure markdown>
    ![via UART](../../assets/images/Method_RX_UART.png)
    <figcaption>Updating via UART</figcaption>
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

### <span class="custom-heading" data-id="9">Updating via STLink (STM32 Only)</span>

??? Note "Updating via STLink (STM32 Only)"

    - Target: `NamimnoRC_VOYAGER_900_RX_via_STLINK`

    - Device Category: `NamimnoRC VOYAGER 900 MHz`

    - Device: `NamimnoRC VOYAGER 900 RX`

    <figure markdown>
    ![via STLink](../../assets/images/Method_RX_STLink-stm.png)
    <figcaption>Updating via STLink</figcaption>
    </figure>

    The units provided to the documentation team did not have STM32 chips due to the chip shortage, however, the following should apply. 
    
    1. Wire CLK, 3v3, GND and DIO to the recievers STLink pins.
    2. Select the target and set your [Firmware Options] and once done, click on **Build and Flash**.

    <figure markdown>
    ![Build & Flash]
    </figure>

[Build]: ../../assets/images/Build.png
[Build & Flash]: ../../assets/images/BuildFlash.png
[Firmware Options]: ../firmware-options.md
[Wire]: wiring-up.md#namimnorc-voyager-flash

<script src="../../../assets/javascripts/admonition-enhancement.js"></script>