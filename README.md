# Inventory & Sales API

A backend API for managing products, inventory, and sales.

## Tech Stack
- Python
- FastAPI
- Uvicorn

## Run Locally

```bash
python3 -m venv venv

Activate the virtural environment, then install dependencies:

pip install -r requirements.txt
uvicorn app.main:app --reload

API Documentation
Visit:
. /docs for Swagger UI
. /health for the health-check endpoint

## 8. commit your work

```bash
git init git add .
git commit -m "set up FastAPI project structure"

If Git asks for your identity, run:

</> Bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"

Then rerun the commit. 

Completion checklist
. uvicorn app.main:app --reload rns
. /health works
. /docs works
. app/main.py exists
. .gitignore exists
. requirements.txt exists
. First Git commit completed