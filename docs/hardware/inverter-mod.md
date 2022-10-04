---
template: main.html
description: A short guide on how to add a resistor for the R9M ACCST Inverter Mod.
---

![HW Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/hardware.png)

## Overview

- To benefit from the higher bitrate of 400 kilobits per second using `OpenTX`/`EdgeTX` you need to **add a pullup resistor to the inverter** of the serial port on the R9M 2018🗻🆙
- Strongly suggested being done for anybody looking for higher than standard packet rates using `ExpressLRS` 🔮

## Identification

⚠️ This is only required for the 2018 version of the module which has a `ACCST` logo on the case 🔍

## Modification

Easy - connect a **300Ω to 1000Ω resistor** between the `3.3V` and inverter pin as shown in the picture 👧

<figure markdown>
<img class="center-img" src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/FrSky%20R9M%20(2018%20model)%20resistor%20mod.png" width="100%">
</figure>

## Transmitter Notes

Some Radios/Transmitters will require the Inverter/[Crossfire Mod](https://blog.seidel-philipp.de/fixed-inverter-mod-for-tbs-crossfire-and-frsky-qx7/) depending on the Baud Rate you want to use or you can use. 

| Radio | Baud Rate | Inverter/Crossfire Mod | R9M ACCST MOD |  Other Notes |
|---|---|---|---|---|
| X9D | 400000 | Not Needed | Required | See [Troubleshooting](./x9d-troubleshooting.md) |
| X10S Express | 400000 | Not Needed | Required | - |
| X10S | 400000 | Required. [Modding Guide.](https://blog.seidel-philipp.de/fixed-inverter-mod-for-tbs-crossfire-and-frsky-qx7/#Mod_for_FrSKY_Horus_X10S) | Required | - |
| X12 | 400000 | Required. [Modding Guide.](https://blog.seidel-philipp.de/fixed-inverter-mod-for-tbs-crossfire-and-frsky-qx7/#Mod_fuer_FrSKY_Horus_X12) | Required | - |
| QX7 | 400000 | Required. [Modding Guide.](https://blog.seidel-philipp.de/fixed-inverter-mod-for-tbs-crossfire-and-frsky-qx7/#Mod_for_FrSKY_Taranis_QX7) | Required | See [Troubleshooting](./x9d-troubleshooting.md) |
| QX7 | 115200 | Not Needed | Not Needed | Max Packet Rate supported is 250Hz |
| Others | 400000+ | Not Needed | Required | TX16S, TX12, T16/T18, etc |

`ACCESS` radios don't need the Inverter/Crossfire mod.