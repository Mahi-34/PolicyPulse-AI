# Member 2 - RAG Handoff Guide

## 1. What Member 1 Completed

Member 1 completed the knowledge and retrieval layer of PolicyPulse AI:

Raw Documents
-> Docling Parsing
-> Metadata Extraction
-> Chunking
-> Embeddings
-> Qdrant
-> LlamaIndex
-> retrieve_evidence()

The main retrieval module is:

`rag/retriever.py`

The RAG layer retrieves evidence and source metadata. It does not implement conflict detection, knowledge-gap classification, recommendations, FastAPI, Streamlit or n8n.

---

## 2. Environment

Python:

`3.12.x`

RAG dependencies specified in `requirements.txt`:

- llama-index-core==0.14.24
- llama-index-vector-stores-qdrant==0.10.3
- llama-index-embeddings-huggingface==0.8.0
- qdrant-client==1.19.1
- sentence-transformers==6.0.1
- transformers==5.17.0

Embedding model:

`BAAI/bge-small-en-v1.5`

---

## 3. Installation

From the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install pytest
```

---

## 4. Environment Variables

`.env.example` is included in the repository.

Never commit API keys, passwords or other secrets.

The current Member 1 RAG retrieval layer uses local Qdrant and does not require an API key.

---

## 5. Qdrant Setup

Member 2 must create their own local Qdrant instance.

They should NOT connect to Member 1's laptop.

The project uses:

`http://localhost:6333`

Qdrant collection:

`policypulse_documents`

Start Qdrant with Docker:

```powershell
docker pull qdrant/qdrant
docker run -d --name qdrant -p 6333:6333 -p 6334:6334 qdrant/qdrant
```

If a container named `qdrant` already exists, start it instead:

```powershell
docker start qdrant
```

Verify the container:

```powershell
docker ps
```

Qdrant should be accessible at:

`http://localhost:6333`

---

## 6. Rebuild the Knowledge Base

Raw documents are stored under:

`data/raw/`

Processed documents are stored under:

`data/processed/`

Chunked data is stored under:

`data/chunked/`

Process the documents:

```powershell
python -m ingestion.process_all
```

Ingest the chunks into Qdrant:

```powershell
python -m ingestion.ingest
```

The ingestion process creates LlamaIndex nodes, generates embeddings using:

`BAAI/bge-small-en-v1.5`

and stores the vectors and metadata in the:

`policypulse_documents`

Qdrant collection.

Member 2 should rebuild the knowledge base on their own machine because the Qdrant database is local.

---

## 7. Using retrieve_evidence()

Import the retrieval function:

```python
from rag.retriever import retrieve_evidence
```

Function signature:

```python
retrieve_evidence(
    query: str,
    departments: list[str] | None = None,
    top_k: int = 5
)
```

### query

`query` is the natural-language question that should be searched against the knowledge base.

Example:

```python
result = retrieve_evidence(
    "What is the purchase approval requirement?",
    departments=["Finance"],
    top_k=5
)
```

### departments

`departments` is an optional department filter.

For example:

```python
departments=["Finance"]
```

Multiple departments can be provided:

```python
departments=["Finance", "Procurement"]
```

Multiple departments are combined using OR filtering.

Example:

```python
result = retrieve_evidence(
    "What approvals are required for a purchase of Rs 8 lakh?",
    departments=["Finance", "Procurement"],
    top_k=10
)
```

### top_k

`top_k` controls the maximum number of chunks returned.

Default:

`top_k=5`

Example:

```python
result = retrieve_evidence(
    "What is the approval process?",
    top_k=3
)
```

This requests up to 3 retrieved evidence chunks.

---

## 8. Return Structure

The function returns a dictionary containing the original query and the retrieved evidence.

Example structure:

```python
{
    "query": "...",
    "results": [
        {
            "text": "...",
            "department": "...",
            "document": "...",
            "document_type": "...",
            "source_file": "...",
            "policy_title": "...",
            "version": "...",
            "effective_date": "...",
            "owner_department": "...",
            "section": "...",
            "chunk_id": "...",
            "score": ...
        }
    ]
}
```

The retrieved evidence and metadata should be preserved when passing the results to downstream agents.

The metadata provides traceability to the source material, including:

- Department
- Document name
- Document type
- Source file
- Policy title
- Version
- Effective date
- Owner department
- Section
- Chunk ID
- Retrieval score

This allows downstream agents to identify where the retrieved evidence originated.

---

## 9. Retrieval Behaviour and Limitations

The current retriever uses semantic similarity search.

It does not currently use a tested relevance threshold.

Therefore, an unrelated query may still return the nearest organizational chunks instead of returning an empty result.

For example, an irrelevant question can still produce semantically nearest chunks from the enterprise knowledge base.

This should be considered when implementing the Knowledge Gap Agent.

The downstream agent should determine whether the retrieved evidence is sufficient to answer the user's question.

