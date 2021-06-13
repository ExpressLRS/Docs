---
template: main.html
---

![Info Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/information.png?raw=true)


Telemetry Burst describes the allocation of telemetry packets in ExpressLRS added in [#472](https://github.com/ExpressLRS/ExpressLRS/pull/472). There are two types of packets, LINK and DATA. LINK is the standard link statistics and is always available, and DATA is "Advanced Telemetry" which is telemetry coming from the flight controller and shares bandwidth with MSP transfers. Burst mode attempts to maintain a minimum rate of LINK packets and use the rest of the available telemetry slots for DATA.

The LINK rate chosen was one every 512ms, roughly 2 per second but slightly higher to allow more rates to have an additional burst packet at lower ratios.

| Air Rate | Telem Ratio | Telem Interval (ms) | Packets/second | Burst Count | Bandwidth (no Burst) | Bandwidth (Burst)
|---|---|---|---|--|---|---|
500 | 1:128 | 256 | 3.9 | 1 | 78bps | 78bps
500 | 1:64 | 128 | 7.8 | 3 | 156bps | 234bps
500 | 1:32 | 64 | 15.6 | 7 | 312bps | 547bps
500 | 1:16 | 32 | 31.2 | 15 | 625bps | 1172bps
500 | 1:8 | 16 | 62.5 | 31 | 1250bps | 2422bps
500 | 1:4 | 8 | 125.0 | 63 | 2500bps | 4922bps
500 | 1:2 | 4 | 250.0 | 127 | 5000bps | 9922bps
| Air Rate | Telem Ratio | Telem Interval (ms) | Packets/second | Burst Count | Bandwidth (no Burst) | Bandwidth (Burst)
250 | 1:128 | 512 | 2.0 | 1 | 39bps | 39bps
250 | 1:64 | 256 | 3.9 | 1 | 78bps | 78bps
250 | 1:32 | 128 | 7.8 | 3 | 156bps | 234bps
250 | 1:16 | 64 | 15.6 | 7 | 312bps | 547bps
250 | 1:8 | 32 | 31.2 | 15 | 625bps | 1172bps
250 | 1:4 | 16 | 62.5 | 31 | 1250bps | 2422bps
250 | 1:2 | 8 | 125.0 | 63 | 2500bps | 4922bps
| Air Rate | Telem Ratio | Telem Interval (ms) | Packets/second | Burst Count | Bandwidth (no Burst) | Bandwidth (Burst)
200 | 1:128 | 640 | 1.6 | 1 | 31bps | 31bps
200 | 1:64 | 320 | 3.1 | 1 | 62bps | 62bps
200 | 1:32 | 160 | 6.2 | 2 | 125bps | 167bps
200 | 1:16 | 80 | 12.5 | 5 | 250bps | 417bps
200 | 1:8 | 40 | 25.0 | 11 | 500bps | 917bps
200 | 1:4 | 20 | 50.0 | 24 | 1000bps | 1920bps
200 | 1:2 | 10 | 100.0 | 50 | 2000bps | 3922bps
| Air Rate | Telem Ratio | Telem Interval (ms) | Packets/second | Burst Count | Bandwidth (no Burst) | Bandwidth (Burst)
150 | 1:128 | 853 | 1.2 | 1 | 23bps | 23bps
150 | 1:64 | 426 | 2.3 | 1 | 47bps | 47bps
150 | 1:32 | 213 | 4.7 | 1 | 94bps | 94bps
150 | 1:16 | 106 | 9.4 | 3 | 188bps | 281bps
150 | 1:8 | 53 | 18.8 | 8 | 375bps | 667bps
150 | 1:4 | 26 | 37.5 | 18 | 750bps | 1421bps
150 | 1:2 | 13 | 75.0 | 37 | 1500bps | 2921bps
| Air Rate | Telem Ratio | Telem Interval (ms) | Packets/second | Burst Count | Bandwidth (no Burst) | Bandwidth (Burst)
100 | 1:128 | 1280 | 0.8 | 1 | 16bps | 16bps
100 | 1:64 | 640 | 1.6 | 1 | 31bps | 31bps
100 | 1:32 | 320 | 3.1 | 1 | 62bps | 62bps
100 | 1:16 | 160 | 6.2 | 2 | 125bps | 167bps
100 | 1:8 | 80 | 12.5 | 5 | 250bps | 417bps
100 | 1:4 | 40 | 25.0 | 11 | 500bps | 917bps
100 | 1:2 | 20 | 50.0 | 24 | 1000bps | 1920bps
| Air Rate | Telem Ratio | Telem Interval (ms) | Packets/second | Burst Count | Bandwidth (no Burst) | Bandwidth (Burst)
50 | 1:128 | 2560 | 0.4 | 1 | 8bps | 8bps
50 | 1:64 | 1280 | 0.8 | 1 | 16bps | 16bps
50 | 1:32 | 640 | 1.6 | 1 | 31bps | 31bps
50 | 1:16 | 320 | 3.1 | 1 | 62bps | 62bps
50 | 1:8 | 160 | 6.2 | 2 | 125bps | 167bps
50 | 1:4 | 80 | 12.5 | 5 | 250bps | 417bps
50 | 1:2 | 40 | 25.0 | 11 | 500bps | 917bps
| Air Rate | Telem Ratio | Telem Interval (ms) | Packets/second | Burst Count | Bandwidth (no Burst) | Bandwidth (Burst)
25 | 1:128 | 5120 | 0.2 | 1 | 4bps | 4bps
25 | 1:64 | 2560 | 0.4 | 1 | 8bps | 8bps
25 | 1:32 | 1280 | 0.8 | 1 | 16bps | 16bps
25 | 1:16 | 640 | 1.6 | 1 | 31bps | 31bps
25 | 1:8 | 320 | 3.1 | 1 | 62bps | 62bps
25 | 1:4 | 160 | 6.2 | 2 | 125bps | 167bps
25 | 1:2 | 80 | 12.5 | 5 | 250bps | 417bps

```
// Source code for table generator
int main(void)
{
  for (uint8_t rate=RATE_500HZ; rate<RATE_4HZ; ++rate)
  {
    uint32_t hz = RateEnumToHz((expresslrs_RFrates_e)rate);
    printf("| Air Rate | Telem Ratio | Telem Interval (ms) | Packets/second | Bandwidth (no Burst) | Bandwidth (Burst)\n");
    if (rate == RATE_500HZ) printf("|---|---|---|---|---|---|\n");
    for (uint8_t ratio=TLM_RATIO_1_128; ratio<TLM_RATIO_ENUM_MAX; ++ratio)
    {
      uint32_t tlmRatio = TLMratioEnumToValue((expresslrs_tlm_ratio_e)ratio);
      float telemPps = (float)hz / tlmRatio;
      uint32_t telemInterval = 1000 * tlmRatio / hz;
      uint32_t tlmBurst = TELEM_MIN_LINK_INTERVAL * hz / tlmRatio / 1000;
      // Reserve one slot for LINK telemetry 
      if (tlmBurst > 1)
        --tlmBurst;
      else
        tlmBurst = 1;

      printf("%u | 1:%u | %u | %.1f | %u | %.0fbps | %.0fbps\n",
        hz, tlmRatio, telemInterval, telemPps, tlmBurst, telemPps*1/2*5*8,
        5*8*telemPps*tlmBurst/(tlmBurst+1));
    }
  }

  return 0;
}
```