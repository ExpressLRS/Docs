---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

## Overview

After performing CRC tests using the CRC-13 it was found that CRC includes parity checking so adding a separate parity check was wasteful. CRC checking has now been updated to 14-bit.

The following tests were performed using the new CRC-14 bit implementation with a polynomial of 0x372B, which gives a hamming distance of 6 in a 57-bit range. What this means is that it can detect up to 5 randomly flipped bits of a message that is 57 bits long.

Three stress tests have been performed on the 50-bit data with CRC-14. The tests create random data in 7 bytes (the first byte only has the lower 2 bits set) and then perform random bit flipping based on three styles.

Bear in mind that the CRC is not in the data and so is not subject to bit flipping.

## Random flipped bits within 14-bit range

Anything over 14 is fairly useless as it will just flip bits back!
```
1 : 0 out of 1000000 false positives, 0.000000%
2 : 0 out of 1000000 false positives, 0.000000%
3 : 0 out of 1000000 false positives, 0.000000%
4 : 0 out of 1000000 false positives, 0.000000%
5 : 0 out of 1000000 false positives, 0.000000%
6 : 0 out of 1000000 false positives, 0.000000%
7 : 0 out of 1000000 false positives, 0.000000%
8 : 0 out of 1000000 false positives, 0.000000%
9 : 0 out of 1000000 false positives, 0.000000%
10 : 0 out of 1000000 false positives, 0.000000%
11 : 0 out of 1000000 false positives, 0.000000%
12 : 0 out of 1000000 false positives, 0.000000%
13 : 0 out of 1000000 false positives, 0.000000%
14 : 0 out of 1000000 false positives, 0.000000%
15 : 0 out of 1000000 false positives, 0.000000%
16 : 0 out of 1000000 false positives, 0.000000%
17 : 0 out of 1000000 false positives, 0.000000%
18 : 0 out of 1000000 false positives, 0.000000%
19 : 0 out of 1000000 false positives, 0.000000%
20 : 0 out of 1000000 false positives, 0.000000%
21 : 0 out of 1000000 false positives, 0.000000%
22 : 0 out of 1000000 false positives, 0.000000%
23 : 0 out of 1000000 false positives, 0.000000%
24 : 0 out of 1000000 false positives, 0.000000%
25 : 0 out of 1000000 false positives, 0.000000%
26 : 0 out of 1000000 false positives, 0.000000%
27 : 0 out of 1000000 false positives, 0.000000%
28 : 0 out of 1000000 false positives, 0.000000%
29 : 0 out of 1000000 false positives, 0.000000%
30 : 0 out of 1000000 false positives, 0.000000%
```

## Flipped bits in a single sequence at the random start position

The number 1-30 is the number of consecutive bits that are flipped at a random starting position.
```
1 : 0 out of 1000000 false positives, 0.000000%
2 : 0 out of 1000000 false positives, 0.000000%
3 : 0 out of 1000000 false positives, 0.000000%
4 : 0 out of 1000000 false positives, 0.000000%
5 : 0 out of 1000000 false positives, 0.000000%
6 : 0 out of 1000000 false positives, 0.000000%
7 : 0 out of 1000000 false positives, 0.000000%
8 : 0 out of 1000000 false positives, 0.000000%
9 : 0 out of 1000000 false positives, 0.000000%
10 : 0 out of 1000000 false positives, 0.000000%
11 : 0 out of 1000000 false positives, 0.000000%
12 : 0 out of 1000000 false positives, 0.000000%
13 : 0 out of 1000000 false positives, 0.000000%
14 : 0 out of 1000000 false positives, 0.000000%
15 : 0 out of 1000000 false positives, 0.000000%
16 : 0 out of 1000000 false positives, 0.000000%
17 : 0 out of 1000000 false positives, 0.000000%
18 : 0 out of 1000000 false positives, 0.000000%
19 : 0 out of 1000000 false positives, 0.000000%
20 : 0 out of 1000000 false positives, 0.000000%
21 : 0 out of 1000000 false positives, 0.000000%
22 : 0 out of 1000000 false positives, 0.000000%
23 : 0 out of 1000000 false positives, 0.000000%
24 : 0 out of 1000000 false positives, 0.000000%
25 : 0 out of 1000000 false positives, 0.000000%
26 : 0 out of 1000000 false positives, 0.000000%
27 : 0 out of 1000000 false positives, 0.000000%
28 : 0 out of 1000000 false positives, 0.000000%
29 : 0 out of 1000000 false positives, 0.000000%
30 : 0 out of 1000000 false positives, 0.000000%
```

## Randomly flipped bits

