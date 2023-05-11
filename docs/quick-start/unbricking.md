---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/quick-start.png)

## HELP I BRICKED MY RX!

Take a breath, calm down, relax. If you’ve had a failed update your RX or TX might be in a non-working state. The good news is that unless the hardware is damaged, it’s impossible to brick any of the ExpressLRS hardware. ANY of the hardware can be recovered using the serial passthrough feature of a flight controller, or with a usb-serial adapter. 

Let’s start with the RX’s, since they are usually the trickiest. There are two main classes of receivers. STM32 based and ESP8285 based. If you’re not sure, you probably have an ESP8285 based RX. The main difference is that the STM32 RX’s don’t have WiFi. 

Now, ALL the ESP8285 based RX’s have a factory installed bootloader onboard which CANNOT be damaged or tampered with. You can completely screw up the upgrade and always get it back using this default bootloader. 

First, we must stop betaflight getting in the way and screwing things up with telemetry. Load up the configurator, go to the configuration page and then disable telemetry. Press save and reboot. If not already done so, the RX must be wired to the Flight controller or a USB-SERIAL adapter. 

Take note that the RX wires goes to the TX and vice versa, BOTH wires must be connected. If your receiver was already working properly and it’s still wired in you’ve already done this step.

Next, we must activate the ROM bootloader. On every ESP8285 based RX there is a GPIO0 pin somewhere on the board, it may be connected to a button, or it may be a bare pad on the PCB. You must connect this pin to ground, THEN apply power. If you’ve done it right the LED should be solid on. How exactly this is done depends on the type of receiver:

- If you have a receiver with a button, just hold it down while you apply power to enter the bootloader. Keep holding the button until the configurator starts uploading to the RX.
- If you have an EP1/EP2 you have to short the boot pad which is located just above GND to GND with solder. 

#### Happymodel EP1, EP2 boot pads:

![HM2400 connection](../assets/images/hm2400.png)

Once the receiver is in bootloader mode, all you need to do is configure the RX in the configurator as per normal and then upload with the ‘via_BetaflightPassthrough’ method. If all goes well, you should see it upload successfully. 

> If the flashing process still fails try to move the 5V RX wire to the pin that requires LiPo to power it on. You need to power up the receiver only during the "Passthrough Done" stage or the "Connecting ..." stage.

If you’ve still got the boot pad bridged with solder, you’ll need to remove the solder before it will work again. Congratulations! You’ve unbricked your receiver, go fly!

## Wall of Text? Here's a vid!

<iframe width="640" height="390" src="https://www.youtube.com/embed/jYLwaWBkM_A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## A step-by-step guide

1. Make sure your Receiver only powers up with a LiPo Connected.
    - If your receiver powers up with just USB connected, move the 5v wire of the receiver into a 5v pad that only powers up with LiPo connected.
        - Take a multi-meter in DC Voltmeter mode.
        - Plug in USB into your Flight Controller. Disconnect LiPo.
        - Probe/check each of the 5v pads in the Flight Controller.
        - The 5v pads that read 0v on the multi-meter are pads that will only power up when a LiPo is connected.
        - Solder your Receiver 5v into this pad.
    - If in the above steps, you're not able to find a 5v pad suitable for this procedure, follow the following:
        - Disconnect the 5v wire of the Receiver from the 5v pad on the Flight Controller.
        - Solder a different length of wire into any of the 5v pad on the Flight Controller.
        - Expose a suitable length of conductor of this wire that you can connect with the Receiver's 5v wire LATER.

2. If you've connected a LiPo from the previous step, disconnect it. Also unplug the Flight Controller from your computer.

3. Bridge the Boot Pads on the Receiver to put it in Bootloader mode manually.
    - If your Receiver has a button, take an alligator clip to keep the button pressed.
    - If your Receiver only has one Boot pad, connect it to a Ground pad.

4. Connect to Betaflight or INAV Configurator and make sure you've properly [configured your FC](receivers/configuring-fc.md) for ExpressLRS use. Set `Telemetry` to **disabled** for now.

5. Save & Reboot. Close Betaflight Configurator. Also close any other App that's potentially using COM Ports.
    !!! info Cura Slicer
        We found Cura Slicer and possibly others like it would keep a COM port open or busy preventing successful flashing/recovery via Passthrough.

6. Unplug-replug the USB cable.

7. On the ExpressLRS Configurator, select the Firmware Version you're trying to recover to. Select your Device Category and Device Target as well, along with your usual Firmware Options.

8. Set the Flashing Method to `Betaflight Passthrough`.

9. Click the `Build and Flash` button. Wait for the Line **PASSTHROUGH DONE** to appear in the Build Log.

10. Plug in LiPo or twist the 5v Wires together to power up the receiver (see Step 1).

11. Wait for the process to finish, hopefully with the Success Message. Otherwise repeat the procedure above or try a different approach (like reflashing via FTDI/UART Adapter).

12. You can now power down the flight controller, disconnect LiPo and/or USB.

13. Remove the boot pads bridging or connection to ground, or, if your Receiver has a button, then alligator clip pressing the button.

14. Repower up the receiver to verify it is back into normal working state.
