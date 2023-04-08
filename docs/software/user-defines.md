---
template: main.html
description: User Defines are firmware flags akin to the Firmware Options. You can use these defines with the Manual Mode in the ExpressLRS Configurator.
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

With more features being added consistently, [`./src/user_defines.txt`](https://github.com/AlessandroAU/ExpressLRS/blob/master/src/user_defines.txt) has gotten complicated 🤷‍♂️. So we will break it down! 🔨 

!!! info

    This is the full list of currently supported User Defines and would help you should you intend to compile the firmware using the [Toolchain](toolchain-install.md) or manual mode on the ExpressLRS Configurator.

## Defines 101

- If these are used in Configurator Manual Mode or user_defines.txt, the value must begin with `-D`. Example: `NO_SYNC_ON_ARM` would be `-DNO_SYNC_ON_ARM`.
- A user definition that begins with `#` is "commented out", i.e. not active.

## Binding Phrase

```
MY_BINDING_PHRASE="default ExpressLRS binding phrase"
```
!!! Important
    This step is simple but **important**. Both the TX and RX NEED to have the same binding phrase or **ExpressLRS WILL NOT WORK**. Anyone using the same binding phrase as you will be able to control your model, so be unique. Set something memorable, and limit to alphanumeric phrases conforming to the Latin alphabet<sup>*</sup>. 

Receivers flashed with firmware builds that do not have binding phrases enabled will support and require the traditional binding method. 📜 For ESP/ESP32 hardware, this value can also be changed through the WebUI.

This feature can, but should not be used as a model match feature (to lock a single specific transmitter to a single specific receiver). For that use, the [Model Match option](model-config-match.md#model-match).

<small><sup>*</sup> This phrase gets md5 hashed and gets built into the binary you will be flashing.</small>

## Regulatory Domain

```
Regulatory_Domain_AU_915
Regulatory_Domain_EU_868
Regulatory_Domain_AU_433
Regulatory_Domain_EU_433
Regulatory_Domain_FCC_915
Regulatory_Domain_ISM_2400
```
This is a relatively simple one - enable whatever regulatory domain you are in. `EU 868` 🇪🇺  is compliant to the frequency but **is not** LBT compliant 👂 . Every other band is near compliant 👿  but may not be fully compliant for your regulatory domain. 

```
TLM_REPORT_INTERVAL_MS=240LU
```
The TX module sends the LinkStats telemetry to the OpenTX frequently to let the handset know the connection is still active and reduce "Telemetry Lost" warnings. Reducing this value may reduce warnings caused by handset errors at higher baud rates. This only affects the connection from the TX module to the handset and does not do anything with the telemetry connection from the receiver. The default value is **240LU**. When changing this value, suffix your milliseconds value with **LU**. For example, to specify a 100ms LinkStats update rate, you have to enter it like this: **100LU**.

## Output Power Limit

````
UNLOCK_HIGHER_POWER 
````
By default the max power of the hardware is limited to what it can safely output without extra cooling. Some hardware supports increasing the power by enabling the following option. Check the [supported hardware](../hardware/hardware-selection.md) page to see if this is available and what cooling modifications can be made. By enabling this, you are risking permanent damage to your hardware, sometimes even when you add extra cooling. For example, R9M modules will burn out without cooling.

## Performance Options

```
LOCK_ON_FIRST_CONNECTION
```
RF Mode Locking - When the RX is waiting for a connection, it cycles through all available rates waiting for a connection on each one. By default, ExpressLRS will go back to this mode after a disconnect (failsafe). If `LOCK_ON_FIRST_CONNECTION` is used, ELRS will not cycle after a disconnect, but instead, just stay at whatever rate the last connection was. This makes connection re-establishment quick, because the RX is always listening at the proper rate. This is generally what everyone wants, but there is utility in being able to switch the TX to the lowest rate to get more range to re-establish a link with a downed model, which can't happen if the RX is locked at the previous rate.

When cycling through the rates, the RX starts with the fastest packet rate and works down to the slowest, then repeats. It waits `PACKET_INTERVAL * PACKS_PER_HOP * HOP_COUNT * 1.1` at each rate. Example: 4ms * 4 * 80 * 1.1 = 1.408s for 250Hz. The duration is extended 10x if a valid packet is received during that time. Even with `LOCK_ON_FIRST_CONNECTION`, the rate can be changed by changing the TX rate using ELRS.lua while connected, or by power cycling the RX.

```
FAN_MIN_RUNTIME=30
```
For TX devices with fans, FAN_MIN_RUNTIME keeps the fan running even after the power level has dropped below the configured Fan Threshold. This prevents the fan from turning on and off every few seconds if the power level is constantly changing. The default is 30 seconds if not defined, the value can be 0-254. There is always a short delay before the fan is activated, which can not be disabled. 

## Compatibility Options

```
UART_INVERTED
```
This **only works** with `ESP32` based TXes (will not work with modules without built-in inversion/uninversion), but enables compatibility with radios that output inverted CRSF, such as the FrSky QX7, TBS Tango 2, RadioMaster TX16S. You want to keep this enabled in most cases. If your radio is T8SG V2 or you use Deviation firmware turn this setting off.

```
RCVR_INVERT_TX
```
This **only works** with `ESP8266/ESP8285` based RXes. Invert the TX pin in the receiver code to allow an inverted RX pin on the flight controller to be used (usually labeled SBUS input or RXI). Inverted CRSF output. RX pin (telemetry) is unaffected. Update via_BetaflightPassthrough will not work, only via_Wifi. Note that just because this description includes the word SBUS, it doesn't mean the RX will output SBUS. It is still a CRSF protocol, only inverted, so CRSF should still be the receiver protocol selected in the flight controller software.

```
RCVR_UART_BAUD=420000
```
Use a custom baud rate on the receiver instead of the default 420000 baud. This is useful for a KISS v1 FC (which runs at 400000) or any other oddball baud, like 115200 for interfacing with an Arduino.

```
USE_R9MM_R9MINI_SBUS
```
**This does not turn on SBUS protocol** it simply changes the pin used for communication from those two side pins (A9 and A10) to use the pin labeled "SBUS" on the RX, which is inverted. This is useful for `F4 FCs` which only have an inverted receiver input UART RX. 🔼. This is only one way, so you lose the telemetry downlink to your radio as well as passthrough flashing. Enabling this turns on CRSF protocol output on the `S.BUS` 🚌 pin on your `R9MM/R9Mini`. `set serialrx_inverted = ON` may also be needed within Betaflight 🐝 for compatibility

## Network Options

```
AUTO_WIFI_ON_INTERVAL=30
```
⚠️ Must be defined if you plan to update your RX over wifi without using a button on the RX ⚠️ This will automatically turn the wifi 📶 on for **any module** that has an `ESP8285` on it if no TX connection is established after N seconds from boot (the 30 is the time). This enables pushing firmware updates to the RX by connecting to its wifi network and visiting `http://10.0.0.1`.

```
HOME_WIFI_SSID
HOME_WIFI_PASSWORD
```

These options set Home Network Access for your Wifi-enabled hardware. With these sets, the devices will try connecting to your existing WiFi Network when you click on "(Wifi) Update" on the ExpressLRS Lua script (for some Tx Modules) or automatically after your set interval time. Once the devices connect to your Home WiFi, the Update page can be accessed anywhere, from any device on the same network. The Tx Module Wifi update page can be reached using the address http://elrs_tx.local, while the receivers' update page can be reached via http://elrs_rx.local.

Wifi mode will first try to connect to the network specified before falling back and creating a new wifi network. The Home Network can also be modified from the website.

## Other Options

```
JUST_BEEP_ONCE
MY_STARTUP_MELODY="<music string>|<bpm>|<semitone offset>" -or-
MY_STARTUP_MELODY="<rtttl string>"
```
For TXes like the R9M, this sets if the TX only beeps one-time **versus** playing a startup song. Currently, it is set to play the startup song 🎼 , but if you don't prefer it, uncomment this to turn it off. ✖️
 
For all your customization needs, use `DMY_STARTUP_MELODY` to define your own startup melody using the BlHeli32 or RTTTL syntax. For BLHeli32, the parameters `music string` and `bpm` are required, whereas `semitone offset` is optional to transpose the entire melody up or down by the defined amount of semitones.

For example, BlHeli32 melodies are available on [Rox Wolf's youtube channel](https://www.youtube.com/playlist?list=PL_O0XT_1mZinetucKyuBUvkju8P7DEg-v), some experimentation may be required though. :musical_note: To write your own melody, **[this (Sheet Music 101)](https://github.com/nseidle/AxelF_DoorBell/wiki/How-to-convert-sheet-music-into-an-Arduino-Sketch)** and **[this (BLHeli Piano)](https://dra6n.github.io/blhelikeyboard.github.io/)** are useful resources.

The build process also supports RTTTL-formatted ringtone strings. RTTTL melodies are delimited by colons `:` and start with a description versus the BLHeli style with pipes `|`. e.g. `Mario:d=4,o=5,b=100:32p,16e6,16e6,16p,16e6,16p,16c6,16e6,16p,16g6,8p,16p,16g`

```
DISABLE_STARTUP_BEEP
```
Disables beep sequence at startup of TX, but the TX will still beep when the CRSF connection is acquired

```
DISABLE_ALL_BEEPS
```
Disables all TX buzzer beeps at any state

```
USE_TX_BACKPACK
```
Enables code for talking to a connected [ESP8266 backpack](https://github.com/ExpressLRS/Backpack) on the TX module, and associated Lua params. The device target should enable this automatically for devices that come with this built-in, but can be added to any device. The TX backpack allows wireless integration with VRx modules and planned telemetry mirroring over wifi.

## Debug Options

```
DEBUG_LOG
```
Turn on debug messages, sent to the TX Backpack UART if available or else right out the main CRSF UART (such as on the receiver).

```
DEBUG_LOG_VERBOSE
```
Use to see verbose debug logging (spammy stuff)

```
DEBUG_RX_SCOREBOARD
```
Print a letter for each packet received or missed (receiver debugging)

```
DEBUG_CRSF_NO_OUTPUT
```
Don't send CRSF messages over the CRSF UART (receiver only). Used to only see logging and not logging mixed with CRSF.

```
DEBUG_RCVR_LINKSTATS
```
Prints a log line for every channels packet received at the RX `ID,Antenna,RSSI,LQ,SNR,PWR,FHSS,TimingOffset`. The ID is generated on the TX side and overwrites CH1-CH4 and increments once for every channel packet. Writes directly to Serial, and does not require DEBUG_LOG. Flash both TX & RX with this enabled to use it if the ID is required.

```
DEBUG_FREQ_CORRECTION
```
Enable reporting of RF FreqCorrection in RX's SNR LinkStatistics, also decreases packet rate on Team2.4 for the additional time needed to include the packet header / enable FreqCorrection. The current FreqCorrection value will be reported in RSNR in the LinkStats scaled -127 to +127, where 127 is the maximum allowable deviation. 200kHz for Team2.4, 100kHz for Team900. Dynamic power must be OFF, or else it will adjust based on the FreqCorrection reported in SNR. **Both the TX and RX must have this definition enabled otherwise they will not bind.**

## Obsolete user_defines

See [Obsolete user_defines](obsolete-defines.md)
