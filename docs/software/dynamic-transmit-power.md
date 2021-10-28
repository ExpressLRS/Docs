---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

## Description

Dynamic Power allows the TX module to *lower* its output power from the configured power level using the telemetry from the RX. The TX will lower power if the RSSI dBm is far enough above the sensitivity limit and will raise power if it is not, has a low LQ, or has a sudden drop in LQ. Advanced telemetry is not required for this feature, just a non-zero Telemetry Ratio.

⚠️ Dynamic Power relies on telemetry. If no telemetry is received by the TX while armed, then the power level will be kicked up to the maximum configured power level. ⚠️

### Feature DEMO
* Lowering/Raising power on a long-range flight: https://www.youtube.com/watch?v=Ah6h-QqM6Xs
* LQ-based power boost: https://www.youtube.com/watch?v=SMOfxdzQIJY

Note: These videos were taken with a test version. The power lowering/raising thresholds are different from the current implementation.

## Details

### Lowering Power

The algorithm averages the last few RSSI dBm readings from the RX and will compare the average with the sensitivity limit for the current packet rate. If the RSSI is far enough from the limit, the TX output power is lowered one level. Example: 250Hz = -108dBm sensitivity limit, if the current RSSI average is above -78dBm, the power will be lowered. This can only occur once every few seconds.

### Raising Power

The output power will never exceed the configured power output level in any situation.

The opposite of the "lower power" algorithm is also in place, to raise power as needed slowly such as when flying away on a long range flight. When the average RSSI is too close to the sensitivity limit for the current packet rate, the TX power is raised one level. Example: 250Hz = -108dBm sensitivity limit, if the current RSSI average is less than -93dBm, the power will be raised. This can only occur once every few seconds.

In addition to the slow power ramp up, there are two LQ-based conditions that will raise the power immediately to the maximum configured value.

1. If the LQ ever drops below a hard limit. Example: LQ of 50% is received by the TX, the power will jump to max.
2. If the LQ drops suddenly in a single telemetry update compared to the moving average. This is intended to react to flying behind a structure where the LQ suddenly takes a hit and is expected to drop further. Example: LQ is running 100% (as ExpressLRS do) and the TX receives a telemetry packet with 80% LQ, the power will jump to max.

### Override via AUX Channel
When this channel is HIGH (>1500us) the dynamic power feature will be disabled and the output power will be set to the configured power level. AUX channels between AUX9-AUX12 (CH13-CH16) is supported.

* Switch feature demo: https://www.youtube.com/watch?v=wdPWw2xu8Ig

## Notes

### Minimum Recommended Telemetry Ratio
Because dynamic power relies on information coming back from the RX to know how to adjust the power, dynamic power is only available if the "Telemetry Ratio" is not set to Off. Any ratio will allow it to operate, but the algorithm is optimized around having at least 2x Link Statistics telemetry packets per second. Link telemetry is always available regardless of if the `ENABLE_TELEMETRY` option is used. Minimum recommended Telemetry Ratio per packet rate:

| Packet Air Rate | ENABLE_TELEMETRY = Off | ENABLE_TELEMETRY = On |
|---|---|---|
| 500Hz | 1:128 | 1:128 |
| 250Hz | 1:128 | 1:64 |
| 200Hz | 1:128 | 1:64 |
| 150Hz | 1:64 | 1:32 |
| 100Hz | 1:64 | 1:32 |
| 50Hz | 1:32 | 1:16 |

On startup, the output power will be set to the max configured value until telemetry is received to be able to lower it. If telemetry is lost, the output power will stay at the current value until telemetry is received again. This is intended to prevent everyone's TX from blasting to max power when swapping batteries. To return to max configured power, restart the transmitter.

### OpenTX Power Readout
The TX power telemetry is not transferred from/to RX, so there's no way to display it on OSD. Instead, readout TPWR from your radio is probably a practical workaround to check the working status of the dynamic power, as shown in the demo video.

1. Firstly, set a logical switch to `|Δ|>x` / `TPWR` / `1mW` as shown in L04 in the picture. 
![OpenTX logical switch page, L04 is set to absolute delta equal or larger than x, TPWR, 1mW](https://cdn.discordapp.com/attachments/738450139693449258/872521918446714920/IMG_9220.JPG)

2. Next, for a readout when the power changes, set a special function triggered from the logical switch previously set, and assign `Play Value` / `TPWR` / `1x` (SF10 in the picture). When you want a readout periodically throughout a flight, choose a switch to trigger another special function, and assign `Play Value` / `TPWR` / [an interval you want] (SF11 in the picture, with 10s interval).
![OpenTX Special function page, SF10 is set to L04, Play Value, TPWR, 1x. SF11 is set to SB1 down, Play Value, TPWR, 10s](https://cdn.discordapp.com/attachments/738450139693449258/872521921382744074/IMG_9221.JPG)

Note: OpenTX has no value for 50mW power in the CRSF telemetry protocol. When TPWR displays 0mW, it is actually 50mW TX power.