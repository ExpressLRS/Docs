---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/quick-start.png)

## General Troubleshooting

### My RX and TX are bound, but Betaflight is not responding to inputs

You most likely updated your receiver via WiFi, but you have wired your receiver wrong or that you have an incorrect receiver configuration. You might want to revisit the [FC Preparation](../../quick-start/rx-fcprep/) page for the Flight Controller setup.

Also make sure that the UART where you connected the receiver to doesn't have inversion and it's in full duplex mode. You can also try a different UART.

## Flashing/Updating

### Invalid serial RX configuration detected

This is often caused by incorrect Serial RX protocol (should be CRSF), or serialrx_inverted = on (should be off) or serialrx_halfduplex=on (should be off). The Passthrough Init section of the log will show you which setting should be corrected. See this [page](../../quick-start/rx-fcprep/) for setting up your Flight Controller.

### RX Serial not found !!!!

Make sure your Serial RX on the Ports Tab of your FC Firmware configurator is set to the correct UART.

### No CLI Available

This message can be seen on the ExpressLRS Configurator Log while using the Passthrough method and can be caused by a busy Com Port. Make sure any other Configurator Apps were closed and unplug-replug your FC to USB. You might also want to use a different USB port or cable.

This could also mean that the FC cannot be detected by the script. This could also due to the FC being in DFU mode, which for passthrough flashing, is not needed.

### 10 Retries but no Success

This can be due to several things:

- Incorrect bootloader is flashed or it's not flashed properly. This mainly happen on the R9 receivers. Go checkout [Bootloader Flashing Guide](../../quick-start/rx-bootloader/).
- Incorrect wiring. Make sure that Rx in the Receiver is connected to a Tx pad in the FC and the Tx in the Receiver is connected to an Rx pad in the FC. Also make sure receiver is getting enough voltage (min 4v5) from the FC or voltage supply. Wiring guide is [here](../../quick-start/rx-fcprep/)
- Receiver is OFF. Check whether the LED on the receiver is lit, indicating it's powered and in working state.
- The UART has hardware inversion. Make sure that the UART you've connected the receiver to is not an SBUS UART that's usually have hardware inversion (most common among F4 Flight Controllers). There are Flight controllers that require you bridge a pair of pads to enable or disable the Hardware inversion of an Rx pad. You can simply try a different UART.
- The LED on the receiver is SOLID, while radio is off, could only mean that the Rx pad in the FC is being pulled LOW, putting the ESP-based receiver (EPs, ES900Rx, etc.) into Bootloader mode unintentionally, which will hinder normal passthrough operations. Feel free to try a different UART.

### I updated via WiFi but now receiver won't work and has SOLID LED

This is a sign that the Wifi flashing didn't go through properly due to premature power cycle. To fix this, you will have to bridge the boot pads (see [here](../../quick-start/rx-fcprep/#happymodel-ep1-ep2-pp)) and reflash using the Passthrough method or using an FTDI adapter.

This video shows the steps albeit using vscode development environment but the ExpressLRS Configurator will work just fine. You might also want to disable Telemetry in Betaflight/emuflight/iNav before attempting recovery.

<iframe width="560" height="315" src="https://www.youtube.com/embed/SShMaLnqZr8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To ensure that the WiFi flashing finished properly, wait until the LED on the receiver blinks slow (indicating it's looking for a TX bind) before pulling off power.