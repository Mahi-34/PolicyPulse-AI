from qdrant_client import QdrantClient
from llama_index.vector_stores.qdrant import QdrantVectorStore


QDRANT_URL = "http://localhost:6333"
QDRANT_COLLECTION = "policypulse_documents"


def get_qdrant_client() -> QdrantClient:
    """
    Create and return a client connected to the local Qdrant server.
    """
    return QdrantClient(url=QDRANT_URL)


def get_vector_store() -> QdrantVectorStore:
    """
    Create and return the LlamaIndex Qdrant vector store.
    """
    client = get_qdrant_client()

    return QdrantVectorStore(
        client=client,
        collection_name=QDRANT_COLLECTION,
    )