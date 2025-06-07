#!/usr/bin/env python3
"""
Example usage of the Game Flow Tracker recipes.
"""

import subprocess
import sys

def run_example(cmd, description):
    """Run an example command and show the description."""
    print(f"\n{'='*60}")
    print(f"EXAMPLE: {description}")
    print(f"COMMAND: {cmd}")
    print(f"{'='*60}\n")
    
    subprocess.run(cmd, shell=True)

def main():
    """Run various examples of the game flow tracker."""
    
    print("GAME FLOW TRACKER EXAMPLES")
    print("=" * 60)
    
    # Example 1: Simple NFL game flow
    run_example(
        "python recipes/game_flow_tracker/recipe_simple.py --event-id 401547417",
        "Track NFL game flow (Atlanta vs Green Bay)"
    )
    
    # Example 2: Export game data
    run_example(
        "python recipes/game_flow_tracker/recipe_simple.py --event-id 401547417 --export game_flow.json",
        "Export game flow data to JSON"
    )
    
    # Example 3: Different sport (NBA)
    run_example(
        "python recipes/game_flow_tracker/recipe_simple.py --event-id 401584793 --sport basketball --league nba",
        "Track NBA game flow"
    )
    
    # Example 4: Full play-by-play analysis (NFL only)
    run_example(
        "python recipes/game_flow_tracker/recipe_simple.py --event-id 401547417",
        "Detailed play-by-play analysis (NFL)"
    )
    
    print("\n" + "="*60)
    print("For live tracking, add --live flag:")
    print("python recipes/game_flow_tracker/recipe_simple.py --event-id YOUR_EVENT_ID --live")
    print("="*60)

if __name__ == "__main__":
    main()