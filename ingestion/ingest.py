import json
import uuid
from pathlib import Path

from llama_index.core import StorageContext, VectorStoreIndex
from llama_index.core.schema import TextNode

from rag.embeddings import get_embedding_model
from rag.qdrant_store import get_vector_store


CHUNKED_DATA_DIR = Path("data/chunked")


def load_chunks():
    """
    Load all Part C chunk JSON files from data/chunked/.
    """
    chunks = []

    json_files = sorted(CHUNKED_DATA_DIR.rglob("*_chunks.json"))

    if not json_files:
        raise FileNotFoundError(
            f"No chunk JSON files found under {CHUNKED_DATA_DIR}"
        )

    for file_path in json_files:
        with open(file_path, "r", encoding="utf-8") as file:
            file_chunks = json.load(file)

        if not isinstance(file_chunks, list):
            raise ValueError(
                f"Expected a list of chunks in {file_path}"
            )

        chunks.extend(file_chunks)

    return chunks


def create_nodes(chunks):
    """
    Convert Part C chunks into LlamaIndex TextNodes.
    """
    nodes = []

    for chunk in chunks:
        chunk_id = chunk["chunk_id"]
        text = chunk["text"]
        metadata = chunk["metadata"].copy()

        # Preserve the original Part C chunk ID in metadata.
        metadata["chunk_id"] = chunk_id

        # Create a deterministic UUID from the Part C chunk ID.
        node_id = str(
            uuid.uuid5(
                uuid.NAMESPACE_URL,
                f"policypulse-ai:{chunk_id}"
            )
        )

        node = TextNode(
            text=text,
            id_=node_id,
            metadata=metadata,
        )

        nodes.append(node)

    return nodes


def main():
    print("Loading Part C chunks...")

    chunks = load_chunks()

    print(f"Loaded chunks: {len(chunks)}")

    nodes = create_nodes(chunks)

    print(f"Created LlamaIndex nodes: {len(nodes)}")

    print("Loading embedding model...")
    embed_model = get_embedding_model()

    print("Connecting to Qdrant...")
    vector_store = get_vector_store()

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    print("Generating embeddings and storing vectors in Qdrant...")

    VectorStoreIndex(
        nodes=nodes,
        storage_context=storage_context,
        embed_model=embed_model,
    )

    print("\nIngestion completed successfully.")
    print(f"Chunks ingested: {len(chunks)}")


if __name__ == "__main__":
    main()