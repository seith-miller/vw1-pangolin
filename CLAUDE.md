# Pangolin - Armored Vehicle Project

## Interaction Style
- Keep responses concise
- Ask one question at a time, don't batch multiple questions

## Git Workflow (git-flow)

- `main` — release branch
- `develop` — integration branch; feature branches merge here
- `feature/<name>` — one per milestone; issue branches merge here

### Issue/PR rules

- Each GitHub milestone has a corresponding `feature/<name>` branch
- Issue branches are created from the milestone's feature branch
- Issue PRs target the milestone's feature branch (NOT `main` or `develop`)
- When the milestone is complete, the feature branch is merged into `develop`
- `develop` merges into `main` at release time

When creating new issues, include a **Branching** section specifying the target feature branch so agent-lab workers and contributors know where to aim their PRs.
