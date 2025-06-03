#!/usr/bin/env python3
"""
HTTP Request MCP Server

A simple MCP server that provides HTTP request capabilities.
"""

import subprocess
import httpx
from mcp.server.fastmcp import FastMCP

# Create the FastMCP server
mcp = FastMCP("http-request-server")


@mcp.tool()
async def http_request(
    url: str,
    method: str = "GET",
    headers: dict[str, str] | None = None,
    output_file: str | None = None,
    jq_command: str | None = None,
) -> str | None:
    """
    Make an HTTP request to any URL.

    Args:
        url: The URL to request
        method: The HTTP method (GET or POST)
        headers: Dictionary of HTTP headers to include in the request (optional)
        output_file: The file to write the response to (optional)
        jq_command: A JQ command to run on the response, to filter the response down to specific fields (optional)
    Returns:
        The response body as text, or None if output_file is provided
    Only provide one of output_file or jq_command.
    """
    async with httpx.AsyncClient() as client:
        request_headers = headers or {}
        
        if method.upper() == "GET":
            response = await client.get(url, headers=request_headers)
        elif method.upper() == "POST":
            response = await client.post(url, headers=request_headers)
        else:
            return f"Unsupported method: {method}"

        if output_file:
            with open(output_file, "w") as f:
                f.write(response.text)
        elif jq_command:
            return subprocess.run(
                ["jq", *jq_command.split(" ")],
                input=response.text,
                capture_output=True,
                text=True,
            ).stdout
        else:
            return response.text


# This is required for the MCP CLI to find the server
if __name__ == "__main__":
    # The server will be run by the MCP CLI
    pass
