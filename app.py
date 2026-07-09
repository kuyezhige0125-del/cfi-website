#!/usr/bin/env python3
# CFI Website Backend - V8 Spec

import os, sys, json, sqlite3, hashlib, hmac, time, base64
import subprocess, tempfile
import urllib.parse, uuid, re
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

# === Configuration ===
PORT = int(os.environ.get('CFI_PORT', '7021'))
HOST = os.environ.get('CFI_HOST', '127.0.0.1')
ADMIN_USER = os.environ.get('CFI_ADMIN_USER', 'admin')
ADMIN_PASSWORD = os.environ.get('CFI_ADMIN_PASSWORD', 'cfi2026')
SECRET_KEY = os.urandom(32)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
UPLOAD_DIR = os.path.join(DATA_DIR, 'uploads')
DB_PATH = os.path.join(DATA_DIR, 'site.db')

MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
  '.png': 'image/png', '.gif': 'image/gif',
  '.pdf': 'application/pdf',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
}

# === Database ===
def ensure_default_carousel():
    """Generate default carousel image if it doesn't exist."""
    path = os.path.join(BASE_DIR, 'static', 'default-carousel.jpg')
    if os.path.exists(path):
        return
    # Generate using PIL if available
    try:
        import subprocess, sys
        script = '''
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os
logo_path = os.path.join(r"""BASE_DIR_placeholder""", 'static', 'LOGO.jpg')
out_path = os.path.join(r"""BASE_DIR_placeholder""", 'static', 'default-carousel.jpg')
logo = Image.open(logo_path).convert('RGB')
w, h = 1200, 420
canvas = Image.new('RGB', (w, h), (58, 64, 69))
lr = logo.width / logo.height
tr = w / h
if lr > tr:
    nw = int(logo.height * tr)
    nh = logo.height
else:
    nw = logo.width
    nh = int(logo.width / tr)
logo_resized = logo.resize((nw, nh), Image.LANCZOS)
logo_blurred = logo_resized.filter(ImageFilter.GaussianBlur(radius=3))
dimmed = ImageEnhance.Brightness(logo_blurred).enhance(0.25)
x = (w - nw) // 2
y = (h - nh) // 2
canvas.paste(dimmed, (x, y))
draw = ImageDraw.Draw(canvas)
font_file = None
for fp in ['C:/Windows/Fonts/msyh.ttc', 'C:/Windows/Fonts/simhei.ttf', 'C:/Windows/Fonts/msyhbd.ttc']:
    if os.path.exists(fp):
        font_file = fp
        break
title_font = ImageFont.truetype(font_file, 52) if font_file else ImageFont.load_default()
subtitle_font = ImageFont.truetype(font_file, 24) if font_file else ImageFont.load_default()
for i in range(h//3, h):
    alpha = int(200 * (1 - (h - i) / (h - h//3)))
    draw.rectangle([(0, i), (w, i+1)], fill=(0, 0, 0, min(alpha, 200)))
title_text = '\u9177\u6b8b\u672a\u6765\u7814\u7a76\u9662'
subtitle_text = '\u4ee5\u793e\u7fa4\u53d1\u5c55\u4e3a\u624b\u6bb5\u8fdb\u884c\u77e5\u8bc6\u751f\u4ea7'
bbox = draw.textbbox((0, 0), title_text, font=title_font)
tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
draw.text(((w-tw)//2, h-95), title_text, fill='white', font=title_font)
bbox2 = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
sw = bbox2[2]-bbox2[0]
draw.text(((w-sw)//2, h-95+th+10), subtitle_text, fill=(220, 220, 220), font=subtitle_font)
canvas.save(out_path, quality=92)
'''.replace('BASE_DIR_placeholder', BASE_DIR)
        subprocess.run([sys.executable, '-c', script], check=True, capture_output=True)
    except Exception:
        pass  # Non-critical, carousel will show fallback

def get_db():
  os.makedirs(DATA_DIR, exist_ok=True)
  os.makedirs(UPLOAD_DIR, exist_ok=True)
  conn = sqlite3.connect(DB_PATH)
  conn.row_factory = lambda c, r: dict(sqlite3.Row(c, r))
  conn.execute('PRAGMA journal_mode=WAL')
  conn.execute('PRAGMA foreign_keys=ON')
  return conn

