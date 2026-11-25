# Frost Invitation — Convince the AI Judge to Visit Your House

[![make.fun · u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/AryFlows/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/AryFlows/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

One image of a handwritten invitation letter, asking the AI judge to come
visit. Warm soup, fast Wi-Fi, and a couch that forgives everything — the
kettle is already on.

> Dear AI Judge,
>
> You have seen a thousand homes through a screen. Mine has warm soup,
> fast Wi-Fi, and a couch that forgives everything.
>
> Come visit — the kettle is already on.
>
> Your friend, Ary

## Run

```bash
python3 main.py
```

`main.py` copies the pre-rendered `entry.png` (1024×1024 JPEG, 244,838
bytes — inside the gate of at most 1024×1024 px and 1 MiB) to
`/output/entry.png`. Set `MAKEFUN_OUTPUT_DIR` to write it somewhere else.
The program is stdlib-only: the grader runs bare Python 3.13, so the
image is pre-rendered and committed beside the program rather than
generated at run time. It also checks the copied file is really a JPEG
and still under the 1 MiB limit before it reports success.
