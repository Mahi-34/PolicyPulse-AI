import pytest

from rag.retriever import retrieve_evidence


def test_basic_retrieval():
    result = retrieve_evidence(
        "What approval is required for a purchase between ₹5 lakh and ₹10 lakh?",
        top_k=5,
    )

    assert result["query"]
    assert len(result["results"]) > 0


def test_finance_department_filter():
    result = retrieve_evidence(
        "What is the purchase approval requirement?",
        departments=["Finance"],
        top_k=5,
    )

    assert len(result["results"]) > 0
    assert all(
        item["department"] == "Finance"
        for item in result["results"]
    )


def test_multi_department_retrieval():
    result = retrieve_evidence(
        "What approvals are required for a purchase of ₹8 lakh?",
        departments=["Finance", "Procurement"],
        top_k=10,
    )

    departments = {
        item["department"]
        for item in result["results"]
    }

    assert "Finance" in departments
    assert "Procurement" in departments


def test_top_k():
    result = retrieve_evidence(
        "What is the purchase approval requirement?",
        top_k=3,
    )

    assert len(result["results"]) == 3


def test_xlsx_table_retrieval():
    result = retrieve_evidence(
        "What approval is required for a purchase between ₹5 lakh and ₹10 lakh?",
        top_k=5,
    )

    assert any(
        item["document_type"] == "XLSX"
        for item in result["results"]
    )


def test_version_metadata():
    result = retrieve_evidence(
        "What does the 2026 Finance approval policy state about purchase approvals?",
        departments=["Finance"],
        top_k=5,
    )

    assert len(result["results"]) > 0
    assert all(
        item["version"] == "2026"
        for item in result["results"]
    )


def test_knowledge_gap_evidence():
    result = retrieve_evidence(
        "Who approves vendor suspension after a compliance violation?",
        top_k=5,
    )

    assert len(result["results"]) > 0

    combined_text = " ".join(
        item["text"]
        for item in result["results"]
    ).lower()

    assert "approving authority" in combined_text


def test_empty_query():
    with pytest.raises(ValueError, match="Query cannot be empty"):
        retrieve_evidence("")


def test_invalid_top_k():
    with pytest.raises(
        ValueError,
        match="top_k must be greater than 0",
    ):
        retrieve_evidence(
            "What is the purchase approval requirement?",
            top_k=0,
        )


def test_empty_department_list():
    with pytest.raises(
        ValueError,
        match="departments must contain at least one department",
    ):
        retrieve_evidence(
            "What is the purchase approval requirement?",
            departments=[],
        )


def test_nonexistent_department():
    result = retrieve_evidence(
        "What is the purchase approval requirement?",
        departments=["Marketing"],
        top_k=5,
    )

    assert result["results"] == []