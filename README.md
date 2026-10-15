# Eco-Guard — Intelligent Economic Inspector

An AI-powered multi-agent system for verifying household survey data (GASTAT, Saudi Arabia).
Three Claude-powered agents — **Demographic**, **Financial**, and **Manager** — analyze each record and produce a 0–100 trust score with recommendations.

> SW 413 – Data Exploration and Visualization · Princess Nourah bint Abdulrahman University · Groupe 02 · 2nd Semester 2026

## Features
- Arabic RTL Streamlit dashboard
- Role-based authentication (PBKDF2 password hashing) with admin audit log
- Manual entry and batch CSV analysis (parallel agents)
- Plotly gauge and bar charts
- Color-coded Excel export

## Architecture
Streamlit frontend (`app.py`, `api_client.py`, `database.py`) → FastAPI backend (`api.py`: `/agent/demographic`, `/agent/financial`, `/agent/manager`) → Anthropic Claude API.

## Run locally
```bash
cd SW413_Groupe02_EcoGuard_Code
pip install -r requirements.txt

# backend
export ANTHROPIC_API_KEY=your_key_here
uvicorn api:app --port 8000

# frontend (new terminal)
export API_BASE_URL=http://localhost:8000
streamlit run app.py
```
Default admin user: `eco` (password from the `ADMIN_PASSWORD` env var).

## Team
| Name | Role |
|---|---|
| Haneen Alshuwayqi | Team Leader & Backend Developer |
| Sumaiya Balatif | Frontend Developer |
| Taif Alshehri | AI & Agents Engineer |
| Munirah Almousa | Data Analyst |
| Bushra Almughirah | Documentation & Visualization |

Original group repository: https://github.com/Haneen-Alshuwayqi/Eco-Guard

## Documents
- [Project Report](SW413_Groupe02_EcoGuard_Report.pdf)
- [Presentation](SW413_Groupe02_EcoGuard_Presentation.pdf)
