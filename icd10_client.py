"""Minimal client for the ICD-10 Code Lookup API (generic sample code).

CONTRACT (from the published OpenAPI spec):
    Base URL:  https://restapi.npidataservices.com/icd10/api/v1
    Auth:      custom header  ApiKey: <ICD10_API_KEY>  (NOT "Authorization: Bearer")
    Format:    GET requests, query-string params, JSON responses
    Spec:      https://restapi.npidataservices.com/icd10/api_spec.yaml
    Docs:      https://restapi.npidataservices.com/icd10

Endpoints (all GET, all under the base URL):
    /getICD10Index        ?letter= &main_term=     Alphabetic Index
    /getICD10EIndex       ?letter= &main_term=     External Causes Index
    /getICD10Details      ?chapter= &section_range= &diag_code=   Tabular detail
    /getICD10Drug         ?letter=                 Table of Drugs & Chemicals
    /getICD10Code         ?query= &index=          Iterative code search
    /getICD10PCSTabular   ?code=                   ICD-10-PCS tabular
    /getICD10Neo          ?letter=                 Table of Neoplasms
    /getICD10SiteMap                               UI sitemap

This is generic, illustrative sample code — replace the placeholder key and adapt
field handling to the live response shapes you receive.
"""

import os

import requests

BASE_URL = "https://restapi.npidataservices.com/icd10/api/v1"
SIGNUP_URL = "https://www.vbcriskanalytics.com/icd10-rest-api-medical-coding-lookup"
API_KEY_ENV = "ICD10_API_KEY"


class Icd10Client:
    """Small client for the ICD-10 Code Lookup API. Returns parsed JSON."""

    def __init__(self, api_key=None, base_url=BASE_URL, timeout=30):
        self.api_key = api_key or os.environ.get(API_KEY_ENV)
        if not self.api_key:
            raise ValueError(
                f"No API key found. Set the {API_KEY_ENV} environment variable. "
                f"Get a key at {SIGNUP_URL}"
            )
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _get(self, path, params=None):
        headers = {"accept": "application/json", "ApiKey": self.api_key}
        clean = {k: v for k, v in (params or {}).items() if v is not None}
        resp = requests.get(
            f"{self.base_url}/{path}", params=clean, headers=headers, timeout=self.timeout
        )
        resp.raise_for_status()
        return resp.json()

    def search_code(self, query, index=None):
        """Iterative ICD-10-CM code search, e.g. search_code('diabetes')."""
        return self._get("getICD10Code", {"query": query, "index": index})

    def index(self, letter=None, main_term=None):
        """Alphabetic Index (by starting letter and/or main term)."""
        return self._get("getICD10Index", {"letter": letter, "main_term": main_term})

    def external_causes_index(self, letter=None, main_term=None):
        return self._get("getICD10EIndex", {"letter": letter, "main_term": main_term})

    def details(self, chapter=None, section_range=None, diag_code=None):
        """Tabular detail by chapter, section range, or a specific diagnosis code."""
        return self._get(
            "getICD10Details",
            {"chapter": chapter, "section_range": section_range, "diag_code": diag_code},
        )

    def drugs(self, letter=None):
        """Table of Drugs and Chemicals."""
        return self._get("getICD10Drug", {"letter": letter})

    def neoplasms(self, letter=None):
        """Table of Neoplasms."""
        return self._get("getICD10Neo", {"letter": letter})

    def pcs_tabular(self, code):
        """ICD-10-PCS tabular data for a procedure code."""
        return self._get("getICD10PCSTabular", {"code": code})

    def sitemap(self):
        return self._get("getICD10SiteMap")
