from pathlib import Path
from docling.document_converter import DocumentConverter


# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


# Supported document formats
SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".xlsx"}


def process_document(source_file: Path):
    """Parse one document and save it as UTF-8 Markdown."""

    try:
        # Identify department from the folder structure
        department = source_file.parent.name

        # Create the corresponding processed department folder
        output_dir = PROCESSED_DIR / department
        output_dir.mkdir(parents=True, exist_ok=True)

        # Create Docling converter
        converter = DocumentConverter()

        # Convert the document
        result = converter.convert(source_file)

        # Export as Markdown
        markdown = result.document.export_to_markdown()

        # Basic document metadata
        document_name = source_file.stem
        document_type = source_file.suffix.lower().replace(".", "").upper()
        source_file_path = source_file.relative_to(PROJECT_ROOT)

        metadata = f"""---
department: {department}
document_name: {document_name}
document_type: {document_type}
source_file: {source_file_path.as_posix()}
---

"""

        markdown = metadata + markdown

        # Output file name
        output_file = output_dir / f"{source_file.stem}.md"

        # Save explicitly as UTF-8
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"SUCCESS: {source_file} -> {output_file}")

        return True

    except Exception as e:
        print(f"FAILED: {source_file}")
        print(f"ERROR: {e}")

        return False


def main():
    """Find and process all supported documents in data/raw."""

    files = [
        file
        for file in RAW_DIR.rglob("*")
        if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    print(f"Found {len(files)} supported documents.")
    print()

    successful = 0
    failed = 0

    for file in files:
        if process_document(file):
            successful += 1
        else:
            failed += 1

    print()
    print("========== PARSING SUMMARY ==========")
    print(f"Total files found : {len(files)}")
    print(f"Successful        : {successful}")
    print(f"Failed            : {failed}")
    print("=====================================")


if __name__ == "__main__":
    main()