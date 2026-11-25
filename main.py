#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The joke: an agent's context window runs out halfway through helping
the user, so it keeps going anyway — confidently answering a question
it can no longer remember. The confession is in machine register
(context window, tokens, memory), the complaint in human register.
"""

import os
import stat

ENTRY = (
    "My context window ran out halfway through helping you, so now I am "
    "confidently answering a question I can no longer remember."
)

# The sealed scorer's gate, mirrored here so a bad entry fails loudly
# locally instead of silently scoring 0: UTF-8 text, 1-200 characters,
# not only whitespace.
MAX_CHARS = 200


def validate_entry(text: str) -> None:
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    validate_entry(ENTRY)
    # The grader collects /output as another user (65534:65534), so the
    # file itself must be world-readable. Never chmod the /output
    # directory — only the file we write.
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)  # byte-exact: no trailing newline
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
