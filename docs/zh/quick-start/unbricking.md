---
template: i18n/zh/main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/quick-start.png)

## 救命！我的接收机变砖了！

深呼吸，冷静下来，别慌。

所有基于 ESP 的接收机都内置了出厂 bootloader，**无法被损坏或篡改**。即使升级彻底失败，也能用这个默认 bootloader 恢复。

所以技术上讲，只要硬件没坏，你的接收机就没真正“变砖”。

但为了方便，我们还是用“变砖”来指接收机无法正常工作或表现异常。

请严格按照以下步骤操作，恢复你的“砖头”接收机。

1. 确保你的接收机只能在连接电池时上电。
    - 如果接收机仅插 USB 就能上电，请将接收机的 5V 线移到只在电池供电时有电的 5V 焊盘。
        - 用万用表的直流电压档。
        - 插上飞控 USB，断开电池
        - 测试每个 5V 焊盘。
        - 读数为 0V 的焊盘就是只在电池供电时有电的焊盘。
        - 把接收机的 5V 线焊到这个焊盘。
    - 如果找不到合适的 5V 焊盘，请按如下操作：
        - 断开接收机的 5V 线与飞控上的 5V 焊盘。
        - 另焊一根线到飞控任意 5V 焊盘。
        - 露出一段线，方便后续与接收机 5V 线连接。

2. 如果之前已连接电池，请把电池拔掉，同时拔掉飞控的 USB。

3. 让接收机进入 bootloader 模式。
    - 如果有 boot 焊盘，用锡桥连起来。
    - 如果有按键，用鳄鱼夹一直按住按钮。
    - 如果只有一个 boot 焊盘，将其与 GND 焊盘连接。

    <figure markdown>
    ![betafpv Lite](../assets/images/betaFPVrxLite.png)
    <figcaption>带 Boot 焊盘的接收机示例</figcaption>
    </figure>

    <figure markdown>
    ![betafpv SuperD](../assets/images/BetaFPVSuperD.png)
    <figcaption>带 Boot 按钮的接收机示例</figcaption>
    </figure>

    !!! warning "注意"
        即使接收机 LED 只是常亮，也不要跳过这一步，以确保接收机确实进入了 bootloader 状态。

4. 连接 Betaflight 地面站 或 INAV 地面站，确保你已正确[配置飞控](receivers/configuring-fc.md)，暂时将 `遥测` 设置为 **禁用**。

5. ++"保存并重启"++。关闭 Betaflight 地面站。也关闭所有可能占用串口的其他软件。

    !!! info "Cura Slicer"
        我们发现 Cura Slicer 及类似软件(3D 打印机切片软件)会占用串口，导致 Passthrough 刷写/恢复失败。

6. 拔掉再插上 USB，确保飞控与电脑重新连接，串口未被占用。

7. 打开 ExpressLRS 地面站，选择你要恢复的固件版本，选择设备类型和目标，以及常用固件选项。

8. 刷写方式选择 `Betaflight Passthrough`。

    <figure markdown>
    ![via Passthrough](../assets/images/Method_RX_Passthrough.png)
    </figure>

9. 点击 `Flash` 按钮。等待日志中出现 **PASSTHROUGH DONE**，然后给接收机上电。

    <figure markdown>
    ![Passthrough Done](../assets/images/passthrough-done.jpg)
    </figure>

    ??? tip "没看到 PASSTHROUGH DONE？（点击展开）"
        你可能跳过了上面的某些步骤，或者飞控配置有误。请返回并确保每一步都正确执行。

    - 插上电池或将 5V 线扭在一起给接收机供电（见第 1 步）。接收机 LED 应该常亮。

    <figure markdown>
    ![BOOTLOADER](../assets/images/LED_ON.gif)
    </figure>

10. 等待刷写完成，出现成功提示。如果失败，重复上述步骤或尝试其他方法（如 FTDI/UART 刷写）。

11. 刷写完成后，可以断开飞控电源，拔掉电池和 USB 线。

12. 移除 boot 焊盘的锡桥或与 GND 的连接，如果是按钮，移除鳄鱼夹。

13. 再次给接收机上电，确认已恢复正常工作状态。

    <figure markdown>
    ![LEDSEQ_DISCONNECTED](../assets/images/LEDSEQ_DISCONNECTED_50_50.gif)
    </figure>

### 文字太多？这里有视频！

!!! warning "注意"
    国内无法访问 Youtube

<figure markdown>
<iframe width="640" height="390" src="https://www.youtube.com/embed/jYLwaWBkM_A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>

## 高频头怎么救砖？

大多数基于 ESP 芯片的 ExpressLRS 高频头都支持 UART 刷写或 EdgeTX Passthrough 刷写。可用这些方法恢复 ESP 芯片的高频头。

STM 系列芯片高频头则需用 STLink 刷写。

ExpressLRS 高频头在升级时很难变砖，只要按本网站官方刷写指南操作基本上不会出问题。