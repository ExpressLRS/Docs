---
template: i18n/zh/main.html
description: 什么是性能测试？如何设置 Aux1 解锁？OSD 上的 RSSI dBm 和链路质量怎么显示？ExpressLRS 遥测怎么配置？你来对地方了！
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

在你第一次使用 ExpressLRS 飞行前，建议对设备进行一些调整，以确保飞行顺利愉快！

## 模式

默认情况下，ExpressLRS 对 AUX 开关采用有限位数（AUX1 用 1 位，其他 AUX 通道用 3-4 位），这会导致 AUX 通道在 Betaflight/INAV 上只有 8 或 16 档分辨率。大多数情况下已经足够（尤其是多旋翼），但如果你需要更高分辨率，可以启用 **Wide** Switch Mode 选项，将 AUX2-AUX8 的分辨率扩展到 128 档。详情请参考 [开关模式页面](../software/switch-config.md)。

需要注意的是，Aux1 应作为你的解锁（ARM）开关，低电平（约 1000us）为未解锁，高电平（约 2000us）为已解锁。AUX1 是低延迟开关，每个包都会发送，只支持开/关（两档）操作。ExpressLRS 用 AUX1 判断模型是否解锁，这是最可靠的解锁方式。如果你把解锁开关设在其他 AUX 通道，可能要等几个包才会发送，没有保证接收机能及时收到。

!!! warning "警告"
    请确保你的 **ARM 模式在 AUX1 通道，且已解锁状态为 ~2000。**

<figure markdown>
![Modes](../assets/images/Modes.jpg)
</figure>

## RSSI 和链路质量

要在 OSD 上显示 RSSI 和链路质量，请将 **RSSI Channel** 和 **RSSI_ADC** 都设置为 {==Disabled==}，这两个设置在接收机标签页。

<figure markdown>
![Conf Tab](../assets/images/ConfigurationTab.png)
</figure>

<figure markdown>
![INAV Config](../assets/images/FC-rxconfig-INAV.png)
</figure>

在 OSD 标签页，使用 **Link Quality** 和 **RSSI dBm value** 元素（不要用 "RSSI Value"）。INAV 在 `CRSF RX Statistics` 区域显示这些内容。

<figure markdown>
![OSD](../assets/images/OSD.jpg)
</figure>

如果你想启用 RSSI dBm 警告，需要在 CLI 用 `set osd_rssi_dbm_alarm = -100` 修改报警阈值。合理的数值是比 ELRS.lua 显示的包速率灵敏度高 5-10（比如 250Hz=-108，则报警设为 -103 到 -98）。

同样，如果你想修改 LQ 报警阈值，可以用 CLI 命令 `set osd_link_quality_alarm = x`，`x` 为你的报警阈值。`60` 是一个不错的起点。

如果你用的是 DJI V1 或 V2（未 root），只能用 "RSSI Value" 作为 OSD 元素，所以你需要在接收机标签页选择 AUX11（LQ）或 AUX12（RSSI）作为 RSSI Channel（见上图）。

对于支持 "Canvas Mode" 或 MSP DisplayPort 的数字图传（Walksnail Avatar、HDZero、DJI O3），配置方式与模拟 FPV 一样，无需设置 RSSI Channel（保持禁用）。

更多信号指标信息请参考这篇[信号健康文章](../info/signal-health.md)。

## 性能测试

<figure markdown>
![ExpressLRS Bench Test](../assets/images/BenchTest.jpg)
<figcaption>ExpressLRS 性能测试</figcaption>
</figure>

上图是性能测试，用于判断你的遥控信号是否正常。这可以帮助你检查天线（尤其是 R9 的 Super 8）或硬件是否有问题。

- 用 Lua 脚本将 ExpressLRS 模块设为最低功率，包速率无所谓。
- 遥控器距离接收机 1 米（3 英尺），通电。确保接收机和 TX 模块天线方向一致。（建议暂时断开 VTX/图传，或让 VTX 进入 pit 模式，或用风扇吹散热）。
- 用 OSD 或遥控器的 Telemetry 页面，记录 RSSI dBm 或 1RSS 遥测数据。

900MHz 硬件，-20dBm 左右说明硬件正常；2.4GHz 硬件，-40dBm 到 -25dBm 都可以。如果数值比这些低（越接近 0 越好），可以检查：

- ExpressLRS 模块天线是否松动。有些 3D 打印模块壳体太厚，RP-SMA/SMA 接头拧不紧，建议拧紧螺母。
- 天线尾线是否损坏或未正确连接主板。
- 用 SMD 天线的接收机，数值会比线天线低。如果热缩管包裹、装在 whoop 机罩、碳板包围或埋在机身里，信号会进一步衰减。
- FrSky 的 Super 8 天线（大多数 R9M 标配）容易损坏或用几周就性能下降。建议更换，或临时修复可在同轴线屏蔽层和 RP-SMA 连接处全焊一圈。另一故障点是同轴线与天线主动元件的连接，天线扭动可能导致断开。

