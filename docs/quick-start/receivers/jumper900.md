---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing/Updating your Receiver Firmware

=== "via STLink"

    !!! note "Note"
        The only way to flash the Jumper R9 Mini to ExpressLRS for the first time is by using STLink. This is a one-way process. There is no returning to the factory firmware after flashing.

    <figure markdown>
    ![via STLink](../../assets/images/Method_RX_STLink-stm.png)
    </figure>

    1. Disconnect the Receiver from your Flight Controller.

    2. Wire up the Receiver into an STLink V2 dongle. Connect `+ to 3v3`, `- to GND`, `C to CLK` and `D to DIO`.

        <figure markdown>
        ![Jumper R9 Mini](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/r900mini-rx/r900mini-side2-closeup.jpg){ style="display: block; margin-left: auto; margin-right: auto; width:70%;" }
        <figcaption>Jumper R9 Mini</figcaption>
        </figure>

        Because those pins are so small one option is to only solder wires on the CLK and DIO then power the receiver with the 5v pin with an external power source. Connect - (Gnd) to both power source and the STLink dongle.

    3. Disable 'Readout Protection'. To do this download the [ST-LINK Utility](https://www.st.com/en/development-tools/stsw-link004.html) and follow this quick [how to video](https://youtu.be/SEYQ1HpRmk0). Or alternatively under linux you can use [OpenOCD](../../software/open-ocd.md).

        How to video:

        <figure markdown>
        <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/SEYQ1HpRmk0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </figure>

    4. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
        ![Configurator Release]{ align=right }

        - Make sure `Official Releases` is active from the horizontal tab.
        - Ensure you select the Released version you want to flash into your Receiver.

        <br clear="right" />
    5. Select the Device Category and Device target matching your hardware.

        - Device Category: 
            - `Jumper 900 MHz`

        - Device: 
            - `Jumper 900 Mini RX`

    6. Set the Flashing Method to `STLink`

        <figure markdown>
        ![via STLink](../../assets/images/Method_RX_STLink-stm.png)
        </figure>

    7. Set the [firmware options] for your device.
        - Regulatory Domain (Mandatory. Choose the domain appropriate for the location or country you're flying).
        - Binding Phrase (Optional, but Highly Recommended. Note this phrase as it should be the same on your other devices, or they will not bind or sync).

    8. Click the ++"Flash"++ button.

        <figure markdown>
        ![Flash]
        </figure>
          
    9. Wait for the process to finish. A Green Success bar will show up in the ExpressLRS Configurator.

    10. The LED on the Receiver should return to Slow Blinking LED pattern after a few seconds.

        <figure markdonw>
        ![LEDSEQ_DISCONNECTED](https://cdn.discordapp.com/attachments/738450139693449258/921065812985520268/LEDSEQ_DISCONNECTED_50_50.gif)
        </figure> 

    11. Rewire your receiver to your Flight Controller. Connect RX2 and TX2 (you will need to solder on the STM32 pins; see step 2 above) to a flight controller. Configure your flight controller per the [FC Configuration Guide].

=== "via Passthrough"

    !!! note "Note"
        This method can only be used to UPDATE the ExpressLRS firmware on a Jumper R9 mini.

    <figure markdown>
    ![via Passthrough](../../assets/images/Method_RX_Passthrough-stm.png)
    </figure>

    1. Make sure you have done your [Receiver Wiring] properly and that your Flight Controller is [Configured]. Also make sure [bootloaders] are already flashed to your R9 receiver when applicable.

        !!! Warning "Important Step!"
            This is an important step and guarantees updating success. If you haven't done these, GO BACK to those pages.

        - Disconnect and close your FC Configurator app (Betaflight Configurator, INAV Configurator, etc).
        - Power-cycle the Flight Controller.
            - If you plugged in LiPo, unplug it.
            - Unplug-replug the USB Cable from your Flight Controller or Computer.
            - If you have to plug in LiPo to power up your Receiver, make sure you have some airflow blowing over your Video Transmitter (VTX). You can also temporarily unplug it from the Flight Controller.

    2. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
        ![Configurator Release]{ align=right }

        - Make sure `Official Releases` is active from the horizontal tab.
        - Ensure you select the Released version you want to flash into your Receiver.

        <br clear="right" />
    3. Select the Device Category and Device target matching your hardware.

        - Device Category: 
            - `Jumper 900 MHz`

        - Device: 
            - `Jumper 900 Mini RX`

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
[FC Configuration Guide]: ../receivers/configuring-fc.md
[firmware options]: ../firmware-options.md
[Receiver Wiring]: wiring-up.md#connecting-a-receiver
