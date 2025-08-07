---
template: i18n/zh/main.html
description: 按照你的需求设置 ELRS 设备！通过固件选项自定义你的接收机和高频头。
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

本页仅介绍你在 ELRS 地面站中初次设置时可能需要的关键选项。关于**所有**可用选项的完整说明，请参阅[用户自定义选项页面](../software/user-defines.md)。

部分选项在高频头和接收端目标中都存在。为了能够正常对频，这些选项必须在发射模块和接收机上保持一致。`team2400`和`team900`也有一些共享选项，同时也有各自频段独有的选项。下方展示了`team2400`和`team900`发射端常见的选项。

<figure markdown>
![2400 TX Options](../assets/images/ConfigurationOptions2400tx.png)
</figure>

<figure markdown>
![900 TX Options](../assets/images/ConfigurationOptions900tx.png)
</figure>

## 无线通信监管域
```
Regulatory_Domain_AU_915
Regulatory_Domain_EU_868
Regulatory_Domain_IN_866
Regulatory_Domain_FCC_915

Regulatory_Domain_ISM_2400
Regulatory_Domain_EU_CE_2400
```
这个选项很简单——根据你所在地区选择对应的法规区域，以确定使用的频率范围。

欧盟法规区域现在已符合 LBT(Listen Before Talk) 要求！

## 对频短语

设置对频短语可以让你跳过传统的对频步骤——强烈建议设置。任何使用相同对频短语的发射端都能连接到使用相同短语的接收机，所以请确保短语具有唯一性。仅限使用英文字母和数字。未启用对频短语的固件需要使用传统的[对频方法](binding.md)。

## 网络选项

```
HOME_WIFI_SSID
HOME_WIFI_PASSWORD
```
设置这两个参数后，“WiFi升级”模式会尝试使用这些信息连接到已有的WiFi网络。建议配置为你刷写固件时所在环境的 WiFi，以免在刷写过程中需要切换电脑或手机的 WiFi。如果设备无法连接该网络，会自动创建自己的热点。
密码默认是`expresslrs`，即 ELRS 的全称

## 其他选项

```
UNLOCK_HIGHER_POWER 
```
为支持的设备启用更高的输出功率，但可能会导致设备过热甚至损坏。启用前请确保设备有足够的散热或已验证不会过热。

```
UART_INVERTED
```
~~仅适用于ESP32发射端。**绝大多数遥控器**都需要开启`UART_INVERTED`，如FrSky QX7、TBS Tango 2、RadioMaster TX16S。T8SG V2或Deviation固件则需关闭此选项。~~
目前**大部分开源遥控器**不需要开启这个功能，若无法使用，请开启此功能

## 接收机专用选项

<figure markdown>
![2400 RX Options](../assets/images/ConfigurationOptions2400rx.png)
</figure>

<figure markdown>
![900 RX Options](../assets/images/ConfigurationOptions900rx.png)
</figure>

!!! attention "注意"
    接收机的配置应与高频头保持一致，才能实现同步和对频。


高频头的大部分选项同样适用于接收机。以下是接收机特有的选项：

### 输出反转

```
RCVR_INVERT_TX
```
如果你的飞控**只有** SBUS/RXI（RX inverted，RX 反转）焊盘，请开启此选项，将接收机的 CRSF 输出反转，以便使用该焊盘。此选项不会将输出转换为 SBUS 协议，仍需在飞控软件中选择CRSF协议。仅适用于 ESP 系列接收机。


```
USE_R9MM_R9MINI_SBUS
```
仅适用于 R9MM/R9Mini，此选项会将接收机的 CRSF 输出从侧边的 A9 和 A10 引脚切换到标有“SBUS”的引脚（反转）。同样不会转换为 SBUS 协议，飞控协议仍需选择 CRSF


**相当于反转的CRSF协议，可以接到飞控的SBUS焊盘**

## 这些选项要不要开启？

```
NO_SYNC_ON_ARM
```
在解锁（ARM）状态下，同步包每5秒发送一次。除非关闭遥测，否则建议保持此选项关闭，否则解锁后失控时无法重新连接。

```
LOCK_ON_FIRST_CONNECTION
```
失控时保持接收机在最后一次连接的包速率，不会尝试所有包速率重新连接。建议保持此选项开启。

## F完整选项列表

完整的用户自定义选项请参阅[用户自定义选项页面](../software/user-defines.md)。

**全部设置完成！现在可以为你的高频头刷写固件了。**
