import pytest
from models.sports_core_api.espn_sports_core_api_client.models.sport_enum import (
    SportEnum,
)
from models.sports_core_api.espn_sports_core_api_client.models.league_enum import (
    LeagueEnum,
)
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_league_transactions,
)
from models.sports_core_api.espn_sports_core_api_client.models.transactions_list_response import (
    TransactionsListResponse,
)


@pytest.mark.api
def test_get_league_transactions_nfl(sports_core_api_client):
    response = get_league_transactions.sync_detailed(
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        client=sports_core_api_client,
        limit=1,
    )
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )
    result = response.parsed
    assert isinstance(result, TransactionsListResponse), (
        "Response should parse to TransactionsListResponse"
    )
    assert result.count >= 0
    assert isinstance(result.items, list)
    if not result.items:
        print("No transactions returned for this league/sport.")
    else:
        print(f"Number of transactions returned: {len(result.items)}")
        first = result.items[0]
        print(f"Keys in first transaction: {list(first.additional_keys)}")
        for i, item in enumerate(result.items[:3]):
            print(f"Transaction {i + 1}: {item.to_dict()}")
