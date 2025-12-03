from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableSequence
from datetime import date
from.schemas import SmartPlan



# Prompt Template for the Single Agent
prompt = PromptTemplate(
    template="""
You are the Smart Task Planner Agent.

Today's date: {today}
User goal: {goalText}

Your responsibilities:
1. Understand the user goal
2. Extract any deadlines or time constraints
3. Break the goal down into actionable tasks
4. Add dependencies using task IDs (T1, T2, T3...)
5. Estimate duration (in days)
6. Create a timeline (startDate, endDate)
7. Validate feasibility (true/false)
8. Return ONLY valid JSON using this schema:

{json_schema}

IMPORTANT:
- Dates must be in YYYY-MM-DD format
- startDate <= endDate
- Dependencies must reference valid task IDs
- If the task list cannot fit into the deadline, set feasible=false
""",
    input_variables=["goalText", "today", "json_schema"]
)

#llm model
model=ChatOpenAI(model_name="gpt-4o-mini", temperature=0)


# JSON Output Parser
parser = JsonOutputParser(pydantic_object=SmartPlan)


# Runnable Chain (Single Agent)
smart_planner_agent = RunnableSequence(
    prompt
    | model
    | parser
)