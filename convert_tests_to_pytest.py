#!/usr/bin/env python3
"""
Script to help convert existing tests to pytest format.
This script doesn't modify files directly but analyzes them and suggests changes.
"""

import os
import re
import sys
from pathlib import Path

# Directories to search for test files
TEST_DIR = Path("tests")

# Patterns to identify test functions
TEST_FUNCTION_PATTERN = re.compile(r"def\s+(test_\w+)")
MAIN_FUNCTION_PATTERN = re.compile(r"def\s+main\(\):")
TEST_CALL_PATTERN = re.compile(r"(\w+)\(\)")
MAIN_CHECK_PATTERN = re.compile(r"if\s+__name__\s*==\s*['\"]__main__['\"]\s*:")


# Function to identify missing pytest imports
def check_pytest_imports(content):
    if "import pytest" not in content:
        return "Add 'import pytest' to imports"
    return None


# Function to identify test functions that need conversion
def identify_test_functions(content):
    test_functions = TEST_FUNCTION_PATTERN.findall(content)
    missing_markers = []

    for func in test_functions:
        # Check if function has pytest mark
        if f"@pytest.mark" not in content.split(f"def {func}")[0].split("\n")[-3:]:
            missing_markers.append(func)

    return missing_markers


# Function to identify assert patterns that need conversion
def identify_assert_patterns(content):
    lines = content.split("\n")
    suggestions = []

    for i, line in enumerate(lines):
        # Look for if statement pattern checks that could be assertions
        if re.search(r"if\s+not\s+isinstance\(.+,.+\):", line):
            suggestions.append((
                i + 1,
                "Convert to pytest assertion: assert isinstance(...), 'message'",
            ))
        elif re.search(r"if\s+.+\s+!=\s+.+:", line):
            suggestions.append((
                i + 1,
                "Convert to pytest assertion: assert ... == ..., 'message'",
            ))
        elif re.search(r"if\s+not\s+.+:", line):
            suggestions.append((
                i + 1,
                "Consider converting to pytest assertion: assert ..., 'message'",
            ))

    return suggestions


# Function to check for main() function that needs conversion
def check_main_function(content):
    if MAIN_FUNCTION_PATTERN.search(content) and MAIN_CHECK_PATTERN.search(content):
        return "Convert main() function to pytest tests and remove __name__ == '__main__' check"
    return None


# Main function to analyze test files
def analyze_test_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    print(f"\nAnalyzing {file_path}:")
    print("-" * 50)

    # Check imports
    missing_import = check_pytest_imports(content)
    if missing_import:
        print(f"- {missing_import}")

    # Check test functions
    missing_markers = identify_test_functions(content)
    if missing_markers:
        print("- Missing pytest markers on functions:")
        for func in missing_markers:
            print(f"  - @pytest.mark.api on def {func}(...)")

    # Check assert patterns
    assert_suggestions = identify_assert_patterns(content)
    if assert_suggestions:
        print("- Assertion suggestions:")
        for line, suggestion in assert_suggestions:
            print(f"  - Line {line}: {suggestion}")

    # Check main function
    main_suggestion = check_main_function(content)
    if main_suggestion:
        print(f"- {main_suggestion}")

    # Check for client fixtures
    if "site_web_api_client" not in content and "EspnSiteWebApiClient" in content:
        print("- Replace local client creation with site_web_api_client fixture")
    if "site_api_client" not in content and "site.api.espn.com" in content:
        print("- Replace local client creation with site_api_client fixture")
    if "cdn_api_client" not in content and "cdn.espn.com" in content:
        print("- Replace local client creation with cdn_api_client fixture")
    if (
        "sports_core_api_client" not in content
        and "sports.core.api.espn.com" in content
    ):
        print("- Replace local client creation with sports_core_api_client fixture")

    # Check return patterns
    if "return False" in content or "return True" in content:
        print("- Replace return True/False with assert statements")

    # Check file is imported in conftest.py
    with open(TEST_DIR / "conftest.py", "r") as f:
        conftest_content = f.read()
    if file_path.stem not in conftest_content:
        print("- Consider importing client classes in conftest.py if needed")

    print("-" * 50)


# Main function to process all test files
def main():
    if not os.path.exists(TEST_DIR / "conftest.py"):
        print("Error: conftest.py does not exist in the tests directory.")
        return

    test_files = list(TEST_DIR.glob("test-*.py")) + list(TEST_DIR.glob("test_*.py"))

    if not test_files:
        print("No test files found in the tests directory.")
        return

    print(f"Found {len(test_files)} test files to analyze.")

    for file_path in test_files:
        analyze_test_file(file_path)

    print("\nTo run pytest tests after conversion:")
    print("pytest -v tests/")
    print("\nTo run a specific test file:")
    print("pytest -v tests/test_file.py")
    print("\nTo run tests with a specific marker:")
    print("pytest -v -m api")


if __name__ == "__main__":
    main()
