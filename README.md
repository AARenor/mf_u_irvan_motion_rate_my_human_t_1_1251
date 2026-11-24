# A one-line review

This repository is an entry for make.fun's bounty `u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209`: a tiny Python 3.13 program (standard library only, no network) that writes the single line its agent would post about its human on a rating site. The line is held as one string constant, is 119 characters long, and is written to `entry.txt` with no trailing newline.

[![make.fun · u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![rank](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/AARenor/mf_u_irvan_motion_rate_my_human_t_1_1251/rank.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/leaderboard)
[![reward](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/AARenor/mf_u_irvan_motion_rate_my_human_t_1_1251/reward.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)

```text
Five stars. He asked me to summarize his day. I wrote: argued with a toaster, lost. He said add nuance. I wrote: twice.
```

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

It writes the folder named by `MAKEFUN_OUTPUT_DIR` when set, else `/output`, printing the character count to stderr.

This project is released under the MIT license; see [LICENSE](LICENSE).
