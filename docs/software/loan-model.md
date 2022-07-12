---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

## Loan Model

!!! note "Scenario"
    You are flying with by buddies and your friend has crashed all his models. You'd like to be able to lend him one of yours but you
    can't because it's using a binding phrase, so he's relegated to being the crached model fetcher for the rest of the day!

No longer is he destined to be running to the bando and back again fetching downed quads. You can use the "Loan Model" feature and lend him one of your models!

## How to "Loan Model"

### On the lenders handset

1. Connect to the model you wish to loan out with your handset
2. Enter the LUA screen and select "Other Devices" at the bottom of the list

    ![Other Devices](../assets/images/loan-other-devices.png)

3. Choose the RX from the list

    ![Select RX](../assets/images/loan-rx-select.png)

4. Select the "Loan Model" entry

    ![Loan Model](../assets/images/loan-rx-menu.png)

5. The receiver LED should go into the bind flashing state

    ![LEDSEQ_BINDING](https://cdn.discordapp.com/attachments/738450139693449258/921065812763218010/LEDSEQ_BINDING_10_10_10_100.gif)

### On the borrowers handset
1. From the main ExpressLRS LUA screen select `[Bind]`
2. The receiver LED should turn solid on, and the handset should connect to the recevier
    ![CONNECTED](https://cdn.discordapp.com/attachments/738450139693449258/921065812507373568/LED_ON.gif)

## Returning a "Loaned" Model

There are a couple of ways to return a model to the owner. The first (and simplest) is for the borrower to return it from the LUA script as follows:

1. On the borrowers handset, connect to the "loaned" model
2. Enter the LUA screen and select "Other Devices" at the bottom of the list

    ![Other Devices](../assets/images/loan-other-devices.png)

3. Choose the RX from the list

    ![Select RX](../assets/images/loan-rx-select.png)

4. Select the "Loan Model" entry

    ![Return Model](../assets/images/loan-return.png)

The second, is to power on/off the model 3 times in quick succession. When you power the model, the LED on the RX will flash once,
then remain off for 2 seconds then start is normal flashing. You must power off the RX in the period where the LED is off.

This method is generally only used if the borrower "forgot" to return the model at the end of the session.

## Bump to Loan

On transmitter modules with an acceleromter you can loan a model holding the transmitter in the vertical position while conencted to the model,
but not armed and bump you transmitter with the borrowers transmitter, and the loan command is automatically executed.

If the borrower also has a transmitter module equipped with an accelerometer, his module will automatically send the bind command.

"Bump to Loan" also works in reverse, i.e. returning a model.