<figure markdown>
![NotSuper8](../assets/images/super8notsuper.jpg)
</figure>

<figure markdown>
![NotSuper8 for sure](../assets/images/super8notsuper2.jpg)
<figcaption>Super8 天线常见故障点</figcaption>
</figure>

- 检查接收机是否有缺失元件，比如 RF 滤波器（在天线或 UFL 附近），也要检查 SMD 天线是否损坏或焊接良好。

<figure markdown>
![missing filter](../assets/images/missingfilter.png)
</figure>

- 大多数 DIY 模块需要把 E28 上的 0 欧姆电阻从 PCB 天线侧移到 UFL 侧。也可以用焊桥，但要确保焊在正确的焊盘上。
- 换接收机或 TX 模块的天线；大多数 ExpressLRS 接收机用 IPEX 1/UFL 接头，只要天线频率合适就能用。2.4GHz 模块可以用旧 WiFi 路由器天线，但不要用双频天线。注意天线接头类型（R9 模块用 RP-SMA，大多数 ExpressLRS 模块用 SMA）。

## Blackbox

Blackbox 可以用来评估飞行时射频链路性能。将 BB 设置为 debug 模式 `RC_SMOOTHING_RATE`，可记录 Betaflight 从接收机收到 RC 包的速率。

## 遥测

接收机会转发飞控发来的部分遥测数据。禁用某些消息只在飞控固件支持时有效。Betaflight 可用如下 CLI 设置禁用遥测项：

```
# 禁用姿态遥测
set telemetry_disabled_pitch = ON
set telemetry_disabled_roll = ON
set telemetry_disabled_heading = ON
# 禁用电池遥测
set telemetry_disabled_voltage = ON
set telemetry_disabled_current = ON
set telemetry_disabled_fuel = ON
# 禁用 GPS 遥测
set telemetry_disabled_altitude = ON
set telemetry_disabled_lat_long = ON
set telemetry_disabled_ground_speed = ON
set telemetry_disabled_heading = ON
# 禁用飞行模式遥测（BF >4.2.9）
set telemetry_disabled_mode = ON 
```

由于遥测消息优先级低，传输数据可能需要一些时间。Lua 设置脚本中的遥测比率控制消息发送频率。比如 1:2 表示每两条消息发一条遥测，数据传输很快；1:64 表示每 64 条消息发一条遥测，传输很慢。

刷新率也影响传输速度。50Hz 比 200Hz 慢。如果需要快速遥测更新，选择高刷新率和较高遥测比率，比如 200Hz 和 1:16 通常效果不错。不同速率和比率下的遥测带宽详见[遥测带宽页面](../info/telem-bandwidth.md)。

完成遥测设置后，打开遥控器的遥测页面，选择 "Discover new sensors"，等待列表填满。

!!! hint "* 星号指示"
    每行有一个 * 星号，表示该遥测传感器刚刚更新。

!!! hint "[ ] 方括号指示"
    如果某行不变且名称为方括号，说明该传感器长时间未更新。

RSSI 和链路质量等首行数值应始终更新（星号闪烁）。如果每秒没有多次更新，遥控器会发出 "telemetry warning"。为避免警告，可用 TLM_REPORT_INTERVAL_MS 设置。

效果如下（如果不是这样，说明设置有问题）：

<figure markdown>
![Link data update speed](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/wiki-from-discord/link.gif)
</figure>

其他数值更新频率不同（取决于刷新率和遥测比率）。比如 50Hz 和 1:64 时更新很慢，每个传感器要几秒：

<figure markdown>
![Slow update rate](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/wiki-from-discord/slow.gif)
</figure>

如果用 200Hz 和 1:2 遥测比率，星号几乎不闪，因为更新太快：

<figure markdown>
![Fast update rate](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/wiki-from-discord/fast.gif)
</figure>

## MSP

可用 Betaflight lua 脚本从遥控器配置 Betaflight。
需要 RX+TX 支持遥测功能。如果 OpenTX 遥测页面没有所有传感器的定期更新，LUA 脚本也无法正常工作。

为获得响应式 UI，ExpressLRS 应配置为高速数据传输，比如 `200Hz/500Hz` 配合 `1:2` Tlm 比率和 `400000` 串口波特率。当前 MSP 限制为 `50Hz`、`115200` 波特率，不能用 `500Hz` 刷新率。VTX 表首次下载较慢，但会缓存。

如果保存设置时出现 "retrying" 提示，说明 Lua 脚本未及时收到响应，但通常设置已生效，刷新页面即可。推荐设置下不会出现此问题，慢速设置可能会出现。

## MAVLINK

详见 [Airport](../software/airport.md)。

**全部完成，可以起飞了！**