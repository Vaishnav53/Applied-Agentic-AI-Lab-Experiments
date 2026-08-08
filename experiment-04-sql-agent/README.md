# Experiment 4: SQL Agent with Tool Use

**Course Code:** MR23-1CS0436  
**Course Name:** Applied Agentic AI  
**Laboratory:** Applied Agentic AI Laboratory  
**Status:** ⬜ Pending  

---

## 🎯 Aim
To develop an autonomous ReAct-based SQL agent equipped with database inspection, query execution, error reflection, and auto-correction tools to answer complex multi-table analytical questions.

---

## 📜 Problem Statement
Unlike single-pass Text-to-SQL (Experiment 1), real-world database queries often fail on first attempt due to syntax errors, ambiguous column names, or missing joins. A single LLM prompt cannot self-correct when execution errors occur. A ReAct (Reason + Act) SQL Agent dynamically inspects database schemas, writes trial queries, captures execution errors, and loops autonomously until it finds the correct result.

---

## 🎯 Objectives
1. Implement a set of database agent tools: `list_tables`, `get_schema`, `execute_sql`, `check_query_syntax`.
2. Construct a ReAct agent loop incorporating thought-action-observation cycles.
3. Add automated error handling and reflection mechanisms for failed SQL executions.
4. Build an interactive web UI that visualizes the agent's internal thought process, tool invocations, and database responses.

---

## 💡 Agentic AI Concept Overview
This experiment introduces **The ReAct (Reasoning + Acting) Agent Pattern & Tool Integration**.

The agent operates in an iterative loop:
1. **Thought:** Reason about what information is needed.
2. **Action:** Select and invoke a specific tool with generated parameters.
3. **Observation:** Read the tool's return value (or error traceback).
4. **Reflection/Repeat:** Adjust strategy until the final answer is derived.

---

## 🏗️ System Architecture & Workflow

```
┌──────────────────┐     ┌─────────────────────────────────────────────────────────┐
│ User Query Input │ ──> │                        ReAct Agent                      │
└──────────────────┘     │  ┌───────────┐    ┌────────────┐    ┌──────────────┐  │
                         │  │  Thought  │ -> │   Action   │ -> │ Observation  │  │
                         │  └───────────┘    └────────────┘    └──────────────┘  │
                         └────────────────────────────┬────────────────────────────┘
                                                      │ Tool Call Invocation
                                                      ▼
                         ┌─────────────────────────────────────────────────────────┐
                         │                     Agent Database Tools                │
                         │  [list_tables] [get_schema] [execute_sql] [validate]    │
                         └─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Technologies Used
* **Programming Language:** Python 3.10+
* **Agent Framework:** LangChain Agents / LangGraph / ReAct Engine
* **Database Tools:** SQLite / SQLAlchemy
* **User Interface:** Streamlit interactive trace viewer

---

## 📦 Installation Instructions

```bash
cd experiment-04-sql-agent
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

---

## 🚀 Execution Instructions

```bash
# Execute agent terminal runner with trace logging
python src/agent.py

# Launch agent reasoning trace UI
streamlit run app.py
```

---

## 📥 Example Inputs & 📤 Expected Outputs

### Example Input
> *"Which department has the highest average employee salary, and how many employees work there?"*

### Expected Output Trace
```
Thought: I need to inspect the tables in the database to locate employee and department data.
Action: list_tables()
Observation: ['employees', 'departments', 'salaries']

Thought: Now I need the schema for employees and departments.
Action: get_schema('employees, departments')
Observation: CREATE TABLE employees (id, name, dept_id, salary)...

Thought: I will write a JOIN query to calculate average salary per department.
Action: execute_sql("SELECT d.dept_name, AVG(e.salary), COUNT(e.id) FROM employees e JOIN departments d ON e.dept_id = d.id GROUP BY d.dept_name ORDER BY AVG(e.salary) DESC LIMIT 1;")
Observation: [('Engineering', 125000.0, 14)]

Final Answer: The Engineering department has the highest average salary ($125,000.00) with 14 employees.
```

---

## 🖼️ Results & Screenshots
*(Agent reasoning trace UI screenshots will be added upon implementation.)*

---

## 📊 Result
*(To be populated after execution verification.)*

---

## 📝 Conclusion
*(To be populated after lab implementation completion.)*

---

## ❓ Viva Voce Questions & Key Concepts

1. **Q: How does a ReAct agent differ from a standard chain pipeline?**  
   *A:* A chain follows a fixed, pre-determined sequence of steps, whereas a ReAct agent dynamically decides which action or tool to take based on runtime observations.

2. **Q: What prevents an agent from entering an infinite tool execution loop?**  
   *A:* Setting `max_iterations`, `recursion_limit`, and implementing cost/token guardrails alongside explicit loop termination conditions.
