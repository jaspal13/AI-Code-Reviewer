# AI Code Reviewer (Diff-based, Multi-Lens)

## Overview

This project is an **AI-assisted code review engine** that analyzes GitHub-style diffs and produces structured review feedback across **three distinct lenses**:

1. **Syntax** – correctness, language-level issues  
2. **Code Quality** – structure, readability, OOP principles, testability  
3. **Design Patterns** – layering, responsibilities, architectural concerns  

The goal is **not** to replace human reviewers, but to:
- catch issues early  
- standardize feedback  
- reduce review fatigue  
- surface higher-level design concerns consistently  

The system is designed with **LLM reliability, validation, and extensibility** in mind.

---

## Why this project exists

Most AI code review tools:
- mix all feedback together  
- produce inconsistent output  
- are hard to trust in real codebases  

This project takes a different approach:
- **explicit schemas**
- **lens-based separation of concerns**
- **validation-first design**
- **LLM as a component, not the system**

The design mirrors how experienced engineers actually review code.

---

## High-level Architecture
```md
Diff Input
↓
Review Orchestrator
↓
[ Syntax Lens ] [ Quality Lens ] [ Design Lens ]
↓ ↓ ↓
Structured Findings (validated)
↓
Review Summary + JSON Output
```

Each lens is designed to evolve into an **independent agent**, making this system a natural fit for **Agentic AI** patterns.

---

## Project Structure
```text
ai-code-reviewer/
├── app/
│ ├── init.py
│ ├── reviewer.py # Core review orchestrator
│ ├── schemas.py # Pydantic models (contract)
│ ├── prompts.py # LLM prompt templates (future)
│ └── llm_client.py # LLM adapter (future)
│
├── examples/
│ └── sample_diff.txt # Example git diff input
│
├── run.py # Local runner / entry point
└── README.md
```


---

## Core Concepts

### 1. Lens-based Reviews

Each finding belongs to exactly one lens:

- `SYNTAX`
- `QUALITY`
- `DESIGN`

This allows:
- clearer feedback
- easier prioritization
- better aggregation and analytics later

---

### 2. Structured Output (Schemas First)

All output is validated using **Pydantic models**.

This ensures:
- consistent JSON output  
- fast failure on invalid LLM responses  
- easier retries and self-healing  

This is especially important because **LLMs are untrusted input sources**.

---

### 3. Separation of Concerns

| Layer | Responsibility |
|----|----|
| `schemas.py` | Data contracts & validation |
| `reviewer.py` | Orchestration logic |
| `prompts.py` | Prompt definitions |
| `llm_client.py` | Model-specific integration |
| `run.py` | Execution / entry point |

This keeps the system maintainable as complexity grows.

---

## Running the project locally

### Prerequisites

- Python 3.10+
- Virtual environment recommended

### Steps

```bash
# from project root
python run.py
```
This will load a sample diff from examples/sample_diff.txt, generate a structured review, print validated JSON output
```json
{
  "summary": {
    "files_reviewed": 1,
    "total_findings": 1,
    "critical_issues": 0,
    "quality_issues": 0,
    "design_suggestions": 1,
    "overall_risk": "medium"
  },
  "reviews": [
    {
      "file": "UserController.java",
      "start_line": 42,
      "end_line": 67,
      "lens": "design",
      "severity": "high",
      "category": "layering",
      "title": "Business logic inside controller",
      "description": "Business logic is present in the controller layer.",
      "recommendation": "Move logic into a service layer.",
      "confidence": "high"
    }
  ]
}
```