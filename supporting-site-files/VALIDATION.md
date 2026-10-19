# Validation record

Review date: 19 October 2026. Portfolio: https://benjanning.github.io/projects/

## Live website

- GitHub Pages built successfully from main, repository root. No build framework or third-party runtime is required.
- Opened the actual deployed homepage and all six case studies in the browser. Checked desktop layouts and a 390 × 844 mobile viewport; all seven pages fit without horizontal overflow and their primary images loaded.
- Checked navigation, project filtering and case-study source links. The application filter shows the two application projects; all-work restores the complete selection.
- 24 live HTTP checks returned 200: homepage, six case pages, six featured assets, stylesheet/script, six source repositories and the main GitHub/profile/portfolio destinations.
- Static HTML check: eight documents (including 404), 158 local file/anchor references, no missing references or missing image alt attributes.
- Typography, spacing, screenshots and charts were reviewed visually. All project pages were captured. Browser screenshots are viewport captures, not a full-page stitched audit.

## Accessibility and loading

Semantic navigation/headings, a skip link, visible keyboard focus, labelled controls, alt text, an aria-live filter result and reduced-motion support are included. Main text contrast is 12.76:1; secondary body text 5.09:1; white button text 8.46:1. Small card/visual labels were darkened after contrast review. This is a focused accessibility review, not a formal certification or screen-reader-user study.

The initial HTML/CSS/JavaScript/favicon/hero-image payload is approximately 93 KB before compression and before lazy-loaded project images. There are no external fonts, analytics or framework bundles. Network timings were sampled during HTTP checks; no Lighthouse/Core Web Vitals score is claimed.

## Project verification

| Project | Validation |
| --- | --- |
| Car rental | Five passing API/authentication test methods: homepage filename, CRUD for both resources, invalid inputs, missing-record 404s and protected routes outside demo mode. Browser created, updated and deleted a temporary synthetic vehicle through the actual interface. MySQL data layer was not integration-tested. |
| Hotel booking | Four passing date/pricing test methods. Browser completed booking dates → room/quantity → demo continuation → confirmation. Two €120 rooms for three nights produced €720. No real reservation or payment. |
| Classification | All 42 notebook code cells executed after corrections. Outputs regenerated. Execution does not prove clinical validity or independent model generalisation. |
| Applied statistics | All 18 project-notebook code cells executed using PlantGrowth.csv. |
| Iris | All 25 notebook code cells executed after portability corrections. |
| Sorting | Four passing regression test methods. New seeded benchmark verified 125 measured sort results against Python sorted(). |

Total: 13 automated test methods and 85 notebook code cells, plus the correctness assertions in 125 benchmark runs.

## Dependencies and publication checks

- npm audit for the sanitized hotel application: zero known vulnerabilities reported.
- pip-audit of the isolated test environment: 92 packages, zero known vulnerabilities after updating the environment-local pip installer. Findings in its original pip 24.0 installer were resolved; system Python was not modified.
- Tested Python packages are pinned in the selected project requirement files. No claim is made that all historical coursework environments were modernised.
- New portfolio/profile/hotel text was scanned for token/private-key patterns; none were found. Heuristic scanning does not prove the absence of every possible secret.
- Historical credential exposure is documented separately for the owner; no secret values appear in public documentation.

## Change application

Thirteen public-repository pull requests were merged normally, with expected branch heads checked. Histories and source attribution were preserved. programming2022 is now a reversible read-only coursework archive. No existing repository visibility was changed, no repository was deleted and no force push/history rewrite was performed.

- [applied_statistics](https://github.com/benjanning/applied_statistics/pull/1) — merged.
- [data-representation-coursework](https://github.com/benjanning/data-representation-coursework/pull/1) — merged.
- [data-representation-project](https://github.com/benjanning/data-representation-project/pull/1) — merged.
- [deploytopythonanywhere](https://github.com/benjanning/deploytopythonanywhere/pull/1) — merged.
- [funddata-assessment](https://github.com/benjanning/funddata-assessment/pull/1) — merged.
- [mywork](https://github.com/benjanning/mywork/pull/1) — merged.
- [pands-problem-sheet](https://github.com/benjanning/pands-problem-sheet/pull/1) — merged.
- [pands-project](https://github.com/benjanning/pands-project/pull/1) — merged.
- [pfda-Project1](https://github.com/benjanning/pfda-Project1/pull/1) — merged.
- [pfda-Project2](https://github.com/benjanning/pfda-Project2/pull/1) — merged.
- [PfDA_Assignment](https://github.com/benjanning/PfDA_Assignment/pull/1) — merged.
- [programming2022](https://github.com/benjanning/programming2022/pull/1) — merged.
- [Sorting-Algorithms-Project](https://github.com/benjanning/Sorting-Algorithms-Project/pull/1) — merged.

## Tested versions

- numpy: 2.5.4
- pandas: 3.0.6
- matplotlib: 3.11.2
- seaborn: 0.13.2
- scipy: 1.18.1
- scikit-learn: 1.9.1
- statsmodels: 0.15.0
- Flask: 3.1.3
- Flask-HTTPAuth: 4.8.1
- mysql-connector-python: 26.7.0
- PyMySQL: 1.2.3
- nbclient: 0.11.0
- ipykernel: 7.4.0
