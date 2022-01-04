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

**The Lua script top bar should always show a stable 0/[user selected packet rate]**

For example: 0/50, 0/150, 0/250, 0/500, ...

When that is the case your radio has crsfshot working and you're good to go. Click [here](quick-start/transmitters/tx-prep.md) to read more on OpenTX.

## How can I flash/update x receiver/module?

See [Getting Started](quick-start/getting-started.md) page

## Will x Receiver work with y TX Module from z Manufacturer?

Any Receiver and TX Module from the same Band (2.4GHz or 900Mhz) will work together. Supported R9 receivers will work with the 900Mhz modules from Happy Model, Namimno RC and the R9M, same with the other 900Mhz receivers, DIY or off-the-shelf. Likewise, any 2.4Ghz receivers should work with any 2.4Ghz TX Modules, from any manufacturer and even the DIY ones. This is as long as they have the same binding phrase and configuration options (Regulatory Domain, Performance Options and Extra Data).

## What's the difference between the different Happymodel 2.4GHz receivers (PP, EP1, EP2)?

The difference between the PP and the EP1/EP2 is only the processor. The PP is the original design and uses an STM32 while the EP1/EP2 use an ESP82xx. Both offer firmware update through Betaflight passthrough, but the EPx also support firmware upload over wifi. The EP1 is the same as the EP2 except it has a U.FL/IPEX1 connector for an external antenna. The wifi capability of the ESP is not used apart from the update procedure, and the wifi is only enabled shortly after power-up if no TX connection is received (`AUTO_WIFI_ON_INTERVAL` if bound, 60s otherwise). Receiver performance should be identical between the two.
If you're confused by the PP being more expensive, it's because there is a shortage of the STM part.

## What is required to achieve a 500hz update rate on 2.4ghz?

Make sure that your radio is set to use 400K Baud Rate and you're running at least OpenTX 2.3.12 or EdgeTX 2.4.0. These firmware versions have Mixer Sync or CRSFShot.

To confirm your update rate is working as intended, you can use the ExpressLRS Lua script to check the current update rate and confirm you are getting 500hz. See [Using the Lua Script](quick-start/transmitters/lua-howto.md).

## How many channels does ELRS support?
12 channels(suspicious asterisk). There is not enough bandwidth to support all full-resolution channels. It is possible that future versions would further expand this by sending extra channel data in a slow upload, but it is not a priority for development. Therefore, ELRS provides:

  * 4x full-resolution (10-bit) channels for sticks (CH1-4)
  * Either:
    * **Standard Mode** 4x 2-position channels sent every frame (increased to 8x in 1.0; dropped in 2.x), OR
    * **HYBRID_SWITCHES_8 Mode** 1x 2-position channel, AUX1 (CH5; Must be used for Arming), 6x 2-position/3-position/6-position (AUX2-7) and 1x 16-position (AUX8), OR
    * **WIDE HYBRID Mode** 1x 2-position channel, AUX1 (CH5; Must be used for Arming), 7x 64 or 128-position channels (AUX2-8). Available via the Lua Script since 2.0.
    
  See [Switch Modes](software/switch-config.md) more more details.


## Is my binding phrase a secret?

No, just like what channel your VTX is on is not a secret. The binding phrase is not security, it is anti-collision. If everyone kept their VTX channel a secret, the chances of you blasting someone out of the sky accidentally is pretty high. To provide the best chance of not interfering with other pilots and them not interfering with you, be sure you're not using the same dumb bind phrase as someone else. Express your style with a hilarious or saucy bind phrase.

## What does RQLY, TQLY, RSSI x2, SNR x2 mean?

| Datapoint| Description   |   Range | Info |
|------|-----------------------------------------|---|---|
| RQly | Uplink - link quality (valid packets)                |  0 - 100  | The number of successful packets out of the last 100 from TX → RX |
| 1RSS | Uplink - received signal strength antenna 1 (RSSI)   | -128 - 0  | RSSI dBm as reported by the RX. Values vary depending on mode, antenna quality, output power and distance |
| 2RSS | Uplink - received signal strength antenna 2 (RSSI)   |           | Second antenna RSSI, used in diversity mode |
| ANT  | RX active antenna                                    | 0 - 1     | Active antenna for diversity RX |
| RSNR | Uplink - signal-to-noise ratio                       |           | SNR reported by the RX. Value varies mostly by radio chip and gets lower with distance (once the agc hits its limit)|
| RFMD | Uplink - packet rate                                 | 0 - 7     | [RF Mode Indexes](info/signal-health.md#rf-mode-indexes-rfmd) |
| TPWR | Uplink - transmitting power                          |           | 50mW reported as 0, as CRSF/OpenTX do not have this option |
| TQly | Downlink - link quality (valid packets)              |  0 - 100  | An LQ indicator of telemetry packets received RX → TX |
| TRSS | Downlink - received signal strength (RSSI)           |           | RSSI dBm of telemetry packets received by TX |
| TSNR | Downlink - signal-to-noise ratio                     |           | SNR reported by the TX for telemetry packets |

