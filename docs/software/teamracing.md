---
template: main.html
description: TeamRacing allows selection between multiple connected models, failsafing all unselected models.
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

## What is Team Racing?

Team Racing is a receiver feature that allows multiple models to be connected to one transmitter at the same time. Each model is assigned to a different switch position and will select that model to control. Any non-selected model is failsafed and will have its telemetry disabled.

The purpose of the receiver selection is to allow a downed model (which is physically unreachable mid-race) to be deactivated and allow the pilot to take control of another model using the same controller. In a default setup, if the pilot plugged in a new model and armed, both models will respond and arm which is incredibly undesirable. This would be used in a Team Race event such as MultiGP Mayhem.

### Formal Definition

Team Racing is defined in this context as:

* 0 or 1 active transmitters with a distinct binding phrase. "One pilot operating their transmitter"
* Multiple receivers bound to that transmitter's binding phrase, all powered at the same time.
* Pilot has the ability to direct which receiver is currently "active" including:
  * Sending channels data and LinkStats information to flight controller
  * Transmitting telemetry to the TX
  * Updating servo positions

### Team Racing does NOT

* Allow multiple pilots (more than 1 active transmitter) to control a model. There is only one binding phrase and ExpressLRS rule is one active transmitter per binding phrase.
* Support different packet rates / switch modes per model. All models use the same packet parameters.
* Encourage pilots to have multiple active models flying at once, e.g. launching a model and putting it into autopilot, then switching to a second model to chase it by effectively failsafing the first via TeamRace switch.
* Adjust VTX power settings when switching.

## Setup

Two configuration parameters are present in the Receiver Lua (ExpressLRS Lua -> Other Devices -> (select receiver item) -> Team Race). See [ExpressLRS Lua script](../quick-start/transmitters/lua-howto.md#team-race)

* Channel - The channel that is checked to determine the currently selected model.
* Position - Which position of the TeamRace Channel activates this model.

No flight controller setup is needed. The receiver selection is completely transparent to the flight controller-- the channels will stop updating and it should failsafe as normal. **NOTE** Servos will wait 1s before switching to failsafe positions, which may be longer than normal (LQ dropping to 0 is usually faster than the 1s hard timeout).

Team Racing works in Hybrid and Wide switch mode as well as FullRes packet modes. When the receiver is in a TeamRace Mismatch mode, the LED will display the "Model Mismatch" blink pattern / color. The Lua will not display Model Mismatch, as telemetry will be disabled.

## VTX Control

No VTX Admin / Control is performed when deselecting a model at this time due to the variety of ways a user might configure their VTX to go into Pit Mode: ExpressLRS VTX Admin Pit Switch, Betaflight PitMode mode switch, or USER1/USER2/pinio_box power cut. The user must still configure their method to disable the deselected VTX using the Team Race channel. For CRSF mode serial output, ExpressLRS guarantees at least one packet with the proper deselected channel position will be sent to the flight controller to handle this.
