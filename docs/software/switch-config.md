---
template: main.html
description: To optimize the performance of ExpressLRS, it has different Switch Modes explained in detail here.
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

# Switch Configs

!!! warning "WARNING" 
    **Put your arm switch on AUX1**, and set it as **~1000 is disarmed, ~2000 is armed**.

## Summary of Switch Configs

This table summarizes the switch configuration modes, available channel switch positions and resolutions, channel update rate, and packet rate as it applies to each channel or flight controller auxiliary channel (Aux). Below the table are descriptions for each option.

| Channel | Flight <br>Controller | Hybrid | Wide | Full Res <br>8ch | Full Res <br>16ch Rate/2 | Full Res <br>12ch Mixed |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1   | Sticks | **Normal<br>Range** | **Normal<br>Range** | **CRSF Ext<br>Limits** | CRSF Ext<br>Limits<sup>H</sup> | **CRSF Ext<br>Limits** |
| 2   | Sticks | **Normal<br>Range** | **Normal<br>Range** | **CRSF Ext<br>Limits** | CRSF Ext<br>Limits<sup>H</sup> | **CRSF Ext<br>Limits** |
| 3   | Sticks | **Normal<br>Range** | **Normal<br>Range** | **CRSF Ext<br>Limits** | CRSF Ext<br>Limits<sup>H</sup> | **CRSF Ext<br>Limits** |
| 4   | Sticks | **Normal<br>Range** | **Normal<br>Range** | **CRSF Ext<br>Limits** | CRSF Ext<br>Limits<sup>H</sup> | **CRSF Ext<br>Limits** |
| **5** | **Aux 1** | **2-pos<br>Arm** | **2-pos<br>Arm** | **2-pos<br>Arm** | **2-pos<br>Arm** | **2-pos<br>Arm** |
| 6   | Aux 2 | *6-pos*<sup>RR</sup> | *64/128<br>-pos*<sup>RR</sup> | *CRSF Ext<br>Limits*<sup>RR</sup> | CRSF Ext<br>Limits<sup>H</sup> | CRSF Ext<br>Limits<sup>H</sup> |
| 7   | Aux 3 | *6-pos*<sup>RR</sup> | *64/128<br>-pos*<sup>RR</sup> | *CRSF Ext<br>Limits*<sup>RR</sup> | CRSF Ext<br>Limits<sup>H</sup> | CRSF Ext<br>Limits<sup>H</sup> |
| 8   | Aux 4 | *6-pos*<sup>RR</sup> | *64/128<br>-pos*<sup>RR</sup> | *CRSF Ext<br>Limits*<sup>RR</sup> | CRSF Ext<br>Limits<sup>H</sup> | CRSF Ext<br>Limits<sup>H</sup> |
| 9   | Aux 5 | *6-pos*<sup>RR</sup> | *64/128<br>-pos*<sup>RR</sup> | *CRSF Ext<br>Limits*<sup>RR</sup> | CRSF Ext<br>Limits<sup>H</sup> | CRSF Ext<br>Limits<sup>H</sup> |
| 10  | Aux 6 | *6-pos*<sup>RR</sup> | *64/128<br>-pos*<sup>RR</sup> | - | CRSF Ext<br>Limits<sup>H</sup> | CRSF Ext<br>Limits<sup>H</sup> |
| 11  | Aux 7 | *6-pos*<sup>RR</sup> | *64/128<br>-pos*<sup>RR</sup> | - | CRSF Ext<br>Limits<sup>H</sup> | CRSF Ext<br>Limits<sup>H</sup> |
| 12  | Aux 8 | *16-pos*<sup>RR</sup> | *64/128<br>-pos*<sup>RR</sup> | - | CRSF Ext<br>Limits<sup>H</sup> | CRSF Ext<br>Limits<sup>H</sup> |
| 13  | Aux 9 | - | - | - | CRSF Ext<br>Limits<sup>H</sup> | CRSF Ext<br>Limits<sup>H</sup> |
| 14  | Aux 10 | - | - | - | CRSF Ext<br>Limits<sup>H</sup> | - |
| 15  | Aux 11 | - | - | - | CRSF Ext<br>Limits<sup>H</sup> | - |
| 16  | Aux 12 | - | - | - | CRSF Ext<br>Limits<sup>H</sup> | - |
|  |  | 50 thru<br>F1000 | 50 thru<br>F1000 | 100&333<br>Only | 100&333<br>Only | 100&333<br>Only |
 
### Switch Position / Channel Resolution

