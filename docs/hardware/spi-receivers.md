---
template: main.html
---

![HW Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/hardware.png)

A few Flight Controllers and AIOs have been released with ExpressLRS receivers on-board using SPI instead of a regular UART. This means you can build a more compact and lightweight whoop or nano longrange rig without the need for an external receiver. More of these flight controllers are coming into stores.

Because the ExpressLRS code is "baked-in" to the flight controller firmware instead of a second microcontroller, these can not be updated the same way external receivers are. These SPI receivers always work with the ExpressLRS firmware of the same major version. That is, ExpressLRS 1.x.x and ExpressLRS 2.x.x need different **Flight Controller** firmware (Betaflight builds).

!!! info "NOTE"
    You cannot use the ExpressLRS Configurator to update these FCs. See the [updating](../../hardware/spi-receivers/#updating) section below.

## Binding Procedure

There are two ways to bind the receiver, as shown below

### Button Binding

Put the receiver into bind mode using any of these procedures:

- "Bind" button in the Betaflight Configurator, Receiver Page (if can't be found, [update](../../hardware/spi-receivers/#updating) the Betaflight firmware).
- using the CLI, type in `bind_rx` and press enter once.
- press the bind button on the flight controller.
- using the CLI, type in `set expresslrs_uid = 0`, press enter once, then save and reboot

Execute [ExpressLRS](../../quick-start/lua-howto/) Lua Script in your handset and press the `Bind` button. The RX and TX should be now bound (indicated by a SOLID LED on the Flight Controller).

**Please mind the order, RX first, TX second.**

Video Tutorial (thanks to @JyeSmith):

<iframe width="560" height="315" src="https://www.youtube.com/embed/U2sxqx2oT4k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


### Binding Phrase

The binding phrase is hashed into 6 bytes represented as numbers. These 6 bytes are referred to as the UID bytes. 
UID bytes are entered into the Betaflight CLI for binding. Please [look below](#setting-binding-phrase) for instructions. 
When building via ExpressLRS Configurator or via VS Code, note down the UID bytes from the build log. You can also use the 
[generator below](#uid-byte-generator) to retrieve your UID bytes from your binding phrase.

![UID String](../assets/images/UIDsource.png)

#### UID Byte Generator

<style>
.bp-input {
  color: #000;
}
</style>

Binding Phrase
<div class="bp-wrapper">
  <input class="md-input bp-input" type="text" placeholder="..." />
</div>

UID Bytes
```
```

#### Setting Binding Phrase
Go to Betaflight CLI and enter the following commands. (Enter your binding phrase above)
```
```

<script type="text/javascript" src="//unpkg.com/crypto-js@4.1.1/crypto-js.js"></script>
<script type="text/javascript">
  window.addEventListener("load", (event) => {
    initBindingPhraseGen();
  });
</script>

## RF Mode Adjustment

These AIOs with ExpressLRS SPI Receivers are set to use 500Hz as default. To adjust it, you will need to go into Betaflight CLI and use the following commands:

```
set expresslrs_rate_index = [your index]
save
```

Where `[your index]` corresponds to the following   :

- 500Hz = 0
- 250Hz = 1
- 150Hz = 2
- 50Hz = 3

With the [Updated](../../hardware/spi-receivers/#updating) Betaflight firmware, adjusting your packet rate from the Lua Script will also adjust the packet rate in the AIO.

## Updating

As mentioned, you must flash a Betaflight firmware that's compatible with the ExpressLRS major version on your transmitter. ExpressLRS 1.x.x TX only works with Betaflight firmware for ExpressLRS 1.x.x, and upgrading the transmitter to ExpressLRS 2.x.x means flashing the flight controller with a different Betaflight version (e.g. Betaflight 4.3-RC1 5933d96). You don't need to update the FC firmware whenever there's minor updates on the main ExpressLRS codebase, unless there's any update on the Betaflight codebase itself for the SPI ExpressLRS receivers.

In preparation for updating, you should save a copy of your `diff all` dump.

Using the latest [Betaflight Configurator](https://github.com/betaflight/betaflight-configurator/releases), navigate into `Firmware Flasher` and select the latest Betaflight release (at the time of writing, it should be set to Release and Release Candidate; and use 4.3.0-RC1). Depending on your AIO board, the target will differ:

* Happymodel AIO: CRAZYBEEF4SX1280
* BetaFPV AIO: BETAFPVF4SX1280
* SPRacing SPH7RF: Coming soon!

!!! warning ""
    The Happymodel Mobula6 900MHz AIO with the CrazyF4 ELRS FC (Target: CRAZYBEEF4DX) doesn't use an SPI ExpressLRS receiver. Check the page for [ES915RX](../../quick-start/rx-hmes900/#es915868rx-discontinued) instead.

Once flashed, you will need to paste in the `diff all` you have saved. Don't forget to type in `save` and press enter once done. Power cycle your flight controller, and you should be set. You may need to set your Binding Phrase once again if you pasted in Factory Diff All. Review your Betaflight settings (no changes needed for the Receiver Type and Protocol; should already be set with `SPI Receiver`, with Provider as `ExpressLRS`), and check your RC link in the Receiver Tab (were sticks moving?).

For more information, head over to the already merged [Betaflight PR page](https://github.com/betaflight/betaflight/pull/10788). We can also help out over at [Discord](https://discord.gg/dS6ReFY)!

*Content taken from the PR page c/o of [@phobos-](https://github.com/phobos-)*
