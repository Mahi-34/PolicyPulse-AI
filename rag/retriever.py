from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core.vector_stores import MetadataFilters, MetadataFilter

from rag.embeddings import get_embedding_model
from rag.qdrant_store import get_vector_store


def retrieve_evidence(
    query: str,
    departments: list[str] | None = None,
    top_k: int = 5,
):
    """
    Retrieve relevant evidence from the PolicyPulse AI knowledge base.

    Parameters:
        query: Natural-language question.
        departments: Optional list of departments to filter results.
        top_k: Maximum number of evidence chunks to retrieve.

    Returns:
        Structured dictionary containing the query and retrieved evidence.
    """

    if not query or not query.strip():
        raise ValueError("Query cannot be empty.")

    if top_k <= 0:
        raise ValueError("top_k must be greater than 0.")

    embed_model = get_embedding_model()
    vector_store = get_vector_store()

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        storage_context=storage_context,
        embed_model=embed_model,
    )

    # Build optional department filter
    filters = None

    if departments is not None:
        if not departments:
            raise ValueError(
                "departments must contain at least one department."
            )

        filters = MetadataFilters(
            filters=[
                MetadataFilter(
                    key="department",
                    value=department,
                )
                for department in departments
            ],
            condition="or",
        )

    retriever = index.as_retriever(
        similarity_top_k=top_k,
        filters=filters,
    )

    retrieved_nodes = retriever.retrieve(query)

    results = []

    for item in retrieved_nodes:
        node = item.node
        metadata = node.metadata or {}

        results.append(
            {
                "text": node.get_content(),
                "department": metadata.get("department"),
                "document": metadata.get("document_name"),
                "document_type": metadata.get("document_type"),
                "source_file": metadata.get("source_file"),
                "policy_title": metadata.get("policy_title"),
                "version": metadata.get("version"),
                "effective_date": metadata.get("effective_date"),
                "owner_department": metadata.get("owner_department"),
                "section": metadata.get("section"),
                "chunk_id": metadata.get("chunk_id"),
                "score": item.score,
            }
        )

    return {
        "query": query,
        "results": results,
    }