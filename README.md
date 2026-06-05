# icd10-code-lookup-examples

Generic, runnable Python sample code for the **ICD-10 Code Lookup API** — search the full
**ICD-10-CM** Alphabetic Index, Tabular List, Table of Drugs & Chemicals, Table of
Neoplasms, External Causes Index, and **ICD-10-PCS** procedure codes from one REST API.
Handy for **medical-coding lookups**, code validators, EHR autocomplete, and superbill tools.

Built and maintained by [VBC Risk Analytics](https://www.vbcriskanalytics.com/icd10-rest-api-medical-coding-lookup).

## Get an API key

Sign up on the **[ICD-10 Code Lookup API](https://www.vbcriskanalytics.com/icd10-rest-api-medical-coding-lookup)** product page./n
Interactive docs (Swagger UI): https://restapi.npidataservices.com/icd10

## Quickstart

```bash
pip install -r requirements.txt
export ICD10_API_KEY=your_api_key_here
python examples.py
```

If `ICD10_API_KEY` is not set, the script prints a friendly message pointing to the sign-up URL.

## Contract

- **Base URL:** `https://restapi.npidataservices.com/icd10/api/v1`
- **Auth:** custom header `ApiKey: <key>` — **not** `Authorization: Bearer`.
- **Format:** `GET` with query-string params; JSON responses.
- **OpenAPI spec:** https://restapi.npidataservices.com/icd10/api_spec.yaml

| Endpoint | Params | Purpose |
|---|---|---|
| `GET /getICD10Code` | `query`, `index` | Iterative code search |
| `GET /getICD10Index` | `letter`, `main_term` | Alphabetic Index |
| `GET /getICD10EIndex` | `letter`, `main_term` | External Causes Index |
| `GET /getICD10Details` | `chapter`, `section_range`, `diag_code` | Tabular detail |
| `GET /getICD10Drug` | `letter` | Table of Drugs & Chemicals |
| `GET /getICD10Neo` | `letter` | Table of Neoplasms |
| `GET /getICD10PCSTabular` | `code` | ICD-10-PCS tabular |
| `GET /getICD10SiteMap` | — | UI sitemap |

### Example request

```bash
curl 'https://restapi.npidataservices.com/icd10/api/v1/getICD10Code?query=diabetes' \
  -H 'accept: application/json' \
  -H "ApiKey: $ICD10_API_KEY"
```

A missing/invalid key returns
`{"errors":[{"message":"Authorization error, invalid ApiKey", ...}],"status":401}`.

> This repository ships **generic illustrative sample code**. Replace the placeholder key
> and adapt response handling to the live payload shapes for each endpoint.

---
Maintained by VBC Risk Analytics. Disclosure: we build the ICD-10 Code Lookup API.
Educational only — not coding, billing, or clinical advice; verify against the official
ICD-10-CM/PCS files and the [API docs](https://restapi.npidataservices.com/icd10).
