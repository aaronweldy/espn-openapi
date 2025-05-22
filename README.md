# ESPN API Client for Python

This project provides Python clients for accessing various ESPN APIs, allowing developers to easily integrate ESPN data into their applications. It includes clients for NFL, fantasy sports, and general sports data, along with generated data models and schemas.

## Project Structure

The project is organized into the following main directories:

- **`models/`**: Contains the auto-generated Python API client code for interacting with different ESPN APIs. Each subdirectory within `models/` corresponds to a specific API (e.g., `cdn_api`, `fantasy_api`).
- **`json_schemas/`**: Includes JSON schema files that define the structure of the data expected from the ESPN APIs. These are useful for validation and understanding the API responses.
- **`json_output/`**: Contains example JSON responses from various API endpoints. These can be helpful for development and testing.
- **`tests/`**: Includes a suite of pytest tests for verifying the functionality of the API clients and data models.
- **`spec-*.yaml`**: OpenAPI (Swagger) specification files used to generate the API client code in the `models/` directory.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/espn-api-client.git
    cd espn-api-client
    ```
    *(Replace `https://github.com/your-username/espn-api-client.git` with the actual repository URL if different)*

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## Basic Usage

Here's a simple example of how to use one of the API clients (e.g., the CDN NFL API client):

```python
from models.cdn_api.espn_cdn_nfl_api_client import Client
from models.cdn_api.espn_cdn_nfl_api_client.api.default import get_schedule
from models.cdn_api.espn_cdn_nfl_api_client.models import Schedule

# Initialize the client
# You may need to configure authentication or base URLs depending on the API
client = Client(base_url="https://site.api.espn.com") # Example base URL, adjust as needed

# Make an API request (example: get NFL schedule)
try:
    schedule_response = get_schedule.sync_detailed(client=client)
    schedule_response.raise_for_status()
    schedule: Schedule = schedule_response.parsed
    # Process the schedule data
    if schedule and schedule.weeks:
        print(f"NFL Schedule for week {schedule.weeks[0].number}:")
        for event in schedule.weeks[0].events:
            print(f"- {event.name} ({event.date})")
    else:
        print("No schedule data found.")

except Exception as e:
    print(f"An error occurred: {e}")

```

**Note:** Each API client in the `models/` directory might have slightly different initialization and usage patterns. Refer to the specific client's documentation or code for details. The base URLs for different APIs will also vary.

## Available API Clients

This project includes clients for the following ESPN APIs, located in the `models/` directory:

-   **`models/cdn_api/` (ESPN CDN API)**:
    -   Provides access to content delivery network (CDN) based data. This often includes schedules, scores, and potentially some media content.
    -   Client module: `models.cdn_api.espn_cdn_nfl_api_client` (Example for NFL, other sports might be available)

-   **`models/fantasy_api/` (ESPN Fantasy API)**:
    -   Allows interaction with ESPN's fantasy sports platform. You can manage leagues, teams, players, and scores.
    -   Client module: `models.fantasy_api.espn_fantasy_api_client`

-   **`models/site_api/` (ESPN Site API)**:
    -   Likely interacts with the main ESPN website's public-facing API. This could provide news, articles, standings, and team information.
    -   Client module: `models.site_api.espn_nfl_api_client` (Example for NFL)

-   **`models/site_web_api/` (ESPN Site Web API)**:
    -   Potentially a different or more specific version of the site API, possibly for newer web components or specific data feeds.
    -   Client module: `models.site_web_api.espn_site_web_api_client`

-   **`models/sports_core_api/` (ESPN Sports Core API)**:
    -   This seems to be a core API for sports data, which might include athlete details, event information, statistics, and more across various sports.
    -   Client module: `models.sports_core_api.espn_sports_core_api_client`

Each client is generated from an OpenAPI specification and provides typed data models for API responses. You can explore the respective subdirectories for specific API operations and models.

## Running Tests

The project uses `pytest` for testing. To run the tests:

1.  Ensure you have installed the development dependencies (including `pytest`). If `pytest` is not listed in `requirements.txt`, you might need to install it separately:
    ```bash
    pip install pytest
    ```
    (Or, ideally, add `pytest` to a `requirements-dev.txt` and install from there.)

2.  Navigate to the root directory of the project.

3.  Run pytest:
    ```bash
    pytest
    ```
    This will discover and run all tests in the `tests/` directory. You should see output indicating the status of each test.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these general steps:

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3.  **Make your changes.** Ensure you add or update tests as appropriate.
4.  **Run tests** to ensure everything is working correctly.
5.  **Commit your changes** with a clear and descriptive commit message.
6.  **Push your branch** to your fork:
    ```bash
    git push origin feature/your-feature-name
    ```
7.  **Open a pull request** to the main repository.

Please ensure your code adheres to any existing style guidelines and that all tests pass.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
