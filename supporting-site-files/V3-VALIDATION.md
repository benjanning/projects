# V3 verification

The six case studies now use successful, commit-identified source packages. See [source-lock.json](source-lock.json) for the exact source commits, verification runs, export revisions, asset hashes and source-owned attribution. The public `release.json` records the portfolio revision and the same source locks.

## Required checks

| Project | Verification required for its release |
| --- | --- |
| Car records | 13 API/authentication regressions; one disposable MySQL CRUD/authentication integration; two frontend-rule checks; three Flask/static browser workflows |
| Classification | Three regression/reproducibility tests, including saved-prediction reconciliation; regenerated model comparison, confusion matrices and feature distributions |
| Hotel | 15 backend/rule checks; one disposable MySQL 8.4 catalog integration; two complete Express/static browser journeys |
| PlantGrowth | Three independent statistics/reproducibility checks; three regenerated figures and computed result summary |
| Sorting | Seven Python tests; three JavaScript trace checks against Python fixtures; one browser control/mobile workflow; 125 saved benchmark observations reconciled to medians/IQR |
| Iris | Three raw-data/provenance/reproducibility checks; three regenerated descriptive figures and computed result summary |
| Portfolio | Four source-package safety regressions; eight HTML documents, six metadata records and local references validated; 15 desktop/mobile/navigation browser tests before deploy and repeated at the public URL |

The desktop/mobile suite visits the homepage and all six case studies at 1440px and 390px, loads every content image, rejects horizontal overflow and browser script errors, checks source receipts and local-run disclosure, and verifies homepage filtering/navigation. The public stage also compares the approved source receipt, all per-project metadata, exact asset bytes, repository URLs and demo URLs. Its browser JSON report and genuine screenshots are saved in the Actions artifact `portfolio-public-browser-evidence` for fourteen days.

## Proved source-to-public update

A controlled car metadata improvement added its already-tested static-demo URL and exact verification description. Source `edd62f12fa25073eeba4a3af3e5131e70e4446cf` passed [source run 39394701328](https://github.com/benjanning/data-representation-project/actions/runs/39394701328). [Sync run 39395230181](https://github.com/benjanning/projects/actions/runs/39395230181) opened [review PR 5](https://github.com/benjanning/projects/pull/5). Its approved build passed and merge `0da800f90ea7e48693423c389c2c8a02a3af0666` passed [deployment and public verification 39395511881](https://github.com/benjanning/projects/actions/runs/39395511881). The public browser showed the intended demo link, the exact source receipt and the corresponding versioned image. Later source updates have followed the same reviewed process.

## Interpretation and limits

The application demos use synthetic browser records. Optional MySQL adapters are tested in fresh CI databases; neither GitHub Pages demo runs a database or production booking service. Classification uses a repeatedly reused exploratory holdout, with false negatives shown and no clinical validation. Statistical intervals state their assumptions and multiplicity adjustment. Iris figures are descriptive and preserve the supplied variant. Sorting timings are recorded observations from one environment; animation pace is not runtime.

Bot PR checks may require an authorised reviewer to approve the workflow run before it expires. The workflow never self-approves or merges. An early bot validation expired before approval; subsequent reviewed runs passed. A Windows shell wildcard mismatch in the hotel test command was corrected with explicit paths, and completed test HTTP connections now close deterministically. Original coursework, history and prior deployed assets remain preserved.

[Publishing and failure handling](AUTOMATION.md)
