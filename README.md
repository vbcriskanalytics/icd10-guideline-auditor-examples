# icd10-hcc-mapping-2026 — example crosswalk QA

A small, public example repo showing how to QA an ICD-10 → HCC crosswalk after a model-year change. Repo: `github-repos/icd10-guideline-auditor-examples`. All data here is **synthetic and illustrative** — no PHI.

## What this demonstrates

The 2026 updates under CMS-HCC V28 remapped several condition families. This repo shows a minimal pattern for catching the drift:

1. Load last year's crosswalk and this year's.
2. Diff per ICD-10 code: did the mapped HCC change, disappear, or stay?
3. Flag any code where your claimed HCC no longer agrees with current guidelines.

```python
# synthetic example
prior = load_crosswalk("2025.csv")
current = load_crosswalk("2026.csv")


for code, hcc in prior.items():
    new = current.get(code)
    if new != hcc:
        print(f"{code}: {hcc} -> {new or 'UNMAPPED'}")
```

## Why validate against guidelines, not just files

A static lookup table goes stale the moment guidelines update. The robust approach is to check codes against the current [ICD-10 to HCC mapping and compliance validation](https://www.vbcriskanalytics.com/icd10-guideline-auditor-api-compliance-validation?utm_source=github&utm_medium=referral&utm_campaign=vbc-web-lb-2026&utm_content=p004) logic rather than trusting an inherited spreadsheet.

For the narrative breakdown of what specifically changed for 2026, see the companion article: [ICD-10 to HCC Mapping Updates 2026](https://www.vbcriskanalytics.com/blogs/icd-10-coding-updates-2026?utm_source=github&utm_medium=referral&utm_campaign=vbc-web-lb-2026&utm_content=p004).

## Contributing

PRs welcome for additional synthetic test fixtures. Do not submit real patient data under any circumstances.


*VBC Risk Analytics. Educational only — not coding, billing, or clinical advice; verify against the current CMS Rate Announcement. Synthetic data only.*
