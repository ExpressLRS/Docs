---
template: i18n/zh/main.html
description: ExpressLRS Web UI 是 ExpressLRS 生态系统的重要组成部分。你可以通过它进行 WiFi 固件升级和参数配置。
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/quick-start.png)

## ExpressLRS Web UI 简介

ExpressLRS Web UI 是 ExpressLRS 生态系统的重要组成部分。在项目早期版本中，Web UI 主要用于升级 ExpressLRS 固件，以及日志记录和调试（部分硬件支持）。

自 ExpressLRS 3.0 起，Web UI 的功能进一步扩展。现在可以直接修改固件参数，包括对频短语、法规区域（900MHz 设备）、UART 反转等。

### 顶部横幅

<figure markdown>
![Web UI Banner](../assets/images/web-banner.png)
<figcaption>ExpressLRS Web UI 顶部横幅</figcaption>
</figure>

### 选项标签页

此标签页允许用户无需重新刷写设备即可更改固件选项，还可以导入和导出配置，方便备份设备设置。

发射端和接收机通用选项：

- 对频短语：在此输入你的对频短语，可以覆盖出厂设置或之前刷写的设置。

    !!! abstract "显示为空？"
        该字段不会显示明文短语。如果看到是空白，不用担心。下一个 UID 字段已包含相关信息。

- UID：当你在上方输入对频短语时，这个只读字段会自动更新为 UID，这是实际存储在设备中的内容。

- 法规区域：仅适用于 900MHz 系统。此字段允许用户更改设备的法规区域。

    !!! abstract "2.4GHz 怎么办？"
        EU_CE 法规区域是编译时选项，LBT 代码需要在编译时加入才能生效。

- WiFi“自动开启”间隔（秒）：设置设备上电后多久自动进入 WiFi 模式（发射端无有效 CRSF 信号或接收机无同步包时）。

=== "接收机选项"

    <figure markdown>
    ![Web UI Banner](../assets/images/web-options-rx.png)
    <figcaption>ExpressLRS 接收机选项标签页</figcaption>
    </figure>

    - UART 波特率：接收机与飞控或其他串口设备通信的速率。一般保持默认 420000。
        - 特例：如使用 KISS/Kiss Ultra 固件，请设置为 400000，因为 KISS 使用该速率。

    - 反转 TX 引脚：一般保持关闭。该选项会反转接收机 TX 引脚输出的 CRSF 信号。
        - 如果接收机要接到飞控的 SBUS 焊盘（没有额外的非反转 RX 焊盘），需开启此选项，并在飞控配置中执行 `set serialrx_inverted = on`。

    - 首次连接锁定：如果你不更改射频模式/包速率，建议开启此项以加快重连速度。

=== "发射端选项"

    <figure markdown>
    ![Web UI Banner](../assets/images/web-options-tx.png)
    <figcaption>ExpressLRS 发射端选项标签页</figcaption>
    </figure>

    - 遥测报告间隔：控制遥测包发送频率。默认 240LU，已足够快，适用于 EdgeTX 或 OpenTX。

    - UART 反转：如在 OpenTX 或 EdgeTX 遥控器上使用发射端模块，需保持开启。外部模块仓的 S.Port 引脚为反转双向引脚。

    - 风扇运行时间（秒）：控制发射端模块风扇在功率降到 Lua 脚本阈值以下后继续运行的时间。

### WiFi 标签页

<figure markdown>
![Web UI Banner](../assets/images/web-homenetwork.png)
<figcaption>ExpressLRS WebUI WiFi 标签页</figcaption>
</figure>

### 模型标签页

<figure markdown>
![Web UI Banner](../assets/images/web-rxmodel.png)
<figcaption>ExpressLRS 接收机模型标签页</figcaption>
</figure>

<figure markdown>
![Web UI Banner](../assets/images/web-pwmoutput.png)
<figcaption>ExpressLRS PWM 接收机输出设置</figcaption>
</figure>

### 按钮标签页

目前仅适用于 RadioMaster Ranger 模块。

<figure markdown>
![Web UI Banner](../assets/images/web-buttonsTX.png)
<figcaption>ExpressLRS 发射端按钮标签页</figcaption>
</figure>

### 固件升级标签页

=== "接收机升级标签页"
    <figure markdown>
    ![Web UI Banner](../assets/images/web-update-rx.png)
    <figcaption>ExpressLRS 接收机升级标签页</figcaption>
    </figure>

