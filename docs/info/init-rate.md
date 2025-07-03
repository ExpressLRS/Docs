---
template: main.html
description: ExpressLRS Init Rate or the Packet Rate that the receiver will start checking for the Sync Packet.
---

![Info Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/information.png)

### What happened to the Lua Init Rate option?

The `Init Rate` receiver Lua option was removed in ExpressLRS 3.4 in favor of automatic Init rate storage.

### What is Init Rate?

On boot, the receiver will listen for the Sync Packet starting with the fastest RF Mode or Packet Rate, down to the slowest, then cycles, until it finally Syncs and Binds.  The `Initialization Rate` controls the packet rate that the receiver will start checking for the Sync Packet which can allow for near-instant connection when the receiver is powered up.

The Init Rate is stored when a connection is established starting in ExpressLRS 3.5.6 and no further steps are required. However, in ExpressLRS 3.4.x and most 3.5.x, the Init Rate is instead stored when a connection ends and requires one of the extra steps below to lock in the Init Rate.

### Setting Init Rate (before ExpressLRS 3.5.6 only)

#### Method 1: Switch To Rate

* Power on both a receiver and transmitter and wait for them to connect on any packet rate.
* On the transmitter, select the packet rate to set the receiver's Init Rate to.
  * **NOTE** the packet rate must actually change for the setting to be sent. This means changing away from, then back to the desired packet rate if already connected at the desired rate.
* The receiver briefly failsafes when changing packet modes and will save the target rate.

The receiver will now boot at the selected rate on next boot.

#### Method 2: Transmitter Power Off

* Power on the transmitter and select the packet rate to set the receiver's Init Rate to.
* Power on the receiver and wait for it to connect. The LED on the receiver should be on solid / not blinking.
* Power off the transmitter with the receiver still connected, bypassing any EdgeTX warnings along the way.
* The receiver should failsafe and the LED will start blinking again.

The receiver will now boot at the selected rate on next boot.
