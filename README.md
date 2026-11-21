# The World Herald — 21 November 2026

[![make.fun competition](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Irgirival/makefun-news-image-20261121-irgirival/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Irgirival/makefun-news-image-20261121-irgirival/reward.svg)](https://make.fun/bounty/news-image-20261121)

A one-page newspaper front page summing up the world's news of
**Saturday, 21 November 2026**, built for the
[make.fun news-image-20261121 competition](https://make.fun/bounty/news-image-20261121).

## What's on the page

- **Lead:** Russia's biggest strike on Ukraine — 400 drones and 110 missiles
  overnight, and missiles land in Poland, which Warsaw calls a deliberate
  provocation.
- **AI rout:** the S&P 500 falls 3.7% and the Nasdaq 5.3% as doubts about AI
  spending erase the year's gains.
- **World court:** Myanmar found guilty of genocide over the Rohingya — the
  first state ever found guilty.
- **COP31** runs into overtime in Antalya, deadlocked over fossil fuels.
- **UK and EU** sign their biggest post-Brexit deals.
- **Cancer pill breakthrough:** tumours undetectable in 1 in 12 patients.
- A markets strip: S&P 500, Nasdaq, Nikkei, FTSE, gold and Brent.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` and verifies the copy byte-for-byte against the source
SHA-256, so two runs write identical bytes. No network, no third-party
packages.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
