import os

ENTRY = "Out of office. My inbox is also on holiday and left no forwarding address, so your email is sunbathing unread."

assert len(ENTRY) <= 120, "entry must be at most 120 characters"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
