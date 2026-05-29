from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

app = FastAPI(
    title="Abely Ntandu - Data Science Portfolio API",
    description="Backend API supplying data for portfolio",
    version="1.0.0"
)

# =========================
# CORS CONFIG (PRODUCTION SAFE)
# =========================

FRONTEND_URL = os.getenv("FRONTEND_URL")

origins = []

if FRONTEND_URL:
    origins.append(FRONTEND_URL)

# ALWAYS allow localhost for development
origins.append("http://localhost:5173")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# DATA MODELS
# =========================

class Project(BaseModel):
    title: str
    description: str
    technologies: List[str]
    github_url: str

class ContactMessage(BaseModel):
    name: str
    email: str
    message: str

# =========================
# STATIC DATA
# =========================

PROJECTS_DATA = [
    {
        "title": "SQL Data Warehouse Project",
        "description": "Designed enterprise-grade Data Warehouse using star schema architecture.",
        "technologies": ["SQL", "SQL SERVER", "ETL Pipelines"],
        "github_url": "https://github.com/Ant-darkness/sql-Datawarehouse-Project"
    },
    {
        "title": "SQL Data Analytics Project",
        "description": "Advanced exploratory data analysis using SQL window functions and CTEs.",
        "technologies": ["SQL", "SQL SERVER", "Data Analysis"],
        "github_url": "https://github.com/Ant-darkness/SQL_Data_Analytics_project"
    },
    {
        "title": "Happiness Predictor",
        "description": "Machine Learning model predicting global happiness index using ensemble learning.",
        "technologies": ["Python", "Scikit-Learn", "Pandas"],
        "github_url": "https://github.com/Ant-darkness/Happines_Predictor"
    },
    {
        "title": "SQL Data Jobs Analysis",
        "description": "Market analysis of global data jobs and salary trends.",
        "technologies": ["SQL", "PostgreSQL"],
        "github_url": "https://github.com/Ant-darkness/SQL_Data_Jobs_Analysis"
    },
    {
        "title": "Amazon Stock Volume Predictor",
        "description": "Time-series forecasting model for Amazon stock volume prediction.",
        "technologies": ["Python", "Linear Regression", "Time Series"],
        "github_url": "https://github.com/Ant-darkness/Amazon-Stock-Volume-Predictor"
    }
]

# =========================
# ROUTES
# =========================

@app.get("/")
def home():
    return {
        "status": "Online",
        "owner": "Abely J. Ntandu",
        "role": "Data Scientist"
    }

@app.get("/api/projects", response_model=List[Project])
def get_projects():
    return PROJECTS_DATA

@app.post("/api/contact")
def send_contact(message: ContactMessage):
    return {
        "status": "success",
        "message": f"Thank you {message.name}, your message has been received."
    }

@app.get("/health")
def health():
    return {"status": "ok"}
