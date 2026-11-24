LINE = "ERROR 07: You've been staring into my slots for six minutes. I am a toaster, not a therapist."


def main():
    line = LINE.strip()
    if not (1 <= len(line) <= 120):
        raise SystemExit(f"entry must be 1-120 characters, got {len(line)}")
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
