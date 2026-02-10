import pytest
from pydantic import ValidationError
from app.schemas import (
    ReviewItem,
    Lens,
    Severity,
    Confidence,
    Category
)
def test_invalid_category_fails():
    """
    A SYNTAX lens review should not accept a DESIGN category.
    This protects domain invariants.
    """
    with pytest.raises(ValidationError):
        ReviewItem(
            file="Test.java",
            line_range="1-5",
            lens=Lens.SYNTAX,
            category=Category.LAYERING,
            severity=Severity.HIGH,
            title="Bad combo",
            description="Invalid",
            recommendation="Fix",
            confidence=Confidence.HIGH,
        )