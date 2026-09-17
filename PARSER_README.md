# PolicyPulse AI — Document Parser

## 1. Purpose

This document describes the document parsing and transformation layer developed for PolicyPulse AI.

The purpose of Part B is to convert raw enterprise documents into structured, machine-readable Markdown while preserving important policy information such as headings, paragraphs, tables, dates, numbers, monetary values, approval thresholds, responsibilities, and exception clauses.

The raw documents are preserved in their original form and are not modified by the parser.

---

## 2. Environment

- Python: 3.12.10
- Docling: 2.128.0
- Operating Environment: Windows
- Output Format: UTF-8 Markdown

Docling was used as the document parsing and transformation library.

---

## 3. Input Corpus

Raw documents are organized by department under:

`data/raw/`

The corpus contains documents from:

- Finance
- HR
- IT
- Legal
- Operations
- Procurement

Supported input formats:

- PDF
- DOCX
- XLSX

A total of 18 documents were processed.

---

## 4. Output Structure

Processed documents are stored under:

`data/processed/`

The department structure from the raw corpus is preserved.

Example:

`data/raw/Finance/Expense_Policy.docx`

is transformed into:

`data/processed/Finance/Expense_Policy.md`

This provides traceability between each processed document and its original source file.

---

## 5. Parser

The production parser is implemented in:

`parser/docling_parser.py`

The parser:

1. Recursively discovers supported documents under `data/raw`.
2. Identifies the department from the source folder.
3. Converts the document using Docling.
4. Exports the parsed document to Markdown.
5. Adds basic document metadata.
6. Saves the output using UTF-8 encoding.
7. Preserves the department-based folder structure.
8. Reports successful and failed files.

The parser does not modify the raw source documents.

---

## 6. Metadata

Each processed Markdown file contains basic metadata:

- Department
- Document name
- Document type
- Source file

Example:

```text
---
department: Finance
document_name: Expense_Policy
document_type: DOCX
source_file: data/raw/Finance/Expense_Policy.docx
---