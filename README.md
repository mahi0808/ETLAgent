# ETLAgent
# GenAI Agent–Driven ETL Pipeline (PoC)

## 📌 Overview

This project is a **proof of concept (PoC)** that demonstrates how a **GenAI-powered agent** can plan, reason, and orchestrate an **ETL (Extract–Transform–Load) pipeline**.

The goal is **not** to build a production-grade system, but to showcase:

* Understanding of **GenAI / agent concepts**
* How LLMs can be applied to **data engineering problems**
* Clear separation between **reasoning (GenAI)** and **execution (deterministic tools)**

This implementation was designed to satisfy the requirements of a *GenAI Agent–Driven ETL* interview assignment.

---

## 🧠 Key Idea

> **GenAI is used for reasoning and planning, not for data processing.**

* The **GenAI agent** reasons over dataset metadata and produces an ETL plan
* **Python, Pandas, and SQLite** execute the plan deterministically
* Rule-based guardrails handle schema drift and data quality

---

## 🏗️ Architecture Overview

```
CSV / Source Data
        ↓
Metadata Extraction (Pandas)
        ↓
Schema Drift Detection
        ↓
GenAI Planning Agent (LLM)
        ↓
Plan Adjustment (Data Quality Rules)
        ↓
Transformation Execution (Pandas)
        ↓
Load to SQLite
```

---

## 📂 Project Structure

```
ETLAgent/
│
├── main.py                  # Orchestrates the ETL pipeline
│
├── agent/
│   ├── __init__.py
│   ├── planner.py           # GenAI + agent reasoning logic
│   └── schema.py            # Expected schema definition
│
├── etl/
│   ├── __init__.py
│   ├── extractor.py         # Metadata extraction + schema drift detection
│   ├── transformer.py       # Executes transformations
│   ├── loader.py            # Loads data to SQLite
│   └── quality.py           # Data quality scoring
│
├── data/
│   └── orders.csv           # Sample input data
│
└── README.md
```

---

## 🤖 Role of GenAI (LLM)

The GenAI agent is responsible for:

* Understanding dataset **structure and schema** (via metadata)
* Deciding **validations** and **transformations**
* Generating an **ETL execution plan** in structured JSON
* Adapting decisions when data quality degrades

The LLM **does not**:

* Read raw data rows
* Execute transformations
* Replace Pandas or SQL

This separation ensures reliability, auditability, and safety.

---

## 🔁 Agent Reasoning Flow

1. **Extract Metadata**

   * Columns
   * Data types
   * Null counts
   * Sample rows

2. **Detect Schema Drift**

   * Missing columns
   * New columns
   * Type mismatches

3. **GenAI Planning**

   * Produces ETL plan (JSON)
   * Defines validations, transformations, and load strategy

4. **Data Quality Adjustment**

   * Low quality → stricter transformations

5. **Execution**

   * Pandas applies transformations
   * SQLite stores final data

---

## 🧪 Data Quality Handling

A simple data quality score is calculated using null counts.

* High quality → standard plan
* Low quality → additional cleaning steps added by the agent

This demonstrates **adaptive behavior**, one of the key evaluation criteria.

---

## 🧱 Schema Drift Handling

The pipeline detects:

* Missing columns → pipeline fails
* New columns → accepted automatically
* Type mismatches → agent decides casting strategy

This logic is implemented using **rule-based guardrails** around the GenAI agent.

---

## ▶️ How to Run

### 1. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
python -m pip install pandas openai
```

### 3. (Optional) Set OpenAI API key

```bash
setx OPENAI_API_KEY "your_api_key_here"
```

> If no API key is provided, the pipeline automatically falls back to a mock planning agent.

### 4. Run the pipeline

```bash
python main.py
```

---

## 🔐 Safety & Reliability

* GenAI output is constrained to **strict JSON**
* `eval()` is never used
* Deterministic fallback logic ensures pipeline reliability
* Execution is fully controlled by Python tools

---

## ⚖️ Trade-offs & Limitations

**Pros**

* Flexible, adaptive ETL planning
* Clear agent-based design
* Easy to extend to new data sources

**Limitations**

* Not suitable for large-scale data
* LLM responses may vary
* Added latency and cost from GenAI calls

---

## 🚀 Future Enhancements

* Support for multiple data sources (API, JSON)
* More advanced data quality metrics
* Integration with workflow orchestrators (Airflow)
* Logging and monitoring for agent decisions

---

## 🎯 Summary

This project demonstrates how **GenAI agents can enhance ETL pipelines** by introducing reasoning, planning, and adaptability—while keeping execution deterministic and safe.

It directly addresses the evaluation criteria of the assignment and serves as a clear, interview-ready example of **GenAI applied to data engineering**.
