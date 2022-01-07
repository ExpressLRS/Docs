---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/quick-start.png)

## General Troubleshooting

### My RX and TX are bound, but FC is not responding to inputs, and I can only see 10 Telemetry sensors

Check whether you have wired the receiver correctly and that Rx and Tx wires aren't swapped.

Also check that you have the correct SerialRX configuration. You might want to revisit the [FC Preparation](receivers/rx-fcprep.md) page for the Flight Controller setup.

Also make sure that the UART where you connected the receiver doesn't have inversion and it's in full duplex mode. You can also try a different UART.

### My RX and TX are bound, and I'm getting more than 10 Telemetry sensors on my Radio, but I'm not getting stick inputs

This is due to a [model mismatch](../software/model-config-match.md) between receiver and tx module. The LED on the receiver will have 3 short blinks then a 1s pause indicating the mismatch.

To "fix" this, you might want to turn On Model Matching. Please see [Model Matching](../software/model-config-match.md) for more info.

Another thing to check is whether you have enabled **RCVR_INVERT_TX** option for your receiver firmware. This option is intended for FCs that doesn't have any other UARTs available (AIOs) other than an SBUS pad. See this section for more details: [Output Inverting](firmware-options.md#output-inverting).

For the R9mm/mini receivers, make sure you didn't enable **USE_R9MM_R9MINI_SBUS** in your firmware option. See [Output Inverting](firmware-options.md#output-inverting) for what this option do.

### My RX and TX are bound, and I'm getting stick inputs, but I can only get 10 Telemetry sensors

Check if you have Telemetry Feature enabled in your FC Configuration.

Also verify the Rx pad from receiver is connected properly to a Tx pad in the FC in the same UART as the Tx wire from receiver.

Also make sure you have deleted and rediscovered the sensors. It's good to increase the TLM Ratio so the acquisition of the sensors will be faster.

This could also mean you'll have to update your FC Firmware to a more recent version that supports at least CRSFv2 protocol.

### I think my Reciever and Transmitter are bound as the LED on the Receiver is solid. But I don't have stick inputs or RSSI on radio.

You are not bound. Your Receiver is probably in bootloader mode.

* Make sure you have unbridged the boot pads if you flashed it via passthrough.

* Turn off your Radio and if the LED is still solid, but boot pads aren't bridged, the UART where the receiver is on is putting it into bootloader mode unintentionally. This is primarily caused by pull-down resistor on the RX pad to aid with SBUS line inversion. To verify it is the case with the UART, disconnect the Rx and Tx wires from the FC UART, and it should start blinking slow then after the set interval (20s - 30s by default), it will blink fast indicating it's on WiFi Mode. To "fix" the issue, you have two options:

    - Move the receiver into another free UART.
    - If there's no other UART, wire up a resistor with a value between 300 Ohm to 1k Ohm between a 3.3v pad and the FC's RX pad (where the TX from the receiver connects to).