| Label | Description |
|:---:| --- |
| **Normal Range** | 10-bit or 1024 positions mapped to PWM 988us to 2012us (1 bit = 1us) |
| **CRSF Ext Limits** | 10-bit or 1024 positions mapped to PWM 885us to 2115us (1 bit = 1.23046875us) |
| **64 / 128-pos** | The bit depth is dependent on the selected telemetry ratio. For a telemetry ratio of 1:2 and 1:4 these channels are 6-bit/64 pos. For all other ratios, these channels are 7-bit/128 pos. The 7-bit/128 positions is 12.5% the resolution of 10-bit, and 6-bit/64 positions is 6.25% the resolution of 10-bit. This may not be enough resolution for a head tracker but definitely enough for flight modes, flaps, gear, etc. |
| **16-pos** | 4-bit which is good for flight modes, flaps, gear, etc. |
| **6-pos** | 3-bit which is good for flight modes, flaps, gear, etc. |
| **2-pos** | 1-bit for Arm, ~1000us is the **disarmed** state and ~2000us is the **armed** state (see the explanations below of why the armed state is very important for safety and performance) |

!!! note
    If using a receiver with PWM outputs and you would like to use the PWM output 5 on the receiver for a servo, gear, etc. Go into the wifi interface of the receiver and map any of the other channels to PWM Output 5. Please always still use AUX1 for the 2-pos Arm switch.

### Channel Update Rate versus Packet Rate

| Label | Description |
|:---:| --- |
| **Bold** | Every packet that is sent will include this channel (So a 150hz Packet Rate = 150hz Channel Update Rate) |
| H <br> Half Speed | Every other packet includes this channel (So a 150hz Packet Rate cut in half = 75hz Channel Update Rate) |
| RR <br> Round Robin | Channel waits its turn to be sent in a packet (So a 150hz Packet Rate sent every 7th packet = 22hz Channel Update Rate) |
| 50 thru<br>F1000 | The Hybrid and Wide switch modes are only avalable on packet rates of 50Hz, 150Hz, 250Hz, 500Hz, D250Hz, D500Hz, F500Hz, F1000Hz |
| 100&333<br>Only | The Full switch modes are only avalable on packet rates of 100Hz Full and 333Hz Full |
 
## Detailed Description of Switch Configs

ExpressLRS has a few options for how switches are transmitted: Under Hybrid and WideHybrid. **The switch mode can only be changed when a receiver is not connected.** Switch mode is changed using Lua configuration, the user_define setting is no longer needed.

For these two switch modes, the first switch (AUX1) is sent with every packet. **Put Your Arm On AUX1**. For the remaining 7 switches, one switch is sent with each packet (in addition to AUX1) and which switch is sent is rotated on each packet. 

1. The default choice is `HYBRID_SWITCHES_8` or just "Hybrid" where the switches are broken into different types

    | Channel | Resolution | Frequency |
    |---|---|---|
    | AUX1 | 1-bit / 2-position | Every packet, ARM channel |
    | AUX2-AUX7 | 3-bit / 2-position, 3-position, or 6-position | Round-robin |
    | AUX8 | 4-bit / 16-position | Round-robin |

    It takes 7 packets to send the complete set of switches before cycling back to AUX2.

2. The other choice is "WideHybrid" mode. It shares much in common with regular Hybrid mode, but with just two different types

    | Channel | Resolution | Frequency |
    |---|---|---|
    | AUX1 | 1-bit / 2-position | Every packet, ARM channel |
    | AUX2-AUX8 | 6 or 7-bit / 64 or 128-position | Round-robin |

    It takes 8 packets to send the complete set of switches before cycling back to AUX2 (one more than Hybrid). WideHybrid uses the 8th slot to transmit extra data to the receiver, including the current transmitter power. This is the only switch mode which can show TPwr on the flight controller's OSD.

### AUX 1 (All Modes)

!!! warning "WARNING" 
    **Put your arm switch on AUX1**, and set it as **~1000 is disarmed, ~2000 is armed**.
    
AUX1 is the low-latency switch, sent with every packet, and only supports on/off (2-position) operation. ExpressLRS uses AUX1 to determine if your model is armed, and should set up on the transmitter as armed at high values.

### AUX 2-7 (Hybrid)

The majority of the aux channels in Hybrid mode, AUX2 - AUX7, work with 2-position switches, 3-position switches, or 6-position switches / selector buttons.

