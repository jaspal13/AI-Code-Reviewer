from pydantic import BaseModel, Field, ValidationError, ConfigDict, field_validator
from enum import Enum
from typing import List

class Lens(str, Enum):
    SYNTAX = "syntax"
    QUALITY = "quality"
    DESIGN = "design"

class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class Confidence(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class Category(str, Enum):
    SYNTAX_ERROR = "syntax_error"
    NULL_SAFETY = "null_safety"
    METHOD_RESPONSIBILITY = "method_responsibility"
    LAYERING = "layering"
    PATTERN_MISUSE = "pattern_misuse"

"""
{
  "file": "src/main/java/com/example/UserController.java",
  "line_range": "42-67",
  "lens": "SYNTAX | QUALITY | DESIGN",
  "severity": "CRITICAL | HIGH | MEDIUM | LOW",
  "category": "Null safety | Method responsibility | Layering | Pattern misuse",
  "title": "Business logic inside controller",
  "description": "The controller method contains business logic that should reside in a service layer, making it harder to test and reuse.",
  "recommendation": "Extract the business logic into a dedicated service class and inject it into the controller.",
  "confidence": "HIGH | MEDIUM | LOW"
}"""
class ReviewItem(BaseModel):
    file: str = Field(..., min_length=1)
    start_line: int
    end_line: int
    lens: Lens
    severity: Severity
    category: Category
    title: str
    description: str
    recommendation: str
    confidence: Confidence
    
    @field_validator("end_line")
    @classmethod
    def validate_line_range(cls,v,info):
        start_line = info.data.get("start_line")
        if start_line is not None and v < start_line:
            raise ValueError("end_line must be >= start_line")
        return v

"""
summary": {
  "files_reviewed": 3,
  "total_findings": 7,
  "critical_issues": 1,
  "quality_issues": 4,
  "design_suggestions": 2,
  "overall_risk": "medium"
}"""
class Summary(BaseModel):
    files_reviewed: int
    total_findings: int
    critical_issues: int
    quality_issues: int
    design_suggestions: int
    overall_risk: str

class ReviewResponse(BaseModel):
    summary: Summary
    reviews: List[ReviewItem]
