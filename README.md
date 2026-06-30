# NHL Schedule CLI

A simple command-line Python application that retrieves an NHL team's regular season schedule and displays games against your favorite opponents. The idea is to have an app that's a simple helper for identifying games that you might want to watch or go see live.

Note: I'm building this end of June 2026. The 2026/2027 season schedule has not been released by the NHL yet. I'm curring using the NHL api to pull down the 2025/2026 season schedule. I plan to update it as soon as the new schedule is made available. 

It's set [on line 3]([https://github.com/jcasman/nhl-schedule-cli/blob/f272031667dbdc920b39cfc1b30ccb8f38d623fe/nhl_api.py#L3](https://github.com/jcasman/nhl-schedule-cli/blob/f272031667dbdc920b39cfc1b30ccb8f38d623fe/nhl_api.py#L3)) in nhl_api.py `SEASON = "20252026"`

## Features

- Choose your favorite NHL team. Mine is the Anaheim Ducks. But you can choose whichever not as good team as you like.

- Choose 1–5 favorite opponents.

- Download the NHL regular season schedule.

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

## Roadmap

Future enhancements may include:

- Interactive team selection menu

- Calendar export (ICS)

- Team logos

- Playoff schedule support

- Favorite teams saved locally

- Travel itinerary support