from pydantic import BaseModel
from typing import List, Optional   
class Task(BaseModel):
    id: str
    title: str
    description: str
    estimatedDurationDays: int
    dependsOn: List[str]
    startDate: str
    endDate: str
    category: str
    priority: str
    
class SmartPlan(BaseModel):
    goal: str
    deadline: Optional[str]
    feasible: bool
    warnings: List[str]
    tasks: List[Task]
    
class GoalRequest(BaseModel):
    goalText: str    