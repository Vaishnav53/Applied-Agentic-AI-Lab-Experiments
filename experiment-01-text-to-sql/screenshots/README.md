# Experiment 01 — Screenshots & Visual Artifacts Directory

**Course Code:** MR23-1CS0436  
**Experiment Name:** Text-to-SQL Workflow  

---

## 📌 Overview

This directory stores verified visual evidence and runtime application screenshots demonstrating the **University Database AI Assistant** web application.

---

## 📷 Required Verification Screenshots

After launching the live web application (`uvicorn app.main:app --port 8000`), capture and add the following high-resolution screenshots:

1. **`01-welcome-dashboard.png`**  
   - Captures the initial Chatbot UI with the header title, loaded LLM provider badge, workflow pipeline bar, and sample question chips.
2. **`02-natural-language-query-execution.png`**  
   - Captures a successful execution of a natural language question (e.g., *"Top 5 students by CGPA"*).  
   - Demonstrates the active workflow pipeline steps, generated SQL code block, tabular database result, and conversational explanation.
3. **`03-complex-join-query.png`**  
   - Captures multi-table JOIN query execution (e.g., *"What is the average CGPA by department?"*).
4. **`04-sql-safety-rejection.png`**  
   - Captures the server-side safety rejection alert when an unsafe query (e.g., `"DROP TABLE students;"`) is attempted.

---

## 🎨 Asset Naming Standard
- Format: Lowercase hyphenated string (e.g., `01-welcome-dashboard.png`).
- Format type: `.png` or `.webp`.
