# RAG Evaluation - PolicyPulse AI

## 1. Evaluation Objective

The RAG evaluation verifies that the Member 1 retrieval layer can retrieve relevant policy evidence from the enterprise knowledge base while preserving department and source metadata.

The evaluation focuses on representative retrieval scenarios rather than formal benchmark metrics.

---

## 2. Retrieval Interface

The main retrieval interface is:

```python
from rag.retriever import retrieve_evidence
```

Function:

```python
retrieve_evidence(
    query: str,
    departments: list[str] | None = None,
    top_k: int = 5
)
```

The function returns retrieved evidence along with metadata such as department, document, source file, policy title, version, section, chunk ID and similarity score.

---

## 3. Automated Testing

Automated tests are implemented in:

`tests/test_retrieval.py`

The test suite contains 11 tests covering:

- Basic retrieval
- Department filtering
- Multi-department retrieval
- Top-k behaviour
- XLSX/table retrieval
- Version metadata
- Knowledge-gap evidence
- Input validation
- Non-existent departments

The completed automated test suite passed:

**11 passed**

---

## 4. Representative Sanity Checks

A final sanity check was performed using representative retrieval queries.

### 4.1 Direct Departmental Retrieval

Query:

> What is the purchase approval requirement?

Filter:

`Finance`

Top-k:

`3`

Observed result:

**3 results returned.**

The top result was retrieved from the Finance Approval Policy and included source metadata such as:

- Department: Finance
- Document: Finance_Approval_Policy
- Version: 2026
- Section: 3. Definitions
- Chunk ID: FINANCE_FINANCE_APPROVAL_POLICY_CHUNK_004

This confirmed that departmental filtering and source metadata were functioning.

---

### 4.2 Cross-Department Retrieval

A cross-department query was tested using:

`Finance` and `Procurement`

Observed result:

**10 results returned.**

The results contained evidence from both Finance and Procurement, confirming that multiple department filters can be used together.

---

### 4.3 Policy-Conflict Retrieval

A conflict-oriented query was tested to retrieve evidence related to approval requirements across departments.

The retrieved results included evidence from both Finance and Procurement.

Representative results included:

- Finance Approval Matrix - Table 2
- Finance Approval Policy - Definitions
- Finance Approval Matrix - Table 3
- Procurement Policy - Procurement Approval
- Finance Approval Policy - Emergency Purchases

This confirms that the RAG layer can retrieve evidence that can subsequently be analyzed by the Conflict Detection Agent.

The RAG layer itself does not determine whether the policies actually conflict.

---

### 4.4 Table and Threshold Retrieval

A query related to approval thresholds was tested.

The retrieved evidence included:

- Finance Approval Matrix - Table 2
- Finance Expense Policy - Approval Requirements
- Finance Approval Policy - Emergency Purchases
- Finance Approval Policy - Definitions
- Finance Approval Policy - Capital Expenditure

This confirmed retrieval of information originating from both tabular and text-based policy documents.

---

### 4.5 Irrelevant / Unavailable Information

An unrelated query was tested:

> What is the weather in Mumbai?

The retriever returned five organizational chunks with lower similarity scores rather than returning an empty result.

The results included documents from HR, Operations and IT.

This behaviour is an identified limitation of the current implementation.

The retriever uses semantic similarity but does not currently apply a tested relevance threshold. Therefore, downstream agents should evaluate whether retrieved evidence is sufficiently relevant before generating an answer or identifying a knowledge gap.

---

## 5. Source Traceability

Retrieved results preserve source metadata including:

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
- Similarity score

This allows downstream components to trace retrieved evidence back to its originating document and section.

---

## 6. Error Handling

The retrieval interface validates important inputs.

The following cases are handled:

- Empty query
- `top_k <= 0`
- Empty department list
- Non-existent department filters

When Qdrant is unavailable, the underlying connection error is surfaced rather than returning fabricated evidence.

---

## 7. Evaluation Limitations

This evaluation is a functional retrieval evaluation and not a formal information-retrieval benchmark.

The project does not currently calculate:

- Precision@K
- Recall@K
- Mean Reciprocal Rank (MRR)
- NDCG

No new evaluation dataset was created for Part F.

The evaluation therefore focuses on whether representative queries retrieve expected evidence and preserve source traceability.

---

## 8. Final Assessment

The Member 1 RAG layer was verified through automated tests and representative sanity checks.

The retrieval pipeline successfully supports:

- Department-specific retrieval
- Cross-department retrieval
- Top-k retrieval
- Table-based evidence retrieval
- Policy-version retrieval
- Evidence retrieval for downstream conflict and knowledge-gap analysis
- Source traceability
- Input validation

The main identified limitation is the absence of a tested semantic relevance threshold for unrelated queries.

The completed RAG layer is ready for integration with the downstream agents implemented by Member 2.