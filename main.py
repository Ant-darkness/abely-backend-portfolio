from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(
    title="Abely Ntandu - Data Science Portfolio API",
    description="Backend API supplying data for Abely's Professional Portfolio",
    version="1.0.0"
)

# Ruhusu Frontend kutoka Vercel iwasiliane na Backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Kwenye production unaweza kuweka URL ya Vercel pekee
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Schemas
class Project(BaseModel):
    title: str
    description: str
    technologies: List[str]
    github_url: str

class ContactMessage(BaseModel):
    name: str
    email: str
    message: str

# Static Data for Portfolio
PROJECTS_DATA = [
    {
        "title": "SQL Data Warehouse Project",
        "description": "Designed and implemented an enterprise-grade Data Warehouse utilizing star schema architecture. Optimized ETL/ELT pipelines for efficient data ingestion and historical tracking.",
        "technologies": ["SQL", "SQL SERVER", "ETL Pipelines"],
        "github_url": "https://github.com/Ant-darkness/sql-Datawarehouse-Project"
    },
    {
        "title": "SQL Data Analytics Project",
        "description": "Advanced exploratory data analysis to extract actionable business insights. Developed complex window functions, CTEs, and aggregations to drive strategic decisions.",
        "technologies": ["SQL", "SQL SERVER", "Data Analysis"],
        "github_url": "https://github.com/Ant-darkness/SQL_Data_Analytics_project"
    },
    {
        "title": "Happiness Predictor",
        "description": "An end-to-end Machine Learning project predicting global happiness indices based on socio-economic metrics. Deployed with high accuracy using ensemble learning.",
        "technologies": ["Python", "Scikit-Learn", "Pandas", "Random Forest"],
        "github_url": "https://github.com/Ant-darkness/Happines_Predictor"
    },
    {
        "title": "SQL Data Jobs Analysis",
        "description": "Comprehensive market analysis of global data-related job roles. Extracted data trends regarding top skills, average salaries, and high-demand tech stacks.",
        "technologies": ["SQL", "Data Cleaning", "PostgreSQL"],
        "github_url": "https://github.com/Ant-darkness/SQL_Data_Jobs_Analysis"
    },
    {
        "title": "Amazon Stock Volume Predictor",
        "description": "A Time-series forecasting model engineered to predict Amazon's stock trading volume, leveraging historical trends.",
        "technologies": ["Python", "Linear regression", "Time Series"],
        "github_url": "https://github.com/Ant-darkness/Amazon-Stock-Volume-Predictor"
    }
]

@app.get("/")
def home():
    return {"status": "Online", "owner": "Abely J. Ntandu", "role": "Data Scientist"}

@app.get("/api/projects", response_model=List[Project])
def get_projects():
    return PROJECTS_DATA

@app.post("/api/contact")
def send_contact(message: ContactMessage):
    # Hapa ujumbe unaweza kuhifadhiwa au kutumwa kwenye email yako
    return {"status": "success", "message": f"Thank you {message.name}, your message has been received."}
