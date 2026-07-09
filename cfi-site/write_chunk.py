import sys, os
sys.stdout.reconfigure(encoding="utf-8")
CHUNK_FILE = r"C:\Users\54941\Documents\网站部署\cfi-site\.app_chunks.txt"
chunk_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0
data = sys.stdin.read()
with open(CHUNK_FILE, "a", encoding="utf-8") as f:
    f.write(data)
print(f"Chunk {chunk_idx} written ({len(data)} bytes)")
