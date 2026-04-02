# Pink Czech History FastAPI App

A simple, very pink and flashy FastAPI web app that shows a one-paragraph overview of the history of the Czech Republic.

## Requirements

- Python 3.9+

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Files

- `main.py` - FastAPI application and pink HTML page.
- `requirements.txt` - Python dependencies.
