# Codex Website Expansion Plan: Multi-Page Project Site with Top Navigation

This file defines the next phase of work for the repository.

The FastAPI demo already exists. The goal now is to turn the demo into a **small multi-page project website** that presents the entire project clearly to visitors, reviewers, and presentation audiences.

The UI layout should use a **top navigation bar** shared across all pages.

---

## Objective

Expand the existing FastAPI + Jinja demo into a polished project website that includes:

- a landing page
- the live demo
- a “how it works” page
- a results page
- an architecture page
- a presentation page
- a visible GitHub link

The site should feel like a **portfolio/demo site**, not just a raw prediction form.

This phase is about:
- narrative
- clarity
- presentation readiness
- better discoverability of project materials

This phase is **not** about:
- rewriting backend logic
- adding a heavy frontend framework
- adding NemoClaw yet

---

## Instructions for Codex

You are working in the GitHub repository `willdaly/ml-group-project`.

Read this file completely before making changes:
- docs/CODEX_WEBSITE_EXPANSION_PLAN.md

---

## Workflow requirements

1. Open a new GitHub issue for website expansion and presentation UI work.
2. Create a new branch for that issue.
3. Do all work on that branch.
4. Open a pull request when complete.

Do NOT work on `main`.

---

## UI layout decision

Use **Option A**:
- a shared **top navigation bar**
- visible across all site pages
- simple, clean, presentation-friendly

The nav should include:

- Home
- Demo
- How It Works
- Results
- Architecture
- Presentation
- GitHub

The GitHub item should link to the repository homepage externally.

---

## Overall site goal

If someone opens the project website, they should understand the project within 2–3 minutes without needing a spoken explanation.

The site should communicate:

1. What the project is
2. Why it matters
3. How it works
4. What the results are
5. How to try it
6. Where to find the code
7. How it connects to the presentation materials

---

## Required implementation tasks

### 1. Add shared top navigation

Create a reusable shared layout or base template for all pages.

Navigation items:
- `Home` → `/`
- `Demo` → `/demo`
- `How It Works` → `/how-it-works`
- `Results` → `/results`
- `Architecture` → `/architecture`
- `Presentation` → `/presentation`
- `GitHub` → external repo link

Requirements:
- keep layout simple
- keep it visually clean
- make it consistent across all pages
- optimize for screenshots and live demo use

---

### 2. Create a landing page

Route:
- `/`

This should act as the homepage and first impression of the project.

Include:
- project title
- one-sentence pitch
- short explanation of the project
- a button linking to `/demo`
- a visible GitHub link
- short bullets for what the system does

Suggested sections:
- Problem
- Solution
- What you can explore on this site

The homepage should feel like a project overview, not a README dump.

---

### 3. Keep and improve the demo page

Route:
- `/demo`

Preserve the existing live demo functionality, but improve presentation.

Add:
- short instructions
- buttons to load example inputs
- cleaner result formatting
- strong visual separation between:
  - binary classification
  - attack category
  - confidence
  - explanation
  - incident summary

The demo page should remain lightweight and stable.

---

### 4. Add a “How It Works” page

Route:
- `/how-it-works`

Purpose:
Explain the project in plain English.

Include sections such as:
- Dataset: NSL-KDD
- Input features
- Binary classification task
- Multiclass attack category task
- Models used
- Preprocessing approach

Content can be based on:
- README
- docs/technical_writeup.md
- docs/presentation_notes.md

Keep this page readable and concise.

---

### 5. Add a Results page

Route:
- `/results`

Display project outputs and explain them.

Include existing generated images if available, such as:
- confusion matrices
- ROC curves
- feature importance
- model comparison visuals

Each visual should have:
- a short heading
- a sentence or two explaining what it means

This page should make the project look like a finished ML system, not just a form demo.

---

### 6. Add an Architecture page

Route:
- `/architecture`

Purpose:
Show the engineering story.

Include a simple architecture breakdown such as:

`core -> services -> API -> demo`

Explain:
- why the refactor happened
- how code is organized
- why this makes the project reusable
- why this sets up later agent integration

Use clean sections and concise explanations.

---

### 7. Add a Presentation page

Route:
- `/presentation`

Purpose:
Expose the project’s presentation material in browser-readable form.

Convert content from:
- `docs/presentation_notes.md`

into readable HTML sections.

Keep the page:
- slide-like
- concise
- easy to skim

If presentation assets already exist in the repo, link to them where appropriate.

---

### 8. Improve content discoverability

Make sure the website surfaces project materials clearly.

Examples:
- link from homepage to `/demo`
- link from homepage to GitHub
- link from architecture page to presentation page
- link from results page to demo page
- link from presentation page to GitHub or docs when helpful

The site should feel connected, not like isolated pages.

---

### 9. Keep implementation simple

Requirements:
- use FastAPI routes
- use Jinja templates
- prefer a shared base template
- do not add React/Vue/Next.js/etc.
- do not introduce unnecessary complexity

This should remain easy to run locally and easy to understand in a class project context.

---

### 10. Update README

Add a section describing the web UI and available pages.

Include:
- how to run the app
- what each page is for
- how to navigate the site
- note that the site now acts as both demo interface and presentation companion

---

## Recommended page structure

Suggested routes:

- `/` — Home / Overview
- `/demo` — Live Demo
- `/how-it-works` — Methods / Explanation
- `/results` — Outputs / Metrics / Visuals
- `/architecture` — Refactor + System Design
- `/presentation` — Slide-style presentation content

---

## Design guidance

Use a **clean top navbar**.

Prioritize:
- clarity
- spacing
- consistency
- screenshot-friendliness
- readability over flashiness

The site should look polished enough for:
- a class presentation
- a portfolio walkthrough
- a repo visitor who lands on it cold

---

## Constraints

- Work on a new branch only
- Keep changes incremental
- Do not rewrite backend logic
- Do not add NemoClaw yet
- Do not introduce a heavy frontend stack
- Keep the app simple, stable, and presentation-friendly

---

## Deliverables

- new GitHub issue
- new branch
- shared top navigation
- new routes and templates
- improved homepage
- improved demo page
- new “How It Works” page
- new “Results” page
- new “Architecture” page
- new “Presentation” page
- updated README
- pull request summarizing the changes

---

## Follow-up instruction

After completing this work, the web app should function as:

- live demo
- project explainer
- presentation companion
- portfolio site

Future work (NOT part of this task):
- agent runtime integration
- real-time monitoring simulation
- async workflows
- production deployment polish
