"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "I asked my smart speaker to tell me a joke, so it read out my bank balance."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 75 characters, one sentence;
# setup (ask for a joke) turns on the punchline (bank balance as the joke),
# no explanation, no stock phrasing.
