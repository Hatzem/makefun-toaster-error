"""Funniest toaster error message entry.

Writes one deadpan ERROR line to entry.txt in the make.fun output dir.
"""
import os

LINE = "ERROR 07: You've been staring into my slots for six minutes. I am a toaster, not a therapist."


def main():
    line = LINE.strip()
    if not (1 <= len(line) <= 120):
        raise SystemExit(f"entry must be 1-120 characters, got {len(line)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
