from pathlib import Path
import json


CHUNKED_DIR = Path("data/chunked")

REQUIRED_METADATA = [
    "department",
    "document_name",
    "document_type",
    "source_file",
]


def validate_chunks():
    """
    Validate all generated chunk JSON files.
    """

    chunk_files = list(
        CHUNKED_DIR.rglob("*_chunks.json")
    )

    print(f"Found {len(chunk_files)} chunk files.\n")

    all_chunks = []
    errors = []

    # --------------------------------------------------
    # Read all chunk files
    # --------------------------------------------------

    for file_path in chunk_files:

        try:
            with file_path.open(
                "r",
                encoding="utf-8"
            ) as file:

                chunks = json.load(file)

        except Exception as error:

            errors.append(
                f"{file_path}: Could not read file - {error}"
            )

            continue

        print(
            f"{file_path} -> {len(chunks)} chunks"
        )

        # --------------------------------------------------
        # Validate individual chunks
        # --------------------------------------------------

        for chunk in chunks:

            all_chunks.append(chunk)

            # Check required metadata
            metadata = chunk.get(
                "metadata",
                {}
            )

            for field in REQUIRED_METADATA:

                if not metadata.get(field):

                    errors.append(
                        f"{file_path}: "
                        f"Missing metadata field "
                        f"'{field}'"
                    )

            # Check chunk ID
            if not chunk.get("chunk_id"):

                errors.append(
                    f"{file_path}: Missing chunk_id"
                )

            # Check text
            if not chunk.get("text", "").strip():

                errors.append(
                    f"{file_path}: Empty chunk text"
                )


    # --------------------------------------------------
    # Check chunk ID uniqueness
    # --------------------------------------------------

    chunk_ids = [
        chunk["chunk_id"]
        for chunk in all_chunks
        if chunk.get("chunk_id")
    ]

    duplicate_ids = {
        chunk_id
        for chunk_id in chunk_ids
        if chunk_ids.count(chunk_id) > 1
    }

    if duplicate_ids:

        for chunk_id in duplicate_ids:

            errors.append(
                f"Duplicate chunk ID: {chunk_id}"
            )


    # --------------------------------------------------
    # Check departments
    # --------------------------------------------------

    expected_departments = {
        "Finance",
        "Procurement",
        "HR",
        "IT",
        "Legal",
        "Operations",
    }

    actual_departments = {
        chunk["metadata"]["department"]
        for chunk in all_chunks
        if chunk.get("metadata")
        and chunk["metadata"].get("department")
    }

    missing_departments = (
        expected_departments
        - actual_departments
    )

    if missing_departments:

        errors.append(
            "Missing departments: "
            + ", ".join(
                sorted(missing_departments)
            )
        )


    # --------------------------------------------------
    # Final result
    # --------------------------------------------------

    print("\n" + "=" * 60)

    print(
        f"Total chunk files: {len(chunk_files)}"
    )

    print(
        f"Total chunks: {len(all_chunks)}"
    )

    print(
        f"Departments found: "
        f"{', '.join(sorted(actual_departments))}"
    )

    print("=" * 60)


    if errors:

        print("\nVALIDATION FAILED")
        print("-" * 60)

        for error in errors:

            print(error)

    else:

        print(
            "\nVALIDATION PASSED"
        )

        print(
            "All chunks contain the required "
            "metadata and valid chunk IDs."
        )


if __name__ == "__main__":

    validate_chunks()