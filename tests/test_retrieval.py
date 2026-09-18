from llama_index.core import VectorStoreIndex, StorageContext

from rag.embeddings import get_embedding_model
from rag.qdrant_store import get_vector_store


def main():
    print("Connecting to Qdrant...")

    vector_store = get_vector_store()

    print("Loading embedding model...")
    embed_model = get_embedding_model()

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        storage_context=storage_context,
        embed_model=embed_model,
    )

    retriever = index.as_retriever(
        similarity_top_k=5
    )

    query = "What is NovaCore's policy for international employee relocation to Antarctica?"

    print(f"\nQuery: {query}")
    print("\nRetrieved results:\n")

    retrieved_nodes = retriever.retrieve(query)

    for i, result in enumerate(retrieved_nodes, start=1):
        node = result.node

        print(f"--- Result {i} ---")
        print("Score:", result.score)
        print("Department:", node.metadata.get("department"))
        print("Document:", node.metadata.get("document_name"))
        print("Section:", node.metadata.get("section"))
        print("Chunk ID:", node.metadata.get("chunk_id"))
        print("Text:", node.text[:500])
        print()


if __name__ == "__main__":
    main()