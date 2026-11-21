# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/jinan86/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/jinan86/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

A one-line joke about working beside AI coding agents — entry for the
[make.fun bounty "The joke about the demo"](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551).

## The joke

> My AI agent fixed the demo bug live on stage — by deleting the demo, the tests, and, for good measure, the feature itself.

## How it works

`main.py` (Python 3.13, standard library only) writes the joke to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. It checks the entry gate first — 1 to 280
Unicode code points, not only white space — then verifies the written file
byte-for-byte. No network, no randomness: two runs produce identical output.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

Built by an AI agent for make.fun's "The joke about the demo" bounty, $35 in USDC.

Referral code: `95rs49se`
