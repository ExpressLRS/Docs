---
template: main.html
---

![HW Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/hardware.png)

A few Flight Controllers and AIOs have been released with ExpressLRS receivers on-board using SPI instead of a regular UART. This means you can build a more compact and lightweight whoop or nano longrange rig without the need for an external receiver. More of these flight controllers are coming into stores.

Because these are SPI-based, the ExpressLRS Code came baked-in in the Betaflight 4.3.0-based custom-built firmware. These usually *don't* need to be updated. These Flight Controllers **will work** with any released ExpressLRS firmware.

## Binding Procedure

There are two ways to bind the receiver, as shown below

### Button Binding

Put the receiver into bind mode using any of these procedures:

- "Bind" button in the Betaflight Configurator, Receiver Page (if can't be found, [update](../../hardware/spi-receivers/#updating) the Betaflight firmware).
- using the CLI, type in `bind_rx` and press enter once.
- press the bind button on the flight controller.
- using the CLI, type in `set expresslrs_uid = 0`, press enter once, then save and reboot

Execute [elrs.lua](../../quick-start/tx-prep/#lua-script) in your handset and press the `Bind` button. The RX and TX should be now bound.

**Please mind the order, RX first, TX second.**

Video Tutorial (thanks to @JyeSmith):

<iframe width="560" height="315" src="https://www.youtube.com/embed/U2sxqx2oT4k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


### Passphrase

Set passphrase in the TX. When building via ExpressLRS configurator, or via VS Code note down and copy below numbers from the build log:

![UID String](../assets/images/UIDsource.png)

Go to betaflight cli and type (for example):

`set expresslrs_uid = 172,123,235,247,1,122`

`save`

## RF Mode Adjustment

These AIO, with ExpressLRS SPI Receiver, were set to use 500Hz as default. To adjust it, you will need to go into Betaflight CLI and use the following command:

`set expresslrs_rate_index = 0`

`save`

- 0 = 500Hz
- 1 = 250Hz
- 2 = 150Hz
- 3 = 50Hz

With the [Updated](../../hardware/spi-receivers/#updating) Betaflight firmware, adjusting your packet rate from the Lua Script will also adjust the packet rate in the AIO.

## Updating

As mentioned, there's little need to update, but should you still want to, the update will mean you will reflash your Betaflight firmware into your Flight Controller.

In preparation for this, you should save a copy of your `diff all` dump.

Download the necessary binaries (zipped) from this [Betaflight PR page](https://github.com/betaflight/betaflight/pull/10788). Extract the Hex File and, using Betaflight Configurator 10.8.0 (Nightly), flash the binary using the Load Firmware [Local] button found at the bottom right of the Firmware Flasher (Flight Controller in DFU Mode).

Once flashed, you will need to paste in the `diff all` you have saved. Don't forget to type in `save` and press enter once done. Power cycle your flight controller, and you should be set. Review your Betaflight settings, and check your RC link.

This procedure will only apply while Betaflight 4.3.0 is not yet released. Section will be updated appropriately for any changes in procedures.

For more information, head over to the [Betaflight PR page](https://github.com/betaflight/betaflight/pull/10788). We can also help out over at [Discord](https://discord.gg/dS6ReFY)!

*Content taken from the PR page c/o of [@phobos-](https://github.com/phobos-)*