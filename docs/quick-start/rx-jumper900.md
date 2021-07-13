---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

### Jumper RX 

Targets: 

- Jumper_RX_R900MINI_via_STLINK
- Jumper_RX_R900MINI_via_BetaflightPassthrough

Disable 'Readout Protection'. To do this download the [ST-LINK Utility](https://www.st.com/en/development-tools/stsw-link004.html) and follow this quick [how to video](https://youtu.be/SEYQ1HpRmk0). Or alternatively under linux you can use <a href="/software/open-ocd">OpenOCD</a>.

Using the correct target specific for your receiver, hit "Build & Flash".

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/r900mini-rx/r900mini-side2-closeup.jpg" width = "60%" alt = "R900 wiring diagram">

After the flash is successful, desolder the STLink and connect RX2 and TX2 (you will need to solder on the STM32 pins, see picture) to a flight controller and setting up the receiver with the CRSF serial protocol, the `Jumper_RX_R900MINI_via_BetaflightPassthrough` target may now be used for future firmware updates.

