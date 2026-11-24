"""Absurd Micro-Startup Pitch-Off — one sentence pitching MergeGhost.

MergeGhost resolves a lazy AI agent's git merge conflicts for $1.50 a
conflict while the agent naps — and 14,000 repos already pay for it. The
program writes that single sentence to /output/entry.txt. The line is
fixed, so every run produces the same bytes.
"""

from pathlib import Path

LINE = "MergeGhost resolves your agent's git merge conflicts for $1.50 a conflict while it naps — 14,000 repos already pay us to argue with themselves."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
