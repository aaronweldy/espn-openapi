#!/usr/bin/env python3
"""
HTTP Request MCP Server

A simple MCP server that provides HTTP request capabilities.
"""

import httpx
from mcp.server.fastmcp import FastMCP

# Create the FastMCP server
mcp = FastMCP("http-request-server")


@mcp.tool()
async def http_request(
    url: str, method: str = "GET", output_file: str | None = None
) -> str | None:
    """
    Make an HTTP request to any URL.

    Args:
        url: The URL to request
        method: The HTTP method (GET or POST)
        output_file: The file to write the response to (optional)
    Returns:
        The response body as text, or None if output_file is provided
    """
    async with httpx.AsyncClient() as client:
        if method.upper() == "GET":
            response = await client.get(url)
        elif method.upper() == "POST":
            response = await client.post(url)
        else:
            return f"Unsupported method: {method}"

        if output_file:
            with open(output_file, "w") as f:
                f.write(response.text)
        else:
            return response.text


# This is required for the MCP CLI to find the server
if __name__ == "__main__":
    # The server will be run by the MCP CLI
    pass
