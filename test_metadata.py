from ingestion.metadata import build_document_metadata, validate_metadata


file_path = "data/processed/Finance/Finance_Approval_Policy.md"

metadata = build_document_metadata(file_path)

print("\nExtracted Metadata:")
for key, value in metadata.items():
    print(f"{key}: {value}")

print("\nMetadata valid:", validate_metadata(metadata))