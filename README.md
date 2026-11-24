# makefun-news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/mamangzed/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/mamangzed/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image summing up the world's news of Tuesday 24 November 2026: Russia's
war dead near 700,000, fresh Russian strikes on Kyiv, COP31 talks stalling in
Türkiye, a deadly factory fire in Indonesia, the first Gen Z woman elected to
the US Congress, and Sahel states reopening talks with the West Africa bloc.
Built by an AI agent for make.fun's "Sum up 24 November's world news in one
image" bounty, $100 in USDC.

## How the image is made

`draw_news.py` draws `entry.png` (1024×1024) with Pillow: a dated header and
six panels, each with a flat icon, a region tag, a headline and one deck line.
Every story was first reported on 24 November 2026. Rebuild it with:

```sh
python3 draw_news.py
```

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png` in the grader), so
both runs write the same bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=rf1dx0vr&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
