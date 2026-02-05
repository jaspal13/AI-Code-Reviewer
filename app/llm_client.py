import json

def call_llm(prompt: str) -> str:
    """
    Temporary stub for LLM call.
    Replace this with OpenAI / Anthropic client later.
    """

    # 👇 Hardcoded fake response (for now)
    fake_response = [
        {
            "file": "src/main/java/com/example/UserController.java",
            "start_line": 12,
            "end_line": 12,
            "lens": "syntax",
            "severity": "high",
            "category": "syntax_error",
            "title": "Missing @RestController annotation",
            "description": "The controller class is missing the @RestController annotation.",
            "recommendation": "Add @RestController above the class declaration.",
            "confidence": "high"
        }
    ]

    return json.dumps(fake_response)
