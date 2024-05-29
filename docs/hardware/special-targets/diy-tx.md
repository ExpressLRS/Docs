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
![custom tx](../../assets/images/diytx0.jpg){ width=50% }
</figure>

### Custom Super Slim ESP 2.4 GHz TX (for lite module bay)

The super slim is an evolution of the slim. It uses the same base hardware as the JR size one. It's the same size as an R9M Lite, and fits in all handsets with a lite module bay such as the X-Lite, X9 Lite, and Tango 2 (with the proper adapter). The rest of the info can be found [here](https://github.com/ExpressLRS/ExpressLRS-Hardware/tree/master/PCB/2400MHz/TX_SX1280_Super_Slim)

<figure markdown>
![custom tx slim](../../assets/images/diytx1.jpg){ width=50% }
</figure>

### Custom 900 MHz TX (not built anymore)

In the beginning, 900 MHz transmitters were sometimes built DIY. Today they're not. If you have one, the max output power defaults to 100mW, but with `UNLOCK_HIGHER_POWER`, that can be increased to 250mW.

## Custom Hardware's Firmware Guide

[PlatformIO](https://platformio.org/) is a prerequisite for developing custom hardware.

The hardware pinouts for ExpressLRS are kept at [ExpressLRS/targets](https://github.com/ExpressLRS/targets/). Clone this repo within `src/` of your [`ExpressLRS/ExpressLRS`](https://github.com/ExpressLRS/ExpressLRS) repo - or, if you run a build, it'll happen automatically.

In the `RX` and `TX` directories, you can find the pinouts and configuration for different layouts stored as JSON files.

Within [`targets.json`](https://github.com/ExpressLRS/targets/blob/master/targets.json), there are listed all the possible build targets for ExpressLRS.

To access your target's configuration, you must add a new entry to the `targets.json` file - mimic the closest existing one and change the values to match your hardware. It's critical the `firmware` field match your processor.

![](/assets/images/targetsFirmwareSelection.png)

Select the matching build target from PlatformIO:

![](/assets/images/platformioSetEnv.png)

After you run a build, you should be met with a hardware configuration selector and your new configuration!

![](/assets/images/UnifiedConfigurationSelector.png)
