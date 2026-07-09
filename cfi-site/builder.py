import sys, os
sys.stdout.reconfigure(encoding="utf-8")
cwd = os.getcwd()
print(f"Working in: {cwd}")

# app.py - base part
base = '''#!/usr/bin/env python3
import http.server, json, sqlite3, os, re, urllib.parse, html as html_mod
import mimetypes, hashlib, uuid, io
from pathlib import Path
BASE_DIR = Path(__file__).parent.resolve()
DATA_DIR = BASE_DIR / "data"
STATIC_DIR = BASE_DIR / "static"
UPLOAD_DIR = DATA_DIR / "uploads"
DB_PATH = DATA_DIR / "site.db"
ENV = os.environ.get("CFI_ENV", "development")
HOST = os.environ.get("CFI_HOST", "127.0.0.1")
PORT = int(os.environ.get("CFI_PORT", "7010"))
ADMIN_USER = os.environ.get("CFI_ADMIN_USER", "admin")
ADMIN_PASSWORD = os.environ.get("CFI_ADMIN_PASSWORD", "cfi2026")
UPLOAD_IMAGE_MAX = 5*1024*1024; UPLOAD_PDF_MAX = 20*1024*1024
ALLOWED_IMAGES = {".jpg",".jpeg",".png"}; ALLOWED_DOCS = {".pdf"}
def get_db():
    db = sqlite3.connect(str(DB_PATH))
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA foreign_keys=ON")
    return db
def esc(t):
    if t is None: return ""
    return html_mod.escape(str(t))
def slugify(text):
    text = str(text).strip().lower()
    text = re.sub(r"[^\\w\\s-]", "", text)
    text = re.sub(r"[\\s_]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")
def get_setting(db, key, default=""):
    row = db.execute("SELECT value FROM site_settings WHERE key=?", (key,)).fetchone()
    return row["value"] if row else default
def parse_tags(tags_str):
    if not tags_str: return []
    return [t.strip() for t in tags_str.split(",") if t.strip()]
'''
with open("app.py", "w", encoding="utf-8") as f:
    f.write(base)
print(f"Base written ({len(base)} bytes)")
