from fastapi import FastAPI
from datetime import date

from .agent import smart_planner_agent
from .schemas import GoalRequest


app = FastAPI(title="Smart Task Planner API")


@app.post("/api/plan")
async def generate_plan(req: GoalRequest):
    today = str(date.today())

    # Invoke Single Agent
    result = smart_planner_agent.invoke({
        "goalText": req.goalText,
        "today": today,
        "json_schema": smart_planner_agent.output_schema.schema_json()
    })

    return result
