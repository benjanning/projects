# Verified project publishing

The portfolio keeps its established URLs and design. `projects.json` is the generated central mirror consumed by `build-site.py`; each featured source repository owns its descriptions and asset definitions in `portfolio/project.json`. Edit the source project, rather than hand-editing generated HTML.

## Source → review → publication

1. A source project's main-branch push or manual **Verified portfolio release** run executes its regression checks. Applications test predictable synthetic journeys and capture the shared frontend; analytical projects regenerate their genuine figures from data/results. Pull requests run checks without publishing.
2. Only after those checks succeed, the workflow exports metadata and image files with their source commit, verification run and SHA-256 hashes. It appends a normal commit to `portfolio-published`; no history is rewritten. Application Pages deployments serve the tested static assets.
3. **Review public project releases** runs daily at 04:17 UTC, or manually. It reads only the six repositories in `source-registry.json`. It checks the exact successful main-branch verification run, approved history, asset names, sizes, file signatures and hashes. It never executes downloaded project code. A pending or failed source release leaves the previous successful portfolio entry in place.
4. The workflow updates the central manifest, source lock and versioned assets, generates pages and validates metadata, links and images. It creates/updates the `automation/portfolio-sync` review PR using only the portfolio repository's own token. It does not approve or merge PRs. No cross-repository write token or stored personal access token is required.
5. After an authorised reviewer merges the PR, the single **Generate, validate and deploy portfolio** workflow regenerates the site, runs regression checks and stages only public website files. GitHub's standard Pages artifact/deploy actions publish it.
6. The final job checks the public `release.json` against the portfolio commit, every case study's metadata, the exact image hashes, repository links and demo URLs. A commit or successful upload alone is not considered publication evidence.

Source metadata, screenshots and charts are a versioned package. A metadata-only update still runs its required verification/capture commands. The displayed source receipt links to the exact commit and successful run, rather than pretending an older screenshot represents an untested newer interface. Figures based on historical measurements retain their measurement provenance and limits.

## Review and failure behaviour

The repository setting allowing Actions-created PRs is required once for `benjanning/projects`. Default workflow token permissions stay read-only; only the sync job requests contents/PR write access. Source export jobs can write only to their own repository. This setting was enabled with the owner's approval. The workflows contain no automatic review or merge step.

Invalid metadata or altered assets fail before a review branch is pushed. Source verification failure prevents a new export. Generation or validation failure prevents deployment, leaving the last deployed site available. Public verification failure marks the release unsuccessful and requires investigation; it is not silently described as a successful sync. The public receipt and Actions history identify the last observed deployed revision. Existing source history and prior asset versions remain recoverable.

If the review branch conflicts with manually edited main content, the sync stops for review instead of overwriting that content. Resolve the PR normally, or merge/close an obsolete PR and start a fresh review branch without force pushing. GitHub schedules can be delayed or disabled after inactivity; the manual trigger remains available.

## Commands

```bash
python supporting-site-files/sync-projects.py
python -m unittest discover -s supporting-site-files/tests -v
python supporting-site-files/build-site.py
python supporting-site-files/validate-site.py
python supporting-site-files/stage-site.py
```

Local sync reads public GitHub resources. GH_TOKEN/GITHUB_TOKEN, if supplied in the process environment, is used only for public API reads; credentials are never saved by the script. In CI the normal repository-scoped token also pushes the review branch and opens its PR. `regenerate-charts.py` remains available as a historical manual helper; source-owned figure scripts now supply versioned releases, so ordinary site generation does not retrain models or rerun benchmarks.

The first successful source-to-public acceptance record, including both commits and deployment run, is documented in the final V3 handover. The system is not considered end-to-end verified until that record exists.
