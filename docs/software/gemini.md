---
template: main.html
description: ExpressLRS Gemini is a Dual Channel 2.4GHz or 900MHz System. Gemini is not Dual Band.
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

## What is Gemini

Gemini is a dual channel 2.4GHz or 900MHz system. However, it is NOT Dual Band.

A Gemini Tx module has 2 sx1280(for 2.4GHz) or sx1276(for 900MHz) tranceivers and simultaneously transmits a packet with a frequency difference of 40MHz. A true diversity Rx is used to receive both packets simultaneously. Transmitting on 2 separate frequencies provides better interference avoidance in a similar way DVDA does by sending repeat packets sequentially on different frequencies.

The current implementation sends identical packets. This provides a good starting point for introducing some novel features in the future!


