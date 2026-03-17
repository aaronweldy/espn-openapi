from models.site_api.espn_nfl_api_client.api.default import get_scoreboard
from models.site_api.espn_nfl_api_client.models.generic_scoreboard_response import (
    GenericScoreboardResponse,
)
from models.site_api.espn_nfl_api_client.models.get_scoreboard_seasontype import (
    GetScoreboardSeasontype,
)
from models.site_api.espn_nfl_api_client.models.get_scoreboard_sport import (
    GetScoreboardSport,
)


def test_ncaa_mens_postseason_scoreboard_tournament_window(site_api_client):
    resp = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport=GetScoreboardSport.BASKETBALL,
        league="mens-college-basketball",
        seasontype=GetScoreboardSeasontype.VALUE_3,
        dates="20250321",
    )
    assert resp.status_code == 200, f"expected 200, got {resp.status_code}"
    data = resp.parsed
    assert isinstance(data, GenericScoreboardResponse)
    assert data.events is not None and len(data.events) >= 4
    first = data.events[0]
    assert first.id
    assert first.competitions


def test_ncaa_womens_postseason_scoreboard_tournament_window(site_api_client):
    resp = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport=GetScoreboardSport.BASKETBALL,
        league="womens-college-basketball",
        seasontype=GetScoreboardSeasontype.VALUE_3,
        dates="20250322",
    )
    assert resp.status_code == 200, f"expected 200, got {resp.status_code}"
    data = resp.parsed
    assert isinstance(data, GenericScoreboardResponse)
    assert data.events is not None and len(data.events) >= 4
