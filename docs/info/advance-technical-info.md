---
template: main.html
---

![Info Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/information.png?raw=true)

This page explain the more technical side for debugging things yourself.

## LUA Status
In normal state, the top right corner of the LUA will display `-` or `C` for RX connection status. in Warning or Critical Warning, the top right corner of the LUA will display a number to debug. As the LUA title will only show the current most critical warning only.

Converting the number on the top right corner to bits, you can decode the on going warnings.

| Bit | Status | Solution |
| ---- | -------------------------------- | ----------------------------------------------------------------- |
0 | RX connection status | connect a RX with TLM ratio other than ``Off`` |
1 | Reserved Status ||
2 | Model Missmatch Warning | set ModelMatch to Off or Select/Set the correct Model ID |
3 | Armed Status | LUA should be closed to maximize sent Stick Command |
4 | Reserved Warning | |
5 | Not While Connected | Do not change this parameter when connected to a RX |
6 | Reserved Critical Warning | |
7 | Reserved Critical Warning | |

## DEBUG Logging
| Defines | Description |
| -------------------------------- | ----------------------------------------------------------------- |
| -DDEBUG_LOG | Turn on debug messages, if disabled then all debugging options (starting with DEBUG_) are disabled |
| -DDEBUG_LOG_VERBOSE | Use DEBUG_LOG_VERBOSE instead (or both) to see verbose debug logging (spammy stuff) |
| -DDEBUG_RX_SCOREBOARD | Print a letter for each packet received or missed (RX debugging) |
| -DDEBUG_CRSF_NO_OUTPUT | Don't send RC msgs over UART |
| -DDEBUG_BF_LINK_STATS | These debugging options send extra information to BetaFlight in the LinkStatistics packet |
