---
template: main.html
description: A short guide on how to add a fan on your FrSky R9M module flashed with ExpressLRS.
---

![Hardware-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/hardware.png)

Initially, this mod is brought to life by [Niklas Voigt](https://discordapp.com/users/773143572354039828) and Seba112PL as a beta tester and is still a work in progress.. if you have suggestions don't hesitate to contact.

!!! warning "DISCLAIMER"
    Users have experienced [temperature issues](https://github.com/ExpressLRS/ExpressLRS/issues/429) on R9M that degrades the link quality. We recommend you use the lowest power setting required for your flight and turn on dynamic power at all times (ELRS v2.0+)

!!! hint "Hot Tip"
    It might seem counterintuitive, but using less power might help for longer flight times and more range by reducing the heat. ELRS does not require a lot of energy and looking at the [long-range leader board](https://github.com/ExpressLRS/ExpressLRS#current-leaderboard)

## 1W Mod
!!! warning "WARNING" 
    With this mod your R9M is still limited to 1W

<figure markdown>
![1W mod top](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/STL/R9M-Fan-Mod-Case/view-top.png){ width=40% }
![1w mod bottom](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/STL/R9M-Fan-Mod-Case/view-bottom.png){ width=40% }
</figure>

You need a **20x20mm** or **25x25mm** **fan** in **5V** version. 
Both sizes are supported. To secure the fan into the cover you can use **2x M2 screws**, a thread is already in the print.
You can solder the pins of the fan directly to the **5v port of the R9M** or use the [**Controllable Fan Mod**](#controllable-fan-mod) which can control the fan out of software (fan blows only at >250mW). 

R9M Fan Mod Cover is built out of four Parts and a Sticker:

<figure markdown>
![r9m Fan Mod Cover](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/STL/R9M-Fan-Mod-Case/view-description.png){ width=50% }
</figure>

### Download

* [R9M-Fan-Case-Cover.stl](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/STL/R9M-Fan-Mod-Case/R9M-Fan-Case-Cover.stl)
* [R9M-Fan-Case-Pins.stl](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/STL/R9M-Fan-Mod-Case/R9M-Fan-Case-Pins.stl)
* [R9M-Fan-Case-XT30.stl](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/STL/R9M-Fan-Mod-Case/R9M-Fan-Case-XT30.stl)
* [R9M-Fan-Case-Standoff.stl](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/STL/R9M-Fan-Mod-Case/R9M-Fan-Case-Standoff.stl) (2x)
* [R9M-ExpressLRS-900MHz.pdf](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/STL/R9M-Fan-Mod-Case/R9M-ExpressLRS-900Mhz.pdf)

or from [Thingiverse](https://www.thingiverse.com/thing:4829360)

## Controllable Fan Mod

Additionally to the fan, you'll need one NPN Transistor (e.g. `2N4401`) or N-Channel MOSFET (e.g. `BS170` has built-in Schottky-Diode) and a resistor (200-3k7)

<figure markdown>
![Fan Mod Controllable](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/wiki-from-discord/n-channel-mosfet.png){ width=40% }'
![Fan Mod Controllable via NPN transistor](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/wiki-from-discord/npn-transistor.png){ width=40% }
</figure>

### R9M2019 Build notice

The PB9 pad location on the R9M2019 module is a bit different. Please see the photo.

<figure markdown>
![PB9 pad location](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/wiki-from-discord/R9M2019.png){ width=40% }
<figcaption>PB9 pad location</figcaption>
</figure>

## 2W Mod 

!!! warning "WARNING"
    Only do this if you are comfortable with modding hardware

In addition to the [3D printed Cover](#download) & the [**Controllable Fan Mod**](#controllable-fan-mod) you'll need:

* Fan + Heatsink `"2507 25MM 25x25x13MM Hydraulic bearing Graphics card Cooling fan with heat sink 5V 12V m.2 SSD Fan with 2pin"`
* Thermal Pad 0.5mm `"1pc 100mmx100mmx0.5mm GPU Northbridge IC LED Chipset Heatsink Cooling Conductive Silicone Thermal Pad,100x100x0.5mm w/ 3.2W/M-K"`

The screw heads are cut off to reduce height.

<figure markdown>
![heatsink view 1](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/wiki-from-discord/heatsink.jpeg){ width=40% }
![heatsink view 2](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/wiki-from-discord/heatsink2.jpeg){ width=40% }
![heatsink view 3](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/wiki-from-discord/heatsink4.jpeg){ width=40% }
![heatsink view 4](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/wiki-from-discord/heatsink5.jpeg){ width=40% }
</figure>

As you can see in picture 3, the 5v fan is connected to the power source of the module, so the fan is used with some overvoltage and spins with higher rpm... tested for a long time and should not be a problem for the fan.
If you don't know how to allow the 2W in the firmware, don't do this mod!🤦‍♂️

## Here are some makes

<figure markdown>
![make 1](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/STL/R9M-Fan-Mod-Case/view-real.jpg){ width=40% }
![make 2](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/wiki-from-discord/make2.jpeg){ width=40% }
![make 3](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/wiki-from-discord/make3.jpeg){ width=40% }
![make 4](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/wiki-from-discord/make4.jpeg){ width=40% }
</figure>
