# Codex Refactor Plan: NSL-KDD Cybersecurity Agent + FastAPI Demo

This file is intended to be added to the repository and used as a working brief for Codex.

## Objective

Refactor this NSL-KDD machine learning class project into a reusable cybersecurity detection engine with a FastAPI demo layer, while preserving the current training/evaluation functionality.

This work must happen on a **new branch**, not on `main`.

---

## Recommended execution strategy

Use Codex in **two passes**.

### Pass 1
Focus on infrastructure and refactor:
- open a GitHub issue
- create a new branch from that issue
- refactor the codebase into reusable layers
- add model persistence
- add inference and reporting services
- add FastAPI app and routes
- add tests
- update README

### Pass 2
Focus on documentation and presentation support:
- create technical writeup
- create architecture notes
- create presentation notes
- polish demo flow
- open a PR

---

## Target architecture

```text
ml-group-project/
  src/
    core/
      data_loader.py
      features.py
      models.py
      train.py
      infer.py
      explain.py
    services/
      training_service.py
      detection_service.py
      reporting_service.py
    api/
      app.py
      schemas.py
      routes/
        health.py
        train.py
        predict.py
        report.py
  templates/
    index.html
    results.html
  static/
  docs/
    technical_writeup.md
    architecture.md
    presentation_notes.md
  models/
  outputs/
  tests/
  main.py
  requirements.txt
  README.md
```

This structure keeps:
- **core ML logic** separate from API code
- **service layer** separate from raw model code
- **demo and docs** cleanly organized
- the repo ready for later NemoClaw or agent-runtime integration

---

## Demo goals

The FastAPI app should make the project easier to demo in a browser.

The preferred demo story is:

1. Show that the project started as an NSL-KDD ML pipeline
2. Show that it was refactored into a reusable cybersecurity detection engine
3. Show a browser-based demo using FastAPI
4. Score one or more records
5. Display:
   - binary classification (`normal` vs `attack`)
   - multiclass attack category
   - confidence score if available
   - analyst-style explanation
   - incident summary
6. Show that the repo now supports technical documentation and presentation generation
7. Explain that the design is ready to be wrapped by NemoClaw later

---

## Required implementation work

### A. Repository and tracking
- Open a GitHub issue for the refactor and demo work
- Create a branch tied to that issue
- Do all work on the new branch
- Open a PR when the work is complete

Suggested branch naming pattern:
- `issue-<number>-cyber-agent-fastapi`
- or `feature/cyber-agent-fastapi`

### B. Refactor code structure
Reorganize the code into clearer modules:

- `src/core/`
  - dataset loading
  - feature prep
  - model definitions
  - training
  - inference
  - explanation helpers

- `src/services/`
  - training service
  - detection service
  - reporting service

- `src/api/`
  - FastAPI app
  - routes
  - request/response schemas

### C. Preserve and improve ML behavior
Keep the current NSL-KDD functionality working, but make it reusable.

Add:
- model save/load support
- inference for single record scoring
- inference for batch scoring
- binary classification (`normal` vs `attack`)
- multiclass attack category
- confidence score if available
- concise analyst-style explanation

### D. Add FastAPI app
Create a small FastAPI app suitable for demos.

Minimum endpoints:
- `GET /health`
- `POST /train`
- `POST /predict`
- `POST /predict/batch`
- `POST /report/incidents`
- `GET /demo`

A lightweight HTML template approach is fine. This does **not** need to become a complex frontend.

### E. Reporting and documentation generation
Create these docs under `docs/`:
- `docs/technical_writeup.md`
- `docs/architecture.md`
- `docs/presentation_notes.md`

These should describe:
- project objective
- dataset and task
- original architecture
- refactor rationale
- new system architecture
- model workflow
- FastAPI demo flow
- testing approach
- limitations
- future work
- path toward later autonomous agent integration

For `presentation_notes.md`, structure it as slide-ready content:
- title / overview
- problem
- dataset
- modeling approach
- refactor
- architecture
- demo
- results
- future work

### F. Tests and developer experience
- update or add tests for core services and API routes
- update README with setup and usage for:
  - training
  - running the FastAPI app
  - scoring records
  - generating demo reports

---

## Constraints

- Do **not** work directly on `main`
- Keep Python + scikit-learn
- Preserve existing functionality where practical
- Prefer incremental refactoring over rewriting from scratch
- Do **not** add NemoClaw yet
- Keep the code understandable for a student project and class demo
- Add or update tests as needed
- Keep pure ML logic separate from API code
- Avoid unnecessary framework complexity

