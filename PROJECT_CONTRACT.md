# PolicyPulse AI — Project Contract

## 1. Project Information

**Project Name:** PolicyPulse AI

**Project Title:**  
An Agentic RAG System for Detecting Cross-Department Policy Conflicts and Knowledge Gaps

**Organization:** NovaCore Technologies Pvt. Ltd.

**Project Type:** Academic AI / Enterprise Knowledge Management Project

---

## 2. Project Objective

PolicyPulse AI is an enterprise AI system designed to work with organizational policies and departmental documents.

The final system will:

1. Answer questions about organizational policies using Retrieval-Augmented Generation (RAG).
2. Detect contradictions between policies belonging to different departments.
3. Detect knowledge and documentation gaps.
4. Provide evidence and source citations for retrieved information.
5. Recommend appropriate actions based on detected conflicts or gaps.
6. Provide an agentic application interface for interacting with the enterprise knowledge base.

The enterprise knowledge corpus will be synthetic and created specifically for this academic project.

---

## 3. Organization

**Organization Name:** NovaCore Technologies Pvt. Ltd.

The organization contains six departments:

1. Finance
2. Procurement
3. HR
4. IT
5. Legal
6. Operations

---

## 4. Technology Stack

The following technology stack is fixed for the overall project:

| Component | Technology |
|---|---|
| Programming Language | Python 3.12.x |
| Document Parser | Docling 2.128.0 |
| RAG Framework | LlamaIndex |
| Vector Database | Qdrant |
| LLM | Ollama Cloud |
| Backend | FastAPI |
| UI | Streamlit |
| Automation | n8n |
| Version Control | Git + GitHub |

Project-specific technologies will be installed progressively according to the relevant project stage.

---

## 5. Knowledge Corpus

The project will use a synthetic enterprise knowledge corpus called:

**Synthetic Enterprise Knowledge Corpus**

The corpus will contain approximately 12–18 enterprise documents.

The target is approximately three documents per department.

Supported document formats include:

- PDF
- DOCX
- XLSX

The documents will represent realistic internal enterprise policies, procedures, approval matrices, standards, and operational guidelines.

The documents will be synthetically created and will not reproduce confidential documents from real organizations.

---

## 6. Corpus Departments

### Finance

Finance documents will cover areas such as:

- Financial approval rules
- Expense policies
- Approval matrices

### Procurement

Procurement documents will cover areas such as:

- Procurement rules
- Vendor onboarding
- Procurement thresholds

### HR

HR documents will cover areas such as:

- Leave policies
- Remote work policies
- Employee guidelines

### IT

IT documents will cover areas such as:

- IT asset management
- Information security
- IT standards

### Legal

Legal documents will cover areas such as:

- Contract policies
- Vendor legal guidelines
- Contract approval requirements

### Operations

Operations documents will cover areas such as:

- Operational procedures
- Service-level requirements
- Escalation procedures

---

## 7. Cross-Department Relationships

The corpus must not consist of unrelated documents.

Documents should reference common organizational processes so that the system can later identify relationships, contradictions, ambiguities, and missing information.

Examples of cross-department relationships include:

- Finance and Procurement approval thresholds
- Procurement and Legal vendor requirements
- HR and IT employee access responsibilities
- Legal and Procurement contract requirements
- Operations and IT incident responsibilities
- Finance and Operations approval responsibilities

---

## 8. Intentional Policy Issues

The corpus will intentionally contain realistic business issues for later AI testing.

These include:

1. Direct contradictions
2. Policy ambiguities
3. Approval conflicts
4. Timing conflicts
5. Responsibility conflicts
6. Knowledge gaps

Every intentional conflict must be documented separately in the project conflict catalog or corpus documentation.

---

## 9. Metadata Standard

Each document should contain identifiable metadata where appropriate:

- Department
- Document Name
- Document Type
- Policy Title
- Version
- Effective Date
- Owner Department

This metadata will later support document filtering, retrieval, evidence tracking, and source citation.

---

## 10. Policy Versions

Selected policies may contain multiple versions, such as:

- 2025
- 2026

Version information may later be used for policy drift or version analysis if required.

Version analysis is optional and should not unnecessarily increase project complexity.

---

## 11. Knowledge Gap Testing

The corpus will intentionally exclude definitive answers to selected operational questions.

These questions will be documented in:

`KNOWLEDGE_GAPS.md`

The purpose is to test whether the final RAG system can recognize insufficient organizational knowledge rather than generating unsupported answers.

---

## 12. Project Directory Structure

The project follows this structure:

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