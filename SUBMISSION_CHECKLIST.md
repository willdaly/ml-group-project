# Submission Checklist

## Required Deliverables

- Dataset included: `data/nsl-kdd/KDDTrain+.txt` and `data/nsl-kdd/KDDTest+.txt`
- Combined code included: `main.py`, `src/`, `EDA.ipynb`, and `tests/`
- Written report included: `Report.md`
- Presentation deck content included: `PRESENTATION.md`
- Generated charts and metrics included: `outputs/`

## Final Pre-Turn-In Checks

- Replace the group-member placeholders in `PRESENTATION.md`
- Confirm the report and deck match the names of the students submitting
- Re-run:

```bash
pytest
python main.py --data-dir data/nsl-kdd --output-dir outputs
```

## Assignment Coverage Map

- Business problem: `Report.md` and Slides 1-2 in `PRESENTATION.md`
- Dataset choice and rationale: `Report.md`, `data/nsl-kdd/README.md`, and Slide 3
- EDA methodology and findings: `EDA.ipynb`, `src/eda.py`, `Report.md`, and Slides 4-5
- Predictive analytics / ML algorithms / metrics: `src/train_models.py`, `Report.md`, and Slides 6-7
- Prescriptive analytics / recommendations: `Report.md` and Slide 8
- Code walkthrough: `main.py`, `src/`, `EDA.ipynb`, and Slide 9
