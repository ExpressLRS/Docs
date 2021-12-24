---
template: main.html
---
# VRx Backpack Setup
![Hardware-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/hardware.png)

## Flashing your VRx Backpack Device

Before wiring up your VRx Backpack, you NEED to first flash the VRx Backpack firmware into it either via WiFi or UART/FTDI.

Good VRx Backpack candidates are the EP1 or EP2 receivers from Happymodel as these have Boot pads, instead of Boot buttons. The Boot pad will be repurposed for the SPI Clock signal from the VRx module.

The VRx firmware you will flash into your Backpack Device will depend on what VRx module you want to connect it to or it will not work properly.

### Flashing via WiFi (ESP-based ExpressLRS Receivers)

Power up your selected VRx Backpack device (connect 5v and gnd pads to any 5v power source). Let it go into WiFi Update mode (fast blinking LED) and load up the WiFi Update page. In the Address bar of your browser, add `?force=true` to ensure it will accept the VRx Backpack firmware. The resulting URL should read `http://10.0.0.1/?force=true` (if you connected via Access Point) or `http://elrs_rx.local/?force=true` (if your device has connected to your local WiFi network).

!!! note ""
    The `?force=true` is not needed for these ESP-based receivers with factory-firmware. It will only be needed if you have flashed the receiver into ExpressLRS v2.0 and wanted to repurpose it for VRx Backpack.

On the Assets section of the [Backpack Release](https://github.com/ExpressLRS/Backpack/releases) on Git Hub, `Download` the binary suited for your VRx module. Upload this binary into the VRx device using the Web Update page. Wait (~30s) until the LED on the VRx device has turned on again.

Alternatively, you can use the ExpressLRS Configurator to create your binaries for you. **Build** your binary, with the set `binding phrase` (Optional) as well as Home Network SSID and Password (Optional; available starting 0.2.0). Upload the resulting binary into the WiFi Update page as outlined above.

### Flashing via FTDI/UART

!!! note ""
    This method is best used for the DIY ESP01F VRx Backpacks, as these devices do not have any firmware from factory.

Connect your FTDI Rx pin into the Tx pad of your VRx Device, and the FTDI Tx pin into the Rx pad of the VRx Device; then the 5v and Gnd pads. The Boot pad needs to be bridged with the Ground pad. Connect your FTDI, with the connected VRx device, into a free USB port (VRx Device's LED should light up SOLID). Using the ExpressLRS Configurator, select your VRx module, select the `via UART` method and set your `binding phrase` (Optional) and the Home Network SSID and Password (Optional; Available starting 0.2.0). Click **Build and Flash** and the compiling and flashing should commence. If done right, the Success bar should appear and your VRx Backpack should now be ready for wiring into your selected VRx Module.

## VRx Module Setup before wiring it all up

You will need to set your VRx module to the highest band and channel it can go, usually Race 8 (5917MHz) before wiring up any VRx Backpack. This is to ensure the VRx Backpack knows "where it is" in the selectable channels.

## Connecting the VRx Backpacks to your VRx Modules

Currently supported VRx Modules include:

* ImmersionRC Rapidfire  
* SkyZone SteadyView
* Generic RX5808 Module
* FENIX Module

The VRx Backpacks communicate to these modules via SPI bus and involves 3 signal lines: `CLK`, `DATA`, `CS`. Depending on your VRx Backpack, they will either need `5v` (ExpressLRS ESP-based Receiver) or `3.3v` (ESP01F module) and of course the `GND` line.

![backpack EP](../../assets/img/backpackEP.png)

For the ESP01F Module, you will have to source out a voltage regulator such as an `AMS1117` (1A Low Drop-out Voltage Regulator) which will lower the 5V voltage from the VRx module to the needed `3.3v`.

![ESP01f Wiring](https://github.com/ExpressLRS/Backpack/raw/master/img/esp-wiring-diagram.jpg)

### Rapidfire Backpack Connection

Follow the wiring guide below for the Rapidfire module. Make sure that the VRx module is set to R8 (5917) for this to work properly.

![Rapidfire Connection](https://github.com/ExpressLRS/Backpack/raw/master/img/rf-wiring0diagram.jpg)

![Rapidfire Backpack](https://github.com/ExpressLRS/Backpack/raw/master/img/esp-on-rf.jpg)

The VRx Backpack fits snugly in the module bay. No further modding needed.

![Rapidfire in Bay](https://github.com/ExpressLRS/Backpack/raw/master/img/installed.jpg)

![Rapidfire Covered](https://github.com/ExpressLRS/Backpack/raw/master/img/front-cover.jpg)

### SteadyView Backpack Connection

You will need to desolder 3 pins from the module, or cut them off. 

Follow the wiring shown on the image below:

![Steadyview Wiring](https://github.com/ExpressLRS/Backpack/wiki/SkyZone-Wiring.jpg)

* Blue wire is the CLK pin (Pin 1; connected to Boot pad, if using an ExpressLRS Receiver).
* Green wire is the DATA pin (Pin 2; connected to the RX pad, if using an ExpressLRS Receiver).
* Yellow wire is the CS pin (Pin 3; connected to the TX pad, if using an ExpressLRS Receiver).

The power supply wires are connected as follows:
* Black wire is GND and connected to Pin 7 of the VRx module.
* Red wire is the 5V supply and connected to the last Pin of the module (Pin 9).

![Tidying it up](https://github.com/ExpressLRS/Backpack/wiki/SkyZone-Assembled.jpg)

![Covered up](https://github.com/ExpressLRS/Backpack/wiki/SkyZone-Lid-On.jpg)

### Generic 5808 Backpack Connection

### FENIX Bacpack Connection

## Binding Backpacks together
