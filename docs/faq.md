---
template: main.html
description: We answer the most commonly asked questions here.
hide:
  - navigation
---

![FAQ-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/faq.png)

## <span class="custom-heading" data-id="1">Why ExpressLRS?</span>

??? faq "Why ExpressLRS?"
    ExpressLRS is a high-performance, open-source radio control protocol built from the ground up to be an extremely fast (**E**xpress), extremely sensitive (**L**ong **R**ange) **S**ystem. ELRS uses Semtech SX12xx LoRa transceivers and a lightweight, highly optimized over-the-air (OTA) protocol to provide superior performance compared to legacy RC links. While ExpressLRS started with DIY and repurposed hardware, a large number of manufacturers are now producing high-quality, low-cost transmitters and receivers to make it easy for anyone to get started!
## <span class="custom-heading" data-id="2">How does ExpressLRS compare to other systems?</span>

??? faq "How does ExpressLRS compare to other systems?"
    ExpressLRS is capable of extremely high packet rates (up to 1000 Hz) and extreme sensitivity (ranges well over 100+ km have been achieved with 2.4 GHz hardware), making it extremely competitive with any commercially available system. And since ExpressLRS is open-source, it costs much less than other systems too!
## <span class="custom-heading" data-id="3">Which OpenTX/EdgeTX version do I need and why should I update?</span>