Approx. Channel Input (us) | Channel Output (us) | Ardupilot Mode
-- | -- | --
988 | 1000 | Mode1 (up position for 2-pos / 3-pos)
1192 | 1275 | Mode2
1398 | 1425 | Mode3
1500 | 1500 | Mode4 (center position in 3-pos)
1602 | 1575 | Mode4
1807 | 1725 | Mode5
2011 | 2000 | Mode6 (down position for 2-pos / 3-pos)

### AUX 8 (Hybrid)

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

### AUX 2-8 (Wide)

In Wide switch mode, AUX2-AUX8 are 7-bit (128 position) for telemetry ratios 1:128 through 1:8, or 6-bit (64 position) for 1:4 and 1:2. These behave more like traditional channels although with lower precision. You can tell you're operating in Wide mode when a switch in the middle position shows up as 1503 instead of 1500.

Wide switch mode also sends current transmitter power to the flight controller to display in the OSD. TPwr is only available at the flight controller in this mode.

Ardupilot Modes don't line up very well with the standard -100% (988us) to +100% (2012us) output range in OpenTX when using a 6-position selector as input. Both the first two and the last two positions get binned into Mode 1 and Mode 6 respectively. To get the full 6 Ardupilot modes, go to the Outputs page on the OpenTX model setup and set the min / max for the channels to -75% / +75%.

## Full Resolution Switch Modes :new:

1. 8ch - Channels 1 to 4 and Channels 6 to 9 are sent 10-bit, Full Resolution at the current selected Packet Rate, along with Channel 5 (AUX1) in 1-bit (2-position) for Arming.

2. 16ch Rate/2 - All the Channels are sent 10-bit but at half rate.

3. 12CH Mixed - Channels 1 to 4 are sent 10-bit, Full Resolution with Channel 5 (AUX1) still in 1-bit, at the selected Packet Rate. Channels 6 to 13 are then sent at 10-bit but at half rate.

## FAQ

### Why do you keep saying "*put arm on AUX1*"?

For safety and performance reasons.

**SAFETY**

AUX1 is sent with every packet going out, this is the most reliable way to be able to tell your model to disarm. If your arm switch is in another aux channel, it may be several packets before that switch is transmitted, and there's no guarantee that the RX will actually receive that packet. There's a non-trivial chance your model **may not ever disarm** if the link quality is low and it just so happens that the packet containing the arm switch is getting missed every time. Forcing the arm switch into every packet on AUX1 means that if **any** packet is received by ExpresLRS, it will disarm your model, not just a less than 1-in-7 chance.

It also protects against unintentional disarms caused by a corrupt packet changing the value of the arm switch to disarmed. Betaflight requires that 4x "disarm" commands are received before disarming to guard against this possibility. With arm on AUX1, a single corrupt packet can not disarm your model. With arm on AUX2-8, the one corrupt switch value will be sent 6 times before the value is refreshed, but the flight controller would have already disarmed by that point.

**PERFORMANCE**

Your transmitter and receiver act differently when “armed” and when “disarmed”. When disarmed, the transmitter and receiver are free to adjust their communication in order to make the LUA and other configuration operations more responsive. When "disarmed", everything will appear to be working appropriately but none of the safeguards will be in place and performance will not be what you expect. 

When `IsArmed` is enabled, these safeguards are enabled:

  - Dynamic Power is fully enabled
  - All "Button" inputs are disabled
  - All "Joystick" (5-way buttons) are disabled
  - Bump to Share is disabled
  - VTX Admin is disabled
  - Integrated VTX channel change is disabled
  - Race telemetry mode is enabled
  - Some thermal-based fan controls are enabled

Arming is an important part of the performance of the control link. Please use Channel 5 (Aux 1) as indicated. Also keep in mind that for ExpressLRS, ~1000us is the **disarmed** state and ~2000us is the **armed** state.

### I use a 3-pos switch for arm, this software is unusable

You can still use a 3-position switch to arm! AUX1 just needs to be 2-position, not the physical switch. Simply adjust the mixer in your transmitter so AUX1 works like an on-off switch. If your 3-position arm switch had a second function as well, such as enabling Blackbox, just use one of the other 7 AUX channels to send the switch on a second channel.

### What about "Normal" one bit switch mode?

In 1.0, there was also a switch mode where there were 8x 1-position switches sent in every packet. This mode was removed in 2.0 due to its unpopularity and the flash space was used for other features.

### Every time I change switch mode in Lua, it changes back!

The switch mode can only be changed when a receiver is not connected, to ensure a consistency between the RX and TX's interpretation  of the switch data. Power down your receiver, wait for the "Telemetry Lost" callout, and the switch mode change will stick.
