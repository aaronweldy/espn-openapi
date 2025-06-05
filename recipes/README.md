# ESPN API Recipes

This directory contains example "recipes" demonstrating common use cases for the ESPN API. Each recipe is a self-contained example showing how to use the generated API client models to accomplish specific tasks.

## Available Recipes

### 1. Today's Scores Across All Sports (`today_scores_all_sports/`)
Fetches and displays live scores from NFL, NBA, MLB, and NHL games happening today. Great for building sports dashboards or quick score checking applications.

**Key Features:**
- Multi-sport scoreboard support (NFL, NBA, MLB, NHL)
- Real-time game status (Final, In Progress, Scheduled)
- Team records and scores
- Flexible date selection
- JSON export capability

**Example Usage:**
```bash
# Get all sports scores for today
python recipes/today_scores_all_sports/recipe.py

# Get NFL scores for a specific date
python recipes/today_scores_all_sports/recipe.py --sport nfl --date 20240908

# Export to JSON
python recipes/today_scores_all_sports/recipe.py --output json --save scores.json
```

### 2. Fantasy Ownership Tracker (`fantasy_ownership_tracker/`)
Tracks fantasy football player ownership percentages and identifies trending players. Useful for finding waiver wire targets and monitoring player value changes.

**Key Features:**
- Top owned players display
- Player search functionality
- Ownership trend tracking (with historical data)
- PPR and standard scoring support
- Data export for trend analysis

**Example Usage:**
```bash
# Show top 20 owned players
python recipes/fantasy_ownership_tracker/recipe.py --top 20

# Search for specific players
python recipes/fantasy_ownership_tracker/recipe.py --players "Patrick Mahomes" "Justin Jefferson"

# Track ownership changes (requires historical data)
python recipes/fantasy_ownership_tracker/recipe.py --movers --days 7

# Export current snapshot for future comparisons
python recipes/fantasy_ownership_tracker/recipe.py --export ownership_snapshot.json
```

## Recipe Structure

Each recipe follows a standard structure:
- `README.md` - Detailed documentation including usage, customization options, and examples
- `recipe.py` - The Python implementation using generated API models
- `requirements.txt` - Additional dependencies (if needed beyond the base ESPN API client)

## Using Recipes

1. **Ensure the ESPN API client is installed:**
   ```bash
   cd /path/to/espn-api
   pip install -e .
   ```

2. **Navigate to a recipe directory:**
   ```bash
   cd recipes/today_scores_all_sports
   ```

3. **Run the recipe:**
   ```bash
   python recipe.py
   ```

4. **Check the README for customization options:**
   ```bash
   python recipe.py --help
   ```

## Creating New Recipes

To create a new recipe, follow the [Recipe Specification](../RECIPE_SPEC.md). Key requirements:

1. Use the generated models from the `models/` directory
2. Include comprehensive error handling
3. Provide both basic and advanced usage examples
4. Document all customization options
5. Make the code reusable and importable

## Recipe Ideas

See [RECIPE_IDEAS.md](../RECIPE_IDEAS.md) for a comprehensive list of recipe ideas covering:
- Live scores and stats
- Fantasy sports analysis
- Historical data trends
- Betting and odds tracking
- Team and player information
- Cross-sport comparisons

## Contributing

When contributing a new recipe:
1. Follow the existing recipe structure
2. Test with real API calls
3. Include example output in the README
4. Consider rate limits and API performance
5. Add your recipe to this README

## Common Patterns

### API Client Creation
```python
# Site API (scores, teams, etc.)
from models.site_api.espn_nfl_api_client import Client as SiteApiClient
client = SiteApiClient(base_url="https://site.api.espn.com/apis/site/v2")

# Fantasy API
from models.fantasy_api.espn_fantasy_api_client import Client as FantasyApiClient
client = FantasyApiClient(base_url="https://lm-api-reads.fantasy.espn.com")
```

### Error Handling
```python
try:
    response = api_call.sync_detailed(client=client, ...)
    if response.status_code == 200:
        return response.parsed
    else:
        print(f"Error: HTTP {response.status_code}")
except Exception as e:
    print(f"API Error: {e}")
```

### Working with UNSET Values
```python
# UNSET is falsy, so you can use simple if statements
if player.stats:  # Instead of: if player.stats is not UNSET
    process_stats(player.stats)
```

### Handling Different Response Types
```python
# Some endpoints return different types based on success/error
if isinstance(response.parsed, ExpectedType):
    # Process successful response
else:
    # Handle error response
```

## Troubleshooting

- **403 Errors**: Ensure you're using the correct base URL for each API
- **Import Errors**: Ensure you've run `make openapi` to generate the latest models
- **Missing Data**: Check if fields exist with `hasattr()` before accessing
- **Type Errors**: The generated models use specific types - check the model definitions

## Notes

- The ESPN API is unofficial and may change without notice
- Be mindful of rate limits when making repeated requests
- Some endpoints require specific parameters (e.g., dates for scoreboards)
- Fantasy data typically requires a valid season year