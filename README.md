# PolicyPulse AI

## An Agentic RAG System for Detecting Cross-Department Policy Conflicts and Knowledge Gaps

PolicyPulse AI is an academic enterprise AI project designed for **NovaCore Technologies Pvt. Ltd.**

The system will use organizational documents from multiple departments to answer policy-related questions, identify cross-department policy conflicts, detect knowledge gaps, provide evidence and citations, and support agentic workflows.

---

## Organization

**NovaCore Technologies Pvt. Ltd.**

Departments included in the knowledge corpus:

1. Finance
2. Procurement
3. HR
4. IT
5. Legal
6. Operations

---

## Project Objectives

The final system will:

- Answer questions about organizational policies using RAG.
- Detect contradictions between departmental policies.
- Detect policy ambiguities.
- Identify knowledge and documentation gaps.
- Provide supporting evidence and source citations.
- Recommend actions based on identified issues.
- Provide an agentic application interface.

---

## Technology Stack

| Component | Technology |
|---|---|
| Programming | Python 3.12.x |
| Document Parser | Docling 2.128.0 |
| RAG Framework | LlamaIndex |
| Vector Database | Qdrant |
| LLM | Ollama Cloud |
| Backend | FastAPI |
| UI | Streamlit |
| Automation | n8n |
| Version Control | Git + GitHub |

---

## Project Structure

```text
PolicyPulse-AI/
│
├── data/
│   ├── raw/
│   │   ├── Finance/
│   │   ├── Procurement/
│   │   ├── HR/
│   │   ├── IT/
│   │   ├── Legal/
│   │   └── Operations/
│   │
│   └── processed/
│
├── parser/
├── ingestion/
├── rag/
├── agents/
├── api/
├── app/
├── n8n/
├── tests/
│
├── .env.example
├── .gitignore
├── PROJECT_CONTRACT.md
├── CORPUS_CATALOG.md
├── KNOWLEDGE_GAPS.md
└── README.md