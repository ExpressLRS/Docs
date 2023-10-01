---
template: main.html
description: ExpressLRS Gemini is a Dual Channel 2.4GHz or 900MHz System. Gemini is not Dual Band.
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

## What is Gemini

Gemini is a dual channel 2.4GHz OR 900MHz system. However, it is currently NOT Dual Band e.g. 2.4GHz and 900MHz simultaneous transmissions.

In Gemini Mode, a TX module simultaneously transmits a packet in two frequencies 40MHz apart for 2.4GHz and ~10MHz apart for 900MHz users.  The packet separation used is half of the frequency domain selected and will vary a little. A true diversity Receiver is used to receive both packets simultaneously. Transmitting on 2 separate frequencies provides better interference avoidance and/or mitigation, in a similar way DVDA does by sending repeat packets sequentially on different frequencies. This means, the Receiver has an increased chance of receiving the packet. This results in a much stable LQ.

## What about using Gemini with DVDA?

Gemini doubles the redundancy of DVDA modes.  For example, D500 sends 2 repeat packets on 2 different frequencies. When using F500 with a Gemini Tx you will now have 4 packets sent across 4 different frequencies.

When using D250 which sends 4 repeat packets across 3 frequencies.  With Gemini you will now have 8 repeat packets across 6 different frequencies.

# What are the benefits?

## Freestylers

Flying in urban environments with lots of RF noise? Gemini will help to dodge the interference and maintain a strong link.

## Racers

Flying at events with 6 to 8 up racers, plus who knows how many handsets left on in the pits, can cause your precious link to take a hit.  Gemini is an obvious choice for these environments when every packet counts.

## Lovers of telemetry

A Gemini Tx has the advantage of not only sending simultaneous packets, but also receiving simultaneous packets.  Or when used in single antenna mode (or switch mode) both antennas will listen for the same TLM packet, in the same way a diversity Rx listens for RC packets.  So your TLM link becomes stronger with fewer missed packets, even when not used in Gemini mode and with single antenna receivers.

## Airport and Mavlink users

For data links a single missed packet can mean more than 1 missed packet. If a single packet is missed, this means the rest of the data that was received for that Mavlink packet is now wasted. As the Mavlink packet may have been split across multiple OTA packets and will not be complete. The single missed packet can turn into 10 packets missed. Gemini will help with making sure you get the highest Mav packet rate possible!

# Will Gemini increase my range?

No. The packet sensitivity remains the same for the RF mode used.  Gemini will help maintain a higher LQ to the point of failsafe.  However failsafe will still happen at approximately the same distance e.g. the moon.

<figure markdown>
<iframe width="640" height="390" src="https://www.youtube.com/embed/VcC50cX3a7E?si=qao7AO_M5Ykbn2jI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</figure>

<figure markdown>
![Gemini Info](../assets/images/gemini-sunjun.png)
</figure>
