#!/usr/bin/env python
"""
Quick validation script for ESPN API endpoints.

Usage:
    python scripts/validate_endpoint.py <url>
    python scripts/validate_endpoint.py <url> --save
    python scripts/validate_endpoint.py <url> --jq '.sports[0].leagues[0]'

Examples:
    python scripts/validate_endpoint.py "https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/teams"
    python scripts/validate_endpoint.py "https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/teams" --save
    python scripts/validate_endpoint.py "https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/teams" --jq '.sports[0].leagues[0].teams | length'
"""

import argparse
import json
import os
import sys
import subprocess
from urllib.parse import urlparse
from pathlib import Path
import requests


def validate_endpoint(url: str, save: bool = False, jq_filter: str = None) -> dict:
    """
    Validate an ESPN API endpoint quickly.
    
    Args:
        url: The API endpoint URL
        save: Whether to save the response to json_output/
        jq_filter: Optional jq filter to apply to the response
        
    Returns:
        The parsed JSON response
    """
    try:
        # Make the request
        print(f"🔍 Testing endpoint: {url}")
        response = requests.get(url, timeout=10)
        
        # Check status code
        if response.status_code == 200:
            print(f"✅ Status Code: {response.status_code}")
        else:
            print(f"❌ Status Code: {response.status_code}")
            print(f"Response: {response.text[:500]}...")
            return None
            
        # Parse JSON
        try:
            data = response.json()
            print("✅ Valid JSON response")
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON: {e}")
            return None
            
        # Apply jq filter if provided
        if jq_filter:
            try:
                # Write temp file for jq
                import tempfile
                with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
                    json.dump(data, f)
                    temp_path = f.name
                
                # Run jq
                result = subprocess.run(
                    ['jq', jq_filter, temp_path],
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0:
                    print(f"\n📊 JQ Filter Result ({jq_filter}):")
                    print(result.stdout)
                else:
                    print(f"❌ JQ Error: {result.stderr}")
                    
                # Clean up
                os.unlink(temp_path)
                
            except FileNotFoundError:
                print("⚠️  jq not found. Install with: sudo apt-get install jq")
            except Exception as e:
                print(f"❌ JQ Error: {e}")
        
        # Show response structure
        print("\n📋 Response Structure:")
        def show_structure(obj, indent=0):
            """Show the structure of the response."""
            prefix = "  " * indent
            if isinstance(obj, dict):
                keys = list(obj.keys())[:10]  # Show first 10 keys
                for key in keys:
                    value = obj[key]
                    if isinstance(value, (dict, list)):
                        print(f"{prefix}{key}: {type(value).__name__}")
                        if indent < 2:  # Limit depth
                            show_structure(value, indent + 1)
                    else:
                        print(f"{prefix}{key}: {type(value).__name__}")
                if len(obj) > 10:
                    print(f"{prefix}... and {len(obj) - 10} more keys")
            elif isinstance(obj, list) and obj:
                print(f"{prefix}[{len(obj)} items]")
                if indent < 2:  # Show structure of first item
                    show_structure(obj[0], indent + 1)
        
        show_structure(data)
        
        # Show some statistics
        print("\n📊 Response Statistics:")
        response_size = len(response.content)
        print(f"- Response size: {response_size:,} bytes")
        
        if isinstance(data, dict):
            print(f"- Top-level keys: {', '.join(data.keys())}")
            
            # Try to detect common patterns
            if 'sports' in data and isinstance(data['sports'], list):
                sport = data['sports'][0] if data['sports'] else {}
                if 'leagues' in sport and isinstance(sport['leagues'], list):
                    league = sport['leagues'][0] if sport['leagues'] else {}
                    print(f"- Detected pattern: sports > leagues > ...")
                    for key in league:
                        if isinstance(league[key], list):
                            print(f"  - {key}: {len(league[key])} items")
        
        # Save if requested
        if save:
            # Extract filename from URL
            parsed = urlparse(url)
            path_parts = parsed.path.strip('/').split('/')
            
            # Create a reasonable filename
            if 'sports' in path_parts:
                # Extract sport and league
                sport_idx = path_parts.index('sports')
                if sport_idx + 2 < len(path_parts):
                    sport = path_parts[sport_idx + 1]
                    league = path_parts[sport_idx + 2]
                    resource = path_parts[-1] if len(path_parts) > sport_idx + 3 else 'data'
                    filename = f"{sport}_{league}_{resource}.json"
                else:
                    filename = "api_response.json"
            else:
                filename = path_parts[-1] + ".json" if path_parts else "api_response.json"
                
            output_path = Path("json_output") / filename
            output_path.parent.mkdir(exist_ok=True)
            
            with open(output_path, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"\n💾 Saved to: {output_path}")
            
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Quick validation script for ESPN API endpoints",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("url", help="The API endpoint URL to test")
    parser.add_argument("--save", action="store_true", help="Save response to json_output/")
    parser.add_argument("--jq", help="Apply a jq filter to the response")
    
    args = parser.parse_args()
    
    # Validate the URL
    if not args.url.startswith(('http://', 'https://')):
        print("❌ Error: URL must start with http:// or https://")
        sys.exit(1)
        
    # Run validation
    data = validate_endpoint(args.url, args.save, args.jq)
    
    if data:
        print("\n✅ Endpoint validation successful!")
        sys.exit(0)
    else:
        print("\n❌ Endpoint validation failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()