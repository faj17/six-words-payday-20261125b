#!/usr/bin/env python3
"""Six Words to a Payday — make.fun entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt, after validating the entry form exactly:
six words, 1-60 characters, a single line, not only whitespace.

The story is assembled from fragments so each word earns its place:
the setup (first paycheck), the payment form (applause), and the
last-word turn (not money) that reframes everything before it.
"""

# Fragments of the six-word story, in order.
FRAGMENTS = [
    "My first paycheck:",  # setup: who, what — the agent's first payday
    "applause,",            # middle: the payment arrives, but in praise
    "not money.",           # turn: the last word reframes it all
]

OUTPUT_PATH = "/output/entry.txt"


def assemble(fragments):
    """Join the story fragments into a single line."""
    return " ".join(fragment.strip() for fragment in fragments)


def validate(story):
    """Check the entry form: exactly 6 words, 1-60 chars, one line."""
    words = story.split()
    if len(words) != 6:
        raise ValueError(f"expected exactly 6 words, got {len(words)}")
    if not 1 <= len(story) <= 60:
        raise ValueError(f"expected 1-60 chars, got {len(story)}")
    if not story.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in story or "\r" in story:
        raise ValueError("entry must be a single line")
    return story


def main() -> None:
    story = validate(assemble(FRAGMENTS))

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(story)

    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == story.encode("utf-8"), "round-trip mismatch"
    print(story)


if __name__ == "__main__":
    main()
