---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

# User Defines Explained
With more features being added consistently, [`./src/user_defines.txt`](https://github.com/AlessandroAU/ExpressLRS/blob/master/src/user_defines.txt) has gotten complicated 🤷‍♂️. So we will break it down! 🔨 

*Note: This is the full list of currently supported User Defines and would help you should you intend to compile the firmware using the [Toolchain](../../software/toolchain-install/) or Manual Mode on the ExpressLRS Configurator.

## Defines 101
- To enable/disable anything in the user defines, simply add or remove a `#` in front of anything that has a `-D`.
- We recommend reading this page **in its entirety** before first flashing ⚡ to have a better sense of the options.

## Binding Phrase
```
-DMY_BINDING_PHRASE="default ExpressLRS binding phrase"
```
This step is simple but **important**. Both the TX and RX NEED to have the same binding phrase or **ExpressLRS WILL NOT WORK**. Anyone using the same binding phrase as you will be able to control your model, so be unique. Set something memorable, and limit to alphanumeric phrases conforming to the Latin alphabet<sup>*</sup>. Receivers flashed with firmware builds that do not have binding phrase enabled will support and require the traditional binding method. 📜 

<small><sup>*</sup> This phrase gets md5 hashed and gets built into the binary you will be flashing.</small>

## Regulatory Domain
```
#-DRegulatory_Domain_AU_915
#-DRegulatory_Domain_EU_868
#-DRegulatory_Domain_AU_433
#-DRegulatory_Domain_EU_433
#-DRegulatory_Domain_FCC_915
#-DRegulatory_Domain_ISM_2400
```
This is a relatively simple one - enable whatever regulatory domain you are in. `EU 868` 🇪🇺  is compliant to the frequency but **is not** LBT compliant 👂 . Every other band is near compliant 👿  but may not be fully compliant for your regulatory domain. 

```
#-DTLM_REPORT_INTERVAL_MS=320LU
```
It makes the TX module send the telemetry data to the OpenTX every 320 ms by default. This stops the telemetry lost warnings when running a high telemetry ratio, or low rates like 50hz.
     
Default value is **320LU**. If you want to change that you have to suffix your milliseconds value with **LU**. For example, in order to specify 100 ms telemetry update rate you have to enter it like this: **100LU**.

Typically, you want to keep **320LU** value for OpenTX based radios, and **100LU** for ErskyTx ones.

## Output Power Limit
There has been some reports of the R9M modules showing instability at >250mw with stock cooling. This in part because the ELRS uses a higher duty cycle for transmission compared to stock firmware. By default the power of any TX is limited to 250mw but you can unlock up to 1000mw (for hardware that supports it) by enabling the following option. Do this at your own risk if you make no cooling modifications-- R9M modules will burn themselves out without cooling.

````
#-DUNLOCK_HIGHER_POWER 
````
We published [R9M Fan Mod Cover](../../hardware/fan-mod/), a custom 3d printed backplate with room for a fan and extra cooling to allow for maximum power (1-2W depending on the mod).
 
<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/STL/R9M-Fan-Mod-Case/view-top.png" data-canonical-src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/STL/R9M-Fan-Mod-Case/view-top.png" width="20%" height="auto" /><img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/STL/R9M-Fan-Mod-Case/view-bottom.png" data-canonical-src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/STL/R9M-Fan-Mod-Case/view-bottompng" width="20%" height="auto" />

## Performance Options
```
#-DNO_SYNC_ON_ARM
```
**no sync on arm** doesn't transmit sync packets while armed. This is useful for racing as there is less time & packets wasted 🗑️ on sending sync packets. **HOWEVER** if you are doing serious long range ⛰️, keep this commented because in the case of a sustained failsafe, link can not be regained while armed.

AUX1 is the channel ExpressLRS uses to detect "ARMED", and this feature assumes that a **low value of the arm switch is disarmed, and a high value is armed**. OpenTX can invert your switch if you prefer it to be mechanically inverted. It may be best not to enable no sync on arm when you are first setting up ExpressLRS as it can be a source of confusion.
 
```
-DFEATURE_OPENTX_SYNC
#-DFEATURE_OPENTX_SYNC_AUTOTUNE
```
These features enable **lower latency** 🏃‍♂️ and **offset** from the OpenTX radio to the TX. The first lowers latency and should be kept enabled. The second is more experimental and can lower the offset from the radio by tuning it as close as possible to `0`, but is experimental (even in 1.0) and is best left disabled. 

Both require [OpenTX `2.3.12`](https://www.open-tx.org/) or above. In order to install it, you will have to use OpenTX companion application. 

You can also use [EdgeTX](https://github.com/EdgeTX/edgetx).

```
-DLOCK_ON_FIRST_CONNECTION
```
RF Mode Locking - When the RX is waiting for a connection, it cycles through all available rates waiting for a connection on each one. By default, ExpressLRS will go back to this mode after a disconnect (failsafe). If `LOCK_ON_FIRST_CONNECTION` is used, ELRS will not cycle after a disconnect, but instead just stay on whatever rate the last connection was. This makes connection re-establishment quick, because the RX is always listening at the proper rate. This is generally what everyone wants, but there is utility in being able to switch the TX to the lowest rate to get more range to re-establish a link with a downed model, which can't happen if the RX is locked at the previous rate.

When cycling through the rates, the RX starts with the fastest packet rate and works down to the slowest, then repeats. It waits `PACKET_INTERVAL * PACKS_PER_HOP * HOP_COUNT * 1.1` at each rate. Example: 4ms * 4 * 80 * 1.1 = 1.408s for 250Hz. The duration is extended 10x if a valid packet is received during that time. Even with `LOCK_ON_FIRST_CONNECTION`, the rate can be changed by changing the TX rate using ELRS.lua while connected, or by power cycling the RX.

```
#-DUSE_DIVERSITY
```
Enable antenna-switching diversity for RX that support it.

## Compatability Options
```
-DUART_INVERTED
```
This **only works** with `ESP32` based TXes (will not work with modules without built-in inversion/uninversion), but enables compatibility with radios that output inverted CRSF, such as the FrSky QX7, TBS Tango 2, RadioMaster TX16S. You want to keep this enabled in most of the cases. If your radio is T8SG V2 or you use Deviation firmware turn this setting off.
```
-DUSE_UART2
```
This enables integration with Jye's **[FENIX rx5805 pro-diversity module](https://github.com/JyeSmith/FENIX-rx5808-pro-diversity)** 👷 

```
#-DUSE_R9MM_R9MINI_SBUS
```
**This does not turn on SBUS protocol** it simply changes the pin used for communication from those two side pins (A9 and A10) to use the pin labeled "SBUS" on the RX, which is inverted. This is useful for `F4 FCs` which only have an inverted receiver input UART RX. 🔼. This is only one way, so you lose the telemetry downlink to your radio as well as passthrough flashing. Enabling this turns on CRSF protocol output on the `S.BUS` 🚌 pin on your `R9MM/R9Mini`. `set serialrx_inverted = ON` may also be needed within Betaflight 🐝 for compatibility

## Other Options

```
-DAUTO_WIFI_ON_INTERVAL=30
```
⚠️ Must be defined if you plan to update your RX over wifi without using a button on the RX ⚠️ This will automatically turn the wifi 📶 on for **any module** that has an `ESP8285` on it if no TX connection is established after N seconds from boot (the 30 is the time). This enables pushing firmware updates to the RX by connecting to its wifi network and visiting `http://10.0.0.1`.

```
#-DJUST_BEEP_ONCE
#-DMY_STARTUP_MELODY="<music string>|<bpm>|<semitone offset>" -or-
#-DMY_STARTUP_MELODY="<rtttl string>"
```
For TXes like the R9M, this sets if the TX only beeps one-time **versus** playing a startup song. Currently, it is set to play the startup song 🎼 , but if you don't prefer it, uncomment this to turn it off. ✖️
 
For all your customization needs, use `DMY_STARTUP_MELODY` to define your own startup melody using the BlHeli32 or RTTTL syntax. For BLHeli32, the parameters `music string` and `bpm` are required, whereas `semitone offset` is optional to transpose the entire melody up or down by the defined amount of semitones.

Example BlHeli32 melodies are available on [Rox Wolfs youtube channel](https://www.youtube.com/playlist?list=PL_O0XT_1mZinetucKyuBUvkju8P7DEg-v), some experimentation may be required though. :musical_note: To write your own melody, **[this (Sheet Music 101)](https://github.com/nseidle/AxelF_DoorBell/wiki/How-to-convert-sheet-music-into-an-Arduino-Sketch)** and **[this (BLHeli Piano)](https://dra6n.github.io/blhelikeyboard.github.io/)** are useful resources.

The build process also supports RTTTL-formatted ringtone strings. RTTTL melodies are delimited by colons `:` and start with a description versus the BLHeli style with have pipes `|`. e.g. `Mario:d=4,o=5,b=100:32p,16e6,16e6,16p,16e6,16p,16c6,16e6,16p,16g6,8p,16p,16g`

```
-DUSE_ESP8266_BACKPACK
```
This enables communication with the **[ESP Backpack](../../hardware/esp-backpack)** for over-the-air updates (`env:FrSky_TX_R9M_via_WiFi`) 🖥️ and debugging via WebSocket 🔍. Uncommented by default, does not need to be changed.

## Obsolete user_defines

See [Obsolete user_defines](../../software/obsolete-defines)
