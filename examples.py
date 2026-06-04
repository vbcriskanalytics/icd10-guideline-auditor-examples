"""Runnable examples for the ICD-10 Code Lookup API (generic sample code).

    pip install -r requirements.txt
    export ICD10_API_KEY=your_api_key_here
    python examples.py
"""

import json
import os
import sys

from icd10_client import API_KEY_ENV, SIGNUP_URL, Icd10Client


def main():
    if not os.environ.get(API_KEY_ENV):
        print(f"Set {API_KEY_ENV} first. Get a key at {SIGNUP_URL}")
        sys.exit(0)

    client = Icd10Client()

    # Search for codes matching a term.
    results = client.search_code("diabetes")
    print("Search 'diabetes' ->")
    print(json.dumps(results, indent=2)[:600], "...")

    # Pull tabular detail for a specific code.
    detail = client.details(diag_code="E11.9")
    print("\nDetail for E11.9 ->")
    print(json.dumps(detail, indent=2)[:600], "...")


if __name__ == "__main__":
    main()
