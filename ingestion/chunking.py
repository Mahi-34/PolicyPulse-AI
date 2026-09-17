from pathlib import Path
import re
import json

from ingestion.metadata import build_document_metadata


def is_heading(line: str) -> bool:
    """
    Identify Markdown headings and bold numbered headings.
    """

    # Markdown heading:
    # ## 1. Purpose
    if re.match(r"^#{1,6}\s+", line.strip()):
        return True

    # DOCX-style heading:
    # **1. Purpose**
    # **2. Scope**
    if re.match(r"^\*\*\d+\.\s+.*\*\*\s*$", line.strip()):
        return True

    return False


def clean_heading(line: str) -> str:
    """
    Convert different heading formats into plain section names.
    """

    line = line.strip()

    # Remove Markdown heading symbols
    line = re.sub(r"^#{1,6}\s+", "", line)

    # Remove bold Markdown markers
    line = re.sub(r"^\*\*(.*?)\*\*$", r"\1", line)

    return line.strip()


def split_into_sections(content: str) -> list[dict]:
    """
    Split PDF/DOCX-style Markdown documents into logical sections.

    YAML frontmatter is excluded from chunk text.
    """

    lines = content.splitlines()

    sections = []

    current_heading = "Document Introduction"
    current_content = []

    in_frontmatter = False

    for line in lines:

        # ---------------------------------------------
        # Skip YAML frontmatter
        # ---------------------------------------------

        if line.strip() == "---":
            in_frontmatter = not in_frontmatter
            continue

        if in_frontmatter:
            continue

        # ---------------------------------------------
        # Detect headings
        # ---------------------------------------------

        if is_heading(line):

            # Save previous section
            if current_content:

                text = "\n".join(
                    current_content
                ).strip()

                if text:
                    sections.append({
                        "section": current_heading,
                        "text": text
                    })

            # Start new section
            current_heading = clean_heading(line)

            current_content = []

        else:

            current_content.append(line)

    # ---------------------------------------------
    # Save final section
    # ---------------------------------------------

    if current_content:

        text = "\n".join(
            current_content
        ).strip()

        if text:
            sections.append({
                "section": current_heading,
                "text": text
            })

    return sections


def split_xlsx_tables(content: str) -> list[dict]:
    """
    Split XLSX-derived Markdown into logical table chunks.

    Consecutive Markdown table lines are kept together.
    """

    lines = content.splitlines()

    sections = []

    current_table = []
    table_number = 0

    in_frontmatter = False

    for line in lines:

        # ---------------------------------------------
        # Skip YAML frontmatter
        # ---------------------------------------------

        if line.strip() == "---":
            in_frontmatter = not in_frontmatter
            continue

        if in_frontmatter:
            continue

        # ---------------------------------------------
        # Detect Markdown table rows
        # ---------------------------------------------

        if line.strip().startswith("|"):

            current_table.append(line)

        else:

            # Save existing table
            if current_table:

                table_number += 1

                sections.append({
                    "section": f"Table {table_number}",
                    "text": "\n".join(
                        current_table
                    ).strip()
                })

                current_table = []

            # Preserve non-table text
            if line.strip():

                sections.append({
                    "section": "Document Introduction",
                    "text": line.strip()
                })

    # Save final table
    if current_table:

        table_number += 1

        sections.append({
            "section": f"Table {table_number}",
            "text": "\n".join(
                current_table
            ).strip()
        })

    return sections


def create_chunks(file_path: str) -> list[dict]:
    """
    Create logical RAG-ready chunks from a processed Markdown file.
    """

    path = Path(file_path)

    content = path.read_text(
        encoding="utf-8"
    )

    # ---------------------------------------------
    # Extract document metadata
    # ---------------------------------------------

    document_metadata = build_document_metadata(
        file_path
    )

    # ---------------------------------------------
    # Choose chunking strategy
    # ---------------------------------------------

    document_type = (
        document_metadata
        .get("document_type", "")
        .upper()
    )

    if document_type == "XLSX":

        sections = split_xlsx_tables(
            content
        )

    else:

        sections = split_into_sections(
            content
        )

    # ---------------------------------------------
    # Create chunks
    # ---------------------------------------------

    chunks = []

    for index, section_data in enumerate(
        sections,
        start=1
    ):

        chunk_id = (
            f"{document_metadata['document_id']}"
            f"_CHUNK_{index:03d}"
        )

        chunk_metadata = (
            document_metadata.copy()
        )

        chunk_metadata["section"] = (
            section_data["section"]
        )

        chunk_metadata["chunk_id"] = (
            chunk_id
        )

        chunks.append({
            "chunk_id": chunk_id,
            "text": section_data["text"],
            "metadata": chunk_metadata
        })

    return chunks


def save_chunks(
    chunks: list[dict],
    output_file: str
):
    """
    Save chunks as a JSON file.
    """

    output_path = Path(
        output_file
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with output_path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            chunks,
            file,
            indent=2,
            ensure_ascii=False
        )


if __name__ == "__main__":

    # ---------------------------------------------
    # TEST INPUT
    # ---------------------------------------------

    input_file = (
        "data/processed/Finance/"
        "Finance_Approval_Policy.md"
    )

    # ---------------------------------------------
    # TEST OUTPUT
    # ---------------------------------------------

    output_file = (
        "data/chunked/Finance/"
        "Finance_Approval_Policy_chunks.json"
    )

    # ---------------------------------------------
    # CREATE CHUNKS
    # ---------------------------------------------

    chunks = create_chunks(
        input_file
    )

    # ---------------------------------------------
    # SAVE CHUNKS
    # ---------------------------------------------

    save_chunks(
        chunks,
        output_file
    )

    # ---------------------------------------------
    # DISPLAY RESULTS
    # ---------------------------------------------

    print(
        f"Created {len(chunks)} chunks."
    )

    print("\nFirst chunk:")
    print("-" * 60)

    print(
        chunks[0]["text"]
    )

    print("\nMetadata:")

    for key, value in (
        chunks[0]["metadata"].items()
    ):
        print(
            f"{key}: {value}"
        )

    print("\nOutput saved to:")

    print(output_file)