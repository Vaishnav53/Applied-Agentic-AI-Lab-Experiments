# Experiment 6: Policy Compliance Agent

**Course Code:** MR23-1CS0436  
**Course Name:** Applied Agentic AI  
**Laboratory:** Applied Agentic AI Laboratory  
**Status:** ⬜ Pending  

---

## 🎯 Aim
To build a Policy Compliance Evaluation Agent that combines rule-based deterministic checks with LLM evaluators to audit enterprise documents, detect regulatory violations, and validate synthetic compliance test data.

---

## 📜 Problem Statement
Organizations operate under complex regulatory frameworks (GDPR, HIPAA, SOC2, financial compliance). Manually auditing internal policies or customer-facing documentation is slow, expensive, and prone to human error. Pure LLM approaches without rule-based guardrails can miss explicit deterministic violations. A hybrid compliance agent combines regex/rule engines with semantic LLM evaluation to deliver automated, auditable compliance scores.

---

## 🎯 Objectives
1. Implement a rule engine for deterministic compliance checks (PII detection, keyword blacklists, formatting rules).
2. Construct an LLM semantic evaluator for policy nuance and contextual violation detection.
3. Build a synthetic compliance data generator to evaluate agent precision and recall.
4. Create an interactive compliance audit report dashboard.

---

## 💡 Agentic AI Concept Overview
This experiment introduces **Hybrid Compliance Evaluation & Guardrailed Agent Systems**.

The agent employs a dual-pass architecture:
1. **Pass 1 (Deterministic Rules):** Fast regex and pattern matching to flag explicit non-compliance (e.g., exposed SSNs, credit card numbers, prohibited legal terms).
2. **Pass 2 (Semantic LLM Guard):** Contextual reasoning to check alignment with broad organizational policies.

---

## 🏗️ System Architecture & Workflow

```
┌───────────────────┐     ┌─────────────────────────────────────────────────────────┐
│ Input Document /  │ ──> │               Dual-Pass Compliance Agent                │
│ Policy Text       │     │  ┌───────────────────────┐   ┌───────────────────────┐  │
└───────────────────┘     │  │  Pass 1: Deterministic│   │  Pass 2: Semantic LLM │  │
                          │  │  Rule/Regex Engine    │   │  Evaluator & Guard    │  │
                          │  └───────────────────────┘   └───────────────────────┘  │
                          └────────────────────────────┬────────────────────────────┘
                                                       │
                                                       ▼
                          ┌─────────────────────────────────────────────────────────┐
                          │         Compliance Audit Report & Violation Logs        │
                          └─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Technologies Used
* **Programming Language:** Python 3.10+
* **Rule Engine:** Regex / Pydantic / Guardrails AI / Guidance
* **LLM Engine:** OpenAI API / Anthropic Claude
* **User Interface:** Streamlit Compliance Dashboard

---

## 📦 Installation Instructions

```bash
cd experiment-06-policy-compliance
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

---

## 🚀 Execution Instructions

```bash
# Run synthetic dataset generation and evaluation
python src/evaluate.py

# Launch compliance audit report dashboard
streamlit run app.py
```

---

## 📥 Example Inputs & 📤 Expected Outputs

### Example Input
> A draft customer privacy policy document containing an exposed test email and ambiguous data retention timelines.

### Expected Output
> **Compliance Status:** ❌ Non-Compliant (Score: 68/100)  
> **Rule Violations:** Exposed PII detected (Line 42).  
> **Semantic Findings:** Data retention period fails GDPR Section 5 criteria.  
> **Recommended Fix:** Replace explicit test email with anonymized placeholder and specify 30-day deletion SLA.

---

## 🖼️ Results & Screenshots
*(Compliance dashboard screenshots will be added upon implementation.)*

---

## 📊 Result
*(To be populated after execution verification.)*

---

## 📝 Conclusion
*(To be populated after lab implementation completion.)*

---

## ❓ Viva Voce Questions & Key Concepts

1. **Q: Why is a hybrid (rule-based + LLM) approach preferred for compliance auditing over an LLM alone?**  
   *A:* Rule-based engines guarantee 100% deterministic precision for explicit patterns (like credit card numbers), while LLMs excel at contextual policy interpretation.

2. **Q: How does synthetic data generation help evaluate compliance agents?**  
   *A:* Synthetic data allows controlled creation of positive, negative, and edge-case test vectors to measure precision, recall, and false positive rates.
