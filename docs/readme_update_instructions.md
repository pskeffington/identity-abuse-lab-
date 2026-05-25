# README Update Instructions

The current reviewer-facing README draft is stored at:

```text
docs/readme_current.md
```

Before creating the `v0.1-lab-baseline` release, replace the root `README.md` with the contents of `docs/readme_current.md`.

## Rationale

The root README was initialized early in the project. The reviewer-facing draft now reflects the current state of the repository, including:

- enriched detection results;
- safety boundary;
- current detector list;
- Sigma-style rule list;
- reproducibility commands;
- manuscript status;
- reviewer links; and
- release-status references.

## Manual command

From a local clone:

```bash
cp docs/readme_current.md README.md
git add README.md
git commit -m "docs: update README for v0.1 baseline review"
```

## Release gate

Do not tag `v0.1-lab-baseline` until the root README has been updated or the release notes clearly identify `docs/readme_current.md` as the current reviewer guide.
