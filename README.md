# NHL Schedule CLI

A simple command-line Python application that retrieves an NHL team's regular season schedule and displays games against your favorite opponents. The idea is to have an app that's a simple helper for identifying games that you might want to watch or go see live.

NHL released the 2026/2027 schedule on July 16, 2026. I edited nhl_api.py [on line 3]([https://github.com/jcasman/nhl-schedule-cli/blob/f272031667dbdc920b39cfc1b30ccb8f38d623fe/nhl_api.py#L3](https://github.com/jcasman/nhl-schedule-cli/blob/f272031667dbdc920b39cfc1b30ccb8f38d623fe/nhl_api.py#L3)) to `SEASON = "20262027"`

[https://www.nhl.com/news/nhl-releases-2026-27-regular-season-schedule](https://www.nhl.com/news/nhl-releases-2026-27-regular-season-schedule)

## Features

- Choose your favorite NHL team. Mine is the Anaheim Ducks. But you can choose whichever not-quite-as-good team as you like.
- Choose 1–5 favorite opponents.
- Application uses current NHL regular season schedule.
- Display matching games with:
  - Date
  - Opponent
  - Home or Away
  - Arena



## Requirements

- Python 3.13+
- uv



## Installation

```bash

git clone [https://github.com/jcasman/nhl-schedule-cli.git](https://github.com/jcasman/nhl-schedule-cli.git)

cd nhl-schedule-cli

uv sync

```



## Run

```bash

uv run python [main.py](http://main.py)

```

Example:

```

Favorite team: Ducks

Opponents: Kings, Sharks, Leafs

```



