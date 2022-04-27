---
template: main.html
---

![HW Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/hardware.png)

This is the hardware landing page! Welcome in. To navigate through this (large) subsection, use the sidebar on the **left**.

These pages show information on certain modifications to hardware, and certain ELRS specific hardware. More and more manufacturers are coming up with their own take of the ExpressLRS Hardware and the list keeps growing.

At the time of writing, here are the ExpressLRS-supported Transmitter Modules and Receivers, along with a few Flight Controllers and AIO boards.

## 2.4GHz Transmitter modules

### Happymodel ES24Tx

[Flashing Guide](../quick-start/transmitters/es24tx.md)

[Manufacturer Website](http://www.happymodel.cn/index.php/category/product/2-4g-system/elrs/)

### NamimnoRC Flash

[Flashing Guide](../quick-start/transmitters/flash2400.md)

### Axis Thor TX

Includes Color TFT display, built in motion sensor and thermally controlled fan

[Flashing Guide](../quick-start/transmitters/axis-thor.md)

[Manufacturer Website](https://www.axisflying.com/product/axisflying-elrs-2-4g-module-thor-tx-pro-10-1000mw/)

### BetaFPV Nano 2.4GHz

[Flashing Guide](../quick-start/transmitters/betafpv2400.md)

[Manufacturer Website](https://betafpv.com/products/elrs-nano-tx-module?variant=39416993382534)

### Jumper AION Nano TX

[Flashing Guide](../quick-start/transmitters/jumper-aion.md)

### Vantac Lite TX

[Flashing Guide](../quick-start/transmitters/vantac-lite.md)

### Ghost TX

[Flashing Guide](../quick-start/transmitters/ghost2400.md)

*Note: STLink first time flash, irreversible*

### Siyi FM30

[Flashing Guide](../quick-start/transmitters/siyifm30.md)

Max output power: 100mW default, 250mW with `UNLOCK_HIGHER_POWER`

## 2.4GHz Receivers

To help find the right receiver for your needs, see the [Receiver Selection](receiver-selection.md) page.

### Happymodel EP1 & EP2

[Flashing Guide](../quick-start/receivers/hmep2400.md)

[Manufacturer Website](http://www.happymodel.cn/index.php/category/product/2-4g-system/elrs/)

### Happymodel PP

[Flashing Guide](../quick-start/receivers/hmpp2400.md)

[Manufacturer Website](http://www.happymodel.cn/index.php/category/product/2-4g-system/elrs/)

### NamimnoRC Flash

[Flashing Guide](../quick-start/receivers/flash2400.md)

### Axis Thor RX

[Flashing Guide](../quick-start/receivers/axis-thor.md)

[Manufacturer Website](https://www.axisflying.com/product/axisflying-elrs-2-4g-module-thor-tx-pro-10-1000mw/)

### BetaFPV Nano 2.4GHz

[Flashing Guide](../quick-start/receivers/betafpv2400.md)

[Manufacturer Website](https://betafpv.com/products/elrs-nano-receiver?variant=39416095408262)

### MatekSys 2.4GHz Receivers

[Flashing Guide](../quick-start/receivers/matek2400.md)

[Manufacturer Website](http://www.mateksys.com/?portfolio=elrs-r24)

### Jumper AION Mini 2.4GHz Recievers

[Flashing Guide](../quick-start/receivers/jumper-aion.md)

### Vantac RX

[Flashing Guide](../quick-start/receivers/vantac2400.md)

### Ghost Atto Receivers

[Flashing Guide](../quick-start/receivers/ghost2400.md)

*Note: STLink first time flash, irreversible*

### Siyi FR Mini

[Flashing Guide](../quick-start/receivers/siyiFRmini.md)

Max telemetry power: 100mW default, 250mW with `UNLOCK_HIGHER_POWER`

*Note: only guaranteed to work on the v3.0 of the receiver*

## 900Mhz Transmitter Modules

### Frsky R9M (inc. Lite & Lite Pro)

[Flashing Guide](../quick-start/transmitters/frsky-r9modules.md)

[Fan Mod](https://www.expresslrs.org/2.0/hardware/fan-mod/)

Max output power: 250mW default, 1W with `UNLOCK_HIGHER_POWER`

### Happymodel ES900TX

[Flashing Guide](../quick-start/transmitters/es900tx.md)

[Manufacturer Website](http://www.happymodel.cn/index.php/category/product/2-4g-system/elrs/)

Max output power: 250mW default, 1W with `UNLOCK_HIGHER_POWER`

### NamimnoRC Voyager

[Flashing Guide](../quick-start/transmitters/voyager900.md)

### BetaFPV Nano 900Mhz

[Flashing Guide](../quick-start/transmitters/betafpv900.md)

[Manufacturer Website](https://betafpv.com/products/elrs-nano-tx-module?variant=39416993415302)

## 900Mhz Receivers

### Frsky R9 Receivers

- R9MM
- R9 Mini
- R9MX
- R9 Slim
- R9 Slim+

[Flashing Guide](../quick-start/receivers/r9.md)

### Jumper R9 Mini

[Flashing Guide](../quick-start/receivers/jumper900.md)

### Happymodel ES900RX

[Flashing Guide](../quick-start/receivers/hmes900.md)

[Manufacturer Website](http://www.happymodel.cn/index.php/category/product/2-4g-system/elrs/)

### NamimnoRC Voyager

[Flashing Guide](../quick-start/receivers/voyager900.md)

### BetaFPV Nano 900Mhz

[Flashing Guide](../quick-start/receivers/betafpv900.md)

[Manufacturer Website](https://betafpv.com/products/elrs-nano-receiver?variant=39416095441030)

## Flight Controllers with onboard ExpressLRS Receivers

### Happymodel ELRS F4 2G4 AIO

[Manufacturer Website](http://www.happymodel.cn/index.php/2021/05/19/happymodel-elrs-f4-2g4-aio-5in1-flight-controller-built-in-spi-2-4ghz-elrs-rx/)

*Note: SPI-based receiver. Doesn't need the ExpressLRS Configurator for updates. See this [page](spi-receivers.md) for more info.*

### Happymodel CrazyF4 ELRS AIO 900Mhz

[Manufacturer Website](http://www.happymodel.cn/index.php/2021/04/22/happymodel-crazyf4-elrs-aio-5in1-flight-controller-built-in-900mhz-elrs-rx/)

*Note: Receiver firmware can be updated using the [ES915/868RX](../quick-start/receivers/hmes900.md#es915868rx-discontinued/) methods.*

### BetaFPV F4 1S 12A AIO

[Manufacturer Website](https://betafpv.com/products/f4-1s-12a-flight-controller?variant=39409298768006)

*Note: Receiver firmware can be updated using the [Beta FPV Nano 2.4GHz](../quick-start/receivers/betafpv2400.md) methods*

### SPRacing H7RF

[Manufacturer Website](http://seriouslypro.com/spracingh7rf)

*Note: SPI-based receiver. Doesn't need the ExpressLRS Configurator for updates. See this [page](spi-receivers.md) for more info.*

## DIY TX Modules

See this page [here](special-targets/diy-tx.md)

## DIY Receivers

See this page [here](special-targets/diy-rx.md)
