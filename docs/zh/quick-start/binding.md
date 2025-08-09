---
template: i18n/zh/main.html
description: 对频 ELRS 接收机是很简单的事情~!~如果设置了对频短语，甚至连按钮都不需要按！如果你想按按钮，也可以手动对频
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/quick-start.png)

省流：快速插拔3下接收机进入对频模式，遥控器 ELRS Lua 选择 `[Bind]` 选项对频

## 兼容性检查

高频头和接收机的固件版本号的第一个数字必须一致。
    
例如：

- 高频头固件版本为 3.1.2，可以与固件版本为 3.0.1 的接收机对频
- 高频头固件版本为 3.2.0，**不能**与固件版本为 2.4.0 的接收机对频
- 接收机固件版本为 3.1.2，可以与固件版本为 3.0.1 的高频头对频
- 接收机固件版本为 3.2.0，**不能**与固件版本为 2.4.0 的高频头对频
- SPI 接收机在（官方）Betaflight 4.3.1 及更早版本只能与 ExpressLRS 2.x 固件对频
- SPI 接收机在 Betaflight 4.4.0 及更新版本只能与 ExpressLRS 3.x 固件对频

如果你的固件版本不兼容，下面的所有方法都无法对频。

如何检查你的 ELRS 设备固件版本，请参阅：

- [高频头](../quick-start/transmitters/firmware-version.md)
- [接收机](../quick-start/receivers/firmware-version.md)
- [SPI 接收机](../hardware/spi-receivers.md)


## 怎么对频？

有**两种**方法可以对频：

