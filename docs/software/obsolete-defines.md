---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

This page contains old user_defines.txt that have been removed or superseded by new defines.

New items should be added to the top of the list so the last entry here is the oldest. The order of each entry should be [code]definename[/code] followed by the original text of the documentation, ending with a separate paragraph "**REMOVED** [version] [replacement or reason for removal]".

## Obsolete Defines

```
USE_ESP8266_BACKPACK
```
This enables communication with the **[ESP Backpack](../hardware/backpack/esp-backpack.md)** for over-the-air updates (`env:FrSky_TX_R9M_via_WiFi`) 🖥️ and debugging via WebSocket 🔍. Uncommented by default, does not need to be changed.

**REMOVED** 2.0 development. Replaced with USE_TX_BACKPACK.

```
#-DHYBRID_SWITCHES_8
```
Changes how the AUX channels are sent over the air. The default option is Normal Mode with 8x 2-position low-latency switches. Enabling `HYBRID_SWITCHES_8` changes this to 1x 2-pos + 6x 7-pos + 1x 16-pos, with only the 2-position being low-latency. In Normal Mode, all switches are sent with every packet, in Hybrid Mode, only AUX1 is sent with every packet and the rest are rotated through. Note: The switch mode MUST match between the RX and TX. A detailed explanation of the differences between the two options can be found in [Switch Modes](switch-config.md), but
  1. If only two position switches are needed, and they must be updated as fast as possible: Normal Mode
  2. Almost everyone: Hybrid Mode (Put ARM on AUX1)

**REMOVED** 2.0 development, all switch modes are available via Lua configuration. HYBRID_SWITCHES_8 is always enabled / available.

```
#-DENABLE_TELEMETRY
```
Enable advanced telemetry support. This option must be enabled on both **TX** and **RX**. The following telemetry messages are supported:

* GPS
* BATTERY_SENSOR
* ATTITUDE
* DEVICE_INFO
* FLIGHT_MODE
* MSP_RESP

**Note 1**: Increase the telemetry rate with the
ExpressLRS lua script. Increase the rate until the sensor lost
warnings go away. It is normal to set it up to 1:16 with 200 Hz
refresh rate.

**Note 2**: It must be enabled together with **HYBRID_SWITCHES_8**.

**REMOVED** 2.0 development, ENABLE_TELEMETRY is always enabled. Advanced Telemetry will only be sent if telemetry messages are received from the FC.

```
-DUSE_500HZ
```
This enables 500Hz mode for 2.4 GHz RXes and TXes. The drawback is that you have to give up 25Hz mode to add 500Hz mode. It requires [OpenTX 2.3.12 or Newer](https://www.open-tx.org/2021/06/14/opentx-2.3.12), [EdgeTX](https://github.com/EdgeTX/edgetx) or a Radio firmware that has CRSFShot or Mixer Sync. 

**REMOVED** 1.0.0-RC9, this option is now always enabled and in turn, 25Hz has been dropped/removed.

```
-DUSE_UART2
```
This enables integration with Jye's **[FENIX rx5805 pro-diversity module](https://github.com/JyeSmith/FENIX-rx5808-pro-diversity)**

**REMOVED** Somewhere in the 1.0.0-RC cycle. Feature removed.

```
-DFAST_SYNC
```
Option that adds faster initial syncing, by changing how long the receiver waits for a connection in each mode while not connected. This option is now the default, but disabling it can help syncing at lower packet rates (50Hz and below).

**REMOVED** 1.0.0-RC2 initial sync replaced with a full FHSS period wait

````
#-DR9M_UNLOCK_HIGHER_POWER 
````
**REMOVED** 1.0.0-RC1 replaced with generic `-DUNLOCK_HIGHER_POWER`

```
#-DARM_CHANNEL=AUX1
```
If you are using a different channel than the default you **need** to edit 🔥 (or you may not be able to gain sync safely - default is listed in `#DARM_CHANNEL` as AUX1 which is Channel 5).

NB This feature assumes that a low value of the arm switch is disarmed, and a high value is armed. If you have the arm switch reversed it will not work correctly and the link won't be established. For this reason it may be best not to enable no sync on arm when you are first setting up ExpressLRS as it can be a source of confusion.

**REMOVED** 1.0.0-RC1 AUX1 is **always** the arm switch now, no longer configurable

```
#-DLOCK_ON_50HZ
```
`LOCK_ON_50HZ` locks the RX at `50Hz` mode from the powerup. (Only recommended for longrange, and partly redundant with previous feature.) Merged in [Pull 143](https://github.com/AlessandroAU/ExpressLRS/pull/143)

**REMOVED** 1.0.0-RC1 not sure why this was removed

```
-DAUTO_WIFI_ON_BOOT
```
**REMOVED** 1.0.0-RC1 replaced with `-DAUTO_WIFI_ON_INTERVAL=X`
