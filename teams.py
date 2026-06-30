TEAM_ALIASES = {
    "ducks": "ANA",
    "anaheim": "ANA",
    "anaheim ducks": "ANA",

    "bruins": "BOS",
    "boston": "BOS",
    "boston bruins": "BOS",

    "sabres": "BUF",
    "buffalo": "BUF",
    "buffalo sabres": "BUF",

    "flames": "CGY",
    "calgary": "CGY",
    "calgary flames": "CGY",

    "hurricanes": "CAR",
    "canes": "CAR",
    "carolina": "CAR",
    "carolina hurricanes": "CAR",

    "blackhawks": "CHI",
    "hawks": "CHI",
    "chicago": "CHI",
    "chicago blackhawks": "CHI",

    "avalanche": "COL",
    "avs": "COL",
    "colorado": "COL",
    "colorado avalanche": "COL",

    "blue jackets": "CBJ",
    "jackets": "CBJ",
    "columbus": "CBJ",
    "columbus blue jackets": "CBJ",

    "stars": "DAL",
    "dallas": "DAL",
    "dallas stars": "DAL",

    "red wings": "DET",
    "wings": "DET",
    "detroit": "DET",
    "detroit red wings": "DET",

    "oilers": "EDM",
    "edmonton": "EDM",
    "edmonton oilers": "EDM",

    "panthers": "FLA",
    "florida": "FLA",
    "florida panthers": "FLA",

    "kings": "LAK",
    "la kings": "LAK",
    "los angeles": "LAK",
    "los angeles kings": "LAK",

    "wild": "MIN",
    "minnesota": "MIN",
    "minnesota wild": "MIN",

    "canadiens": "MTL",
    "canadians": "MTL",
    "habs": "MTL",
    "montreal": "MTL",
    "montreal canadiens": "MTL",

    "predators": "NSH",
    "preds": "NSH",
    "nashville": "NSH",
    "nashville predators": "NSH",

    "devils": "NJD",
    "new jersey": "NJD",
    "new jersey devils": "NJD",

    "islanders": "NYI",
    "isles": "NYI",
    "new york islanders": "NYI",

    "rangers": "NYR",
    "new york rangers": "NYR",

    "senators": "OTT",
    "sens": "OTT",
    "ottawa": "OTT",
    "ottawa senators": "OTT",

    "flyers": "PHI",
    "philadelphia": "PHI",
    "philadelphia flyers": "PHI",

    "penguins": "PIT",
    "pens": "PIT",
    "pittsburgh": "PIT",
    "pittsburgh penguins": "PIT",

    "sharks": "SJS",
    "san jose": "SJS",
    "san jose sharks": "SJS",

    "kraken": "SEA",
    "seattle": "SEA",
    "seattle kraken": "SEA",

    "blues": "STL",
    "st louis": "STL",
    "st. louis": "STL",
    "st louis blues": "STL",
    "st. louis blues": "STL",

    "lightning": "TBL",
    "bolts": "TBL",
    "tampa bay": "TBL",
    "tampa bay lightning": "TBL",

    "leafs": "TOR",
    "maple leafs": "TOR",
    "toronto": "TOR",
    "toronto maple leafs": "TOR",

    "utah": "UTA",
    "utah hockey club": "UTA",
    "mammoth": "UTA",
    "utah mammoth": "UTA",

    "canucks": "VAN",
    "vancouver": "VAN",
    "vancouver canucks": "VAN",

    "golden knights": "VGK",
    "knights": "VGK",
    "vegas": "VGK",
    "vegas golden knights": "VGK",

    "capitals": "WSH",
    "caps": "WSH",
    "washington": "WSH",
    "washington capitals": "WSH",

    "jets": "WPG",
    "winnipeg": "WPG",
    "winnipeg jets": "WPG",
}


TEAM_NAMES = {
    "ANA": "Anaheim Ducks",
    "BOS": "Boston Bruins",
    "BUF": "Buffalo Sabres",
    "CGY": "Calgary Flames",
    "CAR": "Carolina Hurricanes",
    "CHI": "Chicago Blackhawks",
    "COL": "Colorado Avalanche",
    "CBJ": "Columbus Blue Jackets",
    "DAL": "Dallas Stars",
    "DET": "Detroit Red Wings",
    "EDM": "Edmonton Oilers",
    "FLA": "Florida Panthers",
    "LAK": "Los Angeles Kings",
    "MIN": "Minnesota Wild",
    "MTL": "Montreal Canadiens",
    "NSH": "Nashville Predators",
    "NJD": "New Jersey Devils",
    "NYI": "New York Islanders",
    "NYR": "New York Rangers",
    "OTT": "Ottawa Senators",
    "PHI": "Philadelphia Flyers",
    "PIT": "Pittsburgh Penguins",
    "SJS": "San Jose Sharks",
    "SEA": "Seattle Kraken",
    "STL": "St. Louis Blues",
    "TBL": "Tampa Bay Lightning",
    "TOR": "Toronto Maple Leafs",
    "UTA": "Utah Mammoth",
    "VAN": "Vancouver Canucks",
    "VGK": "Vegas Golden Knights",
    "WSH": "Washington Capitals",
    "WPG": "Winnipeg Jets",
}


def normalize_team_name(team_name):
    cleaned_name = team_name.strip().lower()

    if cleaned_name not in TEAM_ALIASES:
        return None

    return TEAM_ALIASES[cleaned_name]


def get_team_name(team_code):
    return TEAM_NAMES.get(team_code, team_code)