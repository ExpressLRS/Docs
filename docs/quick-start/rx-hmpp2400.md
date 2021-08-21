---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing via Passthrough

Target: `HappyModel_PP_2400_RX_via_BetaflightPassthrough`

The PP receivers do not have Wifi, and so, it can only be updated via Passthrough.

Follow the same wiring as that of the EP receivers shown [here](/quick-start/rx-fcprep/#happymodel-ep1-ep2-pp). The PP has a silkscreened "RT5G" on one of its side indicating the order of the pads, with R = Rx, T = Tx, 5 = 5v and G = Gnd,  respectively. Connect the Rx pad to a Tx pad on the FC, and the Tx pad to an RX pad on the FC, with 5v and Gnd to their usual connections.

The PP **doesn't** have a `Boot` pad either so there's no need to bridge any pads.

Once wired, power up your FC by connecting a LiPo or, if the receiver is getting powered via USB, connect your USB cable to a vacant port.

Using the ExpressLRS Configurator, with the correct Target selected and [Firmware Options](/quick-start/firmware-options) set, hit **Build & Flash**. Wait a bit for the process to finish and you should see a "Success" banner. 

Power-cycle the FC and verify receiver connects to the Tx module (power up the Tx first, then the Receiver).
