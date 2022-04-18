---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

Targets: 

- `Jumper_RX_R900MINI_via_STLINK`
- `Jumper_RX_R900MINI_via_BetaflightPassthrough`

Device Category: `Jumper R900`

Device: `Jumper RX R900MINI`

![via STLink](../../assets/images/Method_RX_STLink-stm.png)

Wire it up to your STLink V2 as follows:

Wire `+ = 3v3`, `- = GND`, `C = CLK` and `D = DIO` to their respective pins on the RX from the StLink.
<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/r900mini-rx/r900mini-side2-closeup.jpg" width = "60%">

Because those pins are so small one option is to only solder a wire on the `CLK` and `DIO` then power it with the 5v pin with an external power source. 

Disable 'Readout Protection'. To do this download the [ST-LINK Utility](https://www.st.com/en/development-tools/stsw-link004.html) and follow this quick [how to video](https://youtu.be/SEYQ1HpRmk0). Or alternatively under linux you can use [OpenOCD](../../software/open-ocd.md).

Using the correct target specific for your receiver, and your [Firmware Options](../firmware-options.md) set, click **Build & Flash** on the ExpressLRS Configurator.

![Build & Flash](../../assets/images/BuildFlash.png)

After the flash is successful, desolder the STLink and connect RX2 and TX2 (you will need to solder on the STM32 pins, see picture) to a flight controller and setting up the receiver with the CRSF serial protocol, the `Jumper_RX_R900MINI_via_BetaflightPassthrough` target may now be used for future firmware updates.

