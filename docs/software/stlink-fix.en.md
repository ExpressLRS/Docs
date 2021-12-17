---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

PlatformIO has an older version of STLink. It is unable to communicate with the STM32L MCUs on some Rx's.  
Affected RX's:  
-(DIY) PP

Swapping out PIO's STLink folder contents with the current STLink will allow using the configurator with these RX's.

**Go to your STLink folder** 
  
- **copy contents of "ST-Link Utility"**  
`C:\Program Files (x86)\STMicroelectronics\STM32 ST-LINK Utility\ST-LINK Utility`

![](https://cdn.discordapp.com/attachments/738450139693449258/840702633383428096/stlink.jpg)

- **paste files from "st-link utility" folder into "stlink" folder in your users PIO location**  
`C:\Users\username\ .platformio\packages\tool-stm32duino`

![](https://cdn.discordapp.com/attachments/738450139693449258/840703335015383140/pio.jpg)

