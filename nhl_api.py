import requests

SEASON = "20252026"


def fetch_team_schedule(team_code):
    url = f"https://api-web.nhle.com/v1/club-schedule-season/{team_code}/{SEASON}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()