=== "发射端升级标签页"
    <figure markdown>
    ![Web UI Banner](../assets/images/web-update-tx.png)
    <figcaption>ExpressLRS 发射端升级标签页</figcaption>
    </figure>

## 如何进入 Web UI
=== "接收机"

    1. 让接收机进入 WiFi 模式。

        === "自动 WiFi 开启"

            1. 确保遥控器和发射端模块关闭。

            2. 给接收机断电再上电。LED 会慢闪，如下图所示。

                <figure markdown>
                ![RX Waiting](../assets/images/LEDSEQ_DISCONNECTED_50_50.gif)
                </figure>

                ??? warning "接收机 LED 不闪烁！（点击展开）"
                    如果 LED 常亮，可能是进入了 Bootloader 模式。请重新接线到其他 UART。如果之前升级失败，可能已软砖。请参考[救砖指南](../quick-start/unbricking.md)。

            3. 等约 60 秒，或直到接收机 LED 快速闪烁，表示已进入 WiFi 模式。

                <figure markdown>
                ![RX WiFi](../assets/images/LEDSEQ_WIFI_UPDATE_2_3.gif)
                </figure>

        === "通过 Lua 脚本"
            1. 确保接收机和发射端已对频并同步。遥控器主屏应有 RSSI 指示，接收机 LED 常亮。

                <figure markdown>
                ![RX Bound](../assets/images/LED_ON.gif)
                </figure>

            2. 按遥控器上的 ++"SYS"++ 键。
                - 老款遥控器或只有一个菜单键，需长按菜单键进入系统菜单。
                - 具体操作请查阅遥控器说明书。
            3. 进入工具菜单，找到并选择 `ExpressLRS` Lua 脚本。

                <figure markdown>
                ![Lua Script]
                </figure>

                - 如果没有该脚本，请从[这里](./transmitters/lua-howto.md)下载并保存到 SD 卡 Scripts/Tools/ 文件夹。
            4. 按 ++enter++ 加载脚本。

                <figure markdown >
                ![Lua Running]
                </figure> 

                - 如果卡在 "Loading..."，请返回[遥控器准备](./transmitters/tx-prep.md)页面，确保已正确配置 ExpressLRS。
                - 右上角应有 C，表示发射端和接收机已连接。
            5. 下拉选择 `Wifi Connectivity` 并按 ++enter++。
            6. 选择 `Enable RX WiFi` 并按 ++enter++。

                <figure markdown>
                ![Lua WiFi RX]
                </figure>

            7. 会短暂显示 `WiFi Running`，接收机 LED 快速闪烁，表示已进入 WiFi 模式。

                <figure markdown>
                ![RX WiFi](../assets/images/LEDSEQ_WIFI_UPDATE_2_3.gif)
                </figure>

                !!! info "说明"
                    接收机进入 WiFi 模式后会断开与发射端的连接，遥控器会提示 "Telemetry Lost"（需安装语音包）。

        === "通过按键"
            1. 如果接收机有 Boot 按钮，可用此方法进入 WiFi 模式。
                - 找到接收机上的 Boot 按钮：

                <figure markdown>
                ![betafpv SuperD](../assets/images/BetaFPVSuperD.png)
                <figcaption>带 Boot 按钮的接收机示例</figcaption>
                </figure>
            
            2. 长按 Boot 按钮 5 秒，LED 快速闪烁，表示进入 WiFi 模式。

                <figure markdown>
                ![RX WiFi](../assets/images/LEDSEQ_WIFI_UPDATE_2_3.gif)
                </figure>
                
    4. 搜索 `ExpressLRS RX` WiFi 热点。
        ![WiFi Hotspot](../assets/images/WifiHotspot.png){ align=right }

        - 如果接收机已刷入家庭 WiFi SSID 和密码，并能连接该网络，则不会显示该热点。
        - 热点密码为 `expresslrs`。

        <br clear="right" />

    5. 在浏览器中访问 Web UI，地址如下：
        - http://10.0.0.1/ —— 连接到 `ExpressLRS RX` 热点时使用

            !!! Note
                该 IP 也常被路由器占用。如果电脑有网线连接，可能会打开路由器或 ISP 配置页面而不是 Web UI。

                建议先断开网络或用手机、平板等设备访问。

            !!! Note
                有些设备会弹出网络登录窗口，点进去可能是不完整的 WebUI。请手动在浏览器输入 http://10.0.0.1/。

        - http://elrs_rx.local —— 如果接收机已配置家庭 WiFi 并连接

            !!! Note
                如果无法访问，可能是电脑或网络未启用 MDNS。

            ??? tip "用 IP 地址访问！（点击展开）"
                === "`arp` 命令"

                    1. 打开命令提示符窗口。
                    2. 输入 `arp -a`，查看所有网络设备。
                    3. 依次尝试标记为 `Dynamic` 的 IP 地址，直到打开 ExpressLRS Web UI。

                === "路由器 DHCP 列表"
                    1. 登录路由器后台。
                    2. 查看 DHCP 列表，找到 "elrs" 设备。
                    3. 记下分配的 IP 地址。
                    4. 在浏览器中输入该 IP 地址访问。

