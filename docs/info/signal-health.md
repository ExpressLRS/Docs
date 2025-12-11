---
template: main.html
description: Know what your LQ and RSSI dBm values mean. Prevent a failsafe by knowing when to turn back!
---

![Info Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/information.png)

RSSI has become somewhat a generic term for how good a signal is, and every manufacturer can have their own scale, with most agreeing that "100" is the best, less than that is bad, and expect have RXLOSS at ???. This is an explanation of the signal metrics provided by ExpressLRS and how to understand their values.

## Two Types of Signal Health

There are two main types of signal information available from ExpressLRS: RSSI and LQI

* RSSI - Received Signal Strength Indicator, this value indicates how **loud** 🎺 the reception is. RSSI must be above the sensitivity level to be understood. Units are dBm and start from 0 and go down as the volume gets lower (-130dBm hard limit).
* LQI - Link Quality Indicator, this value indicates how much of the conversation is being understood and ultimately all that matters. Units are percent, with 100% being every packet is received, and 0% means no packets are being received.

Consider you're having a conversation in a quiet room. Your partner speaks loudly enough for you to hear, so the RSSI of their voice is above the sensitivity of your ears. You're going to understand the conversation because you're hearing every word. That's a 100% LQI-- you're receiving 100% of the words. Now imagine someone blows an air horn right in the middle of a sentence. The RSSI is still the same level, you still hear what you could make out at the same volume, you missed a word so the LQI is lower. The closer the volume of the conversation is to the background noise level in the room, the greater the chance is that you'll miss a word due to it getting mixed in with the background noise and lowering your LQI. Remember, LQI is all that matters. Your partner could shout as loud as they want but if you could hear every word anyway, the volume doesn't matter, you always heard every word.

## Which do I care about?

Both really. LQI is most important because you can't fly if you're not getting packets. RSSI is important because it tells you how close you are to the radio receiver not being able to receive packets at all. I'd say if you have just one, pick LQI, because that tells you what percentage of packets are getting through and you get to make the decision if it isn't enough. What you can't tell from LQI alone is when that number is going to drop off a cliff, and it could happen *extremely* fast because you hit the RSSI sensitivity limit.

## RSSI Sensitivity Limit

This is the lowest theoretical RSSI value that can be distinguished by the radio receiver. It is displayed next to the packet rate in the ELRS.lua script, as different packet rates and frequency bands have different sensitivity limits. Lower rates are more sensitive, -123dBm for 25Hz 915MHz up to -105dBm for 500Hz 2400MHz. This gives you the limit you know you can't fly below.

