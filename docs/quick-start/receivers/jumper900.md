---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing via STLink

- Target: `Jumper_RX_R900MINI_via_STLINK`

- Device Category: `Jumper R900`

- Device: `Jumper RX R900MINI`

<figure markdown>
![via STLink](../../assets/images/Method_RX_STLink-stm.png)
<figcaption>Flashing via STLink</figcaption>
</figure>

Wire it up to your STLink V2 as follows:

Wire `+ = 3v3`, `- = GND`, `C = CLK` and `D = DIO` to their respective pins on the RX from the StLink.

<figure markdown>
<img style="display: block; margin-left: auto; margin-right: auto;" src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/r900mini-rx/r900mini-side2-closeup.jpg" width = "60%">
<figcaption>Jumper R9 Mini</figcaption>
</figure>

Because those pins are so small one option is to only solder a wire on the `CLK` and `DIO` then power it with the 5v pin with an external power source. 

Disable 'Readout Protection'. To do this download the [ST-LINK Utility](https://www.st.com/en/development-tools/stsw-link004.html) and follow this quick [how to video](https://youtu.be/SEYQ1HpRmk0). Or alternatively under linux you can use [OpenOCD](../../software/open-ocd.md).

How to video:
<figure markdown>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/SEYQ1HpRmk0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>

Using the correct target specific for your receiver, and your [Firmware Options] set, click **Build & Flash** on the ExpressLRS Configurator.

<figure markdown>
![Build & Flash]
</figure>

After the flash is successful, desolder the STLink and connect RX2 and TX2 (you will need to solder on the STM32 pins, see picture) to a flight controller and setting up the receiver with the CRSF serial protocol.

## Updating via Passthrough

- Target: `Jumper_RX_R900MINI_via_BetaflightPassthrough`

- Device Category: `Jumper R900`

- Device: `Jumper RX R900MINI`

<figure markdown>
![via Passthrough](../../assets/images/Method_RX_Passthrough-stm.png)
<figcaption>Updating via Passthrough</figcaption>
</figure>

After flashing via STLink, the `Jumper_RX_R900MINI_via_BetaflightPassthrough` target may now be used for future firmware updates.
Select the target and set your [Firmware Options] and once done, click on **Build and Flash**.

<figure markdown>
![Build & Flash]
</figure>

[Build & Flash]: ../../assets/images/BuildFlash.png
[Firmware Options]: ../firmware-options.md