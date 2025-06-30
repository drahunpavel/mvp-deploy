# Python MVP Microservices

This project is a minimal MVP composed of two FastAPI-based microservices with shared logic extracted into a common module

##  Endpoints

#### `/auth-api`
- `POST /register` — Register a new user
- `POST /login` — Authenticate and receive a token

#### `/ui-api`
- `GET /info` — Retrieve basic application info

##  Setup & Run

Each service has its own virtual environment

### 1. Create and activate virtual environment

```bash
cd backend/auth-api # and backend/ui-api
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
pip install -e ../shared
```
### 3. Configure environment variables

```bash
cp .env.example .env
```
Then open .env and replace placeholder values

### 4. Run the service

```bash
python3 main.py
```