from rich.console import Console
from rich.table import Table

from nhl_api import fetch_team_schedule
from teams import get_team_name, normalize_team_name

console = Console()


def parse_opponents(opponents_text):
    opponents = []

    for opponent in opponents_text.split(","):
        cleaned_name = opponent.strip()

        if cleaned_name:
            opponents.append(cleaned_name)

    return opponents


def find_matching_games(games, favorite_team_code, opponent_codes):
    matching_games = []

    for game in games:
        game_type = game.get("gameType")

        if game_type != 2:
            continue

        home_team = game["homeTeam"]["abbrev"]
        away_team = game["awayTeam"]["abbrev"]

        if home_team == favorite_team_code:
            opponent_code = away_team
            home_away = "Home"
        else:
            opponent_code = home_team
            home_away = "Away"

        if opponent_code in opponent_codes:
            matching_games.append(
                {
                    "date": game.get("gameDate", "Unknown"),
                    "opponent": opponent_code,
                    "home_away": home_away,
                    "venue": game.get("venue", {}).get("default", "Unknown"),
                }
            )

    return matching_games


def main():
    console.print("[bold blue]NHL Schedule CLI[/bold blue]")

    favorite_team = input("Enter your favorite team: ").strip()
    opponents_text = input("Enter 1 to 5 opponents, separated by commas: ").strip()

    opponents = parse_opponents(opponents_text)

    if len(opponents) < 1:
        console.print("[red]Please enter at least one opponent.[/red]")
        return

    if len(opponents) > 5:
        console.print("[red]Please enter no more than five opponents.[/red]")
        return

    favorite_team_code = normalize_team_name(favorite_team)

    if favorite_team_code is None:
        console.print(f"[red]Unknown favorite team: {favorite_team}[/red]")
        return

    opponent_codes = []

    for opponent in opponents:
        opponent_code = normalize_team_name(opponent)

        if opponent_code is None:
            console.print(f"[red]Unknown opponent: {opponent}[/red]")
            return

        opponent_codes.append(opponent_code)

    console.print()
    console.print(f"Fetching schedule for {favorite_team_code}...")

    schedule_data = fetch_team_schedule(favorite_team_code)

    games = schedule_data.get("games", [])

    matching_games = find_matching_games(games, favorite_team_code, opponent_codes)

    console.print(f"Found {len(matching_games)} matching regular-season games.")

    results_table = Table(title="Matching Games")
    results_table.add_column("Date")
    results_table.add_column("Opponent")
    results_table.add_column("Home/Away")
    results_table.add_column("Venue")

    for game in matching_games:
        results_table.add_row(
            game["date"],
            get_team_name(game["opponent"]),
            game["home_away"],
            game["venue"],
        )

    console.print()
    console.print(results_table)


if __name__ == "__main__":
    main()