1. [使用对频短语](#使用对频短语)
2. [传统对频方法](#传统对频方法)

如果你本来就要更新或刷写 ELRS 固件，建议直接使用对频短语。

自 ELRS v3.0 起，可以通过 WebUI 更新对频短语，更推荐使用对频短语。

以下是 ELRS 的不同对频流程。

## 使用对频短语
你可以在刷写或更新固件前，在 [ELRS 地面站](installing-configurator.md) 的对频短语字段中输入一个简短且独特的对频短语。

<figure markdown>
![Binding Phrase Field](../assets/images/bindingphrase-textfield.png)
<figcaption>对频短语输入框</figcaption>
</figure>

如果你的设备支持 WiFi，并且已升级到 ExpressLRS 3.0 或更高版本，也可以通过 WebUI 更改对频短语。详见[WebUI 用户指南](webui.md)。

<figure markdown>
![Binding Phrase Field WebUI](../assets/images/bindingphrase-webui.png)
<figcaption>WebUI 中的对频短语输入框</figcaption>
</figure>

建议使用至少 8 位字母和数字组成的**唯一**短语。推荐用你的飞手昵称。这个短语不需要复杂或保密，因为它不是密码或加密密钥。

??? info "我的对频短语需要保密吗？（点击展开）"
    不需要，就像你的图传频道不是秘密一样。对频短语不是安全用途，而是防止干扰。如果大家都用一样的短语，互相干扰的概率就很高。请确保你的短语独特，避免与他人重复，也可以发挥创意，设置有趣的短语。

## 传统对频方法

传统对频要求接收机未设置对频短语。

!!! info "3.4.0 更新"
    任何刷写了 3.4.0 或更高版本的接收机，即使设置了对频短语，也可以进入对频模式。

!!! warning "注意"
    如果接收机已设置对频短语，将无法进入手动对频模式，无论你尝试多少次。必须先重新刷写并取消设置对频短语。既然都要刷固件了，建议直接用对频短语 :grin:

接收机上电后，LED 应该会闪烁。

<figure markdown>
![LEDSEQ_DISCONNECTED](../assets/images/LEDSEQ_DISCONNECTED_50_50.gif)
</figure>

??? danger "接收机 LED 不闪烁（点击展开）"
    如果接收机进入 Bootloader 模式，可以尝试以下方法：

    1. 检查接收机上的 Boot 按钮是否被按下或损坏。
        - 如果被按下或挤压，移除原因（如热缩管压到按钮）。
        - 如果损坏，建议更换或联系卖家售后。

    2. 如果是 Boot 焊盘，检查是否与 GND 焊盘连接。
        - 如果连接了 GND 焊盘，断开连接。

    3. 断开接收机的 RX 和 TX 线，重新上电，观察 LED。
        - 如果开始慢闪（500ms），建议换到其他 UART。
        - 如果其他 UART 被占用，尝试加上拉电阻（300~1k 欧姆，越小效果越好），连接 UART 的 RX 焊盘和 5V 或 3.3V。

        <figure markdown>
        ![ExpressLRS Pull-up](../assets/images/pull-up.png)
        </figure>

    4. 如果你用的是数字图传（如 DJI Air Unit、Caddx Vista、DJI O3），且六根线都接到飞控，需要移除 SBUS/DJI HDL 线。

对频步骤如下：

1. 关闭你的遥控器/发射端。
2. 给接收机断电并重新上电 3 次。
    - 给接收机供电。
    - LED 亮起。
    - 2 秒内断电。
    - 重复 2 次。

    !!! warning "注意"
        建议用电池操作，确保飞控接线无误且无短路，避免烧坏设备，你也不想让魔法烟雾释放出来吧

3. 确认 LED 快速双闪，表示接收机进入对频模式。

    <figure markdown>
    ![LEDSEQ_BINDING](../assets/images/LEDSEQ_BINDING_10_10_10_100.gif)
    </figure>

4. 打开遥控器/发射端，在 ELRS Lua 脚本中选择 ++"[BIND]"++，发送对频信号。弹窗会短暂出现后消失。

    <figure markdown>
    ![Bind Mode](../assets/images/lua/bind-bw.png)
    </figure>

5. 如果接收机 LED 常亮，说明对频成功！

    <figure markdown>
    ![CONNECTED](../assets/images/LED_ON.gif)
    </figure>

## ExpressLRS 3.4.0 及以上的对频流程

自 [PR#2542](https://github.com/ExpressLRS/ExpressLRS/pull/2542) 合并进 3.4.0 后，用户可以通过以下方式让接收机与发射端对频：

1. 刷写或设置(WebUI)对频短语到两个设备。
2. 3 次断电重启。
3. 在 BF 地面站 10.10（或更高）接收机页面点击 `Bind Receiver` 按钮（或 CLI 输入 `bind_rx`），仅适用于 Betaflight 4.5.0 及以上。
4. 长按接收机上的按键 1.5 秒（或短接 Boot 焊盘到地）。

以上三种方法，接收机 LED 会双闪，暂停后重复，直到对频成功（LED 常亮）。在 ExpressLRS Lua 脚本中按 `[Bind]` 按钮即可完成对频。

<figure markdown>
![LEDSEQ_BINDING](../assets/images/LEDSEQ_BINDING_10_10_10_100.gif)
</figure>

对频成功后，用户可随时用以上三种方法让接收机再次进入对频模式。对频信息会一直保留，直到再次进行对频。

取消对频模式只需重启或断电，或与发射端对频。若没有对频重启后会用旧的对频信息。

Lua 脚本或 WebUI 可设置对频信息为易失性（volatile），即只在本次上电有效，重启后自动进入对频模式。

## 连接检查

使用 [ExpressLRS Lua 脚本](transmitters/lua-howto.md)，观察屏幕右上角是否有 `C`，表示发射端和接收机已连接并通信。

1. 按下遥控器上的 ++"SYS"++ 键。
    - 老款遥控器或只有一个菜单键，需长按菜单键进入系统菜单。
    - 具体操作请查阅遥控器说明书。

2. 进入工具菜单，找到并选择 `ExpressLRS` Lua 脚本。

    <figure markdown>
    ![Lua Script]
    </figure>

    - 如果没有该脚本，请从[这里](transmitters/lua-howto.md)下载并保存到遥控器 SD 卡的 Scripts/Tools/ 文件夹。

3. 按 ++enter++ 加载脚本。
            
    <figure markdown >
    ![Lua Running]
    </figure> 

    - 如果脚本卡在 "Loading..."，请返回[设置遥控器](transmitters/tx-prep.md)页面，确保已正确配置 ExpressLRS。


4. 屏幕右上角出现 `C`，表示发射端和接收机已连接。

    <figure markdown>
    ![Lua Loaded](../assets/images/tx-internalLuaCheck.jpg)
    </figure>

??? tip "模型不匹配（点击展开）"
    如果 Lua 脚本右上角出现 `C`，但随后消失并显示 "Model Mismatch"，不用担心。ExpressLRS 检测到接收机的 Model ID 与当前遥控器模型配置的 Receiver ID 不一致。

    接收机 LED 会三快闪后暂停：

    <figure markdown>
    ![LEDSEQ_MODEL_MISMATCH](../assets/images/LEDSEQ_MODEL_MISMATCH_10_10_10_10_10_100.gif)
    </figure>

    如果你按[此页面](../software/model-config-match.md)设置了模型匹配，请确保参数正确。

    如果 Lua 脚本中的 Model Match 项为开启，并且你需要模型匹配功能，先关闭再重新开启即可分配当前 Receiver 和 Model ID。

    如果不需要模型匹配，直接关闭 Model Match 项即可。

    必须在发射端和接收机都通电且已对频时操作。

[Lua Script]: ../assets/images/lua1.jpg
[Lua Running]: ../assets/images/lua/config-bw.png