---

## Main prompt for Codex

```text
You are working in the GitHub repository `willdaly/ml-group-project`.

Read this file completely before making changes:
- docs/CODEX_REFACTOR_PLAN.md

Goal:
Refactor this NSL-KDD machine learning class project into a reusable cybersecurity detection engine with a FastAPI demo layer, while preserving the current training/evaluation functionality. The work must happen on a new branch, not on `main`.

Workflow requirements:
1. Open a GitHub issue describing the refactor and demo work.
2. Create a new branch for that issue from the current default branch.
3. Do all work on that new branch.
4. When complete, commit the changes and open a pull request.

Project intent:
This repository currently behaves like a class submission pipeline. I want it to evolve into a more product-like cybersecurity agent foundation:
- reusable ML core
- service layer for detection/reporting
- FastAPI app for demos
- documentation for technical writeup and presentation
- structured so it can later be wrapped by NemoClaw or another agent runtime

Constraints:
- Do not work directly on `main`
- Keep Python + scikit-learn
- Preserve existing functionality where practical
- Prefer incremental refactoring over rewriting from scratch
- Do not add NemoClaw yet
- Keep the code understandable for a student project and class demo
- Add or update tests as needed

Required implementation tasks:

A. Repository and tracking
- Open a GitHub issue for the refactor
- Create a branch tied to that issue
- Use a clear branch name related to the issue and FastAPI cyber agent refactor

B. Refactor code structure
Reorganize the code into a cleaner structure such as:
- `src/core/` for data loading, feature prep, models, training, inference, explanation
- `src/services/` for training, detection, and reporting services
- `src/api/` for FastAPI app, routes, and request/response schemas

C. Preserve and improve ML functionality
- Keep the current NSL-KDD training flow working
- Add model save/load support
- Add reusable inference functions for:
  - single record scoring
  - batch scoring
  - binary classification (`normal` vs `attack`)
  - multiclass attack category classification
  - confidence score if available
  - concise analyst-style explanation

D. Add FastAPI application
Create a small FastAPI app for demos with endpoints such as:
- `GET /health`
- `POST /train`
- `POST /predict`
- `POST /predict/batch`
- `POST /report/incidents`
- `GET /demo` or a minimal browser page for interacting with the system

The demo should be simple and useful, not overengineered.
A lightweight HTML template approach is fine.
The goal is to make the project feel visual and demoable in a browser.

E. Reporting and documentation generation
Create documentation files under `docs/`:
- `docs/technical_writeup.md`
- `docs/architecture.md`
- `docs/presentation_notes.md`

These should describe:
- project objective
- dataset and task
- original architecture
- refactor rationale
- new system architecture
- model workflow
- FastAPI demo flow
- testing approach
- limitations
- future work
- path toward later autonomous agent integration

For `presentation_notes.md`, structure the content so it can easily become slides:
- title / overview
- problem
- dataset
- modeling approach
- refactor
- architecture
- demo
- results
- future work

F. Tests and developer experience
- Update or add tests for core services and API routes
- Update README with setup and usage for:
  - training
  - running the FastAPI app
  - scoring records
  - generating demo reports

Implementation guidance:
- Keep pure ML logic separate from API code
- Keep code modular and readable
- Reuse existing code where sensible instead of rewriting everything
- Avoid unnecessary frameworks beyond FastAPI and standard Python tooling
- Make the repo clearly better suited for demos, technical writeups, and future agent integration

Deliverables:
- new GitHub issue
- new branch
- refactored code
- FastAPI app
- updated tests
- updated README
- docs/technical_writeup.md
- docs/architecture.md
- docs/presentation_notes.md
- pull request summarizing the changes
```

---

## Follow-up instruction for Codex

Send this immediately after the main prompt:

```text
Work in small commits. Before making large structural changes, inspect the current repository structure and preserve anything still useful. Prefer a clean, reviewable PR over a maximal rewrite.
```

---

## Suggested repo placement

Save this file at:

```text
docs/CODEX_REFACTOR_PLAN.md
```

That way your instruction to Codex can simply say to read that file first.

---

## Optional note to include in your first Codex message

You can also prepend this one-liner:

```text
Start by reading docs/CODEX_REFACTOR_PLAN.md, then open the issue and create the working branch before making any code changes.
```
