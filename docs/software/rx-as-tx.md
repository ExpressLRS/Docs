---
template: main.html
description: Flash a spare ExpressLRS receiver with transmitter firmware and use it as a small TX module.
---

![Software Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png)

## Description

RX-as-TX flashes transmitter firmware onto receiver hardware. A receiver has the same radio parts as a small transmitter module, so a spare receiver can drive a JR module bay, a simulator dongle, or an [AirPort](airport.md) data link.

The feature was added in ExpressLRS 3.5.0.

!!! warning "Warning"
    A receiver has a much smaller antenna and far less cooling than a real TX module. Output power is limited, and the device gets hot at the higher power levels. Do not expect the range of a normal transmitter module, and do not use RX-as-TX for a long range flight.

!!! warning "Regulatory"
    You are still responsible for the regulatory domain and the power limits where you fly. Flash the correct domain for your country, exactly as you would for any other transmitter.

## Supported Hardware

| Receiver type | Internal (full duplex) | External (half duplex) |
|---|---|---|
| ESP32 | Yes | Yes |
| ESP8285 | Yes | No |
| STM32 | No | No |

The ExpressLRS Configurator refuses any combination that is not in this table.

The target must also have both a serial RX pin and a serial TX pin in its hardware layout. A receiver without both pins cannot be used, and the Configurator stops with `Cannot select this target as RX-as-TX`.

!!! note "STM32 receivers"
    STM32 receivers are not supported. The FrSky R9 and SIYI FM30 pages describe an older method that flashes a specific STM32 target over STLink. That is a separate, legacy procedure and it is not the RX-as-TX option described here.

## Internal versus External

`internal` and `external` describe how the module talks to the handset.

* `internal` is full duplex. The handset uses separate RX and TX lines. Use this for an internal module bay, and for any ESP8285 receiver.
* `external` is half duplex. The build moves the serial RX pin onto the serial TX pin so a single wire carries both directions. Use this for a JR module bay, which has one signal pin.

## Flashing

RX-as-TX is hidden until Expert Mode is turned on in the ExpressLRS Configurator.

1. Open the ExpressLRS Configurator and turn on Expert Mode.
2. Select the device category and the device target for the receiver you are converting.
3. Set the `RX_AS_TX` option to `internal` or `external`, following the table above.
4. Set the regulatory domain and the binding phrase as you would for any other device.
5. Flash the receiver with the method you would normally use for that receiver, for example UART or WiFi.

After flashing, the device is a transmitter. It no longer behaves as a receiver, it appears with the transmitter WiFi name, and it uses the transmitter Lua script.

## Wiring to a JR Module Bay

Use the `external` build for a JR bay. Connect the serial TX pin of the receiver to the signal pin of the bay, plus ground and a supply the receiver accepts.

!!! danger "Check the bay voltage"
    A JR module bay usually supplies battery voltage, which is far above what a receiver accepts. Feeding the bay voltage straight into a receiver will destroy it. Check the voltage rating of your receiver and add a regulator if you need one.

## Returning to Receiver Firmware

Flash the normal receiver firmware for the same target, with Expert Mode off or with `RX_AS_TX` cleared. Use UART flashing if the device no longer connects the way you expect, since the device is running transmitter firmware and will not behave like a receiver.

If a flash fails and the device stops responding, follow the [Unbricking](../quick-start/unbricking.md) procedure for the receiver.
