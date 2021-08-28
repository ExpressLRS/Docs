![FAQ-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/faq.png)

Below, we have a list of frequently asked questions about ELRS

## Why ExpressLRS?

ExpressLRS is competing with some of the best commercial solutions out there, but all are expensive 🙁. Well, ELRS is not 😄, it can be set up for around 60$ (Using second-hand r9 hardware). It also is better than many (higher sensitivity, lower latency👌).

## Is it better than the commercial solutions?

It is faster than most links out there with a latency of 6.5ms (at 200hz). At 250hz 100mW 2.4GHz it is capable of ranges 30km+.

## Which OpenTX version works with ExpressLRS

[OpenTX 2.3.12](https://www.open-tx.org/downloads.html#Releases23-ref) or newer should work just fine. No need to use OpenTX Nightly, unless you have requirements not present in the Stable versions.

[EdgeTX 2.4.0](https://github.com/EdgeTX/edgetx) or newer should work too.

## Why do I need to update OpenTX?

ExpressLRS needs your radio to support crsfshot (a.k.a. Mixersync) to work properly. This will give you the lowest possible latency and optimal consistency of the RC link. When your radio does not have crsfshot working, this often shows in your ExpressLRS Lua script. The Lua script top bar will show inconsistent numbers like 0:63 or is stuck at 0:250 at every packet rate rate you select.

**The Lua script top bar should always show a stable 0:[user selected packet rate]**

For example: 0:50, 0:150, 0:250, 0:500, ...

When that is the case your radio has crsfshot working and you're good to go. Click [here](../quick-start/tx-prep/) to read more on OpenTX.

## How can I flash/update x receiver/module?

See [Getting Started](../quick-start/getting-started/) page

## Will x Receiver work with y TX Module from z Manufacturer?

Any Receiver and TX Module from the same Band (2.4GHz or 900Mhz) will work together. Supported R9 receivers will work with the 900Mhz modules from Happy Model, Namimno RC and the R9M, same with the other 900Mhz receivers, DIY or off-the-shelf. Likewise, any 2.4Ghz receivers should work with any 2.4Ghz TX Modules, from any manufacturer and even the DIY ones. This is as long as they have the same binding phrase and configuration options (Regulatory Domain, Performance Options and Extra Data).

## What's the difference between the different Happymodel 2.4GHz receivers (PP, EP1, EP2)?

The difference between the PP and the EP1/EP2 is only the processor. The PP is the original design and uses an STM32 while the EP1/EP2 use an ESP82xx. Both offer firmware update through Betaflight passthrough, but the EPx also support firmware upload over wifi. The EP1 is the same as the EP2 except it has a U.FL/IPEX1 connector for an external antenna. The wifi capability of the ESP is not used apart from the update procedure, and the wifi is only enabled shortly after power-up if no TX connection is received (`AUTO_WIFI_ON_INTERVAL` if bound, 60s otherwise). Receiver performance should be identical between the two.
If you're confused by the PP being more expensive, it's because there is a shortage of the STM part.

## What is required to achieve a 500hz update rate on 2.4ghz on OpenTX?

Make sure to enable the "Use_500hz" option when you flash the TX and RX. You must also be on a version of OpenTX that supports Mixer Sync (TBS Nightly, ELRS Nightly, OpenTX 2.3.12 or newer, or EdgeTX). USE_500Hz option is now enabled be default starting with 1.0.0-RC9 (6358aa).

To confirm your update rate is working as intended, you can use the ExpressLRS Lua script to check the current update rate and confirm you are getting 500hz.

## How many channels does ELRS support?
12 channels(suspicious asterisk). There is not enough bandwidth to support all full-resolution channels (e.g. for pan/tilt servos). It is possible that future versions could include some tricks to expand this by sending extra channel data in a slow upload, but it is not a priority for development. Therefore, ELRS provides:
  * 4x full-resolution (10-bit) channels for sticks (CH1-4)
  * Either:
    * **Standard Mode** 4x 2-position channels sent every frame (increased to 8x in 1.0), OR
    * **HYBRID_SWITCHES_8 Mode** 8x 3-position channels, where CH5 (AUX1/ARM) is sent every frame, and the other 7 are sent round-robin (7 frames to send all channels) also changed in 1.0, see [Switch Modes](../software/switch-config/)

## Is my binding phrase a secret?

No, just like what channel your VTX is on is not a secret. The binding phrase is not security, it is anti-collision. If everyone kept their VTX channel a secret, the chances of you blasting someone out of the sky accidentally is pretty high. To provide the best chance of not interfering with other pilots and them not interfering with you, be sure you're not using the same dumb bind phrase as someone else. Express your style with a hilarious or saucy bind phrase.

## What does RQLY, TQLY, RSSI x2, SNR x2 mean?

| Datapoint| Description   |   Range | Info |
|------|-----------------------------------------|---|---|
| RQly | Uplink - link quality (valid packets)                |  0 - 100  | The number of successful packets out of the last 100 from TX → RX |
| 1RSS | Uplink - received signal strength antenna 1 (RSSI)   | -128 - 0  | RSSI dBm as reported by the RX. Values vary depending on mode, antenna quality, output power and distance |
| 2RSS | Uplink - received signal strength antenna 2 (RSSI)   |           | Second antenna RSSI, used in diversity mode |
| ANT  | RX active Antenna                                    |           | Not populated currently |
| RSNR | Uplink - signal-to-noise ratio                       |           | SNR reported by the RX. Value varies mostly by radio chip and gets lower with distance (once the agc hits its limit)|
| RFMD | Uplink - update rate                                 |           |  |
| TPWR | Uplink - transmitting power                          |           | 50mW reported as 0, as CRSF/OpenTX do not have this option |
| TQly | Downlink - link quality (valid packets)              |  0 - 100  | An LQ indicator of telemetry packets received RX → TX |
| TRSS | Downlink - received signal strength (RSSI)           |           | RSSI dBm of telemetry packets received by TX |
| TSNR | Downlink - signal-to-noise ratio                     |           | SNR reported by the radio in the TX module when receiving telemetry packets |


## Is it normal to get "RF Signal Critical" when plugging in?
Yes. When the connection is first established, the link quality starts at 0 and climbs as packets are received. Expect low RF Signal warnings until enough packets are reported received to pass your warning threshold set in OpenTX -> Telemetry -> RSSI -> Low alarm / Critical alarm.