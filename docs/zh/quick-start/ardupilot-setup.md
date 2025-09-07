---
template: i18n/zh/main.html
description: ELRS支持ArduPilot！本指南为你提供正确的ArduPilot参数设置。
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

## ArduPilot 串口设置

ArduPilot 固件必须为 4.1 或更高版本才能运行 CRSF 协议。
和所有串口接收机一样，你需要将接收机的 TX/RX 焊盘连接到飞控上的 UART，并在 ArduPilot 中为对应 UART 启用串口接收（Serial RX）。
在 Mission Planner 中，请进入 ```配置/调试 -> 全部参数表```，设置如下参数：
```
SERIALx_PROTOCOL = 23 (RCIN)
RSSI_TYPE = 3 (ReceiverProtocol)
```
ELRS的包速率与 ArduPilot 的 CRSF 包速率不同，ArduPilot 会持续报告速率不匹配，但最近已提供关闭该提示的选项。你可以通过如下参数关闭该通知（不会影响 RC 链路和遥测链路）：
```
在 RC_OPTIONS 中勾选"Suppress CRSF mode/rate message for ELRS systems".
```
建议开启 RC_OPTIONS 中的"Use 420kbaud for ELRS protocol"，这样会让飞控与接收机使用 420K 的波特率通信


<figure markdown>
![RC_Options Bitmask](../assets/images/ArduRCOPTIONS.png)
</figure>

设置好上述参数后，请断开并重新连接电池和 USB，重启飞控。ArduPilot 应自动识别 ELRS 接收机，如果未成功，请将打开 ``RC_PROTOCOL`` 中的 "CRSF" 选项，并设置如下参数：
```
SERIALx_PROTOCOL = 23 (RCIN)
SERIALx_BAUD = 115
RSSI_TYPE = 3 (ReceiverProtocol)
```

## ArduPilot 飞行模式通道

~~ArduPilot 默认飞行模式通道为通道 8，但 ELRS 的 8 位开关通道在混合开关模式下为通道 12。你需要将遥控器设置为通道 12 控制飞行模式，并设置 ArduPilot 参数：~~

~~FLTMODE_CH=12~~

~~如果你使用的是宽开关模式（仅 ELRS V2 及以上版本支持），可以用任意通道选择 8 个飞行模式（除通道 15 为 LQ，通道 16 为 RSSI）。~~

就 ELRS 当前版本(3.5.6)而言，可以使用16个通道中的任意一个通道控制飞行模式，前提是 Switch Mode 设置为 **Wide**

## ArduPilot 的 RSSI 和 Link Quality(LQ)
如需在 OSD 上显示 RSSI 和 LQ（百分比），请设置：
```
RSSI_TYPE = 3 (ReceiverProtocol)
```

然后进入 OSD 选项卡，将 RSSI 和 LQ 元素放置在你想要的位置。

如果你感觉控制有延迟或卡顿，请检查接收机与飞控的连接。
部分飞控还需要使用支持 DMA 的 UART

祝你飞行愉快！ :airplane:
