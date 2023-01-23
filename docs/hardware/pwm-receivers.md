---
template: main.html
description: ExpressLRS supports PWM output without the need of converters.
---

![HW Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/hardware.png)

ExpressLRS now supports direct PWM output from receivers that have been specifically designed for this mode. Any version-compatible TX firmware (e.g. 2.0.0 TX with 2.0.0 RX) works with PWM receivers-- only the RX firmware is specific to PWM. This documentation refers to only receivers with native PWM output, not receivers attached to external CRSF to PWM converters such as the [CRServoF](https://github.com/CapnBry/CRServoF/) or Matek CRSF-PWM-C.

## Channel Mapping and Failsafe
The default channel mapping is straight through: CH1 from the TX goes to PWM Output 1, CH2 to Output 2, etc. To change this on ESP-based receivers, allow the receiver to go into WiFi mode then use the WebUI to configure the mapping. Any input channel can be mapped to any output channel, and the same input can be used for as many outputs as desired. AUX1/CH5 is always 1-bit, so you'll likely want to change this mapping to a channel with more resolution.

<figure markdown>
![default PWM Output webui](../assets/images/web-pwmoutput.png)
<figcaption>PWM Output WebUi</figcaption>
</figure>

Failsafe values are set using this UI as well with values that can range from 988us to 2012us. Failsafe is entered if the receiver is connected and 1 second passes without a valid channels packet being received. On startup, no pulses are generated until a transmitter connects, allowing ESC throttle calibration with the standard "raise the throttle before connecting" method. The default failsafe value is 1500us for all channels except Output 3, which defaults to 988us.

## Channel Resolution
PWM output is still subject to the resolution of the ELRS protocol, which means there are still only 4x full resolution channels (10-bit CH1-CH4) and 8x switch channels (CH5-CH12). For the best resolution on the switch channels, use `Switch Mode: Wide` and a `TLM Ratio` of `1:8` to `1:256` for 7-bit (128 pos) switch channel resolution. Higher TLM Ratios (1:2 and 1:4) are reduced to 6-bit (64 pos) resolution. Remember that switch channels are sent one per packet in Wide mode, taking 8 packets to send all 7 channels (e.g. 150Hz mode 1:64 = 18.657Hz updates to CH6-CH12). AUX1/CH5 is sent in every packet in all switch modes but is only 1-bit (2-pos).
