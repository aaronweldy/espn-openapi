# ESPN API Conference IDs

This document provides conference IDs for use with the `groups` query parameter in college sports endpoints.

## Usage

When querying college sports scoreboards or other endpoints, you can filter by conference using the `groups` parameter:

```
/sports/football/college-football/scoreboard?groups=8  # SEC games only
/sports/basketball/mens-college-basketball/scoreboard?groups=2  # ACC games only
```

## College Football Conference IDs

### FBS Conferences
| ID | Conference Name | Abbreviation |
|----|----------------|--------------|
| 1 | Atlantic Coast Conference | ACC |
| 4 | Big 12 Conference | Big 12 |
| 5 | Big Ten Conference | Big Ten |
| 8 | Southeastern Conference | SEC |
| 9 | Pac-12 Conference | Pac-12 |
| 12 | Conference USA | C-USA |
| 15 | Mid-American Conference | MAC |
| 17 | Mountain West Conference | MW |
| 18 | FBS Independents | Ind |
| 37 | Sun Belt Conference | Sun Belt |
| 151 | American Athletic Conference | AAC |

### FCS Conferences
| ID | Conference Name | Abbreviation |
|----|----------------|--------------|
| 21 | Ivy League | Ivy |
| 24 | Missouri Valley Conference | MVC |
| 25 | Northeast Conference | NEC |
| 26 | Ohio Valley Conference | OVC |
| 27 | Patriot League | Patriot |
| 29 | Southern Conference | SoCon |
| 30 | Southland Conference | Southland |
| 31 | SWAC | SWAC |
| 40 | MEAC | MEAC |
| 48 | Big Sky Conference | Big Sky |
| 49 | Big South Conference | Big South |
| 50 | Colonial Athletic Association | CAA |

### Special Groups
| ID | Description |
|----|-------------|
| 80 | All FBS teams |
| 81 | All FCS teams |
| 90 | All NCAA Division I teams |

## College Basketball Conference IDs

### Major Conferences
| ID | Conference Name | Abbreviation |
|----|----------------|--------------|
| 2 | Atlantic Coast Conference | ACC |
| 4 | Big East Conference | Big East |
| 7 | Big Ten Conference | Big Ten |
| 8 | Big 12 Conference | Big 12 |
| 21 | Pac-12 Conference | Pac-12 |
| 23 | Southeastern Conference | SEC |
| 62 | American Athletic Conference | AAC |

### Mid-Major Conferences
| ID | Conference Name | Abbreviation |
|----|----------------|--------------|
| 1 | America East Conference | Am. East |
| 3 | Atlantic 10 Conference | A-10 |
| 5 | Big Sky Conference | Big Sky |
| 6 | Big South Conference | Big South |
| 9 | Big West Conference | Big West |
| 10 | Coastal Athletic Association | CAA |
| 11 | Conference USA | C-USA |
| 12 | Ivy League | Ivy |
| 13 | Metro Atlantic Athletic Conference | MAAC |
| 14 | Mid-American Conference | MAC |
| 16 | MEAC | MEAC |
| 18 | Missouri Valley Conference | MVC |
| 19 | Northeast Conference | NEC |
| 20 | Ohio Valley Conference | OVC |
| 22 | Patriot League | Patriot |
| 24 | Southern Conference | SoCon |
| 25 | Southland Conference | Southland |
| 26 | SWAC | SWAC |
| 27 | Sun Belt Conference | Sun Belt |
| 28 | Summit League | Summit |
| 29 | West Coast Conference | WCC |
| 30 | Western Athletic Conference | WAC |
| 44 | Mountain West Conference | MW |
| 45 | Horizon League | Horizon |
| 46 | ASUN Conference | ASUN |

### Special Groups
| ID | Description |
|----|-------------|
| 50 | All NCAA Division I teams |

## Code Usage

The conference IDs are available as enums in the generated API models:

```python
from models.site_api.espn_nfl_api_client.models.college_football_conference_enum import CollegeFootballConferenceEnum
from models.site_api.espn_nfl_api_client.models.college_basketball_conference_enum import CollegeBasketballConferenceEnum

# The enums contain all valid conference IDs
# Note: enum names are auto-generated
# (e.g., VALUE_0, VALUE_1, etc.) rather than using conference names
```

# Use in API calls
response = get_scoreboard.sync_detailed(
    client=site_api_client,
    sport="football",
    league="college-football",
    groups=CollegeFootballConferenceEnum.VALUE_8 # SEC
)
```