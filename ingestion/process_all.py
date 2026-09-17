from pathlib import Path

from ingestion.chunking import create_chunks, save_chunks


PROCESSED_DIR = Path("data/processed")
CHUNKED_DIR = Path("data/chunked")


def process_all_documents():
    """
    Process every Markdown document in data/processed/
    and save the generated chunks under data/chunked/.
    """

    markdown_files = list(
        PROCESSED_DIR.rglob("*.md")
    )

    print(f"Found {len(markdown_files)} Markdown files.\n")

    total_chunks = 0

    for file_path in markdown_files:

        # Create chunks
        chunks = create_chunks(
            str(file_path)
        )

        # Preserve department folder structure
        relative_path = file_path.relative_to(
            PROCESSED_DIR
        )

        output_path = (
            CHUNKED_DIR
            / relative_path.parent
            / f"{file_path.stem}_chunks.json"
        )

        # Save chunks
        save_chunks(
            chunks,
            str(output_path)
        )

        total_chunks += len(chunks)

        print(
            f"{file_path} -> "
            f"{len(chunks)} chunks"
        )

    print("\n" + "=" * 60)
    print(
        f"Processed documents: {len(markdown_files)}"
    )
    print(
        f"Total chunks created: {total_chunks}"
    )
    print("=" * 60)


if __name__ == "__main__":
    process_all_documents()