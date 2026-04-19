# Codex Demo Polish Plan: FastAPI Cybersecurity Demo

This file defines the next phase of work after the FastAPI refactor.

The architecture is already complete. The goal now is to **improve demo quality, usability, and presentation readiness**.

---

## Objective

Make the FastAPI cybersecurity demo:
- easier to present live
- visually clearer
- more reliable during demos
- supported by a simple runbook and example inputs

This phase is about **polish, not new architecture**.

---

## Instructions for Codex

You are working in the GitHub repository `willdaly/ml-group-project`.

Read this file completely before making changes:
- docs/CODEX_DEMO_POLISH_PLAN.md

---

## Workflow requirements

1. Open a new GitHub issue for demo polish work.
2. Create a new branch for that issue.
3. Do all work on that branch.
4. Open a pull request when complete.

Do NOT work on `main`.

---

## Goals

Improve the FastAPI demo so it is:
- easy to use in a browser
- easy to explain in a presentation
- easy to run without mistakes
- visually clean for screenshots

---

## Required implementation tasks

### 1. Improve `/demo` page

Enhance the demo experience:

- Add prefilled example inputs
- Provide buttons like:
  - "Load benign example"
  - "Load attack example"
- Make outputs visually clear:
  - binary classification
  - attack category
  - confidence score
  - explanation
- Format results in a clean card or section layout

Keep it simple and lightweight (no heavy frontend frameworks).

---

### 2. Add example input files

Create a new directory:
examples/
Add:
- `benign_record.json`
- `attack_record.json`
- `demo_batch.json`

These should be valid inputs for `/predict` and `/predict/batch`.

---

### 3. Add demo runbook

Create:
docs/demo_runbook.md
Include:

- how to install dependencies
- how to train models
- how to start FastAPI
- how to open the demo
- a **60-second demo script**

Example flow:
1. Start server
2. Open `/demo`
3. Load benign example → show result
4. Load attack example → show result
5. Show incident summary

---

### 4. Update README

Add a new section:

## Quick Demo

Include:
- commands to run the app
- link to `/demo`
- short explanation of what to show

---

### 5. Improve result formatting

Make prediction outputs easier to read:

- clearly label:
  - "Normal" vs "Attack"
  - attack category
  - confidence
- format explanations cleanly
- ensure consistent output structure

---

### 6. Keep scope tight

DO:
- improve usability
- improve clarity
- improve presentation

DO NOT:
- rewrite architecture
- add NemoClaw yet
- introduce complex frontend frameworks
- significantly change ML logic

---

## Constraints

- Work on a new branch only
- Keep changes incremental and readable
- Prefer small commits
- Keep the demo simple and stable
- Optimize for live demo and screenshots

---

## Deliverables

- new GitHub issue
- new branch
- improved `/demo` UI
- `examples/` folder with sample inputs
- `docs/demo_runbook.md`
- updated README
- pull request summarizing changes

---

## Follow-up instruction

After completing this work, the repository should be:
- demo-ready
- presentation-ready
- portfolio-ready
- stable enough for live walkthroughs

Future work (NOT part of this task):
- NemoClaw / agent integration
- async workflows
- productionization
