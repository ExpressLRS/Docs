---
template: main.html
description: ESPNOW Example ESP8266 or ESP32
title: ESPNOW Example ESP8266 or ESP32
---

![Software Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png)

## Description

ExpressLRS now has support for Espnow Backpack. This is a simple example for the ESP8266 and ESP32 to receive data from a Backpack using the CRSF protocol.

## Hardware Requirements

ESP8266 and ESP32 board.

## Example Code

https://github.com/druckgott/ELRS-Backpack-Example-ESPNOW

## Software Requirements

Ensure both your transmitter module and your receiver are up to date with the latest release versions; follow the [Firmware Update Guide](../../quick-start/getting-started/) for detailed instructions.

The minimum version to use this feature is:
- Receiver firmware: `3.5.0`
- Backpack firmware: `1.5.0`

## Setting up

1. Install Visual Studio Code and Platform io https://code.visualstudio.com/download

2. Install git.

3. Add project to Visual Studio code and compile and flash.

# Config the sketch:
 * On the website https://expresslrs.github.io/web-flasher/, the private UID must be generated (using the same password as the ELRS system).
 * This UID must be entered in the sketch under ``` uint8_t UID[6] = {106,19,19,206,193,30};```.

 * In the ELRS Backpack, Telemetry ESPNOW must be enabled (tested with Backpack version 1.5.1).

 * A telemetry connection between the transmitter and, for example, the drone/flight controller must be established.