---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/quick-start.png)

Binding can be done with either a hard coded unique binding phrase or in a more traditional way where you put the receiver and transmitter into bind mode, and they link up. There is no reason to use traditional binding if you're flashing both your TX and RX firmware anyway. If you used a bind phrase in your user defines, there is no need to read this article. Proceed to the [next section](/quick-start/pre-1stflight). If not, here is how to bind an ELRS TX and RX.

## Unique Phrase

You need to have a **unique** binding phrase in the [`user_defines.txt`](https://github.com/ExpressLRS/ExpressLRS/wiki/User-Defines#binding-phrase) file or entered in the "Custom Binding Phrase" box in the Configurator.  After flashing your TX and RX, they will bind automatically. [Is my binding phrase a secret?](https://github.com/ExpressLRS/ExpressLRS/wiki/FAQ#is-my-binding-phrase-a-secret)

```
-DMY_BINDING_PHRASE="default ExpressLRS binding phrase"
```

## Traditional Binding

For traditional binding, the binding phrase must be commented out in user_defines on the RX.

1. Power off your transmitter
2. Plug in and unplug your receiver three times
3. Make sure the LED is doing a quick double blink, which indicates the receiver is in bind mode
4. Use the [BIND] button on the Lua script, which sends out a binding pulse
5. If the receiver has a solid light, it's bound!

Important: If the RX firmware has a bind phrase, the RX will never enter binding mode using the above procedure. It must be flashed without a binding phrase to do traditional binding. Why would you not use a bind phrase though if you're already having to flash the RX anyway? :grin:

## Connection Check

Go to the `Telemetry Page` of your model setup and try to find new sensors. If the telemetry data shows up then you are connected!