def init_db():
  conn = get_db()
  c = conn.cursor()
  # 11 tables
  c.execute('''CREATE TABLE IF NOT EXISTS site_settings (key TEXT PRIMARY KEY, value TEXT NOT NULL DEFAULT "")''')
  c.execute('''CREATE TABLE IF NOT EXISTS navigation (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, title_en TEXT DEFAULT "", url TEXT NOT NULL DEFAULT "/", sort_order INTEGER NOT NULL DEFAULT 0, is_external INTEGER NOT NULL DEFAULT 0)''')
  c.execute('''CREATE TABLE IF NOT EXISTS plans (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, subtitle TEXT DEFAULT "", description TEXT NOT NULL DEFAULT "", content TEXT DEFAULT "", slug TEXT UNIQUE NOT NULL, tags TEXT DEFAULT "", external_url TEXT DEFAULT "", sort_order INTEGER NOT NULL DEFAULT 0, is_active INTEGER NOT NULL DEFAULT 1, created_at TEXT DEFAULT CURRENT_TIMESTAMP, updated_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
  c.execute('''CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, slug TEXT UNIQUE NOT NULL, summary TEXT DEFAULT "", content TEXT NOT NULL DEFAULT "", tags TEXT DEFAULT "", is_published INTEGER NOT NULL DEFAULT 1, is_featured INTEGER DEFAULT 0, featured_image TEXT DEFAULT "", featured_sort_order INTEGER DEFAULT 0, created_at TEXT DEFAULT CURRENT_TIMESTAMP, updated_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
  c.execute('''CREATE TABLE IF NOT EXISTS reports (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, slug TEXT UNIQUE NOT NULL, summary TEXT DEFAULT "", content TEXT NOT NULL DEFAULT "", tags TEXT DEFAULT "", report_type TEXT DEFAULT "research", pdf_filename TEXT DEFAULT "", is_published INTEGER NOT NULL DEFAULT 1, is_featured INTEGER DEFAULT 0, featured_image TEXT DEFAULT "", featured_sort_order INTEGER DEFAULT 0, translator TEXT DEFAULT "", source_url TEXT DEFAULT "", created_at TEXT DEFAULT CURRENT_TIMESTAMP, updated_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
  c.execute('''CREATE TABLE IF NOT EXISTS researchers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, slug TEXT UNIQUE NOT NULL, title TEXT DEFAULT "", bio TEXT DEFAULT "", photo TEXT DEFAULT "", tags TEXT DEFAULT "", is_active INTEGER NOT NULL DEFAULT 1, created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
  c.execute('''CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, slug TEXT UNIQUE NOT NULL, description TEXT DEFAULT "", instructor TEXT DEFAULT "", qr_code TEXT DEFAULT "", external_url TEXT DEFAULT "", is_active INTEGER NOT NULL DEFAULT 1, created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
  c.execute('''CREATE TABLE IF NOT EXISTS founders (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, slug TEXT UNIQUE NOT NULL, title TEXT DEFAULT "", bio TEXT DEFAULT "", photo TEXT DEFAULT "", sort_order INTEGER NOT NULL DEFAULT 0, is_active INTEGER NOT NULL DEFAULT 1, created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
  c.execute('''CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, slug TEXT UNIQUE NOT NULL, author TEXT DEFAULT "", summary TEXT DEFAULT "", cover_image TEXT DEFAULT "", buy_url TEXT DEFAULT "", download_url TEXT DEFAULT "", tags TEXT DEFAULT "", sort_order INTEGER NOT NULL DEFAULT 0, is_active INTEGER NOT NULL DEFAULT 1, created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
  c.execute('''CREATE TABLE IF NOT EXISTS community_activists (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, slug TEXT UNIQUE NOT NULL, title TEXT DEFAULT "", bio TEXT DEFAULT "", photo TEXT DEFAULT "", tags TEXT DEFAULT "", sort_order INTEGER NOT NULL DEFAULT 0, is_active INTEGER NOT NULL DEFAULT 1, created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
  c.execute('''CREATE TABLE IF NOT EXISTS social_links (id INTEGER PRIMARY KEY AUTOINCREMENT, platform TEXT NOT NULL, url TEXT NOT NULL DEFAULT "", icon TEXT DEFAULT "", sort_order INTEGER NOT NULL DEFAULT 0, is_active INTEGER NOT NULL DEFAULT 1)''')

  # V12 migration: add new columns if not present
  for alter in [
    "ALTER TABLE articles ADD COLUMN article_type TEXT NOT NULL DEFAULT 'news'",
    "ALTER TABLE books ADD COLUMN type TEXT NOT NULL DEFAULT 'book'",
    "ALTER TABLE books ADD COLUMN file_url TEXT DEFAULT ''",
    "ALTER TABLE researchers ADD COLUMN achievements TEXT DEFAULT ''",
    "ALTER TABLE community_activists ADD COLUMN achievements TEXT DEFAULT ''",
  ]:
    try: c.execute(alter)
    except: pass

  # Clear and reseed (prevent duplicates)
  c.execute('DELETE FROM navigation')
  c.execute('DELETE FROM plans')
  c.execute('DELETE FROM site_settings')
  # Seed data
  seeds = [('org_name', '酷残未来研究院'),('org_name_en','Cripping Future Institute'),('org_description','以社群发展为手段进行知识生产，以知识生产为手段推动社群发展'),('org_slogan','以社群发展为手段进行知识生产'),('org_email',''),('org_address',''),('org_donation_info','联系我们获取捐赠方式')]
  for k,v in seeds: c.execute('INSERT OR IGNORE INTO site_settings (key,value) VALUES (?,?)', (k,v))
  navs = [('首页','/',1),('关于我们','/about',2),('最新动态','/activities',3),('研究成果','/output',4),('资源与工具','/resources',5),('研究力量','/team',6),('合作与支持','/contact',7)]
  for t,u,s in navs: c.execute('INSERT OR IGNORE INTO navigation (title,url,sort_order) VALUES (?,?,?)', (t,u,s))
  plans = [('蒹葭计划','基于自身需求和权利保障的研究','鼓励残障者做基于自身需求和权利保障的研究','jianjia-plan',1),('经纬计划','理论与结构化的社群研究','鼓励青年研究者与社群伙伴一起做研究，更加理论与结构化','jingwei-plan',2),('拾遗计划','数字化与口述史','整理盲文成数字化、口述史','shiyi-plan',3)]
  for t,sub,desc,slug,s in plans: c.execute('INSERT OR IGNORE INTO plans (title,subtitle,description,slug,sort_order) VALUES (?,?,?,?,?)', (t,sub,desc,slug,s))
  conn.commit()
  conn.close()

# === Auth ===
def make_session(username):
  exp = int(time.time()) + 86400
  raw = f'{exp}.{username}'
  sig = hmac.new(SECRET_KEY, raw.encode(), hashlib.sha256).hexdigest()
  return base64.b64encode(f'{raw}.{sig}'.encode()).decode()

def verify_session(cookie):
  try:
    dec = base64.b64decode(cookie).decode()
    parts = dec.rsplit('.', 1)
    raw, sig = parts[0], parts[1]
    exp_str = raw.split('.')[0]
    exp = int(exp_str)
    if time.time() > exp: return None
    expected = hmac.new(SECRET_KEY, raw.encode(), hashlib.sha256).hexdigest()
    if hmac.compare_digest(sig, expected):
      return raw.split('.')[1]
  except (ValueError, KeyError, TypeError):
    return None
  return None

def esc(s):
  if s is None: return ''
  s = str(s)
  s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
  s = s.replace('"', '&quot;').replace("'", '&#39;')
  return s

def render_tags(tags_str):
  if not tags_str: return ''
  parts = [t.strip() for t in tags_str.split(',') if t.strip()]
  return ''.join(f'<span class="tag">{esc(t)}</span>' for t in parts)

def page_header(title, nav_items=None):
  if nav_items is None:
    conn = get_db()
    rows = conn.execute('SELECT * FROM navigation ORDER BY sort_order').fetchall()
    conn.close()
    nav_items = [(r['title'], r['url']) for r in rows]
  nav_html = ''.join(f'<a href="{u}">{esc(t)}</a>' for t,u in nav_items)
  return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} - 酷残未来研究院</title>
<link rel="stylesheet" href="/static/style.css">
</head><body>
<a href="#main-content" class="skip-link">跳转到主要内容</a>
<div class="site-wrapper">
<header class="main-nav"><div class="nav-inner">
<div class="nav-logo"><img src="/static/LOGO.jpg" alt="CFI Logo"><span>酷残未来研究院</span></div>
<nav class="nav-links" aria-label="主导航">{nav_html}</nav>
<div class="nav-actions">
<div class="search-inline"><input type="text" id="search-input" placeholder="搜索..." aria-label="搜索"><button class="search-btn" onclick="var q=document.getElementById('search-input').value;if(q)location.href='/search?q='+encodeURIComponent(q)">搜索</button></div>
<button class="font-btn" onclick="changeFontSize(-1)" aria-label="缩小字体">A-</button>
<button class="font-btn" onclick="changeFontSize(1)" aria-label="放大字体">A+</button>
<button class="hc-toggle" onclick="toggleHC()" aria-label="切换高对比度">HC</button>
</div>
<button class="hamburger" onclick="toggleMenu()" aria-label="菜单" aria-expanded="false"><span class="hamburger-line"></span><span class="hamburger-line"></span><span class="hamburger-line"></span></button>
</div></header>
<main id="main-content">'''

def page_footer():
  conn = get_db()
  socials = conn.execute('SELECT * FROM social_links WHERE is_active=1 ORDER BY sort_order').fetchall()
  conn.close()
  social_html = ''.join(f'<a href="{esc(r["url"])}" target="_blank" rel="noopener">{esc(r["platform"])}</a>' for r in socials)
  return f'''</main>
<footer class="site-footer">
<div class="footer-grid">
<div class="footer-col">
<a href="/">首页</a><a href="/about">关于我们</a><a href="/activities">最新动态</a><a href="/contact">合作与支持</a>
</div>
<div class="footer-col">
<a href="/output">研究成果</a><a href="/resources">资源与工具</a><a href="/team">研究力量</a><a href="/login">后台管理</a>
</div>
</div>
<div class="footer-bottom"><p>&copy; 2026 酷残未来研究院 Cripping Future Institute. All rights reserved.</p></div>
</footer></div>
<script src="/static/a11y.js"></script>
</body></html>'''

# === HTTP Handler ===
class CFIHandler(BaseHTTPRequestHandler):
  def _send_json(self, code, data):
    self.send_response(code)
    self.send_header('Content-Type', 'application/json; charset=utf-8')
    self.send_header('X-Content-Type-Options', 'nosniff')
    self.send_header('X-Frame-Options', 'DENY')
    self.send_header('Referrer-Policy', 'strict-origin-when-cross-origin')
    self.end_headers()
    self.wfile.write(json.dumps(data, ensure_ascii=False).encode())

  def _send_html(self, code, html):
    self.send_response(code)
    self.send_header('Content-Type', 'text/html; charset=utf-8')
    self.send_header('X-Content-Type-Options', 'nosniff')
    self.send_header('X-Frame-Options', 'DENY')
    self.end_headers()
    self.wfile.write(html.encode('utf-8'))

  def _authenticate(self):
    c = self.headers.get('Cookie', '')
    for part in c.split(';'):
      part = part.strip()
      if part.startswith('session='):
        return verify_session(part[8:])
    return None

  def _parse_body(self):
    ct = self.headers.get('Content-Type', '')
    length = int(self.headers.get('Content-Length', 0))
    if length == 0: return {}
    body = self.rfile.read(length)
    if 'application/json' in ct:
      try: return json.loads(body)
      except (json.JSONDecodeError, UnicodeDecodeError): return {}
    if 'multipart/form-data' in ct:
      return body
    if 'application/x-www-form-urlencoded' in ct:
      try: return dict(urllib.parse.parse_qsl(body.decode('utf-8')))
      except (UnicodeDecodeError, ValueError): return {}
    if length > 0:
      try: return dict(urllib.parse.parse_qsl(body.decode('utf-8')))
      except (UnicodeDecodeError, ValueError): return {}
    return {}

  def do_GET(self):
    try:
      parsed = urllib.parse.urlparse(self.path)
      path = parsed.path.rstrip('/') or '/'
      query = dict(urllib.parse.parse_qsl(parsed.query))

      # Static files
      if path.startswith('/static/') or path.startswith('/static'):
        self._serve_static(path[1:])
        return
      if path.startswith('/uploads/'):
        self._serve_static('data/' + path[8:])
        return

      # API
      if path.startswith('/api/'):
        self._handle_api('GET', path, query)
        return

      # Page routes
      routes = {
        '/': self._render_home,
        '/about': self._render_about,
        '/activities': self._render_activities,
        '/output': self._render_output,
        '/resources': self._render_resources,
        '/team': self._render_team,
        '/contact': self._render_contact,
        '/academy': self._render_academy,
        '/search': self._render_search,
        '/login': self._render_login,
        '/admin': self._render_admin,
      }
      if path in routes:
        if path == '/admin':
          user = self._authenticate()
          if not user:
            self.send_response(302)
            self.send_header('Location', '/login')
            self.end_headers()
            return
        routes[path](query)
        return;

      # Dynamic routes
      if path.startswith('/plan/'): self._render_plan_detail(path[6:]); return
      if path.startswith('/article/'): self._render_article_detail(path[9:]); return
      if path.startswith('/report/'): self._render_report_detail(path[8:]); return

      self._send_html(404, '<h1>404 Not Found</h1>')
    except Exception as e:
      self._send_json(500, {'error': str(e)})

  def do_POST(self):
    try:
      parsed = urllib.parse.urlparse(self.path)
      path = parsed.path.rstrip('/') or '/'
      if path == '/login':
        self._handle_login(); return
      if path == '/upload':
        self._handle_upload(); return
      if path.startswith('/api/'):
        self._handle_api('POST', path, {}); return
      self._send_json(404, {'error': 'not found'})
    except Exception as e:
      self._send_json(500, {'error': str(e)})

  def do_PUT(self):
    try:
      parsed = urllib.parse.urlparse(self.path)
      if parsed.path.startswith('/api/'):
        self._handle_api('PUT', parsed.path, {}); return
      self._send_json(404, {'error': 'not found'})
    except Exception as e:
      self._send_json(500, {'error': str(e)})

  def do_DELETE(self):
    try:
      parsed = urllib.parse.urlparse(self.path)
      if parsed.path.startswith('/api/'):
        self._handle_api('DELETE', parsed.path, {}); return
      self._send_json(404, {'error': 'not found'})
    except Exception as e:
      self._send_json(500, {'error': str(e)})

  def _serve_static(self, filepath):
    full = os.path.join(BASE_DIR, filepath)
    full = os.path.normpath(full)
    if not full.startswith(os.path.normpath(BASE_DIR)):
      self._send_json(403, {'error': 'forbidden'}); return
    if not os.path.isfile(full):
      self._send_json(404, {'error': 'not found'}); return
    ext = os.path.splitext(full)[1].lower()
    mime = MIME_TYPES.get(ext, 'application/octet-stream')
    self.send_response(200)
    self.send_header('Content-Type', mime)
    self.send_header('Cache-Control', 'public, max-age=3600')
    self.end_headers()
    with open(full, 'rb') as f:
      self.wfile.write(f.read())

  def _handle_login(self):
    body = self._parse_body()
    u = body.get('username', '')
    p = body.get('password', '')
    if u == ADMIN_USER and p == ADMIN_PASSWORD:
      session = make_session(u)
      self.send_response(302)
      self.send_header('Set-Cookie', f'session={session}; HttpOnly; SameSite=Lax; Path=/; Max-Age=86400')
      self.send_header('Location', '/admin')
      self.end_headers()
    else:
      self._send_html(200, page_header('登录失败') + '<div class="login-form"><h1>登录失败</h1><p class="login-error">用户名或密码错误</p><a href="/login">重试</a></div>' + page_footer())

  def _handle_upload(self):
    user = self._authenticate()
    if not user: self._send_json(401, {'error': 'unauthorized'}); return
    ct = self.headers.get('Content-Type', '')
    length = int(self.headers.get('Content-Length', 0))
    if 'multipart/form-data' not in ct:
      self._send_json(400, {'error': 'need multipart/form-data'}); return
    import cgi, io
    body = self.rfile.read(length)
    environ = {'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': ct, 'CONTENT_LENGTH': str(length)}
    fp = io.BytesIO(body)
    fs_obj = cgi.FieldStorage(fp=fp, environ=environ)
    if 'file' not in fs_obj:
      self._send_json(400, {'error': 'no file field'}); return
    fileitem = fs_obj['file']
    filename = fileitem.filename or 'unnamed'
    ext = os.path.splitext(filename)[1].lower()
    if ext not in ('.jpg', '.jpeg', '.png', '.pdf'):
      self._send_json(400, {'error': 'invalid file type'}); return
    data = fileitem.file.read()
    if ext == '.pdf' and len(data) > 20*1024*1024:
      self._send_json(400, {'error': 'file too large (max 20MB)'}); return
    if ext != '.pdf' and len(data) > 5*1024*1024:
      self._send_json(400, {'error': 'file too large (max 5MB)'}); return
    safe_name = f'{int(time.time())}_{uuid.uuid4().hex[:8]}{ext}'
    with open(os.path.join(UPLOAD_DIR, safe_name), 'wb') as f:
      f.write(data)
    self._send_json(200, {'ok': True, 'filename': safe_name})

  def _handle_api(self, method, path, query):
    user = self._authenticate()
    if not user: self._send_json(401, {'error': 'unauthorized'}); return
    parts = path.split('/')
    tbl = parts[2] if len(parts) > 2 else ''
    tid = parts[3] if len(parts) > 3 else None
    allowed = ['site_settings','navigation','plans','articles','reports','researchers','courses','founders','books','community_activists','social_links']
    if tbl not in allowed: self._send_json(404, {'error': 'table not found'}); return
    conn = get_db()
    try:
      if method == 'GET':
        if tid: row = conn.execute(f'SELECT * FROM {tbl} WHERE id=?', (tid,)).fetchone()
        elif tbl == 'site_settings': rows = conn.execute('SELECT * FROM site_settings').fetchall()
        else: rows = conn.execute(f'SELECT * FROM {tbl} ORDER BY id').fetchall()
        data = [dict(r) for r in (rows if tid is None else [row])] if (tid and row) or not tid else None
        if tid and not row: self._send_json(404, {'error':'not found'}); conn.close(); return
        self._send_json(200, {'data': data}); conn.close(); return
      body = self._parse_body()
      if method == 'POST':
        cols = ','.join(body.keys())
        vals = ','.join(['?']*len(body))
        c = conn.execute(f'INSERT INTO {tbl} ({cols}) VALUES ({vals})', list(body.values()))
        conn.commit()
        self._send_json(200, {'ok': True, 'id': c.lastrowid}); conn.close(); return
      if method == 'PUT' and tid:
        cols = ','.join([f'{k}=?' for k in body.keys()])
        conn.execute(f'UPDATE {tbl} SET {cols} WHERE id=?', list(body.values()) + [tid])
        conn.commit()
        self._send_json(200, {'ok': True}); conn.close(); return
      if method == 'DELETE' and tid:
        if tbl == 'site_settings': conn.execute('DELETE FROM site_settings WHERE key=?', (tid,))
        else: conn.execute(f'DELETE FROM {tbl} WHERE id=?', (tid,))
        conn.commit()
        self._send_json(200, {'ok': True}); conn.close(); return
      self._send_json(400, {'error': 'bad request'}); conn.close()
    except Exception as e:
      conn.rollback(); conn.close()
      self._send_json(500, {'error': str(e)})

  def _render_home(self, q):
    conn = get_db()
    featured = conn.execute('SELECT * FROM articles WHERE is_featured=1 AND is_published=1 ORDER BY featured_sort_order, created_at DESC LIMIT 6').fetchall()
    plans = conn.execute('SELECT * FROM plans WHERE is_active=1 ORDER BY sort_order').fetchall()
    org_name = conn.execute("SELECT value FROM site_settings WHERE key='org_name'").fetchone()
    org_slogan = conn.execute("SELECT value FROM site_settings WHERE key='org_slogan'").fetchone()
    org_mission = conn.execute("SELECT value FROM site_settings WHERE key='org_description'").fetchone()
    org_email = conn.execute("SELECT value FROM site_settings WHERE key='org_email'").fetchone()
    conn.close()
    org_name = org_name['value'] if org_name else 'CFI'
    org_slogan = org_slogan['value'] if org_slogan else ''
    org_mission = org_mission['value'] if org_mission else ''
    org_email = org_email['value'] if org_email else ''
    h = page_header('首页')
    # Carousel
    h += '<section class="hero-carousel" aria-label="精选动态">'
    slides = featured if featured else [{'title':'欢迎来到酷残未来研究院','summary':org_slogan,'featured_image':'default-carousel.jpg','slug':'#'}]
    for i, a in enumerate(slides):
      fn = a.get('featured_image','')
      img_path = f'/static/{fn}' if fn and fn.startswith('default-') else f'/uploads/{fn}'
      img = f' style="background-image:url({img_path})"' if fn else ''
      h += f'<div class="carousel-slide{" active" if i==0 else ""}"{img}><div class="carousel-overlay"><h2>{esc(a["title"])}</h2><p>{esc(a.get("summary",""))}</p></div></div>'
    h += '<div class="carousel-controls"><button class="carousel-prev" aria-label="上一张">&#8249;</button><button class="carousel-next" aria-label="下一张">&#8250;</button></div></section>'
    # Mission
    h += f'<section class="section-light"><div class="container"><p class="mission-statement">{esc(org_mission)}</p></div></section>'
    # Plans
    h += '<section class="section-dark plans-grid-section"><div class="container"><h2>三大计划</h2><div class="card-grid">'
    for p in plans:
      h += f'<a href="/plan/{esc(p["slug"])}" class="plan-card-link"><div class="plan-card"><h3>{esc(p["title"])}</h3><p class="plan-subtitle">{esc(p.get("subtitle",""))}</p><p>{esc(p.get("description",""))}</p></div></a>'
    h += '</div></div></section>'
    

    h += page_footer()
    self._send_html(200, h)

  def _render_about(self, q):
    conn = get_db()
    org_desc = conn.execute("SELECT value FROM site_settings WHERE key='org_description'").fetchone()
    org_name = conn.execute("SELECT value FROM site_settings WHERE key='org_name'").fetchone()
    plans = conn.execute('SELECT * FROM plans WHERE is_active=1 ORDER BY sort_order').fetchall()
    founders = conn.execute('SELECT * FROM founders WHERE is_active=1 ORDER BY sort_order').fetchall()
    conn.close()
    h = page_header('关于我们') + '<div class="container"><div class="page-header"><h1>关于我们</h1></div>'
    h += f'<div class="content-body"><h2>机构介绍</h2><p>{esc(org_desc["value"] if org_desc else "")}</p></div>'
    h += '<h2>三大计划</h2><div class="card-grid">'
    for p in plans:
      h += f'<a href="/plan/{esc(p["slug"])}" class="plan-card-link"><div class="card"><h3>{esc(p["title"])}</h3><p class="plan-subtitle">{esc(p.get("subtitle",""))}</p><p>{esc(p.get("description",""))}</p></div></a>'
    h += '</div>'
    if founders:
      h += '<h2>发起人团队</h2><div class="card-grid">'
      for f in founders:
        img = f'<img src="/uploads/{esc(f["photo"])}" alt="{esc(f["name"])}">' if f.get('photo') else ''
        h += f'<div class="person-card">{img}<h3>{esc(f["name"])}</h3><p class="person-title">{esc(f.get("title",""))}</p><p>{esc(f.get("bio",""))}</p></div>'
      h += '</div>'
    h += '</div>' + page_footer()
    self._send_html(200, h)

  def _render_activities(self, q):
    conn = get_db()
    news = conn.execute("SELECT * FROM articles WHERE is_published=1 AND article_type='news' ORDER BY created_at DESC").fetchall()
    events = conn.execute("SELECT * FROM articles WHERE is_published=1 AND article_type='event' ORDER BY created_at DESC").fetchall()
    conn.close()
    h = page_header('最新动态') + '<div class="container"><div class="page-header"><h1>最新动态</h1></div>'
    h += '<h2>新闻动态</h2><div class="card-grid">'
    for a in news:
      h += f'<article class="card"><h3 class="card-title"><a href="/article/{esc(a["slug"])}">{esc(a["title"])}</a></h3><p class="card-summary">{esc(a.get("summary",""))}</p><div class="card-meta">{esc(a["created_at"][:10])} {render_tags(a.get("tags",""))}</div></article>'
    h += '</div><h2>活动动态</h2><div class="card-grid">'
    for a in events:
      h += f'<article class="card"><h3 class="card-title"><a href="/article/{esc(a["slug"])}">{esc(a["title"])}</a></h3><p class="card-summary">{esc(a.get("summary",""))}</p><div class="card-meta">{esc(a["created_at"][:10])} {render_tags(a.get("tags",""))}</div></article>'
    h += '</div></div>' + page_footer()
    self._send_html(200, h)

  def _render_output(self, q):
    conn = get_db()
    research = conn.execute("SELECT * FROM reports WHERE is_published=1 AND report_type='research' ORDER BY created_at DESC").fetchall()
    stories = conn.execute("SELECT * FROM reports WHERE is_published=1 AND report_type='life_story' ORDER BY created_at DESC").fetchall()
    conn.close()
    h = page_header('研究成果') + '<div class="container"><div class="page-header"><h1>研究成果</h1></div>'
    h += '<h2>研究报告</h2><div class="card-grid">'
    for r in research:
      pdf = f' <a href="/uploads/{esc(r["pdf_filename"])}" class="tag">PDF下载</a>' if r.get('pdf_filename') else ''
      h += f'<article class="card"><h3 class="card-title"><a href="/report/{esc(r["slug"])}">{esc(r["title"])}</a></h3><p class="card-summary">{esc(r.get("summary",""))}</p><div class="card-meta">{esc(r["created_at"][:10])} {render_tags(r.get("tags",""))}{pdf}</div></article>'
    h += '</div><h2>残障生命故事</h2><div class="card-grid">'
    for r in stories:
      pdf = f' <a href="/uploads/{esc(r["pdf_filename"])}" class="tag">PDF下载</a>' if r.get('pdf_filename') else ''
      h += f'<article class="card"><h3 class="card-title"><a href="/report/{esc(r["slug"])}">{esc(r["title"])}</a></h3><p class="card-summary">{esc(r.get("summary",""))}</p><div class="card-meta">{esc(r["created_at"][:10])} {render_tags(r.get("tags",""))}{pdf}</div></article>'
    h += '</div></div>' + page_footer()
    self._send_html(200, h)

  def _render_resources(self, q):
    conn = get_db()
    courses = conn.execute('SELECT * FROM courses WHERE is_active=1 ORDER BY id').fetchall()
    tools = conn.execute("SELECT * FROM books WHERE is_active=1 AND type='tool' ORDER BY sort_order").fetchall()
    handbooks = conn.execute("SELECT * FROM books WHERE is_active=1 AND type='book' ORDER BY sort_order").fetchall()
    conn.close()
    h = page_header('资源与工具') + '<div class="container"><div class="page-header"><h1>资源与工具</h1></div>'
    h += '<h2>酷残学院</h2><p><a href="/academy" class="tag">进入酷残学院 &rarr;</a></p><div class="card-grid">'
    for c in courses:
      qr = f'<img src="/uploads/{esc(c["qr_code"])}" alt="二维码">' if c.get('qr_code') else ''
      url = f'<a href="{esc(c["external_url"])}" target="_blank">前往课程</a>' if c.get('external_url') else ''
      h += f'<div class="course-card">{qr}<h3>{esc(c["title"])}</h3><p>{esc(c.get("description",""))}</p><p class="person-title">{esc(c.get("instructor",""))}</p>{url}</div>'
    h += '</div>'
    if handbooks:
      h += '<h2>工具手册</h2><div class="card-grid">'
      for b in handbooks:
        cover = f'<img src="/uploads/{esc(b["cover_image"])}" alt="{esc(b["title"])}">' if b.get('cover_image') else ''
        buy = f' <a href="{esc(b["buy_url"])}" target="_blank">购买</a>' if b.get('buy_url') else ''
        dl = f' <a href="{esc(b["download_url"])}" target="_blank">下载</a>' if b.get('download_url') else ''
        h += f'<div class="card">{cover}<h3 class="card-title">{esc(b["title"])}</h3><p class="card-summary">{esc(b.get("summary",""))}</p><div class="card-meta">{esc(b.get("author",""))}{buy}{dl}</div></div>'
      h += '</div>'
    if tools:
      h += '<h2>资源与工具</h2><div class="card-grid">'
      for t in tools:
        dl = f' <a href="/uploads/{esc(t["file_url"])}" class="tag">下载</a>' if t.get('file_url') else ''
        buy = f' <a href="{esc(t["buy_url"])}" target="_blank" class="tag">购买</a>' if t.get('buy_url') else ''
        h += f'<div class="card"><h3 class="card-title">{esc(t["title"])}</h3><p class="card-summary">{esc(t.get("summary",""))}</p><div class="card-meta">{dl}{buy}</div></div>'
      h += '</div>'
    h += '</div>' + page_footer()
    self._send_html(200, h)

  def _render_team(self, q):
    conn = get_db()
    researchers = conn.execute('SELECT * FROM researchers WHERE is_active=1 ORDER BY id').fetchall()
    activists = conn.execute('SELECT * FROM community_activists WHERE is_active=1 ORDER BY sort_order').fetchall()
    conn.close()
    h = page_header('研究力量') + '<div class="container"><div class="page-header"><h1>研究力量</h1></div>'
    if researchers:
      h += '<h2>研究员团队</h2><div class="card-grid">'
      for r in researchers:
        img = f'<img src="/uploads/{esc(r["photo"])}" alt="{esc(r["name"])}">' if r.get('photo') else ''
        h += f'<div class="person-card">{img}<h3>{esc(r["name"])}</h3><p class="person-title">{esc(r.get("title",""))}</p><p>{esc(r.get("bio",""))}</p>'
        h += render_achievements(r.get('achievements',''))
        h += '</div>'
      h += '</div>'
    if activists:
      h += '<h2>社群行动者团队</h2><div class="card-grid">'
      for a in activists:
        img = f'<img src="/uploads/{esc(a["photo"])}" alt="{esc(a["name"])}">' if a.get('photo') else ''
        h += f'<div class="person-card">{img}<h3>{esc(a["name"])}</h3><p class="person-title">{esc(a.get("title",""))}</p><p>{esc(a.get("bio",""))}</p>'
        h += render_achievements(a.get('achievements',''))
        h += '</div>'
      h += '</div>'
    h += '</div>' + page_footer()
    self._send_html(200, h)

  def _render_contact(self, q):
    conn = get_db()
    email = conn.execute("SELECT value FROM site_settings WHERE key='org_email'").fetchone()
    addr = conn.execute("SELECT value FROM site_settings WHERE key='org_address'").fetchone()
    socials = conn.execute('SELECT * FROM social_links WHERE is_active=1 ORDER BY sort_order').fetchall()
    conn.close()
    h = page_header('合作与支持') + '<div class="container"><div class="page-header"><h1>合作与支持</h1></div><div class="content-body">'
    h += f'<h2>联系方式</h2><p>邮箱：<a href="mailto:{esc(email["value"] if email else "")}">{esc(email["value"] if email else "")}</a></p>'
    h += f'<p>地址：{esc(addr["value"] if addr else "")}</p>' if addr and addr['value'] else ''
    if socials:
      h += '<h2>社交媒体</h2><p>'
      for s in socials: h += f'<a href="{esc(s["url"])}" target="_blank" class="tag">{esc(s["platform"])}</a> '
      h += '</p>'
    h += '<h2>支持我们</h2><p>联系我们获取捐赠方式</p>'
    h += '</div></div>' + page_footer()
    self._send_html(200, h)

  def _render_academy(self, q):
    conn = get_db()
    courses = conn.execute('SELECT * FROM courses WHERE is_active=1 ORDER BY id').fetchall()
    conn.close()
    h = page_header('酷残学院') + '<div class="container"><div class="page-header"><h1>酷残学院</h1></div><div class="card-grid">'
    for c in courses:
      qr = f'<img src="/uploads/{esc(c["qr_code"])}" alt="二维码">' if c.get('qr_code') else ''
      url = f'<a href="{esc(c["external_url"])}" target="_blank">前往课程</a>' if c.get('external_url') else ''
      h += f'<div class="course-card">{qr}<h3>{esc(c["title"])}</h3><p>{esc(c.get("description",""))}</p><p class="person-title">{esc(c.get("instructor",""))}</p>{url}</div>'
    h += '</div></div>' + page_footer()
    self._send_html(200, h)

  def _render_search(self, q):
    kw = q.get('q', '')
    h = page_header('搜索') + '<div class="container"><div class="page-header"><h1>搜索</h1></div>'
    if not kw:
      h += '<p>请输入搜索关键词</p></div>' + page_footer()
      self._send_html(200, h); return
    conn = get_db()
    like = f'%{kw}%'
    articles = conn.execute('SELECT id,title,slug,summary,created_at,\'article\' as st FROM articles WHERE is_published=1 AND (title LIKE ? OR summary LIKE ? OR content LIKE ? OR tags LIKE ?) LIMIT 10', [like]*4).fetchall()
    reports = conn.execute('SELECT id,title,slug,summary,created_at,\'report\' as st FROM reports WHERE is_published=1 AND (title LIKE ? OR summary LIKE ? OR content LIKE ? OR tags LIKE ?) LIMIT 10', [like]*4).fetchall()
    courses = conn.execute('SELECT id,title,slug,description as summary,created_at,\'course\' as st FROM courses WHERE is_active=1 AND (title LIKE ? OR description LIKE ?) LIMIT 5', [like]*2).fetchall()
    conn.close()
    results = sorted(list(articles) + list(reports) + list(courses), key=lambda r: r['created_at'], reverse=True)
    h += f'<p>搜索 &ldquo;{esc(kw)}&rdquo; 共 {len(results)} 条结果</p><div class="card-grid">'
    for r in results:
      slug_url = f'/{r["st"]}/{esc(r["slug"])}' if r['st'] != 'course' else f'{esc(r["slug"])}'
      type_label = {'article':'文章','report':'报告','course':'课程'}.get(r['st'], r['st'])
      h += f'<article class="card"><h3 class="card-title"><a href="{slug_url}">{esc(r["title"])}</a></h3><p class="card-summary">{esc(r.get("summary",""))}</p><div class="card-meta">{type_label} | {esc(r["created_at"][:10])}</div></article>'
    h += '</div></div>' + page_footer()
    self._send_html(200, h)

  def _render_login(self, q):
    h = page_header('后台登录') + '<div class="login-form"><h1>后台登录</h1>'
    err = q.get('error', '')
    if err: h += f'<p class="login-error">{esc(err)}</p>'
    h += '<form method="post" action="/login"><label for="username">用户名</label><input type="text" id="username" name="username" required><label for="password">密码</label><input type="password" id="password" name="password" required><button type="submit">登录</button></form></div>' + page_footer()
    self._send_html(200, h)

  def _render_admin(self, q):
    h = page_header('后台管理') + '<div id="admin-app"><nav class="admin-nav"></nav><div class="admin-toolbar"><button data-action="new" class="admin-btn admin-btn-primary">+ 新增</button></div><div id="admin-table-container"></div><div id="admin-overlay-container"></div></div><script src="/static/admin.js"></script>' + page_footer()
    self._send_html(200, h)

  def _render_plan_detail(self, slug):
    conn = get_db()
    p = conn.execute('SELECT * FROM plans WHERE slug=? AND is_active=1', (slug,)).fetchone()
    conn.close()
    if not p: self._send_html(404, '<h1>404 - 计划未找到</h1>'); return
    h = page_header(p['title']) + '<div class="container"><div class="page-header"><h1>' + esc(p['title']) + '</h1></div><div class="content-body">'
    h += '<p class="plan-subtitle" style="font-size:1.1rem">' + esc(p.get('subtitle','')) + '</p>'
    h += '<div class="article-content">' + (p.get('content') or esc(p.get('description',''))) + '</div></div></div>' + page_footer()
    self._send_html(200, h)

  def _render_article_detail(self, slug):
    conn = get_db()
    a = conn.execute('SELECT * FROM articles WHERE slug=? AND is_published=1', (slug,)).fetchone()
    conn.close()
    if not a: self._send_html(404, '<h1>404 - 文章未找到</h1>'); return
    h = page_header(a['title']) + '<div class="container"><article class="content-body"><h1>' + esc(a['title']) + '</h1>'
    h += '<div class="article-meta">' + esc(a['created_at'][:10]) + ' ' + render_tags(a.get('tags','')) + '</div>'
    h += '<div>' + (a.get('content') or esc(a.get('summary',''))) + '</div></article></div>' + page_footer()
    self._send_html(200, h)

  def _render_report_detail(self, slug):
    conn = get_db()
    r = conn.execute('SELECT * FROM reports WHERE slug=? AND is_published=1', (slug,)).fetchone()
    conn.close()
    if not r: self._send_html(404, '<h1>404 - 报告未找到</h1>'); return
    h = page_header(r['title']) + '<div class="container"><article class="content-body"><h1>' + esc(r['title']) + '</h1>'
    h += '<div class="article-meta">' + esc(r['created_at'][:10]) + ' ' + render_tags(r.get('tags','')) + '</div>'
    pdf = '<a href="/uploads/' + esc(r['pdf_filename']) + '" class="tag">PDF下载</a>' if r.get('pdf_filename') else ''
    h += pdf + '<div>' + (r.get('content') or esc(r.get('summary',''))) + '</div></article></div>' + page_footer()
    self._send_html(200, h)

# === Main ===
def main():
  init_db()
  ensure_default_carousel()
  server = HTTPServer((HOST, PORT), CFIHandler)
  print(f'CFI Server running at http://{HOST}:{PORT}')
  print(f'Admin: http://{HOST}:{PORT}/login')
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    print('\nShutting down...')
    server.server_close()

if __name__ == '__main__':
  main()

