# Member 2 — RAG Handoff Guide

## 1. Purpose

Part E implements the RAG retrieval layer for PolicyPulse AI.

The retrieval engine searches the existing Qdrant knowledge base and returns relevant evidence with source metadata. It does not generate final answers or perform conflict/knowledge-gap decisions.

## 2. Main Retrieval Function

File:

`rag/retriever.py`

Function:

```python
retrieve_evidence(
    query: str,
    departments: list[str] | None = None,
    top_k: int = 5
)