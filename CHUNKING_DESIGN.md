# Chunking Design — PolicyPulse AI

## 1. Objective

The objective of Part C was to transform the processed Markdown documents generated in Part B into metadata-enriched, logically structured chunks suitable for the later RAG pipeline.

## 2. Document Characteristics

The corpus contains processed Markdown files generated from PDF, DOCX and XLSX source documents across six departments:

- Finance
- Procurement
- HR
- IT
- Legal
- Operations

The processed documents contain policies, SOPs, procedures, approval matrices, thresholds and other structured information.

## 3. Metadata Schema

Each chunk contains the following core metadata:

- department
- document_name
- document_type
- source_file
- policy_title, where available
- version, where available
- effective_date, where available
- owner_department, where available
- document_id
- section
- chunk_id

The metadata preserves the relationship between a chunk and its original source document.

## 4. Chunking Strategy

A structure-aware chunking approach was implemented instead of arbitrary fixed-length splitting.

PDF-derived Markdown documents are split using Markdown headings.

DOCX-derived Markdown documents are split using bold numbered section headings such as "1. Purpose" and "2. Scope".

XLSX-derived Markdown documents are handled using table-aware chunking, where separate Markdown tables are preserved as separate logical chunks.

## 5. Chunk Size

No single fixed chunk size was imposed.

The corpus contains short policy sections and structured tables where logical boundaries are more meaningful than arbitrary character limits. Therefore, sections and tables are retained as complete logical units.

## 6. Chunk Overlap

No overlap was applied.

The documents are structured policy and reference documents, and the implemented approach preserves complete logical sections and tables rather than splitting them into fixed-size windows.

## 7. Table Handling

Markdown tables are preserved as complete units wherever they represent a logical table.

This preserves relationships between columns, rows and values, which is important for approval thresholds, authorities, requirements and other policy rules.

## 8. Heading Handling

Markdown headings and DOCX-style bold numbered headings are detected as section boundaries.

The detected heading is stored in the chunk metadata as the `section` field.

## 9. Source Traceability

Each chunk retains document-level metadata including department, document name, document type and source file.

A stable document ID and chunk ID are also generated.

The chunk ID follows the format:

DEPARTMENT_DOCUMENT_CHUNK_XXX

This supports debugging, traceability and later citation/reference handling.

## 10. Validation

The chunking pipeline was tested on representative PDF, DOCX and XLSX-derived Markdown outputs.

The complete processed corpus was then processed.

Validation confirmed:

- 18 processed Markdown documents
- 18 generated chunk files
- 203 total chunks
- All six departments represented
- Required metadata fields present
- Chunk IDs present and unique
- Chunk text present
- Structured tables preserved as logical units

The final validation script returned:

VALIDATION PASSED