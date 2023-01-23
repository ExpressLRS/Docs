---
template: main.html
description: This will guide you on how to select the best ExpressLRS (ELRS) radio for your needs
---

![HW Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/hardware.png)

ExpressLRS is hashtag blessed with the benefit of there being many receivers available from a variety of manufacturers. This begs the question "Which receiver is best?" There is no best receiver, there is only one that has the features you want for the price you want to pay in the size you want it. ExpressLRS does not recommend a specific brand or model, but provide the information to help you select the right receiver for your needs. The following page will list manufacturers and features to look out for on their receivers.

!!! note Note
    This list will list primarily 2.4GHz hardware with 900MHz only listed in the frequency category, as 2.4GHz has become a significantly larger portion of the ELRS market.

## Manufacturers:
  * [Axisflying](https://www.axisflying.com)
  * [BetaFPV](https://betafpv.com)
  * [Emax](https://emaxmodel.com)
  * [Foxeer](https://www.foxeer.com)
  * [FrSky](https://www.frsky-rc.com)
  * [GEPRC](https://geprc.com)
  * [Happymodel](https://www.happymodel.cn)
  * [HGLRC](https://www.hglrc.com)
  * [iFlightRC](https://www.iflight-rc.com)
  * [Jumper](https://www.jumper-rc.com)
  * [MatekSys](http://www.mateksys.com)
  * [NamimnoRC](https://m.facebook.com/profile.php?id=100070062095159&_rdr)
  * [RadioMasterRC](https://www.radiomasterrc.com)
  * [Skystars](https://skystars-rc.com)
  * [Vantac](https://www.frsky-rc.com)
## Receiver Selection
This section exists to list out some common features of receivers and will give some examples of receivers with these features.

Each build is different, but these are reccomended things to look for when selecting a receiver:

  * **Whoops / Toothpicks / Light aircraft:** Size is probably the most important feature, with a light small receiver and an onboard antenna being the best choice.
  * **Racing Quads:** Size is again most important. Ceramic antennas could be less easily damaged, and the reduced range of tucking them inside the frame is fine due to the short flight range. An external 2.4GHz antenna dipole is still pretty easy to fit and can be tucked away for a small improvement over the ceramic, but comes with Chance of Choppage.
  * **Freestyle Quads:** Minimum size is no longer an issue so Nano-sized receivers are the best bet here. A LNA is going to give you better reception behind obstacles. External antennas are a benefit as well, but you need to trade off how unobstructed the antenna will be versus getting it chopped. Diversity is of marginal benefit.
  * **Long Range:** For sure you need an LNA, an external antenna, and a PA to extend the telemetry range. This isn't to say these are required for long range, 5km is achievable on a ceramic antenna receiver with no LNA/PA at 250Hz/100mW with a clear line of sight. Diversity is worth a lot more here. For planes without a flight controller, PWM recievers will work great. For absolute maximum range 900MHz can do more but 2.4GHz can still do 50+km.

??? info "Frequency"

    ExpressLRS offers both 2.4GHz and 900MHz systems, with each only working with receivers and transmitters of the same frequency. 2.4GHz is the currently most popular frequency given it's legality, featureset and cost. 2.4GHz links offer the fastest packet rates allowing for a more locked in feel while piloting and still offer massive amounts of range. 900MHz is the original long range frequency and still can be great for high wifi pollution environments with slightly better penetration.

    For new users unless you plan on flying hundreds of kilometers or in a high noise environment we reccomend 2.4GHz hardware:

      * Happymodel EP Series
      * Radiomaster RP Series
      * NamimnoRC Flash Series

    If you have an R9 system or similar or plan on flying beyond reasonable ranges, some great 900MHz receivers include:

      * BetaFPV Nano900
      * Happymodel ES900RX
      * GEPRC Nano 900MHz

??? info "Antenna Type"

    Antennas are where the radio waves come and go from the receiver. ExpressLRS offers many different antenna types, with dipoles and ceramic antennas (see [SMD Antennas](../hardware/smd-antenna.md)) being the most common types of reciever antennas. In terms of range: Ceramic antenna < Mini Dipole ("Minimortal-T" style) < sleeved dipole < Half-wave Dipole. A diagram of the antennas and their sizes for the 2.4GHz band is shown below:

    <figure>
      <img class="center-img" src="../../assets/images/hw-selection/antennas.png"/>
    </figure>

    Unless otherwise noted, most recievers will have a U.FL/IPEX connecter which supports external antennas. Some recievers with ceramic antennas are:

      * Happymodel EP2 
      * Radiomaster RP2
      * MatekSys R24-S

??? info "Diversity"

    Diversity improves reception compared to standard receivers by using multiple antennas. A standard receiver has a single antenna, while antenna diversity uses two antennas and a switch to route the signal from one or the other. True diversity takes it a step further by using two radio chips, each connected to a different antenna, and choosing the one with the strongest reception at any given time. This provides a level of redundancy which is particularly beneficial for flight where the antenna nulls can point towards the pilot (e.g. freestyle flight)

    <figure>
      <img class="center-img" src="../../assets/images/hw-selection/diversity.png"/>
    </figure>

    Some recievers with antenna diversity include:
      
      * Radiomaster RP3
      * Namimno Flash Diversity
      * Matek R24-D

    Some recievers with true diversity include:

      * Happymodel EP1 Dual
      * BetaFPV SuperD

??? info "PWM"

    PWM is used for crafts that do not have flight controllers and allow for direct control of ESCs and Servos. See the page on [PWM](../hardware/pwm-receivers.md) for more in-depth information on using PWM.

    Some PWM recievers include:

      * MatekSys R24-P6
      * Happymodel EPW6
      * Radiomaster ER5A/C

??? info "PA/LNA"

    A Low Noise Amplifier directly adds to your incoming RSSI. Typical gains are in the ballpark of +12dBm which will be observed in the RSSI as being 12dBm higher than it would have been without the LNA. This is because the LNA amplifies the incoming signal coming from the antenna before going to the RF chip, which increases the sensitivity of the receiver by boosting the incoming signal. An LNA also boosts the noise by the same amount so the sensitivity limit will likely be higher than the value quoted by the Lua.

    A Power Amplifier boosts the outgoing signal strength and extends the telemetry range back to the TX. Without a PA, the power output is limited by the RF chip's max power output itself (around +13dBm 20mW). It works the same way as turning up the power output on the transmitter module, however it is not adjustable. The receiver's output is always run at max power, since it runs a much lower duty cycle than the transmitter does (duty cycle = telemetry ratio). Higher numbers are better. Most PAs are 20dBm/100mW, with some being up to 23dBm.

    Recievers with a PA/LNA will have a listed telemetry output power in dBm or mW

    Some recievers with a PA & LNA are the following:
    
      * Radiomaster RP3 (100mW)
      * Skystars Nano SS24D (20dBm)
      * MatekSys R24-D (23dBm)
      * BetaFPV SuperD (20dBm)

??? info "Size"

    The FPV world shook when ELRS released receivers that were half the size of "nano" sized receivers, included the antenna onboard, and still had kilometers of range at 250Hz/100mW. A small receiver can fit in tight places, but remember that tucking a tiny receiver's ceramic antenna deep inside a stack behind carbon reduces its performance, which was already compromised by the elimination of amplifiers to make it that small. Larger ELRS recievers regain these amplifiers offering better reception and telemetry range at the cost of size and weight. The common size classes are shown below, but there are other recievers with slightly different sizes:

    <figure>
      <img class="center-img" src="../../assets/images/hw-selection/sizes.png"/>
    </figure>

    PP Sized Recievers (absolute smallest, lowest range regardless of antennas):

      * Happymodel EP/PP
      * Radiomaster RP
      * BetaFPV Lite

    Nano Sized Recievers (medium sized, can have PA/LNA but tends to lack some features):

      * BetaFPV Nano
      * iFlight RXes
      * Namimno Flash Diversity RX
      * Axisflying Thor RX
      * Namimno Flash RX

    Larger Recievers (most feature rich but also significantly larger)

      * Matek R24-D
      * Radiomaster RP3
      * BetaFPV SuperD
