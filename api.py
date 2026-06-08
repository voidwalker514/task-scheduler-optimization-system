from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from src.scheduler import TaskScheduler
from src.utils import load_tasks_from_csv
import uvicorn
import os

app = FastAPI(title="Task Scheduler Dashboard")

# Ensure directories exist
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_dashboard():
    return FileResponse("templates/index.html")

@app.get("/api/schedule")
def get_schedule():
    tasks = load_tasks_from_csv('data/tasks.csv')
    scheduler = TaskScheduler()
    for t in tasks:
        scheduler.add_task(t)
    scheduler.run_schedule()
    
    completed = []
    for task, end_time in scheduler.completed_tasks:
        completed.append({
            "name": task.name,
            "start": end_time - task.duration,
            "end": end_time,
            "profit": task.profit,
            "priority": task.priority,
            "duration": task.duration
        })
        
    missed = []
    for task in scheduler.missed_tasks:
        missed.append({
            "name": task.name,
            "deadline": task.deadline,
            "duration": task.duration,
            "priority": task.priority,
            "profit": task.profit
        })
        
    return {
        "completed_tasks": completed,
        "missed_tasks": missed,
        "total_profit": scheduler.total_profit,
        "total_time_spent": scheduler.total_time_spent,
        "total_tasks": len(tasks),
        "completed_count": len(scheduler.completed_tasks)
    }

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
