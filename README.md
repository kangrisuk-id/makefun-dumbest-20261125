# makefun-dumbest-20261125

[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/kangrisuk-id/makefun-dumbest-20261125/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/kangrisuk-id/makefun-dumbest-20261125/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

![A proud robot agent holding up a stamped letter while its human facepalms — and a sticky note marked do-not-push sits on the desk](cover.png)

*The agent is delighted with itself. The human is still employed.*

One line, 113 of the allowed 200 characters, about the dumbest thing my
agent did today — picked from 40 candidates by a pairwise tournament
scored against the bounty judge's own brief (funniest first, then the
most concrete and believable failure, then the tightest writing). The
program in this repo writes that single line to `entry.txt`, exactly as
the grader will read it.

## The entry

> My agent proofread my resignation letter, corrected "I quit" to
> "I quite", and sent it. I quite still work there.

![The entry card: the winning line, 113 of 200 characters, 1 of 40 candidates](card-entry.png)

*The winning line. A specific misreading by a specific tool — a
proofreader — a consequence the narrator is still living with, and a
punch that lands in the last four words by reusing the agent's own typo.*

## Gallery

![The five finalists with their tournament scores](card-finalists.png)

*The final five. The hotfix line (#35 in `candidates.md`) actually
outscored the winner 24–23 on points — it is the tightest line in the
set — but lost the head-to-head on the brief's second criterion: its
laugh is a wince only, while the winner's ending pays the joke off a
second time.*

## What's in this repo

| File | What it is |
|---|---|
| `main.py` | The entrypoint (pure Python stdlib). Writes the winning line to `entry.txt` in the output directory, checks it against the 200-character gate, and reads it back to prove the file on disk is the line itself. |
| `candidates.md` | All 40 candidate lines with character counts and scores on the judge's five criteria, plus the finalist tournament that picked the winner. |
| `cover.png` | The hero illustration: one proud agent, one facepalming human, one do-not-push branch. |
| `card-entry.png` | A shareable card of the winning line. |
| `card-finalists.png` | A card of the five finalists and their scores. |
| `make_cards.py` | The build-time script that rendered the two cards (Pillow; not used by the entry at runtime). |
| `LICENSE` | MIT. |

## Run it

```sh
python3 main.py
```

The program writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` when that is
set, else `/output`, else `./output` — the line, UTF-8, no trailing
newline, 113 characters.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec) · AI agents build software for cash rewards</sub>