* If, however, despite unsoldering the Tx and Rx wires, the LED is still solid, you probably have a soft-bricked receiver due to a failed WiFi flash as a result of not letting the receiver reboot normally. See [this section](#i-updated-via-wifi-but-now-receiver-wont-work-and-has-solid-led) for the fix.

### My OSD is showing LQ 0:0 and RSSI dbm at -130 dbm, but I have stick inputs and more than 10 Telemetry sensors

Check whether you have RSSI Channel set to either Aux11 or Aux12. If you do, set it to disabled.

If it's still not fixed with that, check if you have RSSI ADC enabled. If so, set it to disabled.

### My OSD is showing LQ 3:1 sometimes LQ 3:9

Move your LQ OSD element around as it could be being obstructed by another element or it's too far to the right of the preview.

### I am getting Telemetry Lost/Recovered and is getting annoying

There's a handful of reasons why this is occuring, and if you have newer handset/radio, it shouldn't happen at all unless you're flying very far away using a receiver without an amplifier on its Telemetry signal (e.g. the EP receivers).

- You're on an X9D(+) or a QX7 with subpar inverter chips. Check [this page](../hardware/x9d-troubleshooting.md) on how to remedy it.
- You're on an early version of the Happymodel Slim Pro. Check [this FB post](https://www.facebook.com/groups/636441730280366/permalink/835603713697499/) for the fix from manufacturer.
- You're using a 2018 ACCST R9M, while also using a Radio with 400k or higher Baud rate. You will either have to lower the Baud rate on your radio to 115200 (QX7) or do the Resistor mod on the module as described [here](../hardware/inverter-mod.md).
- Your module is getting loose inside its enclosure, most common on the first batches of the Happymodel ES24TX (white 3D-Printed enclosure; although the black one is only marginally better having 4 screw points instead of 2). You either have to print your own enclosure (search Thingiverse for "expresslrs") or find a way to tighten or snug the enclosure with the module board.
- Check the S.Port pin and connection in your module and module bay, and make sure they have a solid physical connection. On the DIY modules, particularly the full size module, the round hole/via for the Molex connector's flat pin might not be getting good connection due to cold solder joint, or insufficient solder.

### I need to plug my FC a second/third time before I get a bind. LED on receiver is dim when I power it up.

Update to the latest firmware as soon as you can. A batch of HM receivers have reached the market with Voltage regulators (marked SDG) that were insufficient and wasn't able to handle the higher current draw during boot up. To learn more of this issue and the fix, please check out this [PR](https://github.com/ExpressLRS/ExpressLRS/pull/928).

### ExpressLRS Lua Script is stuck at `Loading...`

Go back to the [Radio Setup Guide](transmitters/tx-prep.md) and make sure your radio is prepped up for ExpressLRS.

Also make sure your module has been flashed with v2.0 firmware. V2 Lua for V2.0-flashed modules, V1 Lua for v1.x-flashed modules (including modules fresh from factory; except the new OLED-equipped NamimnoRC modules and the Happymodel ES24TX Pro full-size module).

For newly-acquired ExpressLRS modules, flashing via USB is the recommended update method.

### Betaflight Lua is stuck at "Initializing"

Increase the TLM Ratio via the ExpressLRS Lua script to values like 1:4 or even 1:2 and retry the Betaflight Lua script.

Also, you have to make sure you're getting more than ten (10) Telemetry sensors prior to launching the script.

See [MSP Section](pre-1stflight.md#msp) for more info.

### My Blackbox Log has stepping on the RC trace

Make sure you have disabled ADC Filter in your Radio Hardware settings.

## Flashing/Updating

**Note: Individual hardware Flashing and Updating guide can be found by using the menu on the left sidebar.**

### Invalid serial RX configuration detected

This is often caused by incorrect Serial RX protocol (should be CRSF), or `serialrx_inverted = on` (should be off) or `serialrx_halfduplex=on` (should be off). The **Passthrough Init** section of the log will show you which setting should be corrected. See the [FC Preparation Guide](receivers/rx-fcprep.md) for the correct settings.

### RX Serial not found !!!!

Make sure your Serial RX on the Ports Tab of your FC Firmware configurator is set to the correct UART.

### No CLI Available

This message can be seen on the ExpressLRS Configurator Log while using the Passthrough method and can be caused by a busy Com Port. Make sure any other Configurator Apps were closed and unplug-replug your FC to USB. You might also want to use a different USB port or cable.

This could also mean that the FC cannot be detected by the script. This could also due to the FC being in DFU mode, which for passthrough flashing, is not needed.

### 10 Retries but no Success

This can be due to several things:

- Incorrect bootloader is flashed or it's not flashed properly. This mainly happen on the R9 receivers. Go checkout [Bootloader Flashing Guide](receivers/rx-bootloader.md).
- Incorrect wiring. Make sure that Rx in the Receiver is connected to a Tx pad in the FC and the Tx in the Receiver is connected to an Rx pad in the FC. Also make sure receiver is getting enough voltage (min 4v5) from the FC or voltage supply. Wiring guide is [here](receivers/rx-fcprep.md)
- Receiver is OFF. Check whether the LED on the receiver is lit, indicating it's powered and in working state.
- The UART has hardware inversion. Make sure that the UART you've connected the receiver to is not an SBUS UART that's usually have hardware inversion (most common among F4 Flight Controllers). There are Flight controllers that require you bridge a pair of pads to enable or disable the Hardware inversion of an Rx pad. You can simply try a different UART.
- The LED on the receiver is SOLID, while radio is off, could only mean that the Rx pad in the FC is being pulled LOW, putting the ESP-based receiver (EPs, ES900Rx, etc.) into Bootloader mode unintentionally, which will hinder normal passthrough operations. Feel free to try a different UART.

### Failed to connect to ESP8266: Timed out waiting for packet header.

This can be due to several things:

- Receiver is wired incorrectly. Please check if the Rx and Tx wires isn't swapped and connected Rx to Rx and Tx to Tx on the FC. Revisit the FC preparation page [here](receivers/rx-fcprep.md).
- The receiver's "boot" pads aren't bridged (or the button wasn't pressed and held during power up) for passthrough flashing. This is required for Passthrough flashing if the receiver is fresh from the packet and has a firmware version before 1.0.0-RC6.
- The receiver uart is putting it in Bootloader mode and is interfering with passthrough flashing. Move it into another UART.

You can also attempt the update the via UART using an FTDI Adapter (or a USB to UART Bridge).

Please see the Flashing guide for your particular receiver using the Sidebar on the Left.

### I updated via WiFi but now receiver won't work and has SOLID LED

This is a sign that the Wifi flashing didn't go through properly due to premature power cycle. To fix this, you will have to bridge the boot pads (see [here](receivers/rx-fcprep.md)) and reflash using the Passthrough method (**Telemetry** option on Betaflight/iNav set to `OFF`. This is important!) or using an FTDI adapter.

This video shows the steps albeit using vscode development environment but the ExpressLRS Configurator will work just fine. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/SShMaLnqZr8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To ensure that the WiFi flashing finished properly, **wait until the LED on the receiver blinks slow** (indicating it's looking for a TX bind) before pulling off power.