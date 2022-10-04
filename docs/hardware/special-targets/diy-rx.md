---
template: main.html
---
![Hardware-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/hardware.png)

## Custom Hardware

Possibly one of the biggest benefits of using `ExpressLRS` is custom hardware!

- 📶 [Custom ESP 2.4 GHz RX](#custom-esp-24-ghz-rx)
- 📡 [Custom ESP 900 MHz RX](#custom-esp-900-mhz-rx)
- ⚡ [Flashing ESP Based RX](#flashing-custom-rx)

### Custom ESP 2.4 GHz RX

<figure markdown>
<a href="https://github.com/ExpressLRS/ExpressLRS-Hardware/tree/master/PCB/2400MHz/RX_20x20"><img class="center-img" src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/PCB/2400MHz/RX_20x20/v2.0/img/top.PNG?raw=true" width="20%" alt="2.4 GHz 20x20"></a>
</figure>

- 20x20 footprint and uses 0805 size SMD components. SMD components have been positioned on the PCB in a soldering iron friendly way. 🚸 

<figure markdown>
<a href="https://github.com/ExpressLRS/ExpressLRS-Hardware/tree/master/PCB/2400MHz/RX_Nano"><img class="center-img" src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/PCB/2400MHz/RX_Nano/img/front.jpg?raw=true" width="20%" alt="2.4 GHz Nano"></a>
</figure>

- The `ELRS Nano` RX is 18mm x 11mm and uses the same pinout as the `Crossfire Nano` RX. This allows for direct mounting to compatible flight controllers. ⚠️ This PCB uses 0402 SMD components and will require a hot air rework station and probably a microscope. 🔬 

### Custom ESP 900 MHz RX

<figure markdown>
<img class="center-img" src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/PCB/900MHz/RX_Mini_v0.1/img/front.jpg?raw=true" width="20%" alt="Mini_Rx_v0.1">
</figure>

<figure markdown>
<img class="center-img" src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/PCB/900MHz/RX_20x20_0805_SMD/img/populated_side_1.jpg?raw=true" width="20%" alt="20x20_RX_0805_SMD">
</figure>

<figure markdown>
<img class="center-img" src="https://images-na.ssl-images-amazon.com/images/I/51BwxcbSjoL._AC_SL1440_.jpg?raw=true" width = "20%" alt="Esp 01f">
</figure>

* Uses the `ESP-01F` for WiFi and a `RFM95` for our business 🕴️
* Requires ordering PCBs from Gerber files, a regulator chip, a few passives, a `ESP-01F` and a `RFM95` (915/868MHz)
* Multiple RX PCB designs [are available](https://github.com/ExpressLRS/ExpressLRS-Hardware/tree/master/PCB) ✅    
    * [`20x20 RX`](https://github.com/ExpressLRS/ExpressLRS-Hardware/tree/master/PCB/900MHz/RX_20x20_0603_SMD) - discrete SMD antenna for Wifi and RF directly soldered to PCB
        * Target DIY_900_RX_ESP8285_SX127x_via_UART
    * [`20x20 RX 0805`](https://github.com/ExpressLRS/ExpressLRS-Hardware/tree/master/PCB/900MHz/RX_20x20_0805_SMD) - easier to build due to bigger SMD parts. PCB antenna for Wifi and `u.fl` connector for RF
    * [`Mini RX`](https://github.com/ExpressLRS/ExpressLRS-Hardware/tree/master/PCB/900MHz/RX_Mini_v1.1) - the smallest form factor, lightest weight and lowest cost per PCB
* If you need help soldering, please check out [this video](https://www.youtube.com/watch?v=fqHleZjTaH8)

### Flashing Custom RX

#### Before you start

* The steps for building are in each individual [`README.md`](https://github.com/ExpressLRS/ExpressLRS-Hardware/tree/master/PCB) for the RX of your choice
* If you are using an `ESP-12F` instead of `ESP-01F` it is recommended to follow [this [tutorial](https://github.com/AlessandroAU/ExpressLRS/wiki/ESP-Backpack-Addon#board-esp12f) but use the appropriate RX target 🧑‍🏫 

#### Get it flashed

* Connect the serial adapter to `GND`, `TX`, `RX`, and the appropriate `3V3` or `5V`.
* Additionally, connect `IO0` to `GND` to activate the bootloader and enable flashing
* Quite some serial adapters have `TX` and `RX` swapped, mislabeled, or both 😸. Please double-check!
* Finally, select the appropriate RX target, make sure your user defines are correct, and press `Upload` in platformio