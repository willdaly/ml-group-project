# Demo Runbook

Step-by-step instructions for running the NSL-KDD cybersecurity detection demo.

---

## Prerequisites

```bash
pip install -r requirements.txt
```

## 1. Train models (one-time)

```bash
python main.py --data-dir data/nsl-kdd --output-dir outputs --model-dir models
```

This creates `models/binary_model.joblib` and `models/multiclass_model.joblib`.

## 2. Start the FastAPI server

```bash
uvicorn src.api.app:app --reload
```

Server starts at **http://127.0.0.1:8000**.

## 3. Open the demo

Navigate to:

```
http://127.0.0.1:8000/demo
```

---

## 60-Second Demo Script

| Step | Action | What to show |
|------|--------|--------------|
| 1 | Open `/demo` in a browser | Status bar shows "Model ready" |
| 2 | Click **Load Benign Example** | Textarea fills with normal HTTP traffic |
| 3 | Click **Score Record** | Green result card: "Normal Traffic", high confidence |
| 4 | Click **Load Attack Example** | Textarea fills with SYN flood pattern |
| 5 | Click **Score Record** | Red result card: "Attack Detected", attack category, explanation |

### Talking points

- **Binary classification** separates normal from attack traffic.
- **Multiclass model** identifies the attack category (DoS, Probe, R2L, U2R).
- **Confidence score** shows how certain the model is.
- **Explanation** highlights which features drove the prediction.

---

## Useful API endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Check if models are loaded |
| `/predict` | POST | Score a single record |
| `/predict/batch` | POST | Score multiple records |
| `/report/incidents` | POST | Generate incident summary |
| `/demo` | GET | Browser demo page |

## Example curl commands

**Single prediction:**

```bash
curl -s http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d @examples/benign_record.json \
  | python -m json.tool
```

**Batch prediction:**

```bash
curl -s http://127.0.0.1:8000/predict/batch \
  -H "Content-Type: application/json" \
  -d "{\"records\": $(cat examples/demo_batch.json)}" \
  | python -m json.tool
```

**Incident report:**

```bash
curl -s http://127.0.0.1:8000/report/incidents \
  -H "Content-Type: application/json" \
  -d "{\"records\": $(cat examples/demo_batch.json)}" \
  | python -m json.tool
```
