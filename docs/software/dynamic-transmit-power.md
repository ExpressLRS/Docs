---
template: main.html
description: ExpressLRS can limit its transmit power to the level it needs to maintain good Signal Health.
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

## Description

Dynamic Power allows the TX module to lower its output power from the configured power level using signal information from the RX. The TX will lower power if the signal level is above a threshold (see below) and will raise power if it is not, has a low LQ, or has a sudden drop in LQ. Because Dynamic Power relies on telemetry, telemetry must be enabled. That is, "Telem Ratio" must be set to anything except "Off" or "Race".

!!! warning "Warning"
    Dynamic Power relies on telemetry. If no telemetry is received while armed, then the power level will be kicked up to the maximum configured power level.

### How to configure Dynamic Power

In the ELRS Lua script, select `> TX Power`. There are three configurable elements.

* `Max Power`: The output power will never exceed this power output level in any situation.
* `Dynamic`: Three options are available.
    - `Off`: Fixed power, always set power to the configured `Max Power` output.
    - `Dyn`: Dynamic power is enabled.
    - `AUX9`-`AUX12`: Dynamic power is enabled only when this AUX channel is `high`, and power is fixed to the `Max Power` when `low`. [Demo Video](https://www.youtube.com/watch?v=wdPWw2xu8Ig)
* `Fan Thresh`: Fan threshold. If the module has a fan, it will be enabled starting at this power level after a short delay.

Another important setting is to make sure your craft is **armed** on AUX1=`high` (~2000us). See [Switch Modes](switch-config.md) for more information about AUX channels.

## Details

### Starting Power

On module powerup with Dynamic Power enabled, transmit power is set to the minimum supported power.

### Lowering Power

For non-FLRC modes, Dynamic Power uses the average signal to noise ratio (SNR) reported by the receiver. If the SNR is above a threshold, the power will be lowered by one level. SNR is used because it takes into account interference (the "noise" in signal-to-noise) and is not affected by receivers with LNAs, which boost RSSI dBm. The thresholds for lowering the power are specific to each packet rate. For example, 250Hz (LoRa) will lower the power if SNR is <= 9.5 but 150Hz (LoRa) will lower power if the SNR is <= 8.5.

For FLRC modes (packet rates beginning with `F` or `D`) Dynamic Power averages the last few RSSI dBm readings from the RX. If the RSSI is >= -83dBm, the transmit power is lowered by one level.

For both algorithms, the power will only be lowered if the link quality (LQ) is 95% or higher.

### Raising Power

The opposite of the "lowering power" algorithm is also in place, to raise power as needed slowly such as when flying away on a long range flight. The algorithms are the same as for lowering power, except with different thresholds. Examples:

  * 250Hz (LoRa) raise power if SNR <= 3.0
  * 150Hz (LoRa) raise power if SNR <= 0.0
  * F500 (FLRC) raise power if RSSI <= -89 dBm. Note that all FLRC modes use this same limit.

To be proactive when telemetry is not received, Dynamic Power will also increase power one level for each missed telemetry packet, starting when two are missed back to back.

  * TX misses first telemetry packet: no action, maintain power level
  * TX misses second telemetry packet: increase power 1 level
  * TX misses third telemetry packet: increase power 1 level
  * ...
  * TX receives telemetry packet: normal raise / lower conditions apply

In addition to the slow power ramp up, three LQ-based conditions will raise the power immediately to the maximum configured value.

1. If the LQ ever drops below the hard limit (50% LQ), the power will jump to the max.
2. If the LQ drops suddenly in a single telemetry update compared to the moving average. This is intended to react to flying behind a structure where the LQ suddenly takes a hit and is expected to drop further. Example: LQ is running 100% (as ExpressLRS does under most conditions) and the TX receives a telemetry packet with 80% LQ, the power will jump to the max.
3. If telemetry is lost entirely with the arm switch high. Any time the TX is "disconnected" while armed, the power will jump to the max.

## Notes

### Minimum Recommended Telemetry Ratio

Because dynamic power relies on information coming back from the RX to know how to adjust the power, dynamic power is only available if the "Telemetry Ratio" is not set to Off / Race. Any ratio will allow it to operate, but the algorithm is optimized around having at least 2x Link Statistics telemetry packets per second, which is provided with the "Std" telemetry option. If using a manual telemetry ratio, it is recommended to use **at least** the ratio suggested below.

| Packet Air Rate | Telemetry Ratio |
|---|---|
| 1000Hz | 1:128 |
| 500Hz | 1:128 |
| 250Hz | 1:64 |
| 200Hz | 1:64 |
| 150Hz | 1:32 |
| 100Hz | 1:32 |
| 50Hz | 1:16 |

On startup, the output power will be set to the lowest possible value. If telemetry is lost while disarmed, the output power will stay at the current value until telemetry is received again. This is intended to prevent everyone's TX from blasting to max power when swapping batteries.

### OSD Power Display

To see the current output power on your FPV OSD, enable the `Tx uplink power` OSD element. Uplink power is not available if `Switch Mode` is set to `Hybrid`, or older Betaflight (<4.3.0) and iNav (<2.6.0) versions. This value updates 8x more quickly in fullres packet modes.

### EdgeTX / OpenTX Power Readout

Alternatively, a handset special function can be used to generate an audio notification when changes in the power level changes.

* Set a logical switch to `|Δ|>x` / `TPWR` / `1mW` as shown in L04 below. The logical switch triggers when the power changes by at least 1mW.

<figure markdown>
![OpenTX logical switch page, L04 is set to absolute delta equal or larger than x, TPWR, 1mW](https://cdn.discordapp.com/attachments/738450139693449258/872521918446714920/IMG_9220.JPG)
</figure>

* For a readout when the power changes, set a special function triggered from the logical switch, and assign `Play Value` / `TPWR` / `1x` (SF10 in the picture). If instead you'd prefer the power to be read out periodically, choose a switch to enable the special function, and assign `Play Value` / `TPWR` / (SF11 in the picture, with 10s interval).

<figure markdown>
![OpenTX Special function page, SF10 is set to L04, Play Value, TPWR, 1x. SF11 is set to SB1 down, Play Value, TPWR, 10s](https://cdn.discordapp.com/attachments/738450139693449258/872521921382744074/IMG_9221.JPG)
</figure>

!!! note "Note"
    OpenTX has no value for 50mW in the CRSF Telemetry protocol and instead will be read as 0mW. EdgeTX starting 2.5.0 have the proper 50mW readout.
