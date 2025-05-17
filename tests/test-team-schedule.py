import os
from models.site_api.espn_nfl_api_client import Client
from models.site_api.espn_nfl_api_client.api.default.get_nfl_team_schedule import sync
from models.site_api.espn_nfl_api_client.models.nfl_team_schedule_response import (
    NFLTeamScheduleResponse,
)
from models.site_api.espn_nfl_api_client.types import UNSET


def test_get_nfl_team_schedule():
    client = Client(
        base_url=os.environ.get(
            "SITE_API_BASE_URL", "https://site.api.espn.com/apis/site/v2"
        )
    )
    team_id = "12"  # 49ers
    response = sync(team_id=team_id, client=client)
    assert isinstance(response, NFLTeamScheduleResponse)
    print(f"Timestamp: {response.timestamp}")
    print(f"Status: {response.status}")
    print(f"Team: {response.team.display_name}")
    print(f"Season: {response.season.year}")
    print(f"Events: {len(response.events)} games")
    if response.events:
        print(f"First event: {response.events[0].name} on {response.events[0].date}")
    print(f"Bye week: {response.bye_week}")


if __name__ == "__main__":
    test_get_nfl_team_schedule()