=== "发射端模块"

    1. 让发射端模块进入 WiFi 模式。

        === "通过 ExpressLRS Lua 脚本" 

            1. 按遥控器上的 ++"SYS"++ 键。
                - 老款遥控器或只有一个菜单键的需长按菜单键进入系统菜单。
                - 具体操作请查阅遥控器说明书。
            2. 进入工具菜单，找到并选择 `ExpressLRS` Lua 脚本。

                <figure markdown>
                ![Lua Script]
                </figure>

                - 如果没有该脚本，请从[这里](./transmitters/lua-howto.md)下载并保存到 SD 卡 Scripts/Tools/ 文件夹。
            3. 按 ++enter++ 加载脚本。

                <figure markdown >
                ![Lua Running]
                </figure> 

                - 如果卡在 "Loading..."，请返回[遥控器准备](./transmitters/tx-prep.md)页面，确保已正确配置 ExpressLRS。
            4. 下拉选择 `Wifi Connectivity` 并按 ++enter++。
            5. 选择 `Enable WiFi` 并按 ++enter++。

                <figure markdown>
                ![Lua WiFi]
                </figure>

            6. 显示 `WiFi Running`，发射端模块已进入 WiFi 模式。
                - 如果脚本报语法错误，不用担心，模块已进入 WiFi 模式。可能是遥控器或固件较旧，或 Lua 脚本版本较新。

        === "外部模块脱离遥控器"

            1. 将发射端模块从遥控器模块仓取下，用外部电源（2S）或 USB 供电。
            2. 等待 60 秒，RGB LED 会变为绿色呼吸灯，表示进入 WiFi 模式。
                - 带 OLED 屏的模块也会显示 WiFi 模式提示。

    2. 搜索 `ExpressLRS TX` WiFi 热点。
        ![WiFi Hotspot](../assets/images/WifiHotspotTX.png){ align=right }

        - 如果发射端模块已刷入家庭 WiFi SSID 和密码，并能连接该网络，则不会显示该热点。
        - 热点密码为 `expresslrs`。

        <br clear="right" />

    3. 在浏览器中访问 Web UI，地址如下：
        - http://10.0.0.1/ —— 连接到 `ExpressLRS TX` 热点时使用

            !!! Note
                该 IP 也常被路由器占用。如果电脑有网线连接，可能会打开路由器或 ISP 配置页面而不是 Web UI。

                建议先断开网络或用手机、平板等设备访问。

            !!! Note
                有些设备会弹出网络登录窗口，点进去可能是不完整的 WebUI。请手动在浏览器输入 http://10.0.0.1/。

        - http://elrs_tx.local —— 如果发射端模块已配置家庭 WiFi 并连接

            !!! Note
                如果无法访问，可能是电脑或网络未启用 MDNS。

            ??? tip "用 IP 地址访问！（点击展开）"
                === "`arp` 命令"

                    1. 打开命令提示符窗口。
                    2. 输入 `arp -a`，查看所有网络设备。
                    3. 依次尝试标记为 `Dynamic` 的 IP 地址，直到打开 ExpressLRS Web UI。

                === "路由器 DHCP 列表"
                    1. 登录路由器后台。
                    2. 查看 DHCP 列表，找到 "elrs" 设备。
                    3. 记下分配的 IP 地址。
                    4. 在浏览器中输入该 IP 地址访问。

[Lua Script]: ../assets/images/lua1.jpg
[Lua Running]: ../assets/images/lua/config-bw.png
[Lua WiFi]: ../assets/images/lua/wifi-bw.png
[Lua WiFi RX]: ../assets/images/lua/wifi-bw-rx.png