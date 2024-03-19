---
template: main.html
---

![Hardware-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/hardware.png)

## Custom Hardware

Possibly one of the biggest benefits of using `ExpressLRS` is custom hardware!

- 📶 [Custom ESP 2.4 GHz TX](#custom-esp-24-ghz-tx-for-jr-module-bay)
- 📡 [Custom Super Slim ESP 2.4 GHz TX](#custom-super-slim-esp-24-ghz-tx-for-lite-module-bay)
- ⚡ [Custom 900 MHz TX](#custom-900-mhz-tx-not-built-anymore)

### Custom ESP 2.4 GHz TX (for JR module bay)

All of the info on this topic can be found [here](https://github.com/ExpressLRS/ExpressLRS-Hardware/tree/master/PCB/2400MHz/TX_SX1280)

<figure markdown>
![custom tx](../../assets/images/diytx0.jpg){ width=40% class="center-img" }
</figure>

### Custom Super Slim ESP 2.4 GHz TX (for lite module bay)

The super slim is an evolution of the slim. It uses the same base hardware as the JR size one. It's the same size as an R9M Lite, and fits in all handsets with a lite module bay such as the X-Lite, X9 Lite, and Tango 2 (with the proper adapter). The rest of the info can be found [here](https://github.com/ExpressLRS/ExpressLRS-Hardware/tree/master/PCB/2400MHz/TX_SX1280_Super_Slim)

<figure markdown>
![custom tx slim](../../assets/images/diytx1.jpg){ width=40% class="center-img" }
</figure>

### Custom 900 MHz TX (not built anymore)

In the beginning, 900 MHz transmitters were sometimes built DIY. Today they're not. If you have one, the max output power defaults to 100mW, but with `UNLOCK_HIGHER_POWER`, that can be increased to 250mW.