??? faq "Which OpenTX/EdgeTX version do I need and why should I update?"
    ExpressLRS requires [OpenTX 2.3.12](https://www.open-tx.org/downloads.html#Releases23-ref) or newer, as it depends on CRSFshot (a.k.a mixer sync) to work properly. However, as OpenTX is no longer being maintained, it is strongly recommended that you update to [EdgeTX](https://github.com/EdgeTX/edgetx) in order to take advantage of the latest performance improvements and bug fixes. 
	
	Click [here](https://www.expresslrs.org/quick-start/transmitters/tx-prep.md) to read more about radio firmware requirements and setup.

## <span class="custom-heading" data-id="4">How do I flash/update my receiver/module?</span>

??? faq "How do I flash/update my receiver/module?"
    See [Getting Started](https://www.expresslrs.org/quick-start/getting-started.md) for a Quick Setup guide and detailed instructions on flashing, features, hardware, and troubleshooting.

## <span class="custom-heading" data-id="5">Will x Receiver work with y TX Module from z Manufacturer?</span>

??? faq "Will x Receiver work with y TX Module from z Manufacturer?"
    Any Receiver and TX Module from the same Band (e.g. 2.4 GHz or 900 MHz) will work together. For example, a 900 MHz receiver from BetaFPV will work with a 900 MHz TX module from HappyModel. Likewise, any 2.4 GHz receiver will work with any 2.4 GHz TX Modules, from any manufacturer (including DIY ones). This of course assumes the hardware is working properly, flashed with the same major ELRS version (e.g. 3.x), and is using the same binding phrase and configuration options (e.g. Regulatory Domain).

## <span class="custom-heading" data-id="6">What's the difference between the different 2.4 GHz receivers (PP, EP1/RP1, EP2/RP2, EP1 Dual, RP3, RP4TD, TCXO)?</span>

??? faq "What's the difference between the different 2.4 GHz receivers (PP, EP1/RP1, EP2/RP2, EP1 Dual, RP3, RP4TD, TCXO)?"
    Early ELRS receivers like the HappyModel PP used an STM32 MCU, while later designs EP1/EP2/etc use ESP MCUs. All offer firmware updates via UART or Betaflight Passthrough, but the ESP-based hardware also support firmware update and configuration over WiFi. The EP1/RP1 receivers use u.fl (external) antennas, while the EP2/RP2 receivers use on-board ceramic antennas. Receivers like the RP3 and R24D have two antennas for antenna diversity, while receivers like the EP1 Dual, RP4TD, and SuperD add a second parallel RF path to provide full receiver diversity. 
	
	See [here](https://www.expresslrs.org/software/gemini/#comparison-with-other-antenna-modes) for more about different antenna configurations. 

## <span class="custom-heading" data-id="7">What is required to achieve a 1000 Hz update rate on 2.4 GHz?</span>

??? faq "What is required to achieve a 1000 Hz packet rate on 2.4 GHz?"
    In order to achieve the fastest packet rate, your radio must be running a supported [firmware](https://www.expresslrs.org/quick-start/transmitters/tx-prep/#radio-operating-system), set to a minimum [hardware baud rate](https://www.expresslrs.org/quick-start/transmitters/tx-prep/#serial-baud-rate) of 921000, and be connected to a serial ELRS receiver (SPI receivers do not support the FLRC modes required). Also make absolutely sure [ADC filter](https://www.expresslrs.org/quick-start/transmitters/tx-prep/#adc-filter) is disabled on your radio, and that you have applied the appropriate RC Link [Preset](https://betaflight.com/docs/wiki/configurator/presets-tab) in Betaflight. 

    You can use the ELRS lua to check your current packet rate and ensure the radio mixer sync is working properly. See [Using the Lua Script](https://www.expresslrs.org/quick-start/transmitters/lua-howto.md) for more details.

## <span class="custom-heading" data-id="8">How many channels does ELRS support?</span>

??? faq "How many channels does ELRS support?"
    ELRS supports up to 16 channels*. Channels 1-4 are always sent at full-resolution (10-bit). The resolution and update rate of the remaining channels can be configured as follows, based on your requirements:

      * 4x full-resolution (10-bit) channels for sticks (CH1-4) with either:
        * **HYBRID Mode** 1x 2-position channel, AUX1 (CH5; Must be used for Arming), 6x 2-position/3-position/6-position (AUX2-7) and 1x 16-position (AUX8), OR
        * **WIDE Mode** 1x 2-position channel, AUX1 (CH5; Must be used for Arming), 7x 64 or 128-position channels (AUX2-8). Available via the Lua Script since 2.0.
      * 8x full-resolution (10-bit, ext-limits) with 1x 2-position channel, AUX1
      * 16x full-resolution (10-bit, ext-limits, all half rate) with 1x 2-position channel, AUX1
      * 12x full-resolution (10-bit, ext-limits) with 1x 2-position channel, AUX1, channels AUX2-9 run at half rate.
        
      See [Switch Modes](https://www.expresslrs.org/software/switch-config.md) for more details on switch modes and how they work.

## <span class="custom-heading" data-id="9">Is my binding phrase a secret?</span>

??? faq "Is my binding phrase a secret?"
    No, just like what channel your VTX is on is not a secret. If everyone kept their VTX channel a secret, the chances of you blasting someone out of the sky accidentally is high. The binding phrase is *not* used for security, it is used to prevent collisions. Specifically, the binding phrase is hashed and used to seed the random number generator that determines the frequency hopping pattern. Thus, each binding phrase results in a unique hopping pattern, minimizing the likelihood of collisions with other users.  To provide the best chance of not interfering with other pilots and them not interfering with you, be sure you're not using the same dumb bind phrase as someone else. Express your style with a hilarious or saucy bind phrase.

## <span class="custom-heading" data-id="10">What does RQLY, TQLY, RSSI x2, SNR x2 mean?</span>

??? faq "What do RQLY, TQLY, RSSI x2, SNR x2 mean?"

    | Datapoint| Description   |   Range | Info |
    |------|-----------------------------------------|---|---|
    | RQly | Uplink - link quality (valid packets)                |  0 - 100  | The number of successful packets out of the last 100 from TX. TX → RX |
    | 1RSS | Uplink - received signal strength antenna 1 (RSSI)   | -128 - 0  | First antenna RSSI dBm as reported by the RX. Values vary depending on mode, antenna quality, output power and distance. TX → RX |
    | 2RSS | Uplink - received signal strength antenna 2 (RSSI)   |           | Second antenna RSSI dBm, for diversity receivers.  TX → RX |
    | ANT  | RX active antenna                                    | 0 - 1     | Active receiver antenna for diversity RX.  |
    | RSNR | Uplink - signal-to-noise ratio                       |           | SNR reported by the RX. Value varies mostly by radio chip and gets lower with distance (once the agc hits its limit). TX → RX |
    | RFMD | Uplink - packet rate                                 | 0 - 7     | [RF Mode Indexes](info/signal-health.md#rf-mode-indexes-rfmd) |
    | TPWR | Uplink - transmitting power                          |           | 50mW reported as 0, as CRSF/OpenTX do not have this option |
    | TQly | Downlink - link quality (valid packets)              |  0 - 100  | An LQ indicator of telemetry packets received by TX. RX → TX |
    | TRSS | Downlink - received signal strength (RSSI)           |           | RSSI dBm of telemetry packets received by TX. RX → TX |
    | TSNR | Downlink - signal-to-noise ratio                     |           | SNR reported by the TX for telemetry packets. RX → TX |

    See the [Signal Health](https://www.expresslrs.org/info/signal-health/) page for more info on interpreting link stats. 

If you have other questions or concerns, or maybe you need further help that is not covered by this Guide, head over to our Discord Channel or Facebook Group!

<span style="padding-left:15%; display:inline; text-align:center">[ExpressLRS Discord :fontawesome-brands-discord:](https://discord.gg/dS6ReFY){ .md-button }</span>
<span style="padding-left:15%; display:inline; text-align:center">[ExpressLRS Facebook :fontawesome-brands-facebook:](https://www.facebook.com/groups/636441730280366){ .md-button }</span>

<script src="../assets/javascripts/admonition-enhancement.js"></script>
