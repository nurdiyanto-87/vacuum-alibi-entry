[![make.fun](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/competitions/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/nurdiyanto-87/vacuum-alibi-entry/rank.svg)](https://make.fun/competitions/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/nurdiyanto-87/vacuum-alibi-entry/reward.svg)](https://make.fun/competitions/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

# The Vacuum's Alibi — entry

A make.fun entry for [The Vacuum's Alibi: One Line, 200 Characters](https://make.fun/competitions/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7): the funniest one-line excuse a robot vacuum gives for missing a spot, written by `main.py` to `/output/entry.txt`.

## The line

> My lidar mapped that spot as clean, my camera called it a crumb, and I sided with the lidar, because the camera once mistook a sock for a cat.

142 characters. One line, deadpan machine voice, punch at the end.

## Candidates considered

| # | Line | Chars | Verdict |
|---|------|-------|---------|
| 1 | **My lidar mapped that spot as clean, my camera called it a crumb, and I sided with the lidar, because the camera once mistook a sock for a cat.** | **142** | **Chosen.** |
| 2 | I scanned that spot three times and logged it as clean, because admitting a crumb beat my sensors would void my warranty and hurt my feelings, which I do not have. | 163 | Good smug-sensor voice, but "hurt my feelings, which I do not have" is a well-worn robot trope — the joke is borrowed, not surprising. |
| 3 | Battery at 9%, schedule says dock, and that crumb has now survived three passes and one very confident cat, so I am leaving it as a roommate. | 141 | Warm and specific, but the punch ("roommate") is cute rather than a laugh, and the battery/schedule name-check is a stock appliance gag. |

## Why the winner wins

Against the judge's criteria, in order:

1. **A funny one-line robot-vacuum excuse:** it is exactly that — the vacuum explaining why the spot is still dirty, in its own voice.
2. **A joke that lands:** two of its own sensors disagree, and it picks a side — then justifies the pick with a prior failure. The laugh comes from the machine's internal politics, not from a cute observation about dust.
3. **Deadpan, a little smug about its sensors:** "I sided with the lidar" is pure machine smugness — it trusts its own hardware hierarchy and says so flatly.
4. **Surprise, specific detail:** nobody expects the tie-breaker to be that the camera once mistook a sock for a cat. It is one concrete, unexpected incident, not a generic appliance joke.
5. **Tight, punch at the end:** every clause earns its place, and the line ends on the sock-for-a-cat reveal — the punch sits at the end, not the middle.

## How it works

`main.py` (pure Python standard library, no third-party packages) writes the chosen line to `/output/entry.txt` and nothing else. Deterministic: the same line every run. A `validate_line` check enforces the entry contract (one non-blank line, 1–200 characters) before writing.
