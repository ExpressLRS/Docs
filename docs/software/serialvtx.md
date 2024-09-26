---
template: main.html
description: Serial VTX Control
title: Serial VTX
---

![Software Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png)

!!! note "NOTE"
    SmartAudio/Tramp are loosely-defined protocols with edge cases, misinterpretations, and shoddy cloned implementations. ExpressLRS *does not* intend to support the vast majority of VTXes. SmartAudio was tested on a TBS Unify Pro32 HV, and Tramp was tested on an ImmersionRC Tramp HV, and both were tested with OpenVTX. It may work on other hardware, but it's not guaranteed and changes won't be made to accommodate broken implementations.

!!! note "NOTE"
    ESP32 is the only supported platform for SmartAudio/Tramp at this time; ESP8266 RXes lack the necessary UART functionality to do this the right way, and are not supported.

## Description

ExpressLRS now has support for controlling an external video transmitter through SmartAudio/Tramp protocols. This is a powerful feature for PWM+FPV users who don't have a flight controller to manage their VTX settings.

## Hardware Requirements

Using serial VTX control requires at least a secondary UART TX pin assigned on your ESP32-based receiver, such as the RadioMaster RP4TD or the BetaFPV SuperP. You may need to assign a pin as Serial TX using the Lua script "Other devices" section, or using the [RX Web UI](../../quick-start/webui/) if one is not already set up.

## Software Requirements

Ensure both your transmitter module and your receiver are up to date with the latest release versions; follow the [Firmware Update Guide](../../quick-start/getting-started/) for detailed instructions.

The minimum version to use this feature is:
- Receiver firmware: `3.5.0`

## Setting up serial VTX control (via Lua)

1. Open the ExpressLRS LUA script, scroll to the bottom and select `Other Devices`, then select your receiver.

1. Select `Output Map`, and assign an available `Output Ch` as `Serial2 TX`.

1. Select "BACK" to return to the main RX menu

1. Select `Protocol2` and set it to `SmartAudio` or `Tramp`. This configures the RX to output SmartAudio or Tramp on the previously-selected pin.

1. Wire the selected `Output Ch` to your video transmitter's SmartAudio or Tramp pin

1. Select "BACK" to return to the main Lua menu

1. You can now use the ExpressLRS [VTX Administrator](../../quick-start/transmitters/lua-howto#vtx-administrator) function to control your VTX

## Implementation details

ExpressLRS does not intend to support full VTX control, and especially not "VTX Table" functionality. To that end, here are some of the implementation decisions we've made in supporting SmartAudio/Tramp

### Bands/Channels

Only bands A/B/E/F/R/L and channels 1-8 are supported. Custom frequencies, and non-5.8GHz VTXes don't work, and we're not interested in making them work.

### Bidirectionality

These protocols support methods to confirm the settings on the VTX and update them on the controlling device (flight controller, RX). Our implementation is one-way only.

### SmartAudio power levels

SmartAudio has 3 different ways to specify a power level: a raw DAC output value, a power output in dBm, or a "power level" starting from 0. We've chosen to implement the third option.

Here's the result on a Unify Pro32 HV

| VTX Administrator "Pwr Lvl" | Output power in dBm | Output power in mW |
|-----------------------------|---------------------|--------------------|
| 1                           | 14                  | 25                 |
| 2                           | 23                  | 200                |
| 3                           | 27                  | 500                |
| 4                           | 29                  | 800                |

### SmartAudio pit mode

SmartAudio once again has 3 different ways to do something: pit mode is able to be specified as "in-range", "out-range", **both at the same time**, and a running or not flag (which is documented backwards of how it actually works). It's difficult to determine the "right" way of entering/exiting pitmode, and it never behaved how I expected it to in testing. YMMV.

### Tramp power levels

ImmersionRC Tramp takes a completely different approach to power levels; just send the output power you want in mW. Unfortunately this doesn't match our "Pwr Lvl" approach from VTX Administrator, so we had to arbitrarily determine some output power levels. ImmersionRC hardware will only support the first 5; the last 3 are "YMMV" options for "other" video transmitters that support Tramp protocol.

| VTX Administrator "Pwr Lvl" | Output power in mW                        |
|-----------------------------|-------------------------------------------|
| 1                           | 10                                        |
| 2                           | 25                                        |
| 3                           | 200                                       |
| 4                           | 400                                       |
| 5                           | 600                                       |
| 6                           | 1000 (not supported by ImmersionRC Tramp) |
| 7                           | 1600 (not supported by ImmersionRC Tramp) |
| 8                           | 3000 (not supported by ImmersionRC Tramp) |