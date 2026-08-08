"""
Unit Tests for SQL Safety Validation Rules
Experiment 04 — SQL Agent with Tool Use (MR23-1CS0436)
"""

from app.services.sql_validator import sanitize_and_validate_sql

def test_valid_select_query():
    is_safe, error, cleaned = sanitize_and_validate_sql("SELECT * FROM employees WHERE salary > 100000;")
    assert is_safe is True
    assert error == ""
    assert cleaned == "SELECT * FROM employees WHERE salary > 100000"

def test_valid_with_clause_query():
    is_safe, error, cleaned = sanitize_and_validate_sql("WITH dept_avg AS (SELECT department_id, AVG(salary) as avg_sal FROM employees GROUP BY department_id) SELECT * FROM dept_avg;")
    assert is_safe is True
    assert error == ""

def test_blocked_drop_query():
    is_safe, error, _ = sanitize_and_validate_sql("DROP TABLE employees;")
    assert is_safe is False
    assert "prohibited" in error.lower() or "only select" in error.lower()

def test_blocked_delete_query():
    is_safe, error, _ = sanitize_and_validate_sql("DELETE FROM employees WHERE id = 1;")
    assert is_safe is False

def test_blocked_update_query():
    is_safe, error, _ = sanitize_and_validate_sql("UPDATE employees SET salary = 200000 WHERE id = 1;")
    assert is_safe is False

def test_blocked_multiple_statements():
    is_safe, error, _ = sanitize_and_validate_sql("SELECT * FROM employees; DROP TABLE departments;")
    assert is_safe is False
    assert "multiple" in error.lower()
