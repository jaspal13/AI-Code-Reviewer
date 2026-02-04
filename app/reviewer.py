from app.schemas import (
    ReviewResponse,
    ReviewItem,
    Summary,
    Lens,
    Severity,
    Confidence,
    Category,
)

def generate_review(diff: str) -> ReviewResponse:
    """
    Core review orchestrator.
    Later: calls syntax / quality / design analyzers.
    """

    reviews = [
        ReviewItem(
            file="src/main/java/com/example/UserController.java",
            start_line=42,
            end_line=67,
            lens=Lens.DESIGN,
            severity=Severity.HIGH,
            category=Category.LAYERING,
            title="Business logic inside controller",
            description="Business logic is present in the controller layer.",
            recommendation="Move logic into a service layer.",
            confidence=Confidence.HIGH,
        )
    ]

    summary = Summary(
        files_reviewed=1,
        total_findings=1,
        critical_issues=0,
        quality_issues=0,
        design_suggestions=1,
        overall_risk=Severity.MEDIUM,
    )

    return ReviewResponse(summary=summary, reviews=reviews)
 