The RAG layer itself does not decide whether two policies conflict.

It only retrieves relevant evidence and metadata.

---

## 10. Error Handling

The retrieval function validates the following inputs:

- Empty query
- `top_k <= 0`
- Empty department list

Examples of invalid inputs:

```python
retrieve_evidence("")
```

```python
retrieve_evidence(
    "What is the policy?",
    top_k=0
)
```

```python
retrieve_evidence(
    "What is the policy?",
    departments=[]
)
```

These cases raise clear `ValueError` messages.

If Qdrant is unavailable, the underlying connection error is surfaced rather than returning fabricated evidence.

---

## 11. Testing

Automated retrieval tests are located at:

`tests/test_retrieval.py`

Run the tests using:

```powershell
python -m pytest tests/test_retrieval.py -v
```

The retrieval test suite contains 11 tests covering:

- Basic retrieval
- Department filtering
- Multi-department retrieval
- Top-k behaviour
- XLSX/table retrieval
- Version metadata
- Knowledge-gap evidence
- Input validation
- Non-existent departments

The complete test suite previously passed:

`11 passed`

The RAG layer was also manually checked using representative queries covering:

- Direct departmental retrieval
- Cross-department retrieval
- Policy-conflict evidence
- Table and threshold retrieval
- Irrelevant information

No Precision@K, Recall@K, MRR or other formal retrieval metrics were calculated because they were not part of the implemented evaluation.

---

## 12. Member 2 Integration

The intended workflow is:

```text
User Query
    |
    v
Router Agent
    |
    v
retrieve_evidence()
    |
    v
Retrieved Evidence + Metadata
    |
    +--> Conflict Detection Agent
    |
    +--> Knowledge Gap Agent
    |
    +--> Recommendation Agent
    |
    v
Final Response / UI
```

Member 2 should import:

```python
from rag.retriever import retrieve_evidence
```

The downstream agents should consume the retrieved evidence instead of creating a separate retrieval pipeline.

For example:

```python
evidence = retrieve_evidence(
    query=user_query,
    departments=["Finance", "Procurement"],
    top_k=10
)
```

The downstream agent can then access:

```python
evidence["results"]
```

Each result contains both the retrieved text and its source metadata.

This source information should be retained when generating the final response so that the system can provide evidence and traceability.

---

## 13. Member 2 Responsibilities

Member 2 is responsible for implementing the remaining agentic and application layers:

- Router Agent
- Conflict Detection Agent
- Knowledge Gap Agent
- Recommendation Agent
- FastAPI
- Streamlit
- n8n

Member 1's responsibility ends with the working knowledge and RAG retrieval layer.

Member 2 should build the downstream components on top of the existing:

`retrieve_evidence()`

interface.

There is no need to create another vector database or separate retrieval pipeline unless the team later agrees on an architectural change.

---

## 14. Local Setup Reminder

Member 2 should complete the following steps on their own machine:

1. Clone or pull the PolicyPulse-AI repository.
2. Open the project root in VS Code.
3. Create a local Python virtual environment.
4. Activate the virtual environment.
5. Install the dependencies from `requirements.txt`.
6. Start their own local Qdrant instance using Docker.
7. Process the raw documents.
8. Build their local Qdrant knowledge base.
9. Run the retrieval tests.
10. Import `retrieve_evidence()` into the downstream agent workflow.

The Qdrant instance must be local to Member 2's machine.

The repository contains the code and source documents required to recreate the Member 1 RAG layer.

---

## 15. Important Integration Notes

### Do not duplicate the RAG pipeline

Member 2 should use:

```python
from rag.retriever import retrieve_evidence
```

instead of implementing another embedding or vector-search pipeline.

### Preserve metadata

When passing evidence between agents, preserve fields such as:

```text
department
document
source_file
policy_title
version
effective_date
section
chunk_id
score
```

These fields are important for source traceability.

### Qdrant is local

The configured Qdrant URL is:

`http://localhost:6333`

Each team member should run their own local Qdrant instance.

### Retrieval is evidence retrieval

`retrieve_evidence()` retrieves semantically similar evidence.

It does not itself:

- Detect conflicts
- Determine whether a knowledge gap exists
- Generate recommendations
- Route user queries
- Generate the final UI response

Those responsibilities belong to the downstream components implemented by Member 2.

---

## 16. Handoff Summary

Member 1 has completed the following RAG pipeline:

```text
Enterprise Documents
        |
        v
Docling Parsing
        |
        v
Metadata Extraction
        |
        v
Chunking
        |
        v
Embedding Generation
        |
        v
Qdrant Vector Store
        |
        v
LlamaIndex
        |
        v
retrieve_evidence()
```

The main integration point for Member 2 is:

```python
from rag.retriever import retrieve_evidence
```

Member 2 can now use the retrieved evidence as the input to the Router, Conflict Detection, Knowledge Gap and Recommendation agents.

The Member 1 RAG layer is complete and ready for downstream integration.