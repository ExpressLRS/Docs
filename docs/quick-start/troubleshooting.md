---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/quick-start.png)

## General Troubleshooting

### My RX and TX are bound, but FC is not responding to inputs, and I can only see 10 Telemetry sensors

Check whether you have wired the receiver correctly and that Rx and Tx wires aren't swapped.

Also check that you have the correct SerialRX configuration. You might want to revisit the [FC Preparation](../../quick-start/rx-fcprep/) page for the Flight Controller setup.

Also make sure that the UART where you connected the receiver doesn't have inversion and it's in full duplex mode. You can also try a different UART.

### My RX and TX are bound, and I'm getting more than 10 Telemetry sensors on my Radio, but I'm not getting stick inputs

This is due to a [model mismatch](../../software/model-config-match/) between receiver and tx module. The LED on the receiver will have 3 short blinks then a 1s pause indicating the mismatch.

To "fix" this, you might want to turn On Model Matching. Please see [Model Matching](../../software/model-config-match/) for more info.

### My RX and TX are bound, and I'm getting stick inputs, but I can only get 10 Telemetry sensors

Check if you have Telemetry Feature enabled in your FC Configuration.

Also verify the Rx pad from receiver is connected properly to a Tx pad in the FC in the same UART as the Tx wire from receiver.

Also make sure you have deleted and rediscovered the sensors. It's good to increase the TLM Ratio so the acquisition of the sensors will be faster.

### I think my RX and TX are bound as the LED on the Receiver is solid. But I don't have stick inputs or RSSI on radio.

You are not bound. Your Receiver is probably in bootloader mode.

Make sure you have unbridged the boot pads if you did flashed it via passthrough.

Turn off your Radio and if the LED is still solid, but boot pads aren't bridged, the UART where the receiver is on is putting it into bootloader mode unintentionally. Best to move it to another UART. To verify it is the case with the UART, disconnect the Rx and Tx wires from the UART, and it should start blinking slow.

If, however, despite unsoldering the Tx and Rx wires, the LED is still solid, you probably have a soft-bricked receiver due to a failed WiFi flash as a result of not letting the receiver reboot normally. See [this section](../../quick-start/troubleshooting/#i-updated-via-wifi-but-now-receiver-wont-work-and-has-solid-led) for the fix.

### My OSD is showing LQ 0:0 and RSSI dbm at -130 dbm, but I have stick inputs and more than 10 Telemetry sensors

Check whether you have RSSI Channel set to either Aux11 or Aux12. If you do, set it to disabled.

If it's still not fixed with that, check if you have RSSI ADC enabled. If so, set it to disabled.

### My OSD is showing LQ 3:1 sometimes LQ 3:9

Move your LQ OSD element around as it could be being obstructed by another element or it's too far to the right of the preview.

### Betaflight Lua is stuck at Initializing

Increase the TLM Ratio via the ExpressLRS Lua script to values like 1:4 or even 1:2 and retry the Betaflight Lua script.

Also, you have to make sure you're getting more than ten (10) Telemetry sensors prior to launching the script.

See [MSP Section](../../quick-start/pre-1stflight/#msp) for more info.

### My Blackbox Log has stepping on the RC trace

Make sure you have disabled ADC Filter in your Radio Hardware settings.

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

This is a sign that the Wifi flashing didn't go through properly due to premature power cycle. To fix this, you will have to bridge the boot pads (see [here](../../quick-start/rx-fcprep/#happymodel-ep1-ep2-pp)) and reflash using the Passthrough method (**Telemetry** option on Betaflight/iNav set to `OFF`. This is important!) or using an FTDI adapter.

This video shows the steps albeit using vscode development environment but the ExpressLRS Configurator will work just fine. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/SShMaLnqZr8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To ensure that the WiFi flashing finished properly, **wait until the LED on the receiver blinks slow** (indicating it's looking for a TX bind) before pulling off power.