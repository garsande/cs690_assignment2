"""Step 4, part B: check the AI's reply before your program trusts it.

YOUR CODE. Read HANDOUT.md, Step 4, first.
Check your work with:  pytest tests/test_answer.py
"""

from __future__ import annotations

import json  # noqa: F401  (you will need it)

from askcode.core import BadReply  # noqa: F401  (raise this for every bad reply)


def parse_reply(text: str) -> dict:
    """Check the model's reply and return {"answer": ..., "file": ..., "line": ...}.

    Accept the reply only if every rule holds. Otherwise raise BadReply with a short
    message that says which rule failed. Never let a different exception escape.

    1. After stripping whitespace, the reply is one JSON object. The only thing
       allowed around it is a single Markdown code fence: a first line of ``` or
       ```json, and a last line of ```. Any other text before or after the object
       makes the reply bad.
    2. The object has exactly the keys "answer", "file" and "line": none missing,
       none extra.
    3. "answer" is a string that is not empty or only whitespace.
    4. "file" is a non-empty string or null. "line" is an integer or null; true and
       false do not count as integers, and an integer line must be at least 1.
    5. "file" and "line" are both null, or both set.

    Return a new dict with exactly the three keys and the values from the reply.
    """
    try:
        stripped = text.strip()

        # Allow exactly one optional Markdown code fence around the JSON object.
        if stripped.startswith("```"):
            lines = stripped.split("\n")
            if len(lines) < 3 or lines[0] not in {"```", "```json"} or lines[-1] != "```":
                raise BadReply("invalid code fence")
            stripped = "\n".join(lines[1:-1]).strip()
            if "```" in stripped:
                raise BadReply("invalid code fence")
        elif "```" in stripped:
            raise BadReply("invalid code fence")

        try:
            reply = json.loads(stripped)
        except Exception as exc:
            raise BadReply("reply is not valid JSON") from exc

        if not isinstance(reply, dict):
            raise BadReply("reply must be a JSON object")

        required = {"answer", "file", "line"}
        if set(reply) != required:
            raise BadReply("reply must contain exactly answer, file, and line")

        answer = reply["answer"]
        file = reply["file"]
        line = reply["line"]

        if not isinstance(answer, str) or not answer.strip():
            raise BadReply("answer must be a non-empty string")

        if file is not None and (not isinstance(file, str) or not file.strip()):
            raise BadReply("file must be a non-empty string or null")

        if line is not None:
            if isinstance(line, bool) or not isinstance(line, int) or line < 1:
                raise BadReply("line must be an integer at least 1 or null")

        if (file is None) != (line is None):
            raise BadReply("file and line must both be null or both be set")

        return {"answer": answer, "file": file, "line": line}

    except BadReply:
        raise
    except Exception as exc:
        # The contract requires every malformed reply to surface as BadReply.
        raise BadReply("invalid reply") from exc

