Your job is to create an OpenAPI schema (v3.0.0) for the entire ESPN API.

Use the following two links as a reference:
- https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b
- https://github.com/pseudo-r/Public-ESPN-API

Use those files to find the entire set of endpoints you need to generate schemas for.

Your workflow should look like the following:
1. Find an endpoint that is not documented in @spec.yaml.
2. Fetch that endpoint to get an example JSON response. Put this in @json_output.
3. Add the endpoint to spec.yaml. Figure out what models are missing.
4. Add definitions for those models, and run `openapi-python-client generate --path optimizer/espn-api/spec.yaml --output-path optimizer/espn-api/models/ --overwrite`
5. Test the model definitions by making an API call to the new route using the generated Python models in @test-api.py. (run with `uv run espn-api/tests/test-api.py`). Make sure the fields are populated as expected. Put tests in @tests.
6. If anything goes wrong in your test, repeat steps 2-5 again.
7. Once you have fully verified that the new generated types work, pick a new endpoint and start again. Make a Git commit with the new changes. Do NOT consider your job complete until your tests can fully parse the API response with the generated codes.

Keep going until you have a comprehensive OpenAPI spec of all endpoints. Feel free to fetch API routes directly, if it's helpful.