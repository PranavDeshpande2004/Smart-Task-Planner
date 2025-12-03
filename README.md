# 🚀 Smart Task Planner

**Smart Task Planner** converts any user goal into a complete action plan with:
- Tasks  
- Dependencies  
- Durations  
- Timelines  
- Feasibility check  

Built using **FastAPI**, **LangChain**, and a **Single LLM Agent**, with an easy upgrade path to a **multi-agent system (LangGraph)**.

---

## ⭐ Features
- 🧠 AI-driven task breakdown  
- 🔗 Automatic dependency generation  
- ⏳ Smart scheduling with start/end dates  
- 📅 Deadline + feasibility analysis  
- 🧱 Clean JSON output with Pydantic  
- ⚡ FastAPI backend API  

---

## 🏗️ Architecture

**Flow:**  
User → FastAPI → Single LangChain Agent → LLM → JSON Output

             ┌────────────────────────────┐
             │         User Input         │
             │  "Launch a product..."     │
             └──────────────┬─────────────┘
                            │
                            ▼
                 ┌────────────────────┐
                 │      FastAPI       │
                 │   /api/plan API    │
                 └──────────┬─────────┘
                            │
                            ▼
             ┌─────────────────────────────────┐
             │     LangChain Single Agent      │
             │  - Prompt Template              │
             │  - LLM Reasoning                │
             │  - JSON Output Parser (Pydantic)│
             └──────────┬──────────────────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     LLM Response    │
                 │  Tasks + Timeline   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Final JSON Plan    │
                 └──────────────────────┘

### **LLM Responsibilities (Single Agent)**  
1. Understand the user goal  
2. Extract deadlines  
3. Break into tasks  
4. Add task dependencies  
5. Assign durations  
6. Generate a schedule  
7. Validate feasibility  
8. Output structured JSON  

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | FastAPI |
| AI Agent | LangChain (RunnableSequence) |
| LLM | GPT-4.1 / GPT-3.5 / Llama on Groq |
| Validation | Pydantic Models |
| Output | JSON REST API |
| Upgrade Ready | LangGraph (Multi-Agent Architecture) |

---

## 📡 API Usage

### **POST /api/plan**

#### Request Body
```json
{
  "goalText": "Launch a mobile app in 2 weeks"
}

