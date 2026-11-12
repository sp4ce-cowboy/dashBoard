<div align="center">

# dashBoard

**Your whole life as a scoreboard: weighted "directives" in a CSV, and one number for how intact
things are.**<br>
A terminal app in Python and pandas that tracks life domains, sub-areas and directives, scores
them, and reports four indices (overall, daily, entropy and critical), with a timestamped journal
and a day's task pad. Written in Dec 2022.

[![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)](https://github.com/sp4ce-cowboy/dashBoard/blob/36c240ad9e0514e75006f436768333133055316d/main.py#L225-L295)
[![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)](https://github.com/sp4ce-cowboy/dashBoard/blob/36c240ad9e0514e75006f436768333133055316d/main.py#L325-L349)

![Python](https://img.shields.io/badge/Python-450%20lines-555?style=flat-square)

</div>

> [!NOTE]
> This consolidated README page was added by
> [Claude Opus 5.5](https://docs.anthropic.com/en/docs/claude-code) in Nov 2026 using my
> [agentic-repo-analysis](https://github.com/sp4ce-cowboy/agentic-workflows) skill, from the
> project's code, the release and my Orbital proposal. The project itself is from Dec 2022. The
> original README, with more screenshots and the apps that inspired it, is in
> **[README-ORIGINAL.md](README-ORIGINAL.md)**.

## At a glance

| | |
|---|---|
| **What** | A command-line life-organisation system: split life into domains and sub-areas, give each a weighted directive, tick them off, and see a fulfilment ratio |
| **Context** | A personal project from the Dec 2022 winter break, after NUS CS1010E. The idea grew into my [Orbital 2023 proposal](ORBITAL_PROPOSAL.pdf), *P.O.S (Personal Organization System)* |
| **Stack** | Python 3, pandas, CSV and plain-text files |

<img width="760" alt="dashBoard" src="https://github.com/sp4ce-cowboy/dashBoard/assets/19762596/86197e41-1af6-4707-926a-117ed7567fa4">

## The concept

> *"What is not defined cannot be measured. What is not measured, cannot be improved."*

1. Split your life into **domains** (Health, Organisation, Finance…) and those into sub-areas.
2. Give each sub-area **directives** ("Drink 4 l of water daily", "Pay bills on time"), each with a
   weight.
3. Mark each directive **quotidian** (daily) or **entropic** (things that decay if ignored, like a
   budget or a passport), and flag the **critical** ones.
4. Complete them as they come up, and read the indices at any time.

## How it works

Everything lives in readable files beside the program, so deleting the app never deletes your data:

| File | Holds |
|---|---|
| `directives.csv` | One row per directive: domain, entropy type, time of day, points earned, weight, critical flag ([a sample](https://github.com/sp4ce-cowboy/dashBoard/releases/tag/v1.0) ships with the release) |
| `notepad.txt` | Journal entries, each stamped with the date and time |
| `taskpad.txt` | Today's tasks |

- **Indices** ([`Stats`](https://github.com/sp4ce-cowboy/dashBoard/blob/36c240ad9e0514e75006f436768333133055316d/main.py#L225-L295)):
  points earned ÷ total weight, as a percentage, for all directives, the daily ones, the entropic
  ones and the critical ones.
- **Views:** all directives, or sorted by type, by time of day, or by completion, read and filtered
  with pandas.
- **Actions** ([`Execute`](https://github.com/sp4ce-cowboy/dashBoard/blob/36c240ad9e0514e75006f436768333133055316d/main.py#L325-L349),
  `Reset`, `partReset`): complete directives by ID (full points), start a new day by resetting
  the daily ones, or reset everything.
- **Home screen:** the day of the year (Julian day), the date and time, and today's tasks.

## Skills shown

| Skill | Where it shows (click the links for the code) | Docs |
|---|---|---|
| **Python**<br><img alt="Python" src="https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white"> | A menu-driven terminal app with nested functions and file I/O: [`main.py`](https://github.com/sp4ce-cowboy/dashBoard/blob/36c240ad9e0514e75006f436768333133055316d/main.py) | [Python docs](https://docs.python.org/3/) |
| **Data handling with pandas** | Reading, filtering, updating and writing the directives CSV: [`Execute`](https://github.com/sp4ce-cowboy/dashBoard/blob/36c240ad9e0514e75006f436768333133055316d/main.py#L325-L349) | [pandas](https://pandas.pydata.org/docs/) |
| **Metric design** | Four weighted fulfilment indices from one dataset: [`Stats`](https://github.com/sp4ce-cowboy/dashBoard/blob/36c240ad9e0514e75006f436768333133055316d/main.py#L225-L295) | |
| **Product thinking** | User stories, a feature timeline and a ranking and gamification design in the [Orbital proposal](ORBITAL_PROPOSAL.pdf) | |

## On my resume

**Skills:** Python · pandas · CSV data · CLI design · metric design · product proposal

- Built a terminal life-organisation app in Python and pandas (450 lines) that stores weighted "directives" in a CSV and computes four fulfilment indices: overall, daily, entropic and critical.
- Kept all data in plain CSV and text files beside the program (directives, a timestamped journal, a daily task pad), so it stays readable and survives the app being deleted.
- Turned the idea into a proposal for NUS Orbital 2023: user stories, a scoring and ranking system, a feature timeline and a gamified, multi-user design.

## Getting started

```sh
pip3 install pandas
```

Download [the release](https://github.com/sp4ce-cowboy/dashBoard/releases/tag/v1.0) (it includes
a sample `directives.csv`), unzip it, and run `python3 main.py` in that folder.
