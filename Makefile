.PHONY: openapi openapi-site openapi-sports-core openapi-site-web openapi-fantasy run-test

# Main target to generate clients for all OpenAPI specs
openapi: openapi-site openapi-sports-core openapi-site-web openapi-fantasy

# Generate Python client for site.api.espn.com
openapi-site:
	openapi-python-client generate --path spec-site-api.yaml --output-path models/site_api/ --overwrite

# Generate Python client for sports.core.api.espn.com
openapi-sports-core:
	openapi-python-client generate --path spec-sports-core-api.yaml --output-path models/sports_core_api/ --overwrite

# Generate Python client for site.web.api.espn.com
openapi-site-web:
	openapi-python-client generate --path spec-site-web-api.yaml --output-path models/site_web_api/ --overwrite

# Generate Python client for fantasy.espn.com
openapi-fantasy:
	openapi-python-client generate --path spec-fantasy.yaml --output-path models/fantasy_api/ --overwrite

openapi-cdn:
	openapi-python-client generate --path spec-cdn.yaml --output-path models/cdn_api/ --overwrite

# Run a specific test file
run-test:
	uv run $(TEST_FILE)

# Clean generated models
clean:
	rm -rf models/site_api/ models/sports_core_api/ models/site_web_api/ models/fantasy_api/ 