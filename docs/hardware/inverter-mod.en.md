---
template: main.html
---

![HW Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/hardware.png)

- To benefit from the higher bitrate of 400 kilobit per second using `OpenTX` you need to **add a pullup resistor to the inverter** of the serial port on the R9M 2018🗻🆙
- Strongly suggested to be done for anybody looking for higher than standard packet rates using `ExpressLRS` 🔮

## Identification

⚠️ This is only required for the 2018 version of the module which has a `ACCST` logo on the case 🔍 

## Modification

Easy - connect a **300Ω to 1000Ω resistor** between the `3.3V` and inverter pin as shown on the picture 👧

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/FrSky%20R9M%20(2018%20model)%20resistor%20mod.png" width="100%">

## Transmitter Notes

- `X9D` **only** does 400 kbit/s and __does not allow__ lowering the bitrate to 115200 bit/s - 400k Mod is not required.
- `X10S Express` 400k Mod is not required.
- `X10S` **[modification is required](https://blog.seidel-philipp.de/fixed-inverter-mod-for-tbs-crossfire-and-frsky-qx7/)** 🙅 
- `X12` **[modification is required](https://blog.seidel-philipp.de/fixed-inverter-mod-for-tbs-crossfire-and-frsky-qx7/)** 🙅 
- `QX7` allows configuration of the bitrate in the OpenTX hardware menu.  ELRS will work fine using 115200 bit/s but the **[modification is required](https://blog.seidel-philipp.de/fixed-inverter-mod-for-tbs-crossfire-and-frsky-qx7/)** for 400 kbit/s 🙅‍♀️
- The modification is **not** needed for `ACCESS` radios
