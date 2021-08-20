---
template: main.html
---

![HW Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/hardware.png)

## Nuclear RX

The Nuclear RX is designed to be as small as possible, using the same software target as the DIY Nano RX, and assembled by JLCPCB. It uses the 2400MHz band and ExpressLRS firmware.

Features: 
 
- 20x20 stack mounting with break-off tabs for compact applications  
- [SMD Antenna](/hardware/smd-antenna/)
- [Wi-Fi updating](/software/updating/wifi-updating/)  
- Up to 500Hz packet rate  

<img src="https://media.discordapp.net/attachments/738450139693449258/834252910422392832/IMG_0665.JPG?width=910&height=682" width="40%">

When you get your Nuclear RX, it will likely be on the latest release firmware. You'll probably have to update it to work with your TX. To update, follow the steps in the [Wi-Fi updating](/software/updating/wifi-updating) page. Alternatively, you can use [betaflight passthrough](/software/updating/betaflight-passthrough/) should work, but the boot jumper must be bridged while applying power to the RX.

When building, use one of the `DIY_2400_RX_ESP8285_SX1280_via_X` targets. To use `via_wifi`, put your RX in binding mode, connect your computer to the RX's Wi-Fi, and hit upload.

| LED | Status |
| --- | ------ |
| Blinking Slowly | Waiting for Connection  |
| Fast Double Blink | Binding Mode  |
| Super Fast Blink | Wi-Fi Updating Mode  |
| Solid On | Connected  |

If for some reason the RX needs to be in boot mode, bridge the jumpers as shown here:

<img src="https://cdn.discordapp.com/attachments/738450139693449258/858365975489019974/Capture.PNG" width="40%">

## Nuclear TX
### Overview

The Nuclear TX is designed to be the same size as a FrSky slim module and use the same software target as the DIY Slim TX. It uses the 2400MHz band and ExpressLRS firmware. There is also a case that fits a full size JR module bay with the same PCB.

### Before Flight

If you ordered a Nuclear TX that wasn't fully assembled, these steps should help you finish it.

#### Print a case

The latest version of the Nuclear TX STL files can be found [here](https://github.com/SpencerGraffunder/ExpressLRS/tree/nuclear-hardware/PCB/2400MHz/TX_SX1280_Super_Slim/stl). Print the pieces in the orientation in the image and use support. Tree support in Cura works great. Keep in mind that PLA may melt if left in a hot car or in direct sunlight.  
<img src="https://github.com/SpencerGraffunder/ExpressLRS/blob/nuclear-hardware/PCB/2400MHz/TX_SX1280_Super_Slim/img/printlayout.png?raw=true?width=910&height=682" width="40%">

#### Assemble

Slap it together as seen below. Solder the wires to the pin header in the order in the picture, then slide it in from the outside. The header should press in with a little force. Add some glue on the inside to keep it from sliding out when removing it from your handset. Put the SMA pigtail in the hole in the top and screw it down. Use a wrench to make sure it doesn't come loose when you screw on your antenna. Plug the U.FL in to the module and route it under, and looping up around the side.  
<img src="https://github.com/SpencerGraffunder/ExpressLRS/blob/nuclear-hardware/PCB/2400MHz/TX_SX1280_Super_Slim/img/exploded.jpg?raw=true?width=910&height=682" width="40%">

#### Upload firmware

When you get your Nuclear RX, it will likely be on the latest release firmware. You'll probably have to update it to work with the RX you have. To update, follow the steps in the [Wi-Fi updating](/software/updating/wifi-updating/) page. If your transmitter module ever becomes bricked from a bad upload, connect it with a serial adapter as shown here. **MAKE SURE THE ADAPTER IS SET TO 3.3V; 5V WILL KILL THE MODULE!** Use tweezers or solder to bridge the boot jumper while you power on the module to put it in boot mode. Use the target `DIY_2400_TX_ESP32_SX1280_E28_via_UART`.  
<img src="https://github.com/SpencerGraffunder/ExpressLRS/blob/nuclear-hardware/PCB/2400MHz/TX_SX1280_Super_Slim/img/ftdi.png?raw=true?raw=true?width=910&height=682" width="40%">

Note: The version of the boards with the 6-pad layout for programming has the TX and RX named backwards. The actual order of the pins is TX, RX, 3V3, GND, GND.

If you're unable to compile code, you can use the prebuilt binaries from [here](https://github.com/SpencerGraffunder/ExpressLRS/tree/built-binaries/bin) for wifi updates.