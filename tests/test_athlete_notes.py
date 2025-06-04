import json
import pytest
from models.sports_core_api.espn_sports_core_api_client.api.default import get_athlete_season_notes
from models.sports_core_api.espn_sports_core_api_client.models import AthleteNotesResponse, AthleteNote


@pytest.mark.api
@pytest.mark.parametrize("sport,league,year,athlete_id,expected_min_notes", [
    ("football", "nfl", "2025", "3139477", 1),  # Patrick Mahomes
    ("basketball", "nba", "2025", "1966", 1),  # LeBron James
    ("baseball", "mlb", "2025", "33912", 1),  # Cody Bellinger
    ("hockey", "nhl", "2025", "3024816", 0),  # Nathan MacKinnon - may have no notes
])
def test_get_athlete_season_notes(sports_core_api_client, sport, league, year, athlete_id, expected_min_notes, ensure_json_output_dir):
    """Test getting athlete season notes across different sports."""
    response = get_athlete_season_notes.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
        athlete_id=athlete_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, AthleteNotesResponse), "Response should parse to AthleteNotesResponse"
    
    # Validate response structure
    assert hasattr(result, 'count'), "Response should have count"
    assert hasattr(result, 'page_index'), "Response should have page_index"
    assert hasattr(result, 'page_size'), "Response should have page_size"
    assert hasattr(result, 'page_count'), "Response should have page_count"
    assert hasattr(result, 'items'), "Response should have items"
    
    # Validate pagination
    if result.count > 0:
        assert result.page_index >= 1, "Page index should be at least 1 when there are results"
    else:
        assert result.page_index >= 0, "Page index should be non-negative when there are no results"
    assert result.page_size > 0, "Page size should be positive"
    assert result.page_count >= 0, "Page count should be non-negative"
    
    # Validate notes
    assert result.count >= expected_min_notes, f"Expected at least {expected_min_notes} notes, got {result.count}"
    assert len(result.items) == min(result.count, result.page_size), "Items length should match count or page size"
    
    # Validate each note
    for note in result.items:
        assert isinstance(note, AthleteNote), "Each item should be an AthleteNote"
        assert note.id, "Note should have an ID"
        assert note.type, "Note should have a type"
        assert note.date, "Note should have a date"
        assert note.headline, "Note should have a headline"
        assert note.text, "Note should have text"
        assert note.source, "Note should have a source"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/athlete_notes_{sport}_{athlete_id}_{year}_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    print(f"✓ {sport.upper()} athlete {athlete_id} has {result.count} notes for {year} season")


@pytest.mark.api
def test_get_athlete_season_notes_invalid_athlete(sports_core_api_client):
    """Test getting notes for invalid athlete ID."""
    response = get_athlete_season_notes.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        year="2025",
        athlete_id="99999999"  # Invalid athlete ID
    )
    
    # The API may return 200 with empty results or 404
    assert response.status_code in [200, 404], f"Expected status code 200 or 404, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        assert result.count == 0, "Invalid athlete should have no notes"
        assert len(result.items) == 0, "Invalid athlete should have empty items list"


@pytest.mark.api 
def test_get_athlete_season_notes_past_year(sports_core_api_client):
    """Test getting notes for past year."""
    response = get_athlete_season_notes.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl", 
        year="2023",  # Past year
        athlete_id="3139477"
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, AthleteNotesResponse), "Response should parse to AthleteNotesResponse"
    # Past years may or may not have notes, just validate the structure
    assert hasattr(result, 'count'), "Response should have count"
    assert hasattr(result, 'items'), "Response should have items"