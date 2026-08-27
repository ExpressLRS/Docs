---
title: "Introducing ELRS Mobile"
date: 2026-03-21
categories:
  - Community Projects
authors:
  - wbhinton
slug: introducing-elrs-mobile
---

**Introducing ELRS Mobile** 

## **How It All Started**

When ExpressLRS 4.0 was released, I decided to upgrade my fleet to the new firmware. I fly both fixed wings and multirotors that are scattered throughout the basement. I tried to be methodical with the updates, bringing each aircraft to the workbench for upgrade using the ExpressLRS Configurator. I got the transmitters updated, planes updated and multirotors updated, or so I thought. I had several good flying sessions using 4.0. Then, about a week after the mass upgrade session, I got to my flying spot with a quad that had somehow been missed. It was still on 3.6.3. I didn’t have a laptop, and with no cell coverage, I couldn’t even attempt an OTA upgrade using the Web Flasher on my phone. I had to pack up and head home, totally losing a perfect flying day.

I decided there had to be a solution for situations like this, and I was wrong. I couldn’t find anything that allowed for completely offline flashing from a mobile device. I could use the WebFlasher and Configurator to flash while disconnected from the internet, but I would need a laptop and they weren’t really designed for that. 

I went down the rabbit hole looking at how the Web Flasher and Configurator worked. I needed to know how the firmware was accessed and assembled for each individual target. After getting a basic understanding of how things worked, I decided that the Web Flasher would be a good candidate to use as a basis for a Flutter App. 

The app would need to meet a few requirements:

1. Completely offline firmware caching and flashing  
2. Quick and easy connection to the ELRS device, both on WiFi mode and AP mode  
3. Saving the Binding Phrase and WiFi credentials between sessions to prevent needing to re-enter them after each flash.   
4. Have access to the device’s WebUI so changes could be made to the device configuration without reflashing. 

## **Building a Mobile-First Flasher**

Starting with these four requirements and my experience in Flutter, I set out to begin creating ELRS Mobile targeting iOS and Android devices. Using the Web Flasher as an example I was able to recreate the logic in Dart/Flutter giving rise to a cross-platform, mobile first tool that stores and assembles firmware completely offline. 

ELRS Mobile has the following capabilities:

* WiFi Flashing: Over-the-Air flashing for ELRS receivers and transmitters, whether connected to home WiFi or via the devices Access Point.   
* Offline Firmware Caching: You can download and store complete versions of ExpressLRS firmware for every hardware target. The app defaults to a 2 version limit, but you can up that limit if you need to.   
* Firmware Assembly: With the firmware and target information stored locally the app assembles the appropriate firmware, based on the target selected by the user, on your phone before flashing. You can even save the assembled firmware if you have a special use case.   
* Network Discovery: The app utilizes mDNS and other OS level networking services to automatically discover the ELRS device on your local wifi or in Access Point mode.   
* Device Configuration: You can access the WebUI for your ELRS Device directly from the app to make changes to the configuration without needing to flash new firmware. 

**Real-World Testing**

Since getting the first functional version working on my phone I have flashed and re-flashed dozens of receivers and transmitters making sure things work as expected. Through this process I have noticed a few things about flashing from the app and how it has affected my workflow. 

* Speed: Flashing from the app is surprisingly fast. Because the app's Firmware Manager permanently caches the generic firmware binaries and hardware targets directly on your phone's local storage, there is zero waiting around. The app just grabs the files already sitting on your phone, assembles the firmware, and pushes the update over Wi-Fi in seconds.  
* Convenience: Sometimes it's just easier to use your phone instead of booting up a laptop. Even when I'm at home, I find myself using the app for quick OTA updates at the workbench because I don't have to hunt down my laptop or load up the desktop configurator.  
* Connectivity Deserts: Where I live, cell coverage is spotty at best and non-existent in a lot of places. If you are in a dead zone, the web flasher doesn’t work because you can't download the payload. As long as you remember to sync the firmware to your local cache while you have a solid data connection, the app has everything it needs to assemble the binary and flash the hardware completely offline.

Since the initial public release on March 15th, 2026, ELRS Mobile has seen steady growth with over 500 installs in the first month. The reach is global, with users in 59 countries. This has definitely exceeded my expectations and am looking forward to the coming months. 

## **What’s Next**

ELRS Mobile isn’t a replacement for the desktop or web based flashing tools. It’s just another tool in your toolbox that adds a little more flexibility when working with ExpressLRS devices. It’s an independent, free and open sourced community project built by a pilot for pilots. Development is active and ongoing. I am working on improving the Device Configuration integrations and exploring translation options for the global user base. If you are interested in contributing to the project, please visit the [GitHub repository](https://github.com/wbhinton/ELRS-Mobile). The more involvement there is the better we can make the app. You can learn more about ELRS Mobile and how to use it by visiting the website at [elrsmobile.com](http://elrsmobile.com). If you just want to try the app, head over the [Google PlayStore](https://play.google.com/store/apps/details?id=io.datarx.elrsmobile) or [Apple App Store](https://apps.apple.com/us/app/elrs-mobile/id6760490014).

