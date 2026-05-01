from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pipeline import run_research_pipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TopicRequest(BaseModel):
    topic: str

@app.get("/")
def index():
    return FileResponse("index.html")

@app.post("/api/run")
def run_pipeline(req: TopicRequest):
    result = run_research_pipeline(req.topic)
    return {
        "search_result": result.get("search_result", ""),
        "scraped_content": result.get("scraped_content", ""),
        "report": result.get("report", ""),
        "feedback": result.get("feedback", ""),
    }