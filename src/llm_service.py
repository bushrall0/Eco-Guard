import os
import json
from dotenv import load_dotenv

load_dotenv()

def call_llm(prompt: str) -> str:
    import anthropic
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=api_key)
    try:
        response = client.messages.create(
            model=os.environ.get("CLAUDE_MODEL", "claude-sonnet-5-5"),
            max_tokens=4096,
            thinking={"type": "between_tools"},
            system="You must respond with valid JSON only. No text before or after the JSON. No markdown. No code blocks. Pure JSON object.",
            messages=[{"role": "user", "content": prompt}]
        )
        text = "".join(block.text for block in response.content if block.type == "text")
        if not text:
            raise ValueError(f"لم يتم استلام إجابة من النموذج (stop_reason: {response.stop_reason})")
        return text
    except Exception as e:
        error_response = {
            "status": "خطأ",
            "score": 0,
            "issues": [str(e)],
            "notes": "فشل الاتصال"
        }
        return json.dumps(error_response, ensure_ascii=False)