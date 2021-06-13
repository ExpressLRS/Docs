---
template: main.html
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

## OpenTX Version
We recommend [OpenTX-2.3.12 nightlies](https://www.open-tx.org/2019/05/17/2.3-nightlies), which allow for use of `.elrs` files and contain `crsfshot`, which allows for 500Hz+ rates.

## CRSF Protocol

ExpressLRS uses the CRSF serial protocol to communicate between the transmitter and the TX module. To set this up, enter into your model settings, and on the "Model Setup" tab, enable your "External RF" and select "CRSF" as the protocol:

**NOTE: If using 2.4ghz ELRS, the internal module must be turned off.**

![](https://oscarliang.com/ctt/uploads/2018/03/setup-tbs-crossfire-tx-rx-micro-nano-taranis-betaflight-fc-internal-external-rf-mode.jpg)
![](https://oscarliang.com/ctt/uploads/2019/12/JUMPER-T16-EXTERNAL-RF-MODE-PROTOCOL-TBS-CROSSFIRE-CRSF.jpg)

NOTE: If using 2.4ghz ELRS, internal module must be turned off.

## Serial Baud Rate

On some transmitters, the baud rate for comms between the opentx and the ExpressLRS module can be changed. The two rates available are 115200 and 400000. ExpressLRS supports both rates (auto switches to the correct rate on power-up), however, we have found that on the R9M modules, the inverter IC's that are used are not capable of reliably handling 400k baud. If you're using an R9M, select 115200 baud in OpenTX, or do the resistor mod described on the [Supported Hardware](https://github.com/AlessandroAU/ExpressLRS/wiki/Supported-Hardware) page.

## ADC Filter

The ADC filter is enabled by default in OpenTX and is known to cause issues with RC Command data. This can result in "jagged" RC command responses in black box logs, caused by sequential RC packets that have the same command value (which were "smoothed" by the ADC filter).
We recommend turning the ADC filter OFF in [OpenTX](https://www.youtube.com/watch?v=ESr2H_EZ89Q)

![](https://fpvfrenzy.com/wp-content/uploads/2017/11/baud-rate.jpg)

## Lua Script

For faster access to the Lua script, save the `ELRS.lua` File from this link: [ExLRS Lua Script](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS/1.0.x-maintenance/src/lua/ELRS.lua) onto the radio's SD Card in the `Scripts/Tools` folder and Long Press the "SYS" button (for T16 or similar Radios) or the "Menu" button (for Taranis X9D or similar Radios) to access the Tools Menu where you can find ELRS script ready to run with only one click.

NB If you're prompted with `Syntax Error`, make sure you downloaded the raw file, and not html. The file is also available in your local clone, it's located at `src/lua/ELRS.lua`.

![](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/wiki-from-discord/lua1.jpeg)
![](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/wiki-from-discord/lua2)

Also the Lua script was recently updated with an important feature, top right it shows an indicator 0:200 which tells you how many bad UART packets and how many packets/second it's getting from the radio. It can be used to confirm the communication between the Radio and the R9M module is working properly. 

0:200 means : 0 bad packets and 200 good packets (per second). 

The value should match the selected air rate (200 for 200Hz, 50 for 50Hz, etc..)

If it doesn't and is stuck at 250 that means crsfshot isn't working.

![](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/wiki-from-discord/lua3)