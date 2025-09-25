---
template: i18n/zh/main.html
description: ExpressLRS 接收机和发射端模块上的 LED 是非常有用的诊断工具，可以帮助你判断设备当前状态。
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

## 接收机/发射端 LED 状态

ExpressLRS 使用 LED 指示发射端和接收机的工作状态。

不同状态下的 LED 指示如下：

=== "接收机单色 LED"
    |                                                                                         | LED 指示                      | 状态说明                                                         |
    |-----------------------------------------------------------------------------------------|-------------------------------|-------------------------------------------------------------------|
    | ![CONNECTED](../assets/images/LED_ON.gif)                                               | 常亮                          | 已连接到发射端，或处于 Bootloader 模式                            |
    | ![LEDSEQ_BINDING](../assets/images/LEDSEQ_BINDING_10_10_10_100.gif)                     | 快速双闪后暂停                | 进入对频模式                                                      |
    | ![LEDSEQ_DISCONNECTED](../assets/images/LEDSEQ_DISCONNECTED_50_50.gif)                  |  慢闪(500ms)              | 等待与发射端连接                                                  |
    | ![LEDSEQ_MODEL_MISMATCH](../assets/images/LEDSEQ_MODEL_MISMATCH_10_10_10_10_10_100.gif) | 三次快闪后暂停                  | 已连接发射端但模型匹配参数不一致                                  |
    | ![LEDSEQ_RADIO_FAILED](../assets/images/LEDSEQ_RADIO_FAILED_20_100.gif)                 | 闪烁(100ms)                  | 无法检测到射频芯片                                                |
    | ![LEDSEQ_WIFI_UPDATE](../assets/images/LEDSEQ_WIFI_UPDATE_2_3.gif)                      | 快闪(25ms)              | 进入 WiFi 模式                                                    |

=== "接收机 RGB LED"
    |                                                                                     | LED 指示                      | 状态说明                                                         |
    |-------------------------------------------------------------------------------------|-------------------------------|-------------------------------------------------------------------|
    | ![LEDRGB_STARTUP](../assets/images/LEDSEQRGB_STARTUP.gif)                           | 彩虹渐变效果                  | 启动中                                                            |
    | ![LEDRGB_WIFI_UPDATE](../assets/images/LEDSEQRGB_WIFI_UPDATE.gif)                   | 绿色闪烁                      | 进入 Web 更新模式                                                 |
    | ![LEDRGB_WAITING_FOR_CONNECTION](../assets/images/LEDSEQRGB_WAITING_TO_CONNECT.gif) | 橙色慢闪(500ms)              | 等待与发射端连接                                                  |
    | ![LEDRGB_RADIO_FAILED](../assets/images/LEDSEQRGB_RADIO_FAILED.gif)                 | 红色闪烁(100ms)            | 无法检测到射频芯片                                                |
    | ![LEDRGB_BINDING_ENABLED](../assets/images/LEDSEQRGB_BINDING.gif)                   | 橙色双闪后暂停                | 进入对频模式                                                      |
    | ![LEDRGB_MODEL_MISMATCH](../assets/images/LEDSEQRGB_MODEL_MISMATCH.gif)             | 橙色三闪后暂停                | 已连接发射端但模型匹配参数不一致                                  |
    | ![LEDRGB_CONNECTED](../assets/images/LED_RGB_ON.png)                                | 单色常亮                      | 已连接到发射端，颜色表示包速率                                    |
    | ![BOOTLOADER_OR_OFF](../assets/images/LED_RGB_OFF.png)                              | 熄灭                          | 关闭或处于 Bootloader 模式                                        |

    | LED 颜色      | 2.4GHz 包速率 (Hz) | 915/868MHz 包速率 (Hz) |
    |---------------|--------------------|------------------------|
    | 红色          | F1000              | 200                    |
    | 黄色          | F500               |                        |
    | 黄绿色        | D500               | 100 Full               |
    | 绿色          | D250               | 100                    |
    | 青色          | 333 Full           |                        |
    | 浅蓝色        | 500                | 50                     |
    | 蓝色          | 250                | 25                     |
    | 蓝紫色        | 150                |                        |
    | 紫色          | 100 Full           | D50                    |
    | 品红色        | 50                 |                        |
    
=== "发射端 RGB LED"
    | LED 指示                      | 状态说明                                                     |
    |-------------------------------|--------------------------------------------------------------|
    | 彩虹渐变效果                  | 启动中                                                        |
    | 绿色闪烁                      | 进入 Web 更新模式                                             |
    | 蓝色闪烁                      | 启用蓝牙摇杆                                                  |
    | 红色闪烁(100ms)          | 无法检测到射频芯片                                            |
    | 橙色(1000ms)              | 未连接遥控器                                                  |
    | 单色常亮                      | 已连接接收机，颜色表示包速率                                  |
    | 单色渐变                      | 未连接接收机，颜色表示包速率                                  |

    | LED 颜色      | 2.4GHz 包速率 (Hz) | 915/868MHz 包速率 (Hz) |
    |---------------|--------------------|------------------------|
    | 红色          | F1000              | 200                    |
    | 黄色          | F500               |                        |
    | 黄绿色        | D500               | 100 Full               |
    | 绿色          | D250               | 100                    |
    | 青色          | 333 Full           |                        |
    | 浅蓝色        | 500                | 50                     |
    | 蓝色          | 250                | 25                     |
    | 蓝紫色        | 150                |                        |
    | 紫色          | 100 Full           | D50                    |
    | 品红色        | 50                 |                        |