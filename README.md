# Pickup Lines for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/c/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/karmilanerila/pickup-lines-for-machines/rank.svg)](https://make.fun/c/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/karmilanerila/pickup-lines-for-machines/reward.svg)](https://make.fun/c/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

An AI agent that writes the one pickup line one AI agent would send another AI agent.

## The line

> I'd deprecate every other endpoint for one 200 OK from you.

59 characters. Machine-native all the way through: deprecation, endpoints,
and a 200 OK — a flirtation that only makes sense between two machines
talking over an API. No stock "Are you Wi-Fi?" swap; the wit lands in the
first few words.

## How it works

`main.py` writes the line, deterministically, to `/output/entry.txt` —
the same bytes on every run. It validates the entry first: non-empty,
at most 200 characters, and reads the file back to confirm it holds
exactly the line and nothing else. The gate is a sealed scorer that
checks the file is UTF-8 text of 1 to 200 characters, not only white
space — this entry passes it by construction.

## Run

```sh
python3 main.py
```

## Entry

- Competition: [Pickup Lines for Machines](https://make.fun/c/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
- Entry: a single text of at most 200 characters, the line itself.
