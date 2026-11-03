from fastapi import FastAPI

app = FastAPI(
    title="KisanMind AI",
    description="Telugu-First Agentic AI Farming Intelligence Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to KisanMind AI",
        "project": "AI Farming Intelligence Platform",
        "status": "Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "KisanMind AI",
        "version": "1.0.0"
    }


@app.get("/about")
def about():
    return {
        "name": "KisanMind AI",
        "purpose": "Helping farmers make smarter farming decisions",
        "languages": ["Telugu", "English"]
    }