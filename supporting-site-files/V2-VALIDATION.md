# V2 validation and release notes

19 October 2026. V2 preserves the portfolio design, improves GitHub presentation and develops the hotel prototype into a complete synthetic demonstration.

## Hotel

The Express journey was exercised in a browser from homepage dates through room selection, sample guest details, review and confirmation. Two €120 rooms over three nights produced €720. The independent generated static version was tested through the same complete journey at a 390px mobile viewport, including reversed dates, invalid example email, incomplete navigation, refresh recovery and pricing. Screenshot evidence records both modes. Neither creates a real booking or payment.

15 automated tests pass; the optional live MySQL test is skipped. HTTP tests cover the full server workflow, CSRF, client price tampering, invalid selections, duplicate confirmation, changed rates and safe catalog-failure responses. Pure-rule tests cover dates, currency arithmetic, capacity, stock and synthetic guest validation. npm audit reports zero known vulnerabilities. Node syntax checks and the generated static build pass.

No Docker or MySQL executable was available. An isolated MySQL 8.4 Compose setup, synthetic schema, pooled catalog adapter and opt-in integration test are supplied, but a real MySQL connection is not claimed verified. The default demo remains database-free.

## Other featured projects

- Car: six API/authentication test methods pass. Browser create/update/delete was exercised after integer-price validation, missing-delete 404 behavior and form-label improvements.
- Classification: new evaluate.py uses all 30 features, deterministic stratified splitting and five-fold training-only cross-validation. Results are reproduced byte-for-byte in two runs. Chart uncertainty is training-fold standard deviation; the reused holdout is exploratory, not independent clinical validation. Original notebook and its references remain separate.
- Sorting: four current regression test methods pass. Existing verified timings and chart were preserved, since implementations did not change.
- Applied statistics and Iris: source/notebook implementations are unchanged in V2; the existing execution evidence is retained. Their landing pages now lead with genuine charts and concise setup/scope details. No unnecessary rerun is claimed.

## GitHub and portfolio presentation

Six featured READMEs lead with real previews, technology rows, concise functionality and accurate setup/testing notes. Historical documentation was preserved in COURSEWORK.md. Seven supporting/coursework landing pages were simplified. The existing archived programming2022 repository and third-party gitignore fork remain unchanged. No new archive, rename, visibility change, deletion or force push was made.

The profile uses GitHub-compatible two-column HTML with six genuine previews and explicit source/case-study links. Social-preview images are prepared in each featured repository, using real project images and labels. Uploaded settings and pins are only treated as complete after account-state verification.

The established portfolio gains an explicit hotel demo action, a four-screen hotel gallery and the new classification evaluation chart. Static HTML references pass (eight pages, 168 local links/assets/anchors). New-source token/private-key pattern scanning reports no flags; this is heuristic and does not remove historical exposure or prove exhaustive secret absence. Prior credential-rotation actions still apply.

## Attribution and limits

Hotel imagery is illustrative Pexels photo 237371 by Pixabay, with source/license links in the application credits and provenance register. No photographs from the old unverified hotel ZIP were reused. Floorplans are original labelled CSS illustrations. Application screenshots are authentic browser captures, not AI-generated interfaces.

Live release inspection, pull requests and final account-setting outcomes are recorded in the final handover.
