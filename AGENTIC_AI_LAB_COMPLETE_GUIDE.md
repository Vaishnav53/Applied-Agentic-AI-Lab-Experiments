# Applied Agentic AI Laboratory — Complete Experiment, Workflow & Execution Guide

**Course Code:** MR23-1CS0436
**Course Name:** Applied Agentic AI
**Laboratory:** Applied Agentic AI Laboratory
**Repository:** Applied-Agentic-AI-Lab-Experiments
**Current Completed Experiments:** 7 / 12
**Status:** Living Master Laboratory Reference Guide

---

## Master Table of Contents
- [1. Laboratory Overview](#1-laboratory-overview)
- [2. Repository Architecture](#2-repository-architecture)
- [3. Common Environment Setup](#3-common-environment-setup)
- [4. Repository Directory Structure](#4-repository-directory-structure)
- [5. Experiment Status Matrix](#5-experiment-status-matrix)
- [6. Experiment 01 — Text-to-SQL Workflow](#6-experiment-01--text-to-sql-workflow)
- [7. Experiment 02 — RAG-Based Question Answering System](#7-experiment-02--rag-based-question-answering-system)
- [8. Experiment 03 — Prompt Chaining for Summarization](#8-experiment-03--prompt-chaining-for-summarization)
- [9. Experiment 04 — Autonomous ReAct SQL Agent with Tool Use](#9-experiment-04--autonomous-react-sql-agent-with-tool-use)
  - [A. Experiment Identification](#a-experiment-04-identification)
  - [B. Aim](#b-experiment-04-aim)
  - [C. Problem Statement](#c-experiment-04-problem-statement)
  - [D. Learning Objectives](#d-experiment-04-learning-objectives)
  - [E. Concepts Used](#e-experiment-04-concepts-used)
  - [F. Why This Experiment Matters](#f-experiment-04-why-this-experiment-matters)
  - [G. Complete System Architecture](#g-experiment-04-complete-system-architecture)
  - [H. Complete Workflow](#h-experiment-04-complete-workflow)
  - [I. Internal Data Flow](#i-experiment-04-internal-data-flow)
  - [J. Folder Structure](#j-experiment-04-folder-structure)
  - [K. Technology Stack](#k-experiment-04-technology-stack)
  - [L. Installation](#l-experiment-04-installation)
  - [M. Exact Execution Procedure](#m-experiment-04-exact-execution-procedure)
  - [N. How to Use the UI](#n-experiment-04-how-to-use-the-ui)
  - [O. Demonstration Procedure](#o-experiment-04-demonstration-procedure)
  - [P. Sample Inputs](#p-experiment-04-sample-inputs)
  - [Q. Expected Outputs](#q-experiment-04-expected-outputs)
  - [R. Screenshots](#r-experiment-04-screenshots)
  - [S. Testing](#s-experiment-04-testing)
  - [T. Safety / Validation](#t-experiment-04-safety--validation)
  - [U. Limitations](#u-experiment-04-limitations)
  - [V. Troubleshooting](#v-experiment-04-troubleshooting)
  - [W. Viva Questions](#w-experiment-04-viva-questions)
  - [X. Conclusion](#x-experiment-04-conclusion)
- [10. Comparison of Experiments 01–04](#10-comparison-of-experiments-0104)
- [11. Common Execution Guide](#11-common-execution-guide)
- [12. Troubleshooting Guide](#12-troubleshooting-guide)
- [13. Testing Guide](#13-testing-guide)
- [14. Git & GitHub Workflow](#14-git--github-workflow)
- [15. Faculty Demonstration Cheat Sheet](#15-faculty-demonstration-cheat-sheet)
- [16. Viva Preparation Guide](#16-viva-preparation-guide)
- [17. Future Experiments Overview (05–12)](#17-future-experiments-overview-0512)
- [18. Master Guide Maintenance Policy](#18-master-guide-maintenance-policy)

---

## 1. Laboratory Overview

### What is Applied Agentic AI?
**Applied Agentic AI** represents the evolution of artificial intelligence from passive input-output text generation to **autonomous, goal-driven computational systems**. While traditional Large Language Models (LLMs) act as static statistical generators, **Agentic AI systems** leverage reasoning loops, memory structures, vector indices, external database tools, prompt chaining pipelines, and multi-agent collaboration to execute multi-step complex workflows.

### Purpose of this Laboratory
This laboratory course (**MR23-1CS0436**) provides a rigorous, hands-on framework for engineering production-ready Agentic AI applications. Students bridge the gap between theoretical artificial intelligence principles and software architecture by designing, building, testing, and evaluating 12 isolated agentic modules.

### Pedagogical Progression
The 12-experiment sequence advances systematically across five core paradigms:
1. **Tool Augmented Retrieval & Workflows** (Experiments 01–03): Structuring schema-driven SQL generation, hybrid vector-lexical RAG retrieval, and 6-stage sequential prompt chaining.
2. **ReAct & Autonomous Agents** (Experiments 04–06): Building tool-using reasoning agents, multi-agent sales SDR teams, and policy compliance verification agents.
3. **Deep Reflection & Multimodal Intelligence** (Experiments 07–09): Implementing iterative self-reflection loops, visual QA, and reasoning model benchmarks.
4. **Model Adaptation & Optimization** (Experiments 10–11): Domain fine-tuning (LoRA/PEFT) and post-training quantization.
5. **Capstone Agentic Integration** (Experiment 12): Deploying an enterprise multi-agent RAG ecosystem.

---

## 2. Repository Architecture

The repository **`Applied-Agentic-AI-Lab-Experiments`** is structured into isolated, self-contained experiment directories (`experiment-01-text-to-sql`, `experiment-02-rag-qa`, `experiment-03-prompt-chaining`, `experiment-04-sql-agent`, etc.). Each experiment functions as an independent software package with its own:
- Dedicated virtual environment and `requirements.txt`
- Server entry point (`app/main.py`)
- Pydantic schema contracts (`app/schemas.py`) and application settings (`app/config.py`)
- Business logic services (`app/services/*`)
- Glassmorphic Web Application UI (`app/static/*`)
- Unit and integration test suite (`tests/*`)
- Empirical execution screenshots (`screenshots/*`)

---

## 3. Common Environment Setup

### Prerequisites
- **Operating System:** Windows 10/11 (PowerShell), Linux, or macOS
- **Python Runtime:** Python 3.10, 3.11, or 3.14 (Verified on Python 3.14.6)
- **Package Manager:** `pip`
- **Git Version Control:** Git 2.x+

### Environment Configuration Standard
Every experiment includes a safe configuration template (`.env.example`). Real secrets and local API keys are placed inside `.env` (which is strictly excluded by `.gitignore`).

#### Windows PowerShell Setup Pattern:
```powershell
cd "D:\Agentic AI Experiments\experiment-04-sql-agent"
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
Copy-Item .env.example .env
python data/seed.py
```

#### Linux / macOS Setup Pattern:
```bash
cd "D:/Agentic AI Experiments/experiment-04-sql-agent"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python3 data/seed.py
```

---

## 4. Repository Directory Structure

```
D:\Agentic AI Experiments/
│
├── README.md                           # Master repository summary & status matrix
├── AGENTIC_AI_LAB_COMPLETE_GUIDE.md    # Living Master Laboratory Guide (THIS DOCUMENT)
├── LICENSE                             # MIT License
├── .gitignore                          # Excludes secrets, venvs, cache, and DBs
│
├── experiment-01-text-to-sql/          # Exp 01: Text-to-SQL LLM Workflow (Port 8000)
├── experiment-02-rag-qa/               # Exp 02: Cybersecurity Hybrid RAG QA (Port 8001)
├── experiment-03-prompt-chaining/      # Exp 03: 6-Stage Prompt Chaining Summarizer (Port 8002)
│
├── experiment-04-sql-agent/            # Exp 04: Autonomous ReAct SQL Agent with Tool Use (Port 8003)
│   ├── README.md
│   ├── requirements.txt
│   ├── .env.example
│   ├── app/
│   │   ├── main.py                     # FastAPI Entry Point
│   │   ├── config.py                   # Pydantic Settings
│   │   ├── database.py                 # Read-only SQLite Engine & Execution Manager
│   │   ├── models.py                   # SQLAlchemy Models (Department, Employee, Project, EmployeeProject)
│   │   ├── schemas.py                  # Pydantic Request/Response Schemas
│   │   ├── services/
│   │   │   ├── database_tools.py       # Implementation of 4 Database Agent Tools
│   │   │   ├── sql_validator.py        # Token-Based Read-Only SQL Security Validator
│   │   │   ├── llm_service.py          # Grounded LLM Decision Engine (Mock & Real Providers)
│   │   │   └── agent_service.py        # ReAct Autonomous Agent Loop Orchestrator
│   │   └── static/                     # HTML5/CSS/JS Glassmorphic Agent Workbench UI
│   ├── data/
│   │   ├── company.db                  # SQLite Relational Database (4 tables)
│   │   └── seed.py                     # Database Seed Data Script
│   ├── tests/                          # 21 PyTest Unit/Integration Tests
│   └── screenshots/                    # 6 Verified Screenshots & README
│
├── experiment-05-multi-agent-sdr/      # Exp 05: Multi-Agent SDR System (Pending)
├── experiment-06-policy-compliance/   # Exp 06: Policy Compliance Agent (Pending)
├── experiment-07-deep-research/        # Exp 07: Deep Research Agent Workflow (Pending)
├── experiment-08-visual-qa/            # Exp 08: Visual QA & Image Retrieval (Pending)
├── experiment-09-reasoning-benchmark/  # Exp 09: Reasoning Model Benchmarking (Pending)
├── experiment-10-fine-tuning/          # Exp 10: Fine-Tuning Domain Adaptation (Pending)
├── experiment-11-model-optimization/  # Exp 11: Model Quantization & Distillation (Pending)
└── experiment-12-capstone/             # Exp 12: Mini Project Capstone (Pending)
```

---

## 5. Experiment Status Matrix

| Exp # | Experiment Title | Core AI Concept | Primary Interface | Status | Port | Test Count | Documentation |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **01** | Text-to-SQL Workflow | Schema Context & Lexical Read-Only Security Validation | Interactive Web App | ✅ Completed | `8000` | 8 Passed | `README.md` & Master Guide |
| **02** | RAG-Based QA System | Hybrid Vector+Lexical RAG & Term Normalization | Interactive Web App | ✅ Completed | `8001` | 20 Passed | `README.md` & Master Guide |
| **03** | Prompt Chaining Summarizer | 6-Stage Context Propagation & Quality Metrics | Interactive Web App | ✅ Completed | `8002` | 17 Passed | `README.md` & Master Guide |
| **04** | SQL Agent with Tool Use | Bounded ReAct Loop, Schema Reflection & Error Correction | Interactive Web App | ✅ Completed | `8003` | 21 Passed | `README.md` & Master Guide |
| **05** | Multi-Agent SDR System | Autonomous Multi-Agent Role Collaboration | Web Dashboard | ⬜ Pending | `8004` | — | Pending |
| **06** | Policy Compliance Agent | Rule Evaluation & Synthetic Safeguards | Web Dashboard | ⬜ Pending | `8005` | — | Pending |
| **07** | Deep Research Agent | Planning & Iterative Self-Reflection | Web Dashboard | ⬜ Pending | `8006` | — | Pending |
| **08** | Visual QA & Image Search | Multimodal Vision QA & Feature Search | Web Dashboard | ⬜ Pending | `8007` | — | Pending |
| **09** | Reasoning Model Benchmark | Benchmark & CoT Prompting Comparison | Web Dashboard | ⬜ Pending | `8008` | — | Pending |
| **10** | Fine-Tuning Adaptation | LoRA / PEFT Model Domain Adaptation | CLI & Notebook | ⬜ Pending | `8009` | — | Pending |
| **11** | Model Optimization | Post-Training Quantization & Distillation | CLI & Notebook | ⬜ Pending | `8010` | — | Pending |
| **12** | Capstone Mini Project | End-to-End Multi-Agent RAG Ecosystem | Full Web Portal | ⬜ Pending | `8011` | — | Pending |

---

## 6. Experiment 01 — Text-to-SQL Workflow
*(Refer to Section 6 of previous releases for complete Exp 01 documentation)*

---

## 7. Experiment 02 — RAG-Based Question Answering System
*(Refer to Section 7 of previous releases for complete Exp 02 documentation)*

---

## 8. Experiment 03 — Prompt Chaining for Summarization
*(Refer to Section 8 of previous releases for complete Exp 03 documentation)*

---

## 9. Experiment 04 — Autonomous ReAct SQL Agent with Tool Use

### A. Experiment 04 Identification
- **Experiment Number:** 04
- **Experiment Name:** Autonomous ReAct SQL Agent with Tool Use
- **Course Code:** MR23-1CS0436
- **Status:** ✅ Completed & Verified
- **Directory:** `experiment-04-sql-agent`
- **Main Technology:** Python 3.10+, FastAPI, SQLite 3, SQLAlchemy ORM, Pydantic v2, HTML5/CSS Glassmorphism
- **Interface Type:** Web-Based Chatbot Workbench with Safe Agent Execution Trace & Tool Metrics
- **Default Runtime Mode:** Offline Grounded Mode (`MockLLMProvider`) / Configurable External LLM
- **Default Port:** `8003`

### B. Experiment 04 Aim
To design, implement, and evaluate an autonomous SQL agent operating in a controlled ReAct (DECIDE → ACT → OBSERVE → VALIDATE → RETRY/FINISH) loop, equipped with four specialized database tools (`list_tables`, `get_schema`, `check_query_syntax`, `execute_sql`), schema reflection, read-only safety controls, and automated error reflection with query auto-correction.

### C. Experiment 04 Problem Statement
In single-pass Text-to-SQL workflows (Experiment 01), a natural language question is translated into SQL and executed in a single static step. If the generated SQL fails due to an un-aliased column ambiguity, missing JOIN condition, or syntax error, the execution halts. A single prompt cannot self-correct upon execution failure. An **Autonomous ReAct SQL Agent** addresses this by dynamically discovering available tables, inspecting column schemas, validating query syntax, executing read-only SQL, observing execution output, reflecting on error messages, and auto-correcting candidate SQL until a grounded answer is produced.

### D. Experiment 04 Learning Objectives
1. **Tool Augmented Reasoning Loops:** Implement a bounded ReAct iteration loop (`MAX_AGENT_ITERATIONS = 8`) where the agent selects database tools dynamically based on observations.
2. **Safe Structured Agent Trace:** Maintain an auditable execution trace detailing step decisions, tool invocations, sanitized parameters, and observations without exposing hidden chain-of-thought text.
3. **Database Schema Reflection:** Enable agents to inspect tables and schema definitions dynamically rather than assuming fixed database structures.
4. **Error Reflection & Auto-Correction:** Implement reflection mechanisms that capture SQL execution warnings or errors, analyze root causes against schema metadata, and refine candidate queries autonomously.

### E. Experiment 04 Concepts Used

#### 1. ReAct (Reasoning + Acting) Agent Pattern
The agent operates in an iterative loop:
$$\text{Step}_t = \text{Decide}(\text{Question}, \text{History}_{1 \dots t-1}) \longrightarrow \text{InvokeTool}(\text{Tool}_t, \text{Args}_t) \longrightarrow \text{Observe}(\text{Result}_t)$$

#### 2. Safe Structured Action Trace
Rather than displaying unverified model internal thoughts, the agent exposes a safe structured trace object:
$$\text{TraceStep} = \{\text{step}, \text{decision\_summary}, \text{tool}, \text{arguments}, \text{observation}, \text{status}\}$$

#### 3. Bounded Iteration Guardrail
To prevent infinite tool execution loops, execution is strictly capped at `MAX_AGENT_ITERATIONS = 8`.

### F. Experiment 04 Why This Experiment Matters
Enterprise analytical systems require resilient database agents capable of self-correction when querying complex multi-table relational schemas. This experiment demonstrates the fundamental transition from static prompt workflows to autonomous tool-using agents.

### G. Experiment 04 Complete System Architecture

```mermaid
graph TD
    A[User Chatbot UI] -->|1. Question & Max Iterations| B[FastAPI Backend /api/agent/query]
    B -->|2. Run Agent Loop| C[Agent Orchestrator: app/services/agent_service.py]
    C -->|3. Tool 1: list_tables| D[Database Tools: app/services/database_tools.py]
    D -->|4. Available Tables| C
    C -->|5. Tool 2: get_schema| D
    D -->|6. Table Metadata & FKs| C
    C -->|7. Tool 3: check_query_syntax| E[SQL Validator: app/services/sql_validator.py]
    E -->|8. Safety Validation Status| C
    C -->|9. Tool 4: execute_sql| F[Database Engine: app/database.py]
    F -->|10. Data Rows or Execution Error| C
    C -->|11. Error Reflection / Auto-Correction if needed| C
    C -->|12. Final Answer Synthesis| G[LLM Provider: app/services/llm_service.py]
    G -->|13. Grounded Answer| B
    B -->|14. Render Answer + Execution Trace + Tool Metrics + DB Explorer| A
```

#### Component Breakdown
- **Web UI (`static/`)**: Glassmorphic workbench with question input, sample chips, tool invocation counters, Safe Agent Execution Trace timeline, SQL result table, and interactive Database Explorer.
- **FastAPI Router (`app/main.py`)**: Server running on port `8003` handling `/api/agent/query`, `/api/database/schema`, `/api/database/tables`, and `/api/health`.
- **Database Engine (`app/database.py`)**: Connects to `data/company.db` using read-only URI mode (`file:{db_path}?mode=ro`) with standard connection fallback.
- **ORM Models (`app/models.py`)**: Defines SQLAlchemy schemas for `departments`, `employees`, `projects`, and `employee_projects`.
- **Database Tools (`app/services/database_tools.py`)**: Implements `list_tables`, `get_schema`, `check_query_syntax`, and `execute_sql`.
- **SQL Security Validator (`app/services/sql_validator.py`)**: Token-based validator enforcing single-statement `SELECT`/`WITH` queries and blocking DML/DDL keywords.
- **Agent Orchestrator (`app/services/agent_service.py`)**: Controls the bounded ReAct loop, trace building, error reflection, and auto-correction.

### H. Experiment 04 Complete Workflow

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant UI as Chatbot Web UI
    participant API as FastAPI Backend
    participant Agent as Agent Orchestrator
    participant Tools as Database Tools
    participant Val as SQL Validator
    participant DB as SQLite (company.db)

    User->>UI: Types Question ("Which department has the highest average salary?")
    UI->>API: POST /api/agent/query {"question": "...", "max_iterations": 8}
    API->>Agent: run_sql_agent(question, max_iterations=8)
    Agent->>Tools: list_tables()
    Tools-->>Agent: ['departments', 'employees', 'projects', 'employee_projects']
    Agent->>Tools: get_schema(['departments', 'employees'])
    Tools-->>Agent: Columns, Data Types, Foreign Key Metadata
    Agent->>Val: sanitize_and_validate_sql(candidate_sql)
    Val-->>Agent: Validated SELECT Query
    Agent->>DB: execute_read_only_query(sql)
    alt Execution Warning / Column Ambiguity
        DB-->>Agent: Execution Note / Warning
        Agent->>Agent: Reflect on error & refine query (Add column aliases / GROUP BY)
        Agent->>DB: execute_read_only_query(refined_sql)
    end
    DB-->>Agent: Row Results & Columns
    Agent-->>API: Return Answer + Safe Action Trace + Tool Metrics
    API-->>UI: Render Answer + Trace Cards + Explorer
```

### I. Experiment 04 Internal Data Flow
1. **Input**: User submits *"Which department has the highest average employee salary, and how many employees work there?"*.
2. **Step 1 (list_tables)**: Discovers available tables (`departments`, `employees`, `projects`, `employee_projects`).
3. **Step 2 (get_schema)**: Inspects schema for `departments` and `employees`.
4. **Step 3 (check_query_syntax)**: Validates initial candidate query.
5. **Step 4 (execute_sql & Reflection)**: Detects column ambiguity warning on trial query, reflects on schema metadata, refines query with explicit aliases (`d.name AS department_name, AVG(e.salary) AS avg_salary`), and executes refined query.
6. **Step 5 (Final Synthesis)**: Grounded answer synthesized: *Product Management has the highest average salary ($127,000.00) with 3 employees.*

### J. Experiment 04 Folder Structure

```
experiment-04-sql-agent/
├── README.md                           # Comprehensive Experiment Report
├── requirements.txt                    # Project Dependencies
├── .env.example                        # Environment Template
├── app/
│   ├── __init__.py                     # Package Initializer
│   ├── main.py                         # FastAPI Server Entry Point & Router (Port 8003)
│   ├── config.py                       # Pydantic Settings
│   ├── database.py                     # SQLite Connection Engine & Read-Only Executor
│   ├── models.py                       # SQLAlchemy ORM Models (Department, Employee, Project, EmployeeProject)
│   ├── schemas.py                      # Pydantic Schemas (AgentQueryRequest, AgentQueryResponse, ToolCallTrace)
│   ├── services/
│   │   ├── database_tools.py           # Implementation of 4 Database Agent Tools
│   │   ├── sql_validator.py            # Token-Based Read-Only SQL Security Validator
│   │   ├── llm_service.py              # LLM Decision Engine (Mock & Real Providers)
│   │   └── agent_service.py            # ReAct Autonomous Agent Loop Orchestrator
│   └── static/                         # Glassmorphic UI Assets (index.html, style.css, app.js)
├── data/
│   ├── company.db                      # SQLite Relational Database (4 tables)
│   └── seed.py                         # Database Seeding Script
├── tests/                              # 21 Automated PyTest Unit & Integration Tests
└── screenshots/                        # 6 Verified Screenshot Artifacts & README
```

### K. Experiment 04 Technology Stack

| Technology | Purpose | Where Used |
| :--- | :--- | :--- |
| **Python 3.10+** | Programming Language | Core Backend Architecture |
| **FastAPI / Uvicorn** | Web Framework & ASGI Server | `app/main.py` (Port 8003) |
| **SQLite 3 & SQLAlchemy** | Relational Database Engine & ORM | `data/company.db`, `app/database.py`, `app/models.py` |
| **Pydantic v2** | API Schema Validation & Serialization | `app/schemas.py`, `app/config.py` |
| **Vanilla HTML5/CSS3/JS** | Glassmorphic Agent Workbench UI | `app/static/*` |

### L. Experiment 04 Installation
Open Windows PowerShell and navigate to the experiment directory:

```powershell
cd "D:\Agentic AI Experiments\experiment-04-sql-agent"
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
Copy-Item .env.example .env
python data/seed.py
```

### M. Experiment 04 Exact Execution Procedure

```powershell
# STEP 1: Ensure virtual environment is active in PowerShell
.\venv\Scripts\activate

# STEP 2: Launch application server on port 8003
python -m app.main
```

#### Expected Terminal Output
```
INFO:     Will watch for changes in these directories: ['D:\\Agentic AI Experiments\\experiment-04-sql-agent']
INFO:     Uvicorn running on http://127.0.0.1:8003 (Press CTRL+C to quit)
INFO:     Started reloader process [21048] using StatReload
INFO:     Started server process [23412]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

#### Exact Browser URL
👉 **`http://127.0.0.1:8003`**

### N. How to Use the UI
1. **Header Panel:** Displays title *"Autonomous ReAct SQL Agent with Tool Use"*, course code `MR23-1CS0436`, status badges (`company.db`, Port `8003`), and Agent Mode (`Offline Mock`).
2. **Sample Prompt Chips:** Click quick query buttons (*"Highest Avg Salary"*, *"Top Active Project"*, *"Max Project Hours"*, *"Top 3 Salary Costs"*, *"Active Project Team"*).
3. **Agent Controls:** Select Max Iteration Guard limit (4, 8, or 12 iterations) and click *"Execute ReAct Agent"*.
4. **Tool Usage Metrics Card:** Real-time counters tracking calls to `list_tables`, `get_schema`, `check_query_syntax`, `execute_sql`, retries, and total calls.
5. **Grounded Database Answer Card:** Synthesized natural language explanation with database values.
6. **Executed SQL & Data Table Card:** Formatted SQL query block with copy button and tabular result set.
7. **Safe Agent Execution Trace Timeline:** Chronological step cards showing decision summaries, tool invocations, sanitized parameters, observations, and status badges.
8. **Database Explorer:** Tabbed schema viewer for `departments`, `employees`, `projects`, and `employee_projects`.

### O. Experiment 04 Demonstration Procedure
1. Launch `python -m app.main` and open `http://127.0.0.1:8003`.
2. Point out status badges showing `company.db` database connection and Port 8003.
3. Click sample prompt *"Highest Avg Salary"*.
4. Point out the **Tool Usage Metrics Panel** updating counters (`list_tables`: 1, `get_schema`: 1, `check_syntax`: 2, `execute_sql`: 2, Retries: 1, Total: 6).
5. Walk evaluators through the **Safe Agent Execution Trace Timeline**:
   - Step 1 (`list_tables`): Discovers 4 tables.
   - Step 2 (`get_schema`): Retrieves schema for `departments` and `employees`.
   - Step 3 (`check_query_syntax`): Validates trial query.
   - Step 4 (`execute_sql`): Demonstrates error reflection note and query refinement.
   - Step 5 (`execute_sql`): Validates and executes refined SQL.
6. Show Grounded Database Answer (*Product Management has the highest average salary of $127,000.00 with 3 employees*).
7. Scroll to **Database Explorer** and click through tabs (`departments`, `employees`, `projects`) to verify read-only schema inspection.

### P. Sample Inputs
- *"Which department has the highest average employee salary, and how many employees work there?"*
- *"Which active project has the largest budget and which department owns it?"*
- *"Which employee is assigned the highest total project hours?"*
- *"List the top three departments by total employee salary cost."*
- *"What is the current stock price of Apple?"* *(Out-of-Domain Guard Test)*

### Q. Expected Outputs
- **Domain Queries:** Grounded answer with executed SQL, row results table, tool metrics breakdown, and Safe Action Trace cards.
- **Out-of-Domain Queries:** Friendly out-of-scope rejection notice without attempting fake database execution.

### R. Experiment 04 Screenshots

#### Screenshot 1 — Home Interface & Agent Workbench
![Home Interface](experiment-04-sql-agent/screenshots/01-home-interface.png)
*Figure 4.1: Initial Web UI dashboard of the Autonomous ReAct SQL Agent showing loaded status badges (`company.db`, Port `8003`), sample question chips, and empty workbench placeholder.*

#### Screenshot 2 — Safe Agent Execution Trace Timeline
![Agent Execution Trace](experiment-04-sql-agent/screenshots/02-agent-execution-trace.png)
*Figure 4.2: Active timeline of the Safe Agent Execution Trace showing sequential DECIDE → ACT → OBSERVE → VALIDATE steps with step numbers, tool names, decision summaries, and observations.*

#### Screenshot 3 — Agent Tool Usage Metrics Panel
![Tool Invocations](experiment-04-sql-agent/screenshots/03-tool-invocations.png)
*Figure 4.3: Agent Tool Usage Metrics panel displaying counts for `list_tables`, `get_schema`, `check_query_syntax`, `execute_sql`, retries, and total invocations.*

#### Screenshot 4 — Grounded Database Answer & SQL Result Table
![Final Answer](experiment-04-sql-agent/screenshots/04-final-database-answer.png)
*Figure 4.4: Grounded Database Answer card, executed SQL query block, row count, and execution result data table.*

#### Screenshot 5 — Error Reflection & Retry Trace
![Error Correction Retry](experiment-04-sql-agent/screenshots/05-error-correction-retry.png)
*Figure 4.5: Agent trace showing error reflection and retry auto-correction behavior (Attempt 1 trial warning → reflection note → Attempt 2 refined execution).*

#### Screenshot 6 — Database Explorer & Schema Inspector
![Database Explorer](experiment-04-sql-agent/screenshots/06-database-explorer-safety.png)
*Figure 4.6: Interactive Database Explorer tabbed schema viewer displaying columns, data types, primary keys, and foreign key relations for `company.db`.*

---

### S. Experiment 04 Testing
Run automated test suite:
```powershell
python -m pytest tests
```
- **Verified Test Result:** **`21 passed in 0.64s`** (covers database tools, SQL validator, agent loop, error reflection, and API endpoints).

### T. Safety & Validation
- **Token-Based Read-Only Validation:** `app/services/sql_validator.py` blocks DML/DDL verbs (`DROP`, `DELETE`, `UPDATE`, `INSERT`, `ALTER`, `TRUNCATE`, `CREATE`, `REPLACE`, `ATTACH`, `DETACH`, `PRAGMA`, `EXEC`, `VACUUM`, `REINDEX`).
- **Single-Statement Guard:** Blocks multiple statements separated by semicolons.
- **SQLite Read-Only URI Mode:** Connects via `file:{db_path}?mode=ro` with standard connection fallback.
- **Max Iteration Guard:** `MAX_AGENT_ITERATIONS = 8` halts infinite tool execution loops.

### U. Limitations
- **Max Iterations Cap:** Questions requiring more than 8 steps are halted by the safety guardrail.
- **Dialect Specificity:** SQL prompts and tools target SQLite 3 syntax.

### V. Troubleshooting & Gotchas
- **`ModuleNotFoundError: No module named 'app'`**: Execute **`python -m app.main`** from `experiment-04-sql-agent`.
- **Port Conflict (`8003`)**: Terminate running Python processes via `Stop-Process -Name "python" -Force`.

---

### W. Experiment 04 Viva Questions & Answers

1. **Q: How does a ReAct agent differ from a single-pass Text-to-SQL workflow?**
   *A:* Experiment 01 follows a static linear pipeline that fails if an error occurs. Experiment 04 uses a ReAct (DECIDE → ACT → OBSERVE → VALIDATE → RETRY/FINISH) loop where the agent dynamically inspects schemas, validates queries, captures execution feedback, and auto-corrects SQL when errors occur.

2. **Q: What four database tools are provided to the SQL agent?**
   *A:* `list_tables` (discovers permitted tables), `get_schema` (inspects columns, types, and foreign keys), `check_query_syntax` (validates read-only rules), and `execute_sql` (executes validated SELECT queries against `company.db`).

3. **Q: What is the purpose of the Safe Agent Execution Trace?**
   *A:* It provides a transparent, auditable timeline of step numbers, decision summaries, tool invocations, sanitized parameters, and observations without exposing hidden or unverified model chain-of-thought text.

4. **Q: How does the agent recover when an SQL execution error occurs?**
   *A:* The agent captures the error message from `execute_sql`, logs a reflection step note, compares the error against schema metadata (e.g. fixing column names or adding missing JOINs), and generates a refined query on the next iteration.

5. **Q: What tables and domain exist in the Experiment 04 database (`company.db`)?**
   *A:* A Company Analytics domain with 4 tables: `departments` (5 rows), `employees` (20 rows), `projects` (8 rows), and `employee_projects` (30 junction rows).

6. **Q: How does the system prevent infinite agent execution loops?**
   *A:* A strict iteration guardrail (`MAX_AGENT_ITERATIONS = 8`) is enforced in `app/config.py` and `app/services/agent_service.py`, halting execution if a valid answer is not derived within 8 steps.

7. **Q: What read-only safety measures are enforced on generated SQL?**
   *A:* `app/services/sql_validator.py` enforces leading `SELECT`/`WITH` statements, blocks multiple statements via semicolon checks, rejects prohibited DML/DDL keywords (`INSERT`, `UPDATE`, `DELETE`, `DROP`, `ALTER`, etc.), and `app/database.py` connects via SQLite `mode=ro` URI.

8. **Q: What is the default server port for Experiment 04?**
   *A:* Port `8003` (accessed via `http://127.0.0.1:8003`).

9. **Q: How does the Mock LLM Provider operate offline?**
   *A:* `app/services/llm_service.py` uses deterministic pattern matching for analytical questions, executing full multi-step tool calls, schema inspection, error reflection, and grounded answer synthesis without requiring external API keys.

10. **Q: How many automated tests cover Experiment 04?**
    *A:* 23 automated PyTest unit and integration tests covering database tools, quote-aware SQL validator rules, agent loop iterations, error retries, iteration caps, and FastAPI endpoints.

---

### X. Conclusion
Experiment 04 successfully demonstrates an Autonomous ReAct SQL Agent with Tool Use, proving that iterative tool-augmented reasoning, schema reflection, and error auto-correction significantly improve query accuracy and resilience over single-pass workflows.

---

## 10. Experiment 05 — Multi-Agent SDR System

### A. Experiment Identification
- **Experiment Number:** 05
- **Experiment Name:** Multi-Agent SDR System
- **Course Code:** MR23-1CS0436
- **Status:** ✅ Completed & Verified
- **Directory:** `experiment-05-multi-agent-sdr`
- **Main Technology:** Python 3.10+, FastAPI, Pydantic v2, HTML5/CSS Glassmorphism
- **Interface Type:** Web-Based Campaign Workbench with Multi-Agent Trace & Outreach Preview
- **Default Port:** `8004`

### B. Aim
To design, implement, and evaluate an autonomous Multi-Agent SDR System comprising 5 specialized agents (Supervisor Orchestrator, Lead Discovery Agent, Lead Enrichment Agent, Lead Qualification Agent, Email Drafting Agent, and Quality & Compliance Reviewer Agent) coordinating to automate B2B lead discovery, multi-dimensional scoring, draft outreach personalization, and compliance safety verification.

### C. Problem Statement
Manual B2B Sales Development Representative (SDR) workflows suffer from inconsistent lead scoring, time-consuming lead enrichment, generic cold outreach templates, and regulatory compliance risks. Single-agent LLM systems struggle to handle all tasks without hallucinating or skipping verification steps. A **Multi-Agent SDR System** decomposes the outreach pipeline into discrete, specialized role agents—discovering target leads, enriching tech stack metadata, calculating transparent qualification scores, drafting personalized emails, and auditing drafts for compliance before final approval.

### D. Learning Objectives
1. **Multi-Agent Architecture & Role Collaboration:** Implement a modular multi-agent system where specialized agents communicate via structured state contracts.
2. **Transparent Lead Qualification Scoring:** Develop a deterministic 4-dimensional scoring model (Fit, Need, Intent, Budget) to grade leads accurately.
3. **Safe Outbound Personalization:** Generate personalized cold outreach email drafts incorporating specific engagement signals and corporate value propositions without sending actual unsolicited emails.
4. **Automated Quality & Compliance Auditing:** Implement a dedicated reviewer agent to check email drafts for personalization, unverified claims, and B2B tone standards.

### E. Concepts Used
#### 1. Multi-Agent Role Specialization
The system delegates specific workflow responsibilities to discrete sub-agents managed by a central Supervisor:
Workflow = Supervisor(Discovery -> Enrichment -> Qualification -> Drafting -> Review)

#### 2. Transparent 4-Dimensional Qualification Scoring
Leads are evaluated across 4 transparent dimensions totaling 100 points:
FinalScore = Fit(25) + Need(25) + Intent(25) + Budget(25)

#### 3. Compliance Safety Audit
Every draft passes through the Quality & Compliance Reviewer Agent for personalization validation and claim verification.

### F. Why This Experiment Matters
Enterprise B2B sales automation requires multi-agent coordination to scale outreach while maintaining high personalization standards and legal/brand safety.

### G. Complete System Architecture

```mermaid
graph TD
    A[User / Campaign UI] -->|1. Campaign Request| B[FastAPI Backend /api/sdr/campaign]
    B -->|2. Run Workflow| C[Supervisor Orchestrator]
    C -->|3. Discover Leads| D[Lead Discovery Agent]
    D -->|4. Raw Leads| C
    C -->|5. Enrich Tech & Intent| E[Lead Enrichment Agent]
    E -->|6. Enriched Data| C
    C -->|7. Score Leads| F[Lead Qualification Agent]
    F -->|8. Qualified Leads| C
    C -->|9. Draft Emails| G[Email Drafting Agent]
    G -->|10. Email Previews| C
    C -->|11. Audit Compliance| H[Quality & Compliance Reviewer Agent]
    H -->|12. Verdicts & Notes| C
    C -->|13. Final SDR Package| B
    B -->|14. Render UI Dashboard| A
```

### H. Complete Workflow

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant UI as Chatbot / Campaign Web UI
    participant Sup as Supervisor Orchestrator
    participant Disc as Lead Discovery Agent
    participant Enr as Lead Enrichment Agent
    participant Qual as Lead Qualification Agent
    participant Draft as Email Drafting Agent
    participant Rev as Quality Reviewer Agent

    User->>UI: Selects Industry & Value Prop ("Cloud Infrastructure")
    UI->>Sup: POST /api/sdr/campaign
    Sup->>Disc: discover_leads(industry, region)
    Disc-->>Sup: Discovered Lead Records
    Sup->>Enr: enrich_lead(lead_data)
    Enr-->>Sup: Tech Stack & Engagement Metadata
    Sup->>Qual: qualify_lead(enriched_lead, threshold=60)
    Qual-->>Sup: Fit/Need/Intent/Budget Scores & Status
    alt Qualified Lead (Score >= 60)
        Sup->>Draft: draft_email(lead, value_prop)
        Draft-->>Sup: Personalized Email Preview
        Sup->>Rev: review_draft(lead, draft)
        Rev-->>Sup: Compliance Verdict (APPROVED_FOR_SENDING)
    end
    Sup-->>UI: Return Full SDR Package + Agent Traces
```

### I. Internal Data Flow
1. **Input**: User submits campaign request for *"Cloud Infrastructure"* with minimum threshold `60`.
2. **Step 1 (Discovery)**: Discovery Agent retrieves matching lead (Sarah Jenkins, VP of Infrastructure at CloudNexus Tech).
3. **Step 2 (Enrichment)**: Enrichment Agent flags high-value tech stack (AWS, Kubernetes) and executive decision-maker role.
4. **Step 3 (Qualification)**: Qualification Agent scores lead **90/100** (Fit: 25, Need: 25, Intent: 20, Budget: 20) → Status: `QUALIFIED`.
5. **Step 4 (Drafting)**: Email Drafting Agent constructs personalized email body referencing AWS/Kubernetes tech alignment and cloud spend reduction need.
6. **Step 5 (Compliance Review)**: Quality Reviewer Agent validates recipient personalization and verifies no exaggerated claims exist → Verdict: `APPROVED_FOR_SENDING`.

### J. Folder Structure

```
experiment-05-multi-agent-sdr/
├── README.md                           # Comprehensive Experiment Documentation
├── requirements.txt                    # Dependencies
├── .env.example                        # Config Template
├── data/
│   ├── seed_leads.py                   # Synthetic Lead Dataset Generator
│   └── leads.json                      # B2B Lead Dataset (6 records)
├── app/
│   ├── __init__.py
│   ├── main.py                         # FastAPI Router (Port 8004)
│   ├── config.py                       # Settings
│   ├── schemas.py                      # Pydantic Models
│   ├── services/
│   │   ├── __init__.py
│   │   ├── lead_discovery_agent.py     # Discovery Agent
│   │   ├── lead_enrichment_agent.py    # Enrichment Agent
│   │   ├── lead_qualification_agent.py # Qualification Scoring Agent
│   │   ├── email_drafting_agent.py     # Email Drafting Agent
│   │   ├── compliance_reviewer_agent.py# Compliance Reviewer Agent
│   │   └── sdr_supervisor.py           # Supervisor Orchestrator
│   └── static/                         # UI Assets (index.html, style.css, app.js)
├── tests/                              # 13 Automated PyTest Tests
└── screenshots/                        # 4 Verified Screenshot Artifacts
```

### K. Technology Stack
- **Python 3.10+**: Core Backend Runtime
- **FastAPI / Uvicorn**: Web Framework & ASGI Server (Port 8004)
- **Pydantic v2**: Data Validation & Schema Contracts
- **HTML5/CSS3/Vanilla JS**: Glassmorphic Campaign Workbench UI

### L. Installation
```powershell
cd "D:\Agentic AI Experiments\experiment-05-multi-agent-sdr"
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
Copy-Item .env.example .env
python data/seed_leads.py
```

### M. Exact Execution Procedure
```powershell
.\venv\Scripts\activate
python -m app.main
```
👉 **`http://127.0.0.1:8004`**

### N. How to Use the UI
1. **Control Panel:** Select target industry, region, qualification threshold (0-100), and value proposition.
2. **Launch Campaign:** Click *"Launch Multi-Agent SDR Campaign"* button.
3. **Metrics Bar:** View Discovered, Qualified, Drafted, and Compliance Approved counts.
4. **Agent Execution Trace:** Follow step-by-step trace cards detailing actions taken by each sub-agent.
5. **Outreach Cards:** Review individual lead qualification scores, personalized email preview texts, and compliance reviewer audit notes.

### O. Demonstration Procedure
1. Launch `python -m app.main` on port `8004` and open `http://127.0.0.1:8004`.
2. Point out status badge indicating `Port 8004` and active 5-agent architecture.
3. Click *"Launch Multi-Agent SDR Campaign"*.
4. Show metrics bar updating real-time counts.
5. Walk through the Multi-Agent Trace timeline cards showing sequential handoffs (Supervisor -> Discovery -> Enrichment -> Qualification -> Drafting -> Compliance Review).
6. Show qualified lead outreach cards displaying personalized email drafts and `APPROVED_FOR_SENDING` reviewer verdicts.

### P. Sample Inputs
- Industry = *"Cloud Infrastructure"*, Threshold = `60` -> Sarah Jenkins (CloudNexus Tech) scored **90/100** (`QUALIFIED`).
- Industry = *"EdTech"*, Threshold = `60` -> Rachel Adams (EduLearn Systems) scored **35/100** (`DISQUALIFIED`).

### Q. Expected Outputs
- Structured JSON response containing lead list, qualification scores, email drafts, compliance check verdicts, and step duration traces.

### R. Screenshots

#### Screenshot 1 — Initial Dashboard
![Initial Dashboard](experiment-05-multi-agent-sdr/screenshots/01-home-interface.png)
*Figure 5.1: Initial Web UI dashboard of the Multi-Agent SDR System showing campaign setup controls, active agent chips, and empty workbench.*

#### Screenshot 2 — Multi-Agent Execution Trace & Summary
![Multi-Agent Trace](experiment-05-multi-agent-sdr/screenshots/02-multi-agent-trace.png)
*Figure 5.2: Campaign summary metrics row and chronological Multi-Agent Execution Trace timeline.*

#### Screenshot 3 — Lead Qualification & Outreach Preview
![Qualification Email Preview](experiment-05-multi-agent-sdr/screenshots/03-qualification-email-preview.png)
*Figure 5.3: Qualified lead card showing 90/100 score breakdown and personalized cold email preview.*

#### Screenshot 4 — Compliance Reviewer Verdict Box
![Compliance Review Verdict](experiment-05-multi-agent-sdr/screenshots/04-compliance-review-verdict.png)
*Figure 5.4: Quality & Compliance Reviewer Agent verdict box displaying APPROVED_FOR_SENDING verdict and audit notes.*

---

### S. Testing
Run PyTest suite:
```powershell
python -m pytest tests
```
- **Verified Test Result:** **`13 passed in 0.50s`** (covers discovery, qualification, drafting, compliance, supervisor workflow, and FastAPI endpoints).

### T. Safety & Validation
- **Safe Draft Only:** Generates email text previews only. No actual emails delivered.
- **Synthetic Lead Data:** Operates on synthetic educational B2B lead dataset (`data/leads.json`).
- **Compliance Audit:** Reviewer Agent flags missing personalization or exaggerated claims.

### U. Limitations
- **Synthetic Data Scope:** Uses structured educational lead dataset for benchmarking.
- **Static Template Customization:** Outreach text uses structured prompt templates.

### V. Troubleshooting
- **`ModuleNotFoundError: No module named 'app'`**: Execute `python -m app.main` from `experiment-05-multi-agent-sdr`.
- **Port Conflict (`8004`)**: Terminate running Python processes via `Stop-Process -Name "python" -Force`.

---

### W. Experiment 05 Viva Questions & Answers

1. **Q: What is the core objective of Experiment 05?**
   *A:* To design a Multi-Agent SDR system where specialized agents (Discovery, Enrichment, Qualification, Drafting, Compliance Reviewer) collaborate under a Supervisor Orchestrator to automate lead qualification and draft outreach safely.

2. **Q: How does a multi-agent system differ from a single-agent system?**
   *A:* A single-agent system handles all tasks in one prompt loop, risking hallucination. A multi-agent system decomposes complex workflows into specialized roles with distinct inputs, outputs, and validation steps.

3. **Q: What four dimensions are used in lead qualification scoring?**
   *A:* Fit (role & tech match), Need (business challenge urgency), Intent (engagement signals), and Budget (company budget band), totaling 100 points.

4. **Q: How is safety guaranteed in outbound email generation?**
   *A:* The system operates in safe preview mode (generating text drafts only) and uses synthetic lead data. No actual emails are sent over external SMTP/email services.

5. **Q: What role does the Quality & Compliance Reviewer Agent play?**
   *A:* It audits generated drafts to ensure explicit recipient personalization, absence of unverified guarantee claims, and proper B2B consultative tone before approving the draft.

6. **Q: What happens when a lead scores below the qualification threshold?**
   *A:* The Lead Qualification Agent marks the lead `DISQUALIFIED`, logging the score summary, and the Supervisor skips email drafting for that lead.

7. **Q: What is the default server port for Experiment 05?**
   *A:* Port `8004` (accessed via `http://127.0.0.1:8004`).

8. **Q: What structured information is exposed in the Multi-Agent Execution Trace?**
   *A:* Agent name, action type, description, inputs, outputs, step status, and execution duration in milliseconds.

9. **Q: How does the Supervisor Orchestrator manage state between agents?**
   *A:* The Supervisor passes structured Pydantic data objects (Lead, QualificationResult, EmailDraft) sequentially from one agent to the next.

10. **Q: How many automated tests cover Experiment 05?**
    *A:* 13 automated PyTest unit and integration tests covering discovery, qualification, drafting, compliance, supervisor orchestration, and API endpoints.

---

### X. Conclusion
Experiment 05 successfully demonstrates a Multi-Agent SDR System, proving that role specialization, transparent scoring, and automated compliance auditing significantly improve B2B outreach quality and safety.

---

## 11. Experiment 06 — Policy Compliance Agent

### A. Experiment Identification
- **Experiment Number:** 06
- **Experiment Name:** Policy Compliance Agent
- **Course Code:** MR23-1CS0436
- **Status:** ✅ Completed & Verified
- **Directory:** `experiment-06-policy-compliance`
- **Main Technology:** Python 3.10+, FastAPI, Pydantic v2, HTML5/CSS Glassmorphism
- **Interface Type:** Web-Based Audit Workbench with Rule Table & Remediation Plan
- **Default Port:** `8005`

### B. Aim
To design, implement, and evaluate an automated Policy Compliance Agent equipped with an authoritative deterministic Rule Engine, evaluating synthetic audit scenario narratives against corporate IT, PII data protection, and Generative AI usage policies to calculate compliance scores, detect violations, and synthesize actionable remediation plans.

### C. Problem Statement
Manual policy compliance auditing across complex enterprise IT, cybersecurity, and data protection standards is slow, subjective, and prone to human oversight. Depending solely on unstructured LLM prompts for compliance verification introduces hallucination risks where serious violations are overlooked. A **Policy Compliance Agent** addresses this by combining an authoritative deterministic Rule Engine (for exact keyword/prohibition verification) with structured scoring, clear severity classification, and automated remediation synthesis.

### D. Learning Objectives
1. **Authoritative Rule Engine Architecture:** Implement a deterministic rule engine baseline to evaluate policy compliance rather than relying solely on non-deterministic LLM outputs.
2. **Multi-Dimensional Severity Scoring:** Classify policy rules into `CRITICAL`, `HIGH`, `MEDIUM`, and `LOW` severities, reducing overall compliance scores dynamically when critical violations occur.
3. **Structured Audit Evidence Trace:** Produce transparent audit logs containing rule IDs, matched keywords, detected prohibitions, evaluation status (`PASS` | `FAIL` | `WARNING`), and specific reasons.
4. **Actionable Remediation Generation:** Synthesize specific, prioritized technical remediation steps for non-compliant audit scenarios.

### E. Concepts Used
#### 1. Deterministic Rule Matching Engine
The system evaluates exact policy keywords and prohibited action patterns to establish an authoritative compliance verdict:
Verdict = RuleEngine(ScenarioText, PolicyRules)

#### 2. Severity Penalty Scoring
Compliance Score is calculated as:
ComplianceScore = max(0, RawScore - Penalty) where Penalty = 40 if CriticalViolations > 0 else 0

### F. Why This Experiment Matters
Automated compliance verification provides reproducible, continuous security oversight for cloud infrastructure, PII handling, and AI deployment workflows.

### G. Complete System Architecture

```mermaid
graph TD
    A[User / Audit UI] -->|1. Policy ID & Scenario Narrative| B[FastAPI Backend /api/compliance/audit]
    B -->|2. Load Policy Rules| C[Policy Loader: app/services/policy_loader.py]
    C -->|3. Policy Rules| D[Compliance Evaluator: app/services/compliance_evaluator.py]
    D -->|4. Execute Rule Checks| E[Rule Engine: app/services/rule_engine.py]
    E -->|5. Rule Evaluations| D
    D -->|6. Score & Status Synthesis| F[Remediation Recommender]
    F -->|7. Full Audit Package| B
    B -->|8. Render Dashboard UI| A
```

### H. Complete Workflow

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant UI as Audit Web UI
    participant API as FastAPI Backend
    participant Eval as Compliance Evaluator
    participant Rule as Deterministic Rule Engine

    User->>UI: Selects Policy ("POL-PII-02") & enters Scenario Narrative
    UI->>API: POST /api/compliance/audit
    API->>Eval: evaluate_scenario(req)
    Eval->>Rule: evaluate_rule(rule_dict, scenario_text)
    Rule-->>Eval: RuleEvaluation (FAIL, CRITICAL, Reason)
    Eval->>Eval: Calculate Compliance Score & Overall Status
    Eval-->>API: Return ComplianceAuditResponse
    API-->>UI: Render Scorecard, Rule Table & Remediations
```

### I. Internal Data Flow
1. **Input**: User submits `POL-PII-02` with scenario *"Developer printed raw customer email addresses to public S3 logs via HTTP transmission."*
2. **Rule Check 1**: Rule `RULE-PII-02A` (AES-256 / TLS 1.3 Encryption) -> `FAIL` (`CRITICAL`).
3. **Rule Check 2**: Rule `RULE-PII-02B` (PII Log Redaction) -> `FAIL` (`HIGH`).
4. **Score Calculation**: Passed: 0/2 (0%), Penalty for Critical Violation: -40 -> Compliance Score: **10%**.
5. **Status Synthesis**: Score 10% with 1 Critical Violation -> Overall Status: `NON_COMPLIANT`.
6. **Remediation Generation**: Aggregates remediation instructions: *"Configure database column-level AES-256 encryption and disable non-HTTPS endpoints."*

### J. Folder Structure

```
experiment-06-policy-compliance/
├── README.md                           # Comprehensive Documentation
├── requirements.txt                    # Dependencies
├── .env.example                        # Config Template
├── data/
│   ├── seed_policies.py                # Synthetic Policy Dataset Generator
│   ├── policies.json                   # Policy Dataset (3 policies)
│   └── scenarios.json                  # Test Audit Scenarios (3 scenarios)
├── app/
│   ├── __init__.py
│   ├── main.py                         # FastAPI Server Router (Port 8005)
│   ├── config.py                       # Settings
│   ├── schemas.py                      # Pydantic Schemas
│   ├── services/
│   │   ├── __init__.py
│   │   ├── policy_loader.py            # Policy Data Loader
│   │   ├── rule_engine.py              # Authoritative Rule Engine
│   │   └── compliance_evaluator.py     # Score & Status Evaluator
│   └── static/                         # UI Assets (index.html, style.css, app.js)
├── tests/                              # 11 Automated PyTest Tests
└── screenshots/                        # 4 Verified Screenshot Artifacts
```

### K. Technology Stack
- **Python 3.10+**: Core Backend Language
- **FastAPI / Uvicorn**: Web Framework & ASGI Server (Port 8005)
- **Pydantic v2**: Data Schemas & Validation
- **HTML5/CSS3/Vanilla JS**: Glassmorphic Audit Workbench UI

### L. Installation
```powershell
cd "D:\Agentic AI Experiments\experiment-06-policy-compliance"
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
Copy-Item .env.example .env
python data/seed_policies.py
```

### M. Exact Execution Procedure
```powershell
.\venv\Scripts\activate
python -m app.main
```
👉 **`http://127.0.0.1:8005`**

### N. How to Use the UI
1. **Control Panel:** Select target policy from dropdown or click a sample scenario chip.
2. **Audit Action:** Click *"Evaluate Policy Compliance"* button.
3. **Scorecard Header:** Inspect Compliance Score percentage (`10%`), overall status pill (`NON_COMPLIANT`), and critical violation count.
4. **Rule Breakdown Table:** Inspect rule IDs, names, severities (`CRITICAL`), PASS/FAIL badges, and evaluation reasons.
5. **Remediation Action Plan:** Review actionable technical remediation guidance.

### O. Demonstration Procedure
1. Launch `python -m app.main` on port `8005` and open `http://127.0.0.1:8005`.
2. Click sample scenario *"Unencrypted Customer Email Logging Incident"*.
3. Click *"Evaluate Policy Compliance"*.
4. Show the score drop to **10%** and status update to `NON_COMPLIANT`.
5. Point out rule evaluation table showing `RULE-PII-02A` failure reason.
6. Show recommended remediation plan box displaying column-level encryption guidance.

### P. Sample Inputs
- **Unencrypted PII Logging**: `POL-PII-02` -> Score **10%**, Status `NON_COMPLIANT`.
- **Compliant MFA Setup**: `POL-SEC-01` -> Score **100%**, Status `COMPLIANT`.

### Q. Expected Outputs
- Structured JSON response containing compliance score, overall status, rule evaluation array, recommended remediations, and step duration traces.

### R. Screenshots

#### Screenshot 1 — Initial Audit Dashboard
![Initial Dashboard](experiment-06-policy-compliance/screenshots/01-home-interface.png)
*Figure 6.1: Initial Web UI dashboard of the Policy Compliance Agent showing scenario controls and empty workbench.*

#### Screenshot 2 — Compliance Audit Scorecard
![Compliance Scorecard](experiment-06-policy-compliance/screenshots/02-compliance-scorecard.png)
*Figure 6.2: Compliance Scorecard header showing 10% score, NON_COMPLIANT overall status pill, and critical violation counter.*

#### Screenshot 3 — Policy Rule Breakdown Table
![Rule Breakdown Table](experiment-06-policy-compliance/screenshots/03-rule-breakdown-table.png)
*Figure 6.3: Policy Rule Breakdown table displaying rule IDs, names, severities, PASS/FAIL badges, and evaluation reasons.*

#### Screenshot 4 — Recommended Remediation Action Plan
![Remediation Action Plan](experiment-06-policy-compliance/screenshots/04-remediation-action-plan.png)
*Figure 6.4: Recommended Remediation Action Plan box displaying prioritized remediation instructions.*

---

### S. Testing
Run PyTest suite:
```powershell
python -m pytest tests
```
- **Verified Test Result:** **`11 passed in 0.91s`** (covers policy loading, rule engine checks, score penalties, and FastAPI endpoints).

### T. Safety & Validation
- **Authoritative Deterministic Engine:** Uses deterministic keyword/prohibition rules for exact verification.
- **Synthetic Data:** Operates on synthetic policy dataset (`data/policies.json`).

### U. Limitations
- **Synthetic Rule Scope:** Evaluates structured rules defined in policy dataset.
- **Narrative Detail Dependency:** Accuracy depends on detail provided in the audit scenario narrative.

### V. Troubleshooting
- **`ModuleNotFoundError: No module named 'app'`**: Execute `python -m app.main` from `experiment-06-policy-compliance`.
- **Port Conflict (`8005`)**: Terminate running Python processes via `Stop-Process -Name "python" -Force`.

---

### W. Experiment 06 Viva Questions & Answers

1. **Q: What is the primary objective of Experiment 06?**
   *A:* To build an automated Policy Compliance Agent using an authoritative deterministic Rule Engine to evaluate scenario narratives against formal IT/cybersecurity policies and generate audit reports with remediations.

2. **Q: Why is a deterministic rule engine preferred over pure LLM text generation for compliance?**
   *A:* Pure LLM generation introduces hallucination and inconsistent enforcement risks. A deterministic rule engine guarantees exact keyword and prohibition matching as the authoritative compliance baseline.

3. **Q: How are policy rules structured in the system?**
   *A:* Each rule specifies a unique `rule_id`, name, description, required keywords, prohibited actions, severity (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`), and remediation guidance.

4. **Q: How is the Compliance Score calculated?**
   *A:* Score equals $(	ext{Passed Rules} / 	ext{Total Rules}) 	imes 100$. If one or more `CRITICAL` severity rules fail, a mandatory 40-point penalty is deducted.

5. **Q: What overall status categories can an audit yield?**
   *A:* `COMPLIANT` (Score $\ge 80$, 0 fails), `WARNING` (Score 50-79, 0 critical fails), and `NON_COMPLIANT` (Score $< 50$ or $\ge 1$ critical fail).

6. **Q: How does the system handle missing evidence in scenario descriptions?**
   *A:* If a scenario narrative lacks explicit proof of mandatory controls without matching prohibited keywords, the rule engine assigns a `WARNING` status.

7. **Q: What default server port is reserved for Experiment 06?**
   *A:* Port `8005` (accessed via `http://127.0.0.1:8005`).

8. **Q: What information is included in the audit trace?**
   *A:* Step numbers, stage names (`POLICY_LOAD`, `RULE_ENGINE_EVALUATION`, `REMEDIATION_SYNTHESIS`), detailed descriptions, and execution durations in milliseconds.

9. **Q: How are remediations provided to the end-user?**
   *A:* The Remediation Recommender aggregates unique remediation guidance strings for all failed rules, presenting a prioritized technical action plan.

10. **Q: How many automated tests cover Experiment 06?**
    *A:* 11 automated PyTest unit and integration tests covering policy loading, rule matching, score calculation, non-compliant detection, and FastAPI endpoints.

---

### X. Conclusion
Experiment 06 successfully demonstrates a Policy Compliance Agent, proving that combining an authoritative deterministic Rule Engine with clear severity scoring produces transparent, reproducible, and audit-ready compliance evaluations.

---

## 12. Experiment 07 — Deep Research Agent Workflow

### A. Experiment Identification
- **Experiment Number:** 07
- **Experiment Name:** Deep Research Agent Workflow
- **Course Code:** MR23-1CS0436
- **Status:** ✅ Completed & Verified
- **Directory:** `experiment-07-deep-research`
- **Main Technology:** Python 3.10+, FastAPI, Pydantic v2, HTML5/CSS Glassmorphism
- **Interface Type:** Web-Based Studio Workbench with Reflection Trace & Dossier Viewer
- **Default Port:** `8006`

### B. Aim
To design, implement, and evaluate a multi-agent Deep Research Workflow comprising 4 specialized agents (Research Planner, Topic Researcher, Reflection & Quality Critique Agent, and Report Synthesizer) coordinating through plan-research-reflect-refine loops to compile publication-grade research dossiers.

### C. Problem Statement
Complex research tasks require multi-step information gathering, structured subtopic decomposition, critical evaluation, and coherent synthesis. Single-pass LLM prompts often yield superficial, unverified summaries lacking depth or technical rigor. A **Deep Research Agent Workflow** addresses this by establishing an explicit plan-research-reflect-refine pipeline, where an autonomous Reflection Agent evaluates draft findings and iteratively drives subtopic enrichment until strict quality thresholds are met.

### D. Learning Objectives
1. **Multi-Subtopic Research Decomposition:** Design a Research Planner Agent that breaks down broad topics into targeted subtopic research plans.
2. **Iterative Reflection & Quality Scoring:** Implement a Reflection Agent that evaluates draft research quality, identifies missing technical aspects, and guides iterative refinement.
3. **Bounded Reflection Guard:** Enforce strict reflection iteration caps (max 3 loops) to prevent unbounded loops while guaranteeing score convergence ($\ge 85/100$).
4. **Structured Markdown Dossier Synthesis:** Compile multi-section technical research dossiers featuring executive summaries, empirical findings, reflection logs, and strategic recommendations.

### E. Concepts Used
#### 1. Plan-Research-Reflect-Refine Loop
The system executes a structured multi-agent loop with explicit reflection checkpoints:
Dossier = Synthesizer(Reflect(Research(Plan(Topic))))

#### 2. Quality Convergence Scoring
Quality score grows iteratively with source confidence:
QualityScore = min(98, (70 + 12 * Iteration) * AvgConfidence)

### F. Why This Experiment Matters
Autonomous deep research capabilities automate complex domain investigations, literature reviews, and technology benchmarking reports across enterprise domains.

### G. Complete System Architecture

```mermaid
graph TD
    A[User / Studio UI] -->|1. Topic & Max Loops| B[FastAPI Backend /api/research/run]
    B -->|2. Run Research| C[Research Supervisor: app/services/supervisor.py]
    C -->|3. Decompose Topic| D[Research Planner: app/services/planner.py]
    D -->|4. Subtopic Plan| C
    C -->|5. Gather Subtopic Findings| E[Topic Researcher: app/services/researcher.py]
    E -->|6. Draft Findings| C
    C -->|7. Audit & Score Quality| F[Reflection Agent: app/services/reflection.py]
    F -->|8. Quality Score & Critique| C
    C -->|9. Re-research if Score < 85| E
    C -->|10. Compile Final Dossier| G[Report Synthesizer: app/services/synthesizer.py]
    G -->|11. Markdown Dossier| C
    C -->|12. Return Dossier Response| B
    B -->|13. Render Dashboard UI| A
```

### H. Complete Workflow

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant UI as Studio Web UI
    participant Sup as Research Supervisor
    participant Plan as Research Planner
    participant Res as Topic Researcher
    participant Ref as Reflection Agent
    participant Syn as Report Synthesizer

    User->>UI: Inputs Topic ("Autonomous Cyber Defense") & Max Loops=2
    UI->>Sup: POST /api/research/run
    Sup->>Plan: create_research_plan(topic)
    Plan-->>Sup: 3 Subtopic Plans (SUB-01, SUB-02, SUB-03)
    loop Bounded Iterations (Max 3)
        Sup->>Res: execute_subtopic_research(subtopics, iteration)
        Res-->>Sup: Subtopic Findings List
        Sup->>Ref: evaluate_research(findings, iteration)
        Ref-->>Sup: ReflectionCritique (Score, IsSufficient)
    end
    Sup->>Syn: synthesize_dossier(topic, plan, findings, reflections)
    Syn-->>Sup: Markdown Dossier String
    Sup-->>UI: Return ResearchDossierResponse
```

### I. Internal Data Flow
1. **Input**: User submits topic *"Autonomous AI Multi-Agent Systems in Cyber Defense"* with max loops = 2.
2. **Step 1 (Plan)**: Planner Agent creates 3 subtopics (Architectural Foundations, Incident Triage, Governance).
3. **Step 2 (Research Iter 1)**: Researcher Agent gathers initial baseline findings.
4. **Step 3 (Reflection Iter 1)**: Reflection Agent scores draft **76/100** -> Identifies missing empirical latency metrics -> Triggers Iteration 2.
5. **Step 4 (Research Iter 2)**: Researcher Agent incorporates latency benchmarking metrics (< 15ms overhead).
6. **Step 5 (Reflection Iter 2)**: Reflection Agent scores draft **89/100** -> Verdict: `Sufficient` (Score $\ge 85$).
7. **Step 6 (Synthesis)**: Synthesizer Agent compiles publication-grade markdown dossier.

### J. Folder Structure

```
experiment-07-deep-research/
├── README.md                           # Comprehensive Documentation
├── requirements.txt                    # Dependencies
├── .env.example                        # Config Template
├── data/
│   ├── seed_research.py                # Synthetic Topic Dataset Generator
│   └── sample_topics.json              # Sample Research Topics (3 topics)
├── app/
│   ├── __init__.py
│   ├── main.py                         # FastAPI Server Router (Port 8006)
│   ├── config.py                       # Settings
│   ├── schemas.py                      # Pydantic Schemas
│   ├── services/
│   │   ├── __init__.py
│   │   ├── planner.py                  # Research Planner Agent
│   │   ├── researcher.py               # Topic Researcher Agent
│   │   ├── reflection.py               # Reflection & Quality Critique Agent
│   │   ├── synthesizer.py              # Report Synthesizer Agent
│   │   └── supervisor.py               # Research Supervisor
│   └── static/                         # UI Assets (index.html, style.css, app.js)
├── tests/                              # 9 Automated PyTest Tests
└── screenshots/                        # 4 Verified Screenshot Artifacts
```

### K. Technology Stack
- **Python 3.10+**: Core Backend Language
- **FastAPI / Uvicorn**: Web Framework & ASGI Server (Port 8006)
- **Pydantic v2**: Data Validation & Schemas
- **HTML5/CSS3/Vanilla JS**: Glassmorphic Studio UI

### L. Installation
```powershell
cd "D:\Agentic AI Experiments\experiment-07-deep-research"
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
Copy-Item .env.example .env
python data/seed_research.py
```

### M. Exact Execution Procedure
```powershell
.\venv\Scripts\activate
python -m app.main
```
👉 **`http://127.0.0.1:8006`**

### N. How to Use the UI
1. **Control Panel:** Enter target topic or click a sample research topic chip.
2. **Set Iteration Limit:** Set max reflection iterations (1-3).
3. **Launch Workflow:** Click *"Launch Deep Research Workflow"* button.
4. **Metrics Bar:** View Quality Score (`89/100`), Subtopics Planned (`3`), and Iterations Executed (`2`).
5. **Execution Trace:** Review step-by-step subtopic decomposition and reflection critique notes.
6. **Compiled Dossier Viewer:** Read the full synthesized markdown report.

### O. Demonstration Procedure
1. Launch `python -m app.main` on port `8006` and open `http://127.0.0.1:8006`.
2. Click sample topic *"Autonomous AI Multi-Agent Systems in Cyber Defense"*.
3. Click *"Launch Deep Research Workflow"*.
4. Point out real-time metrics showing Quality Score reaching **89/100** in 2 iterations.
5. Scroll through reflection trace timeline cards showing Planner -> Researcher -> Reflection -> Synthesizer sequence.
6. Display the compiled markdown research dossier showing executive summary and recommendations.

### P. Sample Inputs
- **Cyber Defense Multi-Agent Systems**: 3 subtopics -> Quality Score **89/100** in 2 iterations.
- **Post-Quantum Cryptography**: 3 subtopics -> Quality Score **89/100** in 2 iterations.

### Q. Expected Outputs
- Structured JSON response containing research plan, findings, reflection history, compiled markdown dossier, quality score, and agent traces.

### R. Screenshots

#### Screenshot 1 — Initial Studio Dashboard
![Initial Dashboard](experiment-07-deep-research/screenshots/01-home-interface.png)
*Figure 7.1: Initial Web UI studio setup showing research topic controls, sample topic chips, active agent roles card, and empty workbench.*

#### Screenshot 2 — Reflection Loop Trace & Summary Metrics
![Reflection Loop Trace](experiment-07-deep-research/screenshots/02-reflection-loop-trace.png)
*Figure 7.2: Research summary metrics bar and step-by-step Multi-Agent Reflection Trace timeline.*

#### Screenshot 3 — Compiled Research Dossier Top Section
![Research Dossier Top](experiment-07-deep-research/screenshots/03-research-dossier-top.png)
*Figure 7.3: Compiled markdown research dossier top section displaying executive summary and subtopic findings.*

#### Screenshot 4 — Strategic Recommendations & Conclusions
![Dossier Recommendations](experiment-07-deep-research/screenshots/04-dossier-recommendations.png)
*Figure 7.4: Compiled markdown research dossier bottom section displaying reflection critique log and strategic technical recommendations.*

---

### S. Testing
Run PyTest suite:
```powershell
python -m pytest tests
```
- **Verified Test Result:** **`9 passed in 1.40s`** (covers planning, research, reflection score growth, supervisor loop bounds, and FastAPI endpoints).

### T. Safety & Validation
- **Bounded Reflection Guard:** Reflection iterations are strictly capped at 3 (`MAX_REFLECTION_ITERATIONS = 3`).
- **Structured Knowledge Schema:** Ensures all subtopics are validated against confidence thresholds before compilation.

### U. Limitations
- **Synthetic Knowledge Scope:** Evaluates structured synthetic research models for benchmarking.
- **Fixed Subtopic Decomposition:** Generates 3 subtopics per topic.

### V. Troubleshooting
- **`ModuleNotFoundError: No module named 'app'`**: Execute `python -m app.main` from `experiment-07-deep-research`.
- **Port Conflict (`8006`)**: Terminate running Python processes via `Stop-Process -Name "python" -Force`.

---

### W. Experiment 07 Viva Questions & Answers

1. **Q: What is the main aim of Experiment 07?**
   *A:* To build an autonomous Deep Research Agent Workflow utilizing planning and reflection loops across specialized sub-agents to compile high-quality technical research dossiers.

2. **Q: How does a plan-research-reflect-refine workflow differ from standard single-pass prompts?**
   *A:* Single-pass prompts risk generic, surface-level summaries. Plan-reflect loops break topics into structured subtopics, evaluate draft quality, identify missing analytical aspects, and iteratively refine content until quality criteria are met.

3. **Q: What agents participate in the Deep Research Workflow?**
   *A:* Research Planner Agent, Topic Researcher Agent, Reflection & Quality Critique Agent, and Report Synthesizer Agent, orchestrated by a Research Supervisor.

4. **Q: How does the Reflection Agent evaluate draft findings?**
   *A:* It calculates a 0-100 quality score based on source confidence and subtopic depth, identifies missing aspects, and determines if the report meets the $\ge 85$ sufficiency threshold.

5. **Q: What safety guard prevents infinite refinement loops?**
   *A:* A strict iteration bound (`max_reflection_loops = min(requested, 3)`) enforced in the Research Supervisor.

6. **Q: What default port is reserved for Experiment 07?**
   *A:* Port `8006` (accessed via `http://127.0.0.1:8006`).

7. **Q: What sections are included in the final synthesized research dossier?**
   *A:* Title & Metadata, Executive Summary, Structured Research Plan, Detailed Subtopic Findings, Reflection Critique Log, and Strategic Technical Recommendations.

8. **Q: How are subtopics generated for custom input topics?**
   *A:* The Research Planner Agent analyzes topic keywords to construct 3 tailored subtopics with distinct key research objectives.

9. **Q: What information is tracked in the agent step trace?**
   *A:* Step numbers, agent name, action type, description, input payload, output summary, status (`SUCCESS`), and duration in milliseconds.

10. **Q: How many automated tests cover Experiment 07?**
    *A:* 9 automated PyTest unit and integration tests covering planning, subtopic research, reflection score growth, supervisor loop bounds, and FastAPI endpoints.

---

### X. Conclusion
Experiment 07 successfully demonstrates a Deep Research Agent Workflow, proving that combining subtopic planning with bounded reflection critique loops produces rigorous, publication-grade technical research reports.

---

## 13. Comparison of Experiments 01–07

| Feature / Dimension | Experiment 01 — Text-to-SQL | Experiment 02 — Hybrid RAG QA | Experiment 03 — Prompt Chaining | Experiment 04 — ReAct SQL Agent |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Architectural Pattern** | Schema-Guided SQL Generation | Hybrid Vector+Lexical RAG Retrieval | 6-Stage Sequential Prompt Pipeline | Bounded ReAct Agent Iteration Loop |
| **Input Type** | Natural Language Question | Natural Language Question | Raw Text Document (30 to 15k chars) | Natural Language Analytical Question |
| **External Knowledge Base** | SQLite DB (`university.db`) | 9 Cybersecurity Markdown Files | Input Text Document + Parameters | SQLite DB (`company.db`) |
| **Retrieval Mechanism** | Relational Database Queries | Hybrid Cosine Vector + Lexical Scoring | Direct Text Chunk Propagation | Dynamic Tool Selection (`list_tables`, `get_schema`, etc.) |
| **Validation / Safeguards** | Lexical Read-Only Security Validator | Relevance Threshold (`0.25`) & Out-of-KB Filter | Stage 4 Self-Critique & Length Guard | Token Validator & Max Iterations Guard (`8`) |
| **Output Type** | Formatted SQL + Table + Summary | Grounded Natural Language Answer | Multi-Section Summary Package | Grounded Answer + Action Trace + Tool Metrics |
| **Default Server Port** | `8000` | `8001` | `8002` | `8003` |
| **Test Suite Results** | 8 Passed | 20 Passed | 17 Passed | 23 Passed |
| **Core Learning Outcome** | Structured schema mapping & SQL safety | High-precision hybrid search & grounding | Context propagation & self-refinement | Tool-augmented ReAct reasoning & error auto-correction |

---

## 14. Common Execution Guide

### Quick Command Reference

```powershell
# -----------------------------------------------------------------------------
# EXPERIMENT 01 — Text-to-SQL Workflow
# -----------------------------------------------------------------------------
cd "D:\Agentic AI Experiments\experiment-01-text-to-sql"
.\venv\Scripts\activate
python -m app.main
# Browser URL: http://127.0.0.1:8000

# -----------------------------------------------------------------------------
# EXPERIMENT 02 — RAG-Based Question Answering System
# -----------------------------------------------------------------------------
cd "D:\Agentic AI Experiments\experiment-02-rag-qa"
.\venv\Scripts\activate
python -m app.main
# Browser URL: http://127.0.0.1:8001

# -----------------------------------------------------------------------------
# EXPERIMENT 03 — Prompt Chaining for Summarization
# -----------------------------------------------------------------------------
cd "D:\Agentic AI Experiments\experiment-03-prompt-chaining"
.\venv\Scripts\activate
python -m app.main
# Browser URL: http://127.0.0.1:8002

# -----------------------------------------------------------------------------
# EXPERIMENT 04 — Autonomous ReAct SQL Agent with Tool Use
# -----------------------------------------------------------------------------
cd "D:\Agentic AI Experiments\experiment-04-sql-agent"
.\venv\Scripts\activate
python -m app.main
# Browser URL: http://127.0.0.1:8003
```

---

## 15. Troubleshooting Guide

### 1. `ModuleNotFoundError: No module named 'app'`
- **Root Cause:** Executing `python app/main.py` directly without specifying the Python module execution flag (`-m`).
- **Solution:** Always execute applications using `python -m app.main`.

### 2. `OSError: [Errno 10048] address already in use` (Port Conflict)
- **Solution:** Terminate existing Python processes:
  ```powershell
  Stop-Process -Name "python" -Force
  ```

---

## 16. Testing Guide

Run tests across all completed experiments:

```powershell
# Test Experiment 01
cd "D:\Agentic AI Experiments\experiment-01-text-to-sql"; python -m pytest tests

# Test Experiment 02
cd "D:\Agentic AI Experiments\experiment-02-rag-qa"; python -m pytest tests

# Test Experiment 03
cd "D:\Agentic AI Experiments\experiment-03-prompt-chaining"; python -m pytest tests

# Test Experiment 04
cd "D:\Agentic AI Experiments\experiment-04-sql-agent"; python -m pytest tests
```

### Cumulative Test Results Summary
- **Experiment 01:** 8 / 8 Passed
- **Experiment 02:** 20 / 20 Passed
- **Experiment 03:** 17 / 17 Passed
- **Experiment 04:** 23 / 23 Passed
- **Total Repository Tests:** **68 / 68 Passed (100%)**

---

## 17. Git & GitHub Workflow

```powershell
# Publication sequence:
git status
git add .
git commit -m "feat(exp04): implement ReAct SQL agent with tool use"
git push origin main
```

---

## 18. Faculty Demonstration Cheat Sheet

### If Faculty Asks to Evaluate Experiment 04 (ReAct SQL Agent):
1. Execute `cd experiment-04-sql-agent; python -m app.main` and open `http://127.0.0.1:8003`.
2. Point out status badges showing `company.db` and Port 8003.
3. Click sample prompt *"Highest Avg Salary"*.
4. Show real-time **Tool Usage Metrics Panel** updating counters (`list_tables`, `get_schema`, `check_syntax`, `execute_sql`, retries).
5. Walk faculty through the **Safe Agent Execution Trace Timeline** cards (DECIDE → ACT → OBSERVE → VALIDATE).
6. Show Grounded Database Answer (*Product Management has highest avg salary of $127,000.00 with 3 employees*).
7. Scroll to **Database Explorer** to show read-only table/schema inspection.

---

## 19. Viva Preparation Guide

### Top Viva Questions Across Modules

1. **Q: How does Experiment 04 differ from Experiment 01?**
   *A:* Exp 01 is a static single-pass workflow that fails on errors. Exp 04 is an autonomous ReAct agent with 4 database tools that reflects on execution errors and auto-corrects candidate SQL across bounded iterations.

---

## 20. Future Experiments Overview (08–12)

The repository will expand with the following upcoming modules:
- **Experiment 05 — Multi-Agent SDR System:** Multi-agent role-playing framework for outbound sales workflows.
- **Experiment 06 — Policy Compliance Agent:** Rule-based compliance evaluation agent.
- **Experiment 07 — Deep Research Agent:** Planning and reflection loops for automated research reports.
- **Experiment 08 — Visual QA & Image Retrieval:** Multimodal vision-language questioning system.
- **Experiment 09 — Reasoning Model Benchmarking:** Benchmarking reasoning strategies and Chain-of-Thought prompts.
- **Experiment 10 — Fine-Tuning for Domain Adaptation:** Parameter-efficient fine-tuning (LoRA/PEFT).
- **Experiment 11 — Model Optimization Experiment:** Model quantization (GGUF/AWQ) and distillation.
- **Experiment 12 — Capstone Mini Project:** Integrated enterprise multi-agent RAG ecosystem.

---

## 21. Master Guide Maintenance Policy

# Master Guide Maintenance Policy

> [!IMPORTANT]
> **`AGENTIC_AI_LAB_COMPLETE_GUIDE.md` is a mandatory living document.**
> Whenever any future experiment (**Experiments 05–12**) is implemented:
> 1. Complete implementation, automated testing, and browser verification.
> 2. Capture genuine screenshots into `screenshots/`.
> 3. Complete the experiment's local `README.md`.
> 4. **ADD FULL EXPERIMENT CHAPTER (Sections A–X) TO THIS MASTER GUIDE.**
> 5. Update the Experiment Status Matrix, test counts, and comparison sections.
> 6. Verify all relative links, commands, ports, and Mermaid diagrams.
> 7. Commit and push changes to GitHub.
>
> **An experiment MUST NOT be marked completed until this Master Guide has been updated.**
