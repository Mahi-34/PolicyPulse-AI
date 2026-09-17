from pathlib import Path
import re


REQUIRED_FIELDS = [
    "department",
    "document_name",
    "document_type",
    "source_file",
]


def parse_frontmatter(content: str) -> dict:
    """
    Extract metadata from the YAML-style frontmatter
    generated in the processed Markdown files.
    """

    metadata = {}

    if not content.startswith("---"):
        return metadata

    parts = content.split("---", 2)

    if len(parts) < 3:
        return metadata

    frontmatter = parts[1]

    for line in frontmatter.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip()

    return metadata


def extract_table_metadata(content: str) -> dict:
    """
    Extract additional metadata such as policy title,
    version, effective date and owner department
    from the document's Markdown metadata table.
    """

    metadata = {}

    patterns = {
        "policy_title": r"\|\s*(?:\*\*)?Policy Title(?:\*\*)?\s*\|\s*(.*?)\s*\|",
        "version": r"\|\s*(?:\*\*)?Version(?:\*\*)?\s*\|\s*(.*?)\s*\|",
        "effective_date": r"\|\s*(?:\*\*)?Effective Date(?:\*\*)?\s*\|\s*(.*?)\s*\|",
        "owner_department": r"\|\s*(?:\*\*)?Owner Department(?:\*\*)?\s*\|\s*(.*?)\s*\|",
    }

    for field, pattern in patterns.items():
        match = re.search(pattern, content, re.IGNORECASE)

        if match:
            metadata[field] = match.group(1).strip()

    return metadata


def build_document_metadata(file_path: str) -> dict:
    """
    Build normalized metadata for a processed Markdown document.
    """

    path = Path(file_path)

    content = path.read_text(encoding="utf-8")

    metadata = {}

    # Metadata already created by Part B / Docling parser
    metadata.update(parse_frontmatter(content))

    # Additional metadata available inside the document
    metadata.update(extract_table_metadata(content))

    # Create a stable document ID
    department = metadata.get("department", "Unknown")
    document_name = metadata.get("document_name", path.stem)

    document_id = f"{department}_{document_name}".upper()

    metadata["document_id"] = document_id

    return metadata


def validate_metadata(metadata: dict) -> bool:
    """
    Check that all required metadata fields are present.
    """

    missing_fields = [
        field
        for field in REQUIRED_FIELDS
        if not metadata.get(field)
    ]

    if missing_fields:
        print("Missing metadata fields:", missing_fields)
        return False

    return True