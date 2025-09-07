---
template: i18n/zh/main.html
description: 在这里开始你的 ELRS 历程! 这是让你用 ELRS 飞起来的最全面的指南
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

!!! attention "Working In Progress"
    中文翻译工作正在进行，部分内容尚未完成

!!! warning "注意!"
    ELRS 团队与制造商紧密合作，负责审核和测试硬件。只有在测试通过后，才会为特定硬件添加 ELRS 地面站目标。

    如果在 ELRS 地面站中找不到某个硬件，说明该硬件未通过要求，或者制造商选择不合作。在这种情况下，请联系制造商获取技术支持。

    通用目标仅适用于预生产或 DIY 硬件。现成的硬件应使用专用的硬件目标。

    省流: 想支持开源就买在 ELRS 地面站里有的硬件

## 快速入门指南

### 前置条件

你需要熟悉你的遥控器系统(OpenTX/EdgeTX)以及模型设置，因为此指南主要涵盖如何设置你的遥控器以使用ELRS
    
此外,你还需要熟悉飞控固件(Betaflight、INAV等)调参, 此指南只说明如何将 ELRS 接收机正确连接到飞控

### 我应该先做什么？

你已经有了相关的 ELRS 硬件，无论是内置 ELRS 的新遥控器，还是一个外置的ELRS高频头又或者是到手飞套装，你该从哪里开始？

我们的建议如下：

=== "发射端"
    1. [设置遥控器](transmitters/tx-prep.md)
    2. [检查高频头固件版本](transmitters/firmware-version.md)
    3. [更新高频头固件](transmitters/updating.md)

=== "接收端"
    1. [接收机接线](receivers/wiring-up.md)
    2. [配置飞控](receivers/configuring-fc.md)
    3. [检查接收机版本](receivers/firmware-version.md)
    4. [更新接收机固件](receivers/updating.md)

完成以上操作了之后，你可以继续以下步骤:

- [对频](binding.md)
- [性能测试](pre-1stflight.md#性能测试)
- [首飞之前](pre-1stflight.md)
- 起飞!

### 如何使用或浏览本指南

![指南结构](../assets/images/PageOrder.png){ align=right }

<br />
本用户指南旨在帮助新手和有经验的用户。左侧导航菜单从安装ELRS地面站开始，介绍可用选项、遥控器和高频头设置、飞控和接收机设置、“起飞前”页面以及故障排查页面。

<br clear="right" />

你也可以使用下方的页脚导航来依次浏览这些步骤：

<figure markdown>
![Footer Navigation](../assets/images/FooterNav.png)
</figure>

针对特定硬件的刷机指南，页面分别在“升级接收机”或“升级发射端”部分，按英文字母顺序排列。

<figure markdown>
![Menu Updating Receivers](../assets/images/menusectionUpdatingReceivers.png)
</figure>

<figure markdown>
![Menu Updating Transmitters](../assets/images/menusectionUpdatingTransmitters.png)
</figure>

你还可以使用搜索栏查找任何你需要的内容：

<figure markdown>
![Search Bar](../assets/images/SearchBar.png)
</figure>

较长的页面在右侧有 **目录**

![Search Bar](../assets/images/website-tabbed.png){ align=right }

<br />

每种设备的升级方法都可以通过点击对应的标签访问

<br clear="right">

我们希望这些页面能帮助你快速上手 ELRS ，体验业界最优秀、最具创新性的遥控链路之一。

如果你有其他问题或疑虑，或者需要本指南未涵盖的进一步帮助，请加入我们的 Discord 频道！

!!! warning "注意"
    国内无法访问 Discord

[ExpressLRS Discord :fontawesome-brands-discord:](https://discord.gg/dS6ReFY){ .md-button .md-button--primary .center-block }

## 哪里有视频教程？

由于开发进展非常快，视频教程往往很快就会过时。某些教程有时会使用预发布固件目标或用于不同硬件的目标，这可能会造成混淆，尤其是在特定固件目标添加后。

我们很快会添加一个单独的视频板块，但在此之前，除非找到高质量、相关且适用的教程，否则请自行查找。请注意这些视频的发布日期，以确保内容仍然适用。
