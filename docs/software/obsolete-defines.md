---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

This page contains old user_defines.txt that have been removed or superseded by new defines.

New items should be added to the top of the list so the last entry here is the oldest. The order of each entry should be [code]definename[/code] followed by the original text of the documentation, ending with a separate paragraph "**REMOVED** [version] [replacement or reason for removal]".

## Obsolete Defines
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

