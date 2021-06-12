---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

**This documentation applies to versions above 1.0.0-RC1**

***:warning: Put your arm switch on AUX1 :warning:***

ExpressLRS has two options for how switches are transmitted: Normal mode and `HYBRID_SWITCHES_8`. The switch mode selected MUST match (select either Option 1 or Option 2) between the TX module and RX.

1. The default choice is to have 8x 2-position switches. 🥈 That's really about all there is to this mode, other than noting that you should have your arm switch on AUX1. ExpressLRS uses AUX1 to determine if your model is armed.

| Channel | Resolution | Frequency |
|---|---|---|
| AUX1 | 1-bit / 2-position | Every packet, ARM channel |
| AUX2-AUX8 | 1-bit / 2-position | Every packet |


2. The other option is `HYBRID_SWITCHES_8` where the switches are broken into different types

| Channel | Resolution | Frequency |
|---|---|---|
| AUX1 | 1-bit / 2-position | Every packet, ARM channel |
| AUX2-AUX7 | 3-bit / 2-position, 3-position, or 6-position | Round-robin |
| AUX8 | 4-bit / 16-position | Round-robin |

The first switch (AUX1) is sent with every packet. Put. Your. Arm. On. AUX1. For the remaining 7 switches, one switch is sent with each packet (in addition to AUX1). When a switch changes, it is given priority to be sent in the next packet to try to reduce its latency. 

## AUX 1

:warning: Put your arm switch on AUX1 :warning:. AUX1 is the low-latency switch, sent with every packet, and only supports on/off (2-position) operation. ExpressLRS uses AUX1 to determine if your model is armed, and should set up on the transmitter so that ~1000 is disarmed, ~2000 is armed.

## AUX 2-7

The majority of the aux channels, AUX2 - AUX7, work with 2-position switches, 3-position switches, or 6-position switches / selector buttons.

Approx. Channel Input (us) | Channel Output (us) | Ardupilot Mode
-- | -- | --
988 | 1000 | Mode1 (up position for 2-pos / 3-pos)
1192 | 1275 | Mode2
1398 | 1425 | Mode3
1500 | 1500 | Mode4 (center position in 3-pos)
1602 | 1575 | Mode4
1807 | 1725 | Mode5
2011 | 2000 | Mode6 (down position for 2-pos / 3-pos)

## AUX 8

AUX8 is the wide range channel, supporting 16 positions. You can stack all your modes in here, Bardwell style, or get some low-res camera pan action-- 180 degrees / 16 actually isn't terrible. Clever math-heads might note that there's no "center position" (1500us) in a 16-position switch, so using AUX8 with a 3-position switch means it will come out as 1533 at the flight controller.

Switch Position | Channel Output (us) | Switch Position | Channel Output (us)
--|--|--|--
0 | 1000 | 8 | 1533
1 | 1066 | 9 | 1600
2 | 1133 | 10 | 1666
3 | 1200 | 11 | 1733
4 | 1266 | 12 | 1800
5 | 1333 | 13 | 1866
6 | 1400 | 14 | 1933
7 | 1467 | 15 | 2000


## FAQ

### Why do you keep saying "*put arm on AUX1*"?

For safety reasons.

In HYBRID_SWITCHES_8 mode, AUX1 is sent with every packet going out, this is the most reliable way to be able to tell your model to disarm. If your arm switch is in another aux channel, it may be several packets before that switch is transmitted, and there's no guarantee that the RX will actually receive that packet. There's a non-trivial chance your model **may not ever disarm** if the link quality is low and it just so happens that the packet containing the arm switch is getting missed every time. Forcing the arm switch into every packet on AUX1 means that if **any** packet is received by ExpresLRS, it will disarm your model, not just a less than 1-in-7 chance.

It also protects against unintentional disarms caused by a corrupt packet changing the value of the arm switch to disarmed. Betaflight requires that 4x "disarm" commands are received before disarming to guard against this possibility. With arm on AUX1, a single corrupt packet can not disarm your model. With arm on AUX2-8, the one corrupt switch value will be sent 6 times before the value is refreshed, but the flight controller would have already disarmed by that point.

### I use a 3-pos switch for arm, this software is unusable

You can still use a 3-position switch to arm! AUX1 just needs to be 2-position, not the physical switch. Simply adjust the mixer in your transmitter so AUX1 works like an on-off switch. If your 3-position arm switch had a second function as well, such as enabling Blackbox, just use one of the other 7 AUX channels to send the switch on a second channel.

### Why can't I have switches / potentiometers with full 10-bit resolution?

A lot of the magic of ExpressLRS comes from its small packet sizes, there simply is not enough space to put all that data. There are tricks that can be done with interleaving sticks and switches packets but we believe sticks should be in every packet for the lowest control latency. Different switch modes with higher resolution may be added further down the road for setups where higher latency doesn't matter.