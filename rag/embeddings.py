from llama_index.embeddings.huggingface import HuggingFaceEmbedding


EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"


def get_embedding_model() -> HuggingFaceEmbedding:
    """
    Create and return the project's Hugging Face embedding model.
    """
    return HuggingFaceEmbedding(
        model_name=EMBEDDING_MODEL_NAME
    )