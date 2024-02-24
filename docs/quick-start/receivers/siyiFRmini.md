---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

!!! note "Note"
    This is only guaranteed to work on the v3.0 of the receiver.

## Flashing/Updating your Receiver Firmware 

=== "via STLink"

    !!! note "Note"
        The only way to flash the FR Mini to ExpressLRS for the first time is using STLink. This is a one-way process, there is no returning to the stock firmware after flashing.

    <figure markdown>
    ![via STLink](../../assets/images/Method_RX_STLink-stm.png)
    </figure>

    1. Disconnect the Receiver from your Flight Controller.

    2. Wire up the Receiver into an STLink V2 dongle. Find the CLK, DIO,RST, 3v3(VDD) and Gnd pads and wire them to the corresponding pins of the dongle.

        !!! warning "NOTICE"
            VDD is 3.3v ONLY! Do not connect 5v here! :fire:

        <figure markdown>
        ![pinout](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/siyi/jupa/Siyi-12.JPG?raw=true)
        </figure>

        <figure markdown>
        ![stlink](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/siyi/jupa/Siyi-13.JPG?raw=true)
        <figcaption>Siyi FR Mini</figcaption>
        </figure>

    3. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
        ![Configurator Release]{ align=right }

        - Make sure `Official Releases` is active from the horizontal tab.
        - Ensure you select the Released version you want to flash into your Receiver.

        <br clear="right" />
    4. Select the Device Category and Device target matching your hardware.

        - Device Category: 
            - `SIYI 2.4 GHz`

        - Device: 
            - `SIYI FM30 Mini 2.4GHz RX`

    5. Set the Flashing Method to `STLink`

        <figure markdown>
        ![via STLink](../../assets/images/Method_RX_STLink-stm.png)
        </figure>

    6. Set the [firmware options] for your device.
        - Regulatory Domain (Mandatory. Choose the domain appropriate for the location or country you're flying).
        - Binding Phrase (Optional, but Highly Recommended. Note this phrase as it should be the same on your other devices, or they will not bind or sync).

    7. Click the ++"Flash"++ button.

        <figure markdown>
        ![Flash]
        </figure>
          
    8. Wait for the process to finish. A Green Success bar will show up in the ExpressLRS Configurator.

    9. The LED on the Receiver should return to Slow Blinking LED pattern after a few seconds.

        <figure markdonw>
        ![LEDSEQ_DISCONNECTED](https://cdn.discordapp.com/attachments/738450139693449258/921065812985520268/LEDSEQ_DISCONNECTED_50_50.gif)
        </figure> 

    10. Rewire your receiver to your Flight Controller.

        | Flight Controller | FR Mini Receiver |
        |---|---|
        | 5V | VDD |
        | GND | GND |
        | RX | TX2 |
        | TX | RX2 |

        <figure markdown>
        ![pinout](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/siyi/jupa/Siyi-16.JPG?raw=true)
        </figure>

        <figure markdown>
        ![pinout](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/siyi/jupa/Siyi-17.JPG?raw=true)
        </figure>

    Thank you [@JupaCreations](http://www.jupacreations.com/) for contributing.

=== "via Passthrough"

    !!! note "Note"
        This method can only be used to UPDATE the ExpressLRS firmware on an FRmini.

    <figure markdown>
    ![via Passthrough](../../assets/images/Method_RX_Passthrough-stm.png)
    </figure>

    1. Make sure you have done your [Receiver Wiring] properly and that your Flight Controller is [Configured]. Also make sure [bootloaders] are already flashed to your R9 receiver when applicable.

        !!! Warning "Important Step!"
            This is an important step and guarantees updating success. If you haven't done these, GO BACK to those pages.

        - Disconnect and close your FC Configurator app (Betaflight Configurator, INAV Configurator, etc).
        - If your receiver powers up with just USB connected to your flight controller, unplug it. Press and Hold the boot button on the receiver (not the FC) and then plug in the USB. Release the button right after the LED turn solid.
        - If your receiver only powers up with a LiPo connected to your flight controller, unplug it. Then unplug-replug the USB cable to your flight controller. Do not replug LiPo yet.

    2. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
        ![Configurator Release]{ align=right }

        - Make sure `Official Releases` is active from the horizontal tab.
        - Ensure you select the Released version you want to flash into your Receiver.

        <br clear="right" />
    3. Select the Device Category and Device target matching your hardware.

        - Device Category: 
            - `SIYI 2.4 GHz`

        - Device: 
            - `SIYI FM30 Mini 2.4GHz RX`

    4. Set the Flashing Method to `BetaflightPassthrough`

        <figure markdown>
        ![via Passthrough](../../assets/images/Method_RX_Passthrough-stm.png)
        </figure>

    5. Set the [firmware options] for your device.
        - Regulatory Domain (Mandatory. Choose the domain appropriate for the location or country you're flying).
        - Binding Phrase (Optional, but Highly Recommended. Note this phrase as it should be the same on your other devices, or they will not bind or sync).

    6. Click the ++"Flash"++ button.

        <figure markdown>
        ![Flash]
        </figure>
    
    7. Wait for the `Retry...` lines to appear in the Build Log. Connect the LiPo to power up the Receiver if it only powers up with a LiPo connected.

        - `Retry...` lines will not show up if your receiver is already in bootloader mode and gets powered up by USB.
        
    8. Wait for the process to finish. A Green Success bar will show up in the ExpressLRS Configurator.

    9. The LED on the Receiver should return to Slow Blinking LED pattern after a few seconds.

        <figure markdonw>
        ![LEDSEQ_DISCONNECTED](https://cdn.discordapp.com/attachments/738450139693449258/921065812985520268/LEDSEQ_DISCONNECTED_50_50.gif)
        </figure> 

[Configurator Release]: ../../assets/images/ConfiguratorRelease.png
[Flash]: ../../assets/images/BuildFlash.png
[Build]: ../../assets/images/Build.png
[Receiver Wiring]: ../receivers/wiring-up.md
[Configured]: ../receivers/configuring-fc.md
[firmware options]: ../firmware-options.md
[Receiver Wiring]: wiring-up.md#connecting-a-receiver
