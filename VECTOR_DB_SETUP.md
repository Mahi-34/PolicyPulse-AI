\# PolicyPulse AI — Vector Database Setup



\## 1. Vector Database



PolicyPulse AI uses Qdrant as the local vector database.



\- Qdrant version: 1.19.1

\- Deployment: Local Docker container

\- Endpoint: http://localhost:6333

\- Collection: `policypulse\_documents`

\- Vector dimension: 384

\- Distance metric: Cosine

\- Storage: Persistent Docker volume (`qdrant-storage`)



Qdrant is bound to localhost and is not publicly exposed.



\## 2. Embedding Model



The embedding model selected for the knowledge base is:



`BAAI/bge-small-en-v1.5`



The model was tested successfully with LlamaIndex.



\- Embedding dimension: 384

\- Provider: Hugging Face

\- Usage: Local text embeddings

\- Cost: Free/local inference



The embedding model is implemented in:



`rag/embeddings.py`



\## 3. LlamaIndex Integration



LlamaIndex is used to orchestrate the embedding and vector-store layer.



Tested packages:



\- `llama-index-core==0.14.24`

\- `llama-index-vector-stores-qdrant==0.10.3`

\- `llama-index-embeddings-huggingface==0.8.0`

\- `qdrant-client==1.19.1`

\- `sentence-transformers==6.0.1`

\- `transformers==5.17.0`



The Qdrant integration is implemented in:



`rag/qdrant\_store.py`



\## 4. Ingestion



Part C generated chunked JSON files under:



`data/chunked/`



The ingestion process:



1\. Loads all Part C chunk JSON files.

2\. Converts chunks into LlamaIndex `TextNode` objects.

3\. Preserves Part C metadata.

4\. Generates embeddings using `BAAI/bge-small-en-v1.5`.

5\. Stores the resulting vectors and metadata in Qdrant.



The ingestion script is:



`ingestion/ingest.py`



The verified corpus contains:



\*\*203 chunks across the Part C chunk files.\*\*



The verified Qdrant collection contains:



\*\*203 stored points.\*\*



\## 5. Metadata and Traceability



The following metadata is preserved with the stored nodes:



\- `department`

\- `document\_name`

\- `document\_type`

\- `source\_file`

\- `policy\_title`

\- `version`

\- `effective\_date`

\- `owner\_department`

\- `document\_id`

\- `section`

\- `chunk\_id`



This maintains source traceability from:



\*\*Department → Document → Section → Chunk\*\*



\## 6. Duplicate Strategy



Deterministic UUIDs are generated from the original Part C `chunk\_id`.



This provides stable node identifiers when the same chunks are ingested again.



The original Part C `chunk\_id` is also preserved in metadata.



\## 7. Verification Performed



The following tests were completed:



\- Qdrant connection test

\- Qdrant collection verification

\- Embedding generation test

\- LlamaIndex import test

\- Part C chunk loading test

\- Full ingestion test

\- Qdrant vector count verification

\- Metadata preservation test

\- Basic semantic retrieval test

\- Cross-department retrieval test

\- Conflict-evidence retrieval test

\- Low-relevance / knowledge-gap behavior test



\## 8. Retrieval Behavior



Basic semantic retrieval successfully returned relevant Finance policy chunks for a financial approval query.



Cross-department retrieval returned evidence from Legal and Procurement for a vendor-contract query.



A purchase-threshold query retrieved evidence from both Finance and Procurement, demonstrating retrieval of potentially relevant evidence across departments.



A deliberately unrelated query still returned nearest-neighbor results. This indicates that the current retrieval layer does not independently classify a query as a knowledge gap using a relevance threshold. Such behavior should be handled by a later knowledge-gap/agent layer rather than by treating every top-k result as authoritative evidence.



\## 9. Scope of Part D



Part D implements the knowledge and retrieval layer only.



It does not implement:



\- Final answer generation

\- Conflict-resolution logic

\- Knowledge-gap agent

\- Recommendation agent

\- Query-routing agent

\- Streamlit/FastAPI application

\- n8n workflow



These are outside the scope of the Part D knowledge-base implementation.



\## 10. Reproducibility



From the project root, the ingestion process can be executed using:



`python -m ingestion.ingest`



Qdrant must be running locally before ingestion.



The Python dependencies used and tested for this implementation are recorded in:



`requirements.txt`