A sensible warning value is 5-10dBm higher than the sensitivity limit shown in the [RF Mode Indexes](#rf-mode-indexes-rfmd) (e.g. 250Hz=-108dBm, so -103dBm to -98dBm for the alarm).

## RSSI Channel

RSSI and LQI are included already in the protocol used to communicate to the flight controller, so the "RSSI Channel" on the Receiver tab should be set to Disabled. RSSI_ADC  / "Analog RSSI input" on the Configuration tab should also be disabled.

## Available RSSI OSD Fields

* **RSSI dBm** - This is the true RSSI value we've talked about here, and is available on Betaflight after 4.1 (?) and iNav after 2.6 (?)
* **Link Quality** - This is LQI discussed here, and has the same version requirements. Betaflight and iNav (LQ TYPE2 option) display add the RF Mode to this as well, e.g. `7:100` means mode 7 = 250Hz and 100% LQI.
* **RSSI Value** - Or sometimes just **RSSI**. This is the old undefined units of Signal Strength value that everyone is used to with no idea what value is good or what value is too bad. What value you'll actually see here varies, even on ExpressLRS, and is covered in the [RSSI Value OSD field](#rssi-value-osd-field) section. It is not recommended to use this field unless you have to (e.g. DJI).

## RSSI Value OSD field

What appears in the RSSI Value field is based on what is selected as the RSSI Channel as ExpressLRS also sends LQI and RSSI as channels (AUX11/ch15 and AUX12/ch16 respectively). It is better to use the dBm or LQ OSD fields instead of this one if you can. DJI users are forced to use this due to it being the only field supported by their OSD. Changes to RSSI Channel in Betaflight requires a reboot to take effect.

* Disabled is set as the "RSSI Channel" field in Betaflight - Displays RSSI dBm scaled as a percentage from -130dBm to 0dBm. Not recommended since what percentage of 130 is the Sensitivity Limit for your selected rate? Math!
* AUX11/ch15 is set as the "RSSI Channel" - Simply LQI although the value might be slightly off due to rounding.
* AUX12/ch16 is set as the "RSSI Channel" - Displays the RSSI dBm scaled as a percentage from the current Sensitivity Limit to -50dBm and is a decent indicator of how much range is left before the LQI cliff (0 here = Sensitivity Limit).

In iNav, the RSSI Value on the OSD is called RSSI (Signal Strength), and will always display 0. To show a filtered (by iNav) LQI in that field, set the rssi_source to protocol using the CLI with `set rssi_source = PROTOCOL`.

## RF Mode Indexes (RFMD)
OSDs report the packet rate using an index instead of the actual rate, either as a `RATE:LQ%` or with rate in the hundreds digit such as `799` where 7 is the RATE and 99 is the LQ%. Handsets display the rate using the RFMD telemetry item.

![OSD RFMD](../assets/images/OSD_RFMD.png)

=== "ExpressLRS 4.x"
| RFMD | Band | Lua | Packet Rate | Sensitivity <br/>Limit |
|--|--|--|--|--|
| 0 | 900 | 25Hz | 25Hz LoRa | -123dBm |
| 1 | 900 | 50Hz | 50Hz LoRa | -120dBm |
| 2 | 900 | 100Hz | 100Hz LoRa | -117dBm |
| 3 | 900 | 100Hz Full | 100Hz 8ch/12ch/16ch LoRa | -112dBm |
| 5 | 900 | 200Hz | 200Hz LoRa | -112dBm |
| 6 | 900 | 200Hz Full | 200Hz 8ch/12ch/16ch LoRa | -111dBm |
| 7 | 900 | 250Hz | 250Hz LoRa | -111dBm |
| 10 | 900 | D50 | 50Hz DVDA LoRa  | -112dBm |
| 11 | 900 | K1000 Full | 1000Hz 8ch/12ch/16ch FSK | -101dBm |
| 21 | 2.4 | 50Hz | 50Hz LoRa | -115dBm |
| 23 | 2.4 | 100Hz Full | 100Hz 8ch/12ch/16ch LoRa | -112dBm |
| 24 | 2.4 | 150Hz | 150Hz LoRa | -112dBm |
| 27 | 2.4 | 250Hz | 250Hz LoRa | -108dBm |
| 28 | 2.4 | 333Hz Full | 333Hz 8ch/12ch/16ch LoRa | -105dBm |
| 29 | 2.4 | 500Hz | 500Hz LoRa | -105dBm |
| 30 | 2.4 | D250 | 250Hz DVDA FLRC | -104dBm |
| 31 | 2.4 | D500 | 500Hz DVDA FLRC | -104dBm |
| 32 | 2.4 | F500 | 500Hz FLRC | -104dBm |
| 33 | 2.4 | F1000 | 1000Hz FLRC | -104dBm |
| 34 | 2.4 | DK250 | 250Hz DVDA FSK | -103dBm |
| 35 | 2.4 | DK500 | 500Hz DVDA FSK | -103dBm |
| 36 | 2.4 | K1000 | 1000Hz FSK | -103dBm |
| 100 | X-Band | 100Hz Full | 100Hz 8ch/12ch/16ch LoRa Dual Band | -112dBm |
| 101 | X-Band | 150Hz | 150Hz LoRa Dual Band | -112dBm |

=== "ExpressLRS 3.x"
| RFMD | Lua | Packet Rate | Sensitivity <br/>Limit | TX Duration <br/>(us) | TX Interval <br/>(us) |
|:---:|:---:|:---:|---:|---:|---:|
| 14 | D50 | 50Hz | -112dBm | 4640.0 | 5000 |
| 13 | F1000 | 1000Hz | -104dBm | 388.8 | 1000 |
| 12 | F500 | 500Hz | -104dBm | 388.8 | 2000 |
| 11 | D500 | 500Hz | -104dBm | 388.8 | 1000 |
| 10 | D250 | 250Hz | -104dBm | 388.8 | 1000 |
| 9 | 500Hz | 500Hz | -105dBm | 1507.4 | 2000 |
| 8 | 333Hz Full | 333Hz | -105dBm | 2374.4 | 3003 |
| 7 | 250Hz | 250Hz | -108dBm | 3330.0 | 4000 |
| 6 | 200Hz | 200Hz | -112dBm | 4640.0 | 5000 |
| 5 | 150Hz | 150Hz | -112dBm | 5891.9 | 6666 |
| 4 | 100Hz Full | 100Hz | -112dBm | 6690.0 (900) /<br />7605.9 (2.4) | 10000 |
| 3 | 100Hz | 100Hz | -117dBm | 9280.0 | 10000 |
| 2 | 50Hz | 50Hz | -120dBm (900) /<br /> -115dBm (2.4) | 19580 (900) /<br /> 10798 (2.4) | 20000 |
| 1 | 25Hz | 25Hz | -123dBm | 30980 | 40000 |

## What about SNR?
SNR stands for Signal to Noise ratio and compares RSSI dBm to the RF background noise level and is in dB units (not dBm), higher is better. Notice it compares the background noise level and not the Sensitivity Limit. The reported value changes quite a bit from packet to packet and what values are good depend on what packet rate is being used. The RF chip can only approximate the noise level and only registers a value so high above the noise floor leading to this value getting clipped. Add to that, LoRa modulation can actually receive data below the noise floor to some degree.

* All FLRC modes (F1000, F500, D500, D250) always report 0 for SNR.
* TBS Crossfire _I believe_ reports `SNR * 4`-- their values can be much higher.

ExpressLRS uses an averaged SNR to control dynamic power, with the following low/high values. The lowest possible SNR a packet can still be received is 5-10dB lower than the "Raise Power" limit.

### Team2.4
| Packet Rate | "Raise Power" (bad) SNR | "Lower Power" (good) SNR |
|--|--|--|
| 500Hz | 5.0dB | 9.5dB |
| 333Hz Full | 5.0dB | 9.5dB |
| 250Hz | 3.0dB | 8.5dB |
| 150Hz | 0.0dB | 8.5dB |
| 100Hz Full | 0.0dB | 8.5dB |
| 50Hz | -1.0dB | 6.5dB |

### Team900
| Packet Rate | "Raise Power" (bad) SNR | "Lower Power" (good) SNR |
|--|--|--|
| 200Hz | 1.0dB | 3.0dB |
| 100Hz Full | 1.0dB | 3.0dB |
| 100Hz | 1.0dB | 2.5dB |
| 50Hz | 1.0dB | 1.5dB |
| D50 | 1.0dB | 3.0dB |
| 25Hz | -3.0dB | 0.5dB |

## How far can I go on X mW?

Very far? This question is usually used in place of the actual question "Will I get good signal where I fly?" which is impossible to answer.

ExpressLRS 2.4GHz can go over 40km at 250Hz 100mW on omnidirectional antennas with excellent LQI, or it can go 400m with less stellar LQI. By far the biggest factor in determining maximum range is direct line of sight. Blocking line of sight reduces RSSI dBm. A few trees or a building isn't going to keep you from flying due to ExpressLRS's excellent sensitivity even when line of sight isn't available, but range is reduced a bit for every physical object between you and the receiver. Piloting from an elevated position can eliminate some ground obstacles and provide a measurable boost in range.

The second largest factor is interference. Interference is the clobbering of our packets by outside sources, such as WiFi on 2.4GHz or other ISM transmissions on 868/915MHz, and is seen as a drop in LQI well before the sensitivity limit. Increasing TX power output is usually not the solution you'd expect, where each doubling in output power only might only add 10% to the usable range due to interference.

## #Team868/#Team915 or #Team2.4

Unfortunately, there is a misconception about the 2.4GHz range thanks to other radio protocols on the market. ExpressLRS uses LoRa, which has had some amazing results on 2.4GHz. Again, 40km on 100mW 250Hz on 2.4GHz. The advantages of 2.4GHz is that the antennas are 2.5x smaller than 915MHz antennas, and there's more spectrum for ExpressLRS to hop around in, opening up the air for more pilots at once. 868/915MHz does have increased penetration and is the ultimate king of long range flying, but penetration difference may not be as great as you think. The high sensitivity of ExpressLRS receivers allows them to fly places you wouldn't dream of flying FSK-based 2.4 receivers such as FrSky ACCST/ACCESS, FlySky AFHDS2A, Spektrum DMX, or Redpine.

## RF noise

We have all heard the stories of racers powering up his TBS crossfire full module at 2W and causing people to fail-safe during a race. This happens because the 868/915MHz band has limited bandwidth. The solution for this is to use a low power mode during races, so you do not blast anyone out of the sky. 2.4GHz does not have this issue. Flite Test has a world record of having [179 RC airplanes](https://www.guinnessworldrecords.com/world-records/most-rc-model-aircraft-airborne-simultaneously#:~:text=The%20most%20RC%20model%20aircraft,USA%2C%20on%2016%20July%202016) in the sky using 2.4 GHz.

2.4GHz LoRa can also handle WiFi noise very well. [Studies](https://link.springer.com/article/10.1007/s11235-020-00658-w) have been conducted with the coexistence of WiFi and LoRa bands.

868/915 does not have to worry about WiFi signal but it does have to worry about cell towers and other RF noise. You are fighting against thermostats, fire systems, burglar systems and any other device running on that band.
