import json
from app.schemas import (
    ReviewResponse,
    ReviewItem,
    Summary,
    Lens,
    Severity,
    Confidence,
    Category,
)
from app.llm_client import call_llm
from app.prompts import SYNTAX_REVIEW_PROMPT

def generate_review(diff: str) -> ReviewResponse:
    """
    Core review orchestrator.
    Later: calls syntax / quality / design analyzers.
    """
    raw_response = call_llm(
        SYNTAX_REVIEW_PROMPT.format(diff=diff)
    )
    parsed = json.loads(raw_response)
    syntax_reviews = [
        ReviewItem(**item) for item in parsed
    ]

    summary = Summary(
        files_reviewed=len({r.file for r in syntax_reviews}),
        total_findings=len(syntax_reviews),
        critical_issues=sum(1 for r in syntax_reviews if r.severity == Severity.CRITICAL),
        quality_issues=0,
        design_suggestions=1,
        overall_risk=Severity.MEDIUM if syntax_reviews else Severity.LOW
    )

    return ReviewResponse(summary=summary, reviews=syntax_reviews)
 