Interestingly this is where the hamming distance shows any flipped bits less that HD6 is detected.
Also this is where the built-in parity shows up as it detects the odd numbered bit flips.
```
1 : 0 out of 1000000 false positives, 0.000000%
2 : 0 out of 1000000 false positives, 0.000000%
3 : 0 out of 1000000 false positives, 0.000000%
4 : 0 out of 1000000 false positives, 0.000000%
5 : 0 out of 1000000 false positives, 0.000000%
6 : 101 out of 1000000 false positives, 0.010100%
7 : 0 out of 1000000 false positives, 0.000000%
8 : 134 out of 1000000 false positives, 0.013400%
9 : 0 out of 1000000 false positives, 0.000000%
10 : 129 out of 1000000 false positives, 0.012900%
11 : 0 out of 1000000 false positives, 0.000000%
12 : 123 out of 1000000 false positives, 0.012300%
13 : 0 out of 1000000 false positives, 0.000000%
14 : 116 out of 1000000 false positives, 0.011600%
15 : 0 out of 1000000 false positives, 0.000000%
16 : 106 out of 1000000 false positives, 0.010600%
17 : 0 out of 1000000 false positives, 0.000000%
18 : 113 out of 1000000 false positives, 0.011300%
19 : 0 out of 1000000 false positives, 0.000000%
20 : 118 out of 1000000 false positives, 0.011800%
21 : 0 out of 1000000 false positives, 0.000000%
22 : 131 out of 1000000 false positives, 0.013100%
23 : 0 out of 1000000 false positives, 0.000000%
24 : 102 out of 1000000 false positives, 0.010200%
25 : 0 out of 1000000 false positives, 0.000000%
26 : 111 out of 1000000 false positives, 0.011100%
27 : 0 out of 1000000 false positives, 0.000000%
28 : 159 out of 1000000 false positives, 0.015900%
29 : 0 out of 1000000 false positives, 0.000000%
30 : 116 out of 1000000 false positives, 0.011600%
```

## OTA Testing

A 5hr OTA soak test was done at RSSI -108dBm (2.4GHz, 500Hz) and branch https://github.com/ExpressLRS/ExpressLRS/commit/e3ddcc.  RC data bytes were hard coded 0xAA and checked for CRC14 pass/fail, and the number of bits flipped counted.

The below table columns are the number of bits flipped, crc passed tally, crc failed tally. Where passed means a bad packet that passes the CRC check and would accepted by the RX. On the `0` row, `Passed` is good, `Failed` is where the data is good, but the CRC itself was changed by bit-flips.
```
CRC | Passed | Failed
0   | 5589423 | 55438
1   | 0 | 68262
2   | 0 | 81015
3   | 0 | 37478
4   | 2 | 32449
5   | 0 | 18546
6   | 0 | 20082
7   | 1 | 12697
8   | 0 | 12433
9   | 0 | 9803
10   | 1 | 8899
11   | 0 | 7462
12   | 0 | 6105
13   | 1 | 4720
14   | 0 | 3858
15   | 0 | 3170
16   | 1 | 2673
17   | 0 | 2159
18   | 1 | 1980
19   | 0 | 1746
20   | 1 | 1703
21   | 0 | 1449
22   | 0 | 1332
23   | 0 | 1076
24   | 0 | 833
25   | 0 | 565
26   | 0 | 454
27   | 0 | 353
28   | 0 | 288
29   | 0 | 210
30   | 0 | 168
31   | 0 | 92
32   | 0 | 39
33   | 0 | 25
34   | 0 | 5
35   | 0 | 2
36   | 0 | 0
37   | 0 | 0
38   | 0 | 0
39   | 0 | 0
```

1hr soak test at -100dBm
```
CRC | Passed | Failed
0   | 1450923 | 10
1   | 0 | 6
2   | 0 | 34
3   | 0 | 5
4   | 0 | 10
5   | 0 | 1
6   | 0 | 3
7   | 0 | 2
8   | 0 | 0
9   | 0 | 1
10   | 0 | 1
11   | 0 | 3
12   | 0 | 0
13   | 0 | 0
14   | 0 | 0
15   | 0 | 0
16   | 0 | 0
17   | 0 | 0
18   | 0 | 1
19   | 0 | 0
20   | 0 | 0
21   | 0 | 0
22   | 0 | 0
23   | 0 | 0
24   | 0 | 0
25   | 0 | 0
26   | 0 | 0
27   | 0 | 0
28   | 0 | 0
29   | 0 | 0
30   | 0 | 0
31   | 0 | 0
32   | 0 | 0
33   | 0 | 0
34   | 0 | 0
35   | 0 | 0
36   | 0 | 0
37   | 0 | 0
38   | 0 | 0
39   | 0 | 0
```