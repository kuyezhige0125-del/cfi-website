# 酷残未来研究院（CFI）网站需求文档 V5.5

> 版本：V5.5 | 日期：2026-07-09
> 状态：定稿，待开始实现
> 基于 V5.4 + 新增全站搜索功能

---

## 一、项目定位与品牌调性

### 1.1 机构信息

| 字段 | 值 |
|------|-----|
| 中文全称 | 酷残未来研究院 |
| 英文全称 | Cripping Future Institute（CFI） |
| 机构性质 | 残障人发起并领导的独立民间残障研究机构 |
| 兼有职能 | 残障融合咨询与社群发展 |
| 核心理念 | 以社群发展为手段进行知识生产，以知识生产为手段推动社群发展 |
| 品牌标语 | 没有我们的参与，不要做有关我们的决定 — Nothing About Us Without Us |
| 目标受众 | 残障社群、学界研究者、政策制定者、公益行业从业者、公众 |

### 1.2 三大计划定义

| 计划 | 定位 |
|------|------|
| 蒹葭计划 | 鼓励残障者做基于自身需求和权利保障的研究 |
| 经纬计划 | 鼓励青年研究者与社群伙伴一起做研究，更加理论与结构化 |
| 拾遗计划 | 整理盲文成数字化、口述史 |

---

## 二、视觉设计系统

### 2.1 色彩系统

```
点缀色：      #DF4A16 (橙色)   — 仅按钮/导航激活/标签链接/编号
背景色：      #FFF8ED (纸色)   — 大面积底色
深色背景：    #17130F (深褐)   — 页脚 / 深色区块
正文色：      #1A1A1A          — 正文文字
辅助灰：      #6B6B6B          — 次级文字/日期/元信息
边框色：      #2C2C2C          — 粗边框
```

橙色仅限：按钮背景、导航激活态、链接悬停态、数字/编号。

### 2.2 排版

| 层级 | 字重 | 字号 | 字体 |
|------|------|------|------|
| 大标题 | Bold | clamp(2rem,4vw,3rem) | 系统无衬线 |
| 区块标题 | Bold | 1.5rem | 系统无衬线 |
| 卡片标题 | Semibold | 1.125rem | 系统无衬线 |
| 正文 | Regular | 1rem | 系统无衬线 |
| 标签/日期/编号 | Regular | 0.875rem | Courier New / 等宽 |
| 小字/脚注 | Regular | 0.75rem | 系统无衬线 |

等宽字体栈：`"Courier New","Noto Sans Mono CJK SC","Source Han Mono",monospace`

### 2.3 间距与边框

- 基础单位 8px，区块间距 64px，卡片内边距 24px
- 粗边框（4px, #2C2C2C）用于区块分隔
- 细边框（1px, #D4D0C8）用于卡片内部分隔
- 卡片悬浮上移 4px + 阴影加深

### 2.4 Logo

- `static/LOGO.jpg`，导航 48×48px，页脚 64×64px，圆形裁切

---

## 三、信息架构

### 3.1 导航结构（7 项 + 搜索框）

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [Logo] 酷残未来研究院 CFI  [首页] [关于] [活动动态] [计划] [社群&学院] [研究成果] [合作] [🔍搜索] [A-] [A+] [HC] │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

搜索框位于导航栏右侧、无障碍按钮组左侧。点击后展开为输入框，或在小屏设备上弹出全屏搜索遮罩。

### 3.2 关键术语定义

| 术语 | 定义 | 存储位置 |
|------|------|----------|
| 新闻 | 团队合作发布、招募公告、发起人参加外部活动 | articles 表（tags 不含"活动"且不含"读书会"） |
| 活动动态 | 研究院自主举办的活动 | articles 表（tags 含"活动"或"读书会"） |
| 读书会回顾 | 读书会的文字回顾记录 | articles 表（tags 含"读书会"） |
| 研究报告 | 正式学术/社群研究报告 | reports 表 report_type='research' |
| 翻译文章 | 研究员翻译的海外文献 | reports 表 report_type='translation' |
| 手册/图书 | 工具书、手册、出版物 | books 表 |
| 课程 | 酷残学院下开设的课程 | courses 表 |

### 3.3 各页面内容构成

#### 首页 `/`
| 区块（从上到下） | 内容来源 | 说明 |
|------------------|----------|------|
| 轮播图 | articles + reports 中 is_featured=1 的记录；无内容时显示 brand-reference.jpg | 首屏大图轮播 |
| 使命陈述 | site_settings（mission_title + mission_subtitle） | 窄行纸色背景 |
| 三大行动计划 | plans 表，深色卡片区 | 3 张卡片 |
| 最新动态 | articles + reports UNION 混排，最近 6 条 | 标注 [新闻] / [活动] / [报告] |
| 支持我们 | site_settings | 纯文字指引 |

**首页标签显示逻辑：**
```
content_type='article' AND tags 含"活动"或"读书会" → [活动]
content_type='article' AND 其他 → [新闻]
content_type='report' → [报告]
```

#### 关于 `/about`
| 区块 | 内容来源 |
|------|----------|
| 机构介绍 | site_settings（about_body） |
| 三大计划简介 | plans 表 → /plans/xxx |
| 社群学习/酷残学院简介 | site_settings（academy_intro）→ /academy |
| 团队介绍（发起人） | founders 表 |
| 研究员名录 | researchers 表，全部展示 |

4px 粗边框分隔。

#### 活动动态 `/activities`
- articles 表 tags 含"活动"或"读书会"的记录
- 时间倒序，分页 10 条/页

#### 计划 `/plans` + 详情 `/plans/<slug>`

#### 社群 & 学院 `/community`
四区：行动者 / 招募 / 学习资源 / 学院入口。

#### 酷残学院 `/academy` + 详情 `/academy/<slug>`

#### 研究成果 `/output`
- 默认「全部」Tab，分两区（上 reports 下 books）
- Tab 行：全部 | 研究报告 | 翻译文章 | 手册/图书 | 未来扩展
- 可按标签筛选

#### 搜索页 `/search`
详见第五章。

#### 各类详情页
- 文章详情：底部相关报告（同标签，最多 3 条）
- 报告详情：PDF 下载 / 翻译文章译者+原文链接
- 图书详情：封面 + 购买/下载链接

#### 合作 `/contact`
- 联系邮箱
- 社交媒体图标按钮（后台 social_links 表配置）
- 捐助文字说明

---

## 四、数据库设计

### 4.1 表结构总览

| 表名 | 说明 | 状态 |
|------|------|------|
| site_settings | 网站键值配置 | ✅ 已有 |
| navigation | 导航菜单 | ✅ 已有 |
| plans | 三大计划 | ✅ 已有 |
| articles | 新闻 + 活动动态 + 读书会回顾 | ✅ 已有，需新增字段 |
| reports | 研究成果（research / translation） | ✅ 已有，需新增字段 |
| researchers | 研究员 | ✅ 已有 |
| courses | 课程 | ✅ 已有 |
| founders | 发起人 | 🆕 新增 |
| books | 手册/图书 | 🆕 新增 |
| social_links | 社交媒体链接 | 🆕 新增 |
| community_sections | 社群页面结构化内容 | 🆕 新增 |

### 4.2 新增表结构

```sql
CREATE TABLE founders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    title TEXT DEFAULT '',
    bio TEXT DEFAULT '',
    photo TEXT DEFAULT '',
    sort_order INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1,
    created_at TEXT DEFAULT (datetime('now','localtime'))
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT DEFAULT '',
    summary TEXT DEFAULT '',
    cover_image TEXT DEFAULT '',
    buy_url TEXT DEFAULT '',
    download_url TEXT DEFAULT '',
    tags TEXT DEFAULT '',
    sort_order INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1,
    created_at TEXT DEFAULT (datetime('now','localtime'))
);

CREATE TABLE social_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    platform TEXT NOT NULL,
    url TEXT NOT NULL,
    icon TEXT DEFAULT '',
    sort_order INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1
);

CREATE TABLE community_sections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    section_key TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    content TEXT DEFAULT '',
    sort_order INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1
);
```

### 4.3 现有表新增字段

```sql
ALTER TABLE articles ADD COLUMN is_featured INTEGER DEFAULT 0;
ALTER TABLE articles ADD COLUMN featured_image TEXT DEFAULT '';
ALTER TABLE articles ADD COLUMN featured_sort_order INTEGER DEFAULT 0;

ALTER TABLE reports ADD COLUMN is_featured INTEGER DEFAULT 0;
ALTER TABLE reports ADD COLUMN featured_image TEXT DEFAULT '';
ALTER TABLE reports ADD COLUMN featured_sort_order INTEGER DEFAULT 0;
ALTER TABLE reports ADD COLUMN translator TEXT DEFAULT '';
ALTER TABLE reports ADD COLUMN source_url TEXT DEFAULT '';
```

### 4.4 site_settings 默认键

```python
{
    "mission_title": "用社群力量重塑未来",
    "mission_subtitle": "由残障人发起并领导的独立民间研究机构",
    "support_body": "如您有意支持我们的工作，请联系我们获取捐赠方式。",
    "about_body": "（机构详细介绍文本）",
    "academy_intro": "（酷残学院简介文本）",
    "footer_email": "contact@crippingfuture.org",
}
```

### 4.5 关键查询

**首页轮播：**
```sql
SELECT id, title, slug, featured_image, featured_sort_order, 'article' AS ct
FROM articles WHERE is_featured=1 AND is_published=1
UNION ALL
SELECT id, title, slug, featured_image, featured_sort_order, 'report' AS ct
FROM reports WHERE is_featured=1 AND is_published=1
ORDER BY featured_sort_order ASC;
```
无结果时显示默认图 `brand-reference.jpg`。

**首页最新动态：**
```sql
SELECT id, title, slug, created_at, 'article' AS ct, tags
FROM articles WHERE is_published=1
UNION ALL
SELECT id, title, slug, created_at, 'report' AS ct, tags
FROM reports WHERE is_published=1
ORDER BY created_at DESC LIMIT 6;
```

**活动动态：**
```sql
SELECT * FROM articles
WHERE is_published=1 AND (tags LIKE '%活动%' OR tags LIKE '%读书会%')
ORDER BY created_at DESC;
```

**文章相关报告：**
```sql
SELECT * FROM reports WHERE is_published=1 AND (
    tags LIKE '%标签A%' OR tags LIKE '%标签B%' OR ...
)
ORDER BY created_at DESC LIMIT 3;
```

---

## 五、搜索功能（新增）

### 5.1 搜索入口

导航栏右侧设搜索图标按钮 `🔍`。点击后：

- **桌面端：** 导航栏内展开为输入框，输入关键词后回车或点击搜索图标提交
- **移动端：** 弹出全屏遮罩，顶部为输入框 + 取消按钮，下方展示搜索建议或历史

### 5.2 搜索范围

搜索覆盖以下 4 种内容类型，每类型各有其搜索字段：

| 类型 | 数据表 | 搜索字段 | 详情页路由 |
|------|--------|----------|-----------|
| 新闻/活动 | articles | title, content, tags | /articles/<slug> |
| 研究成果 | reports | title, content, tags | /reports/<slug> |
| 手册/图书 | books | title, author, summary, tags | /books/<slug> |
| 课程 | courses | title, description, instructor | /academy/<slug> |

未来可扩展至研究员和研究计划（本版本暂不纳入）。

### 5.3 搜索路由

```
/search?q=关键词
/search?q=关键词&type=article
/search?q=关键词&type=report
/search?q=关键词&type=book
/search?q=关键词&type=course
```

- `q`：搜索关键词（必填）
- `type`：内容类型筛选（可选，不传则搜索全部类型）

### 5.4 搜索查询逻辑

使用 SQLite `LIKE` 查询（零第三方依赖）。关键词先按空格分词，每个分词独立匹配，**所有分词均命中才返回**（精确 AND 逻辑）。

```python
def search_all(db, keyword, type_filter=None):
    terms = [t.strip() for t in keyword.split() if t.strip()]
    if not terms:
        return []
    
    # 构建 WHERE 子句：每个分词必须出现在至少一个搜索字段中
    def build_where(terms, fields):
        clauses = []
        for term in terms:
            pattern = f'%{term}%'
            field_clauses = [f"{f} LIKE ?" for f in fields]
            clauses.append(f"({' OR '.join(field_clauses)})")
        return ' AND '.join(clauses), [pattern for _ in terms for _ in fields]
    
    results = []
    
    # 搜索 articles
    if not type_filter or type_filter == 'article':
        where, params = build_where(terms, ['title', 'content', 'tags'])
        rows = db.execute(f"""
            SELECT id, title, slug, created_at, 'article' AS type, 
                   SUBSTR(content, 1, 200) AS excerpt
            FROM articles WHERE is_published=1 AND {where}
            ORDER BY created_at DESC LIMIT 20
        """, params).fetchall()
        results.extend(rows)
    
    # 搜索 reports（同理）
    # 搜索 books（同理）
    # 搜索 courses（同理）
    
    # 按 created_at 排序
    results.sort(key=lambda r: r['created_at'] if r['created_at'] else '', reverse=True)
    return results
```

**搜索字段对照：**
- articles：title, content, tags
- reports：title, content, tags
- books：title, author, summary, tags
- courses：title, description, instructor

### 5.5 搜索结果页设计

```
┌─ 搜索 ─────────────────────────────────────────────┐
│                                                     │
│  🔍 [___________________关键词________________]     │
│                                                     │
│  搜索结果 共 X 条                                   │
│                                                     │
│  [全部] [新闻/活动] [研究成果] [手册/图书] [课程]    │
│  ───────────────────────────────────────────────    │
│                                                     │
│  [报告] 2026-05-20                                  │
│  无障碍就业调查报告                                 │
│  摘要：本报告基于对XX名残障者的深度访谈...          │
│  ───────────────────────────────────────────────    │
│                                                     │
│  [新闻] 2026-04-15                                  │
│  我们与XX机构达成合作                               │
│  摘要：近日，酷残未来研究院与XX机构签...            │
│  ───────────────────────────────────────────────    │
│                                                     │
│  [图书] 2026-03-01                                  │
│  残障研究入门手册                                   │
│  作者：XXX — 本书面向初入残障研究的...               │
│  ───────────────────────────────────────────────    │
│                                                     │
│  [课程] —                                           │
│  社群研究方法论                                     │
│  讲师：XXX — 本课程将介绍参与式研究方法...          │
│  ───────────────────────────────────────────────    │
│                                                     │
│  ← 上一页   第 1 页 / 共 3 页   下一页 →           │
└─────────────────────────────────────────────────────┘
```

**设计要点：**
- 搜索输入框置顶，当前关键词回填
- 结果按时间倒序混排
- 每项左侧显示类型标签（橙色 Courier New）
- 摘要截取匹配字段前 200 字符
- 类型筛选 Tab 栏（全部 + 4 种类型）
- 分页：每页 10 条
- 无结果时显示：「未找到与"关键词"相关的内容」

**类型标签显示规范：**
```
content_type='article' AND tags 含"活动"/"读书会" → [活动]
content_type='article' AND 其他 → [新闻]
content_type='report' → [报告]
content_type='book' → [图书]
content_type='course' → [课程]
```

### 5.6 搜索结果高亮

搜索结果中的关键词在标题和摘要中高亮显示：

```html
<!-- 将匹配的关键词用 <mark> 包裹 -->
<title>我们与<mark>无障碍</mark>机构达成合作</title>
```

CSS 样式：
```css
.search-highlight { background: #DF4A16; color: #fff; padding: 0 4px; border-radius: 2px; }
```

高对比度模式下：
```css
.high-contrast .search-highlight { background: #FF6B35; color: #000; }
```

### 5.7 搜索性能限制

- 每次搜索最多返回 20 条结果
- 搜索暂不包含 plans（三大计划）和 researchers（研究员）
- 使用 SQL LIKE 搜索，不依赖全文索引（零第三方依赖约束）
- 搜索延迟预期：数据量 < 1000 条时 < 100ms

---

## 六、前台页面详细设计（更新）

### 6.1 全局组件（更新）

#### 顶部导航栏（sticky）

```
┌───────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [Logo] 酷残未来研究院 CFI  [首页] [关于] [活动动态] [计划] [社群&学院] [研究成果] [合作]  [🔍]  [A-] [A+] [HC] │
└───────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

- 搜索按钮位于导航右侧、无障碍按钮组左侧
- 桌面端：点击后输入框在导航栏内展开（宽度约 200px）
- 移动端：点击后全屏遮罩，输入框置顶 + 虚拟键盘自动弹出

### 6.2 首页 `/`

轮播区（首屏）→ 使命陈述 → 三大计划 → 最新动态 → 支持我们

### 6.3-6.10 其他页面

与 V5.4 保持一致。

---

## 七、后台管理系统

### 7.1 技术方案：API + 前端 SPA

后端提供 JSON API（`/api/admin/content/*`），`admin.js` 通过 fetch 调用，页面不刷新。

### 7.2 管理模块

| 模块 | 管理对象 | 特殊功能 |
|------|----------|----------|
| 网站设置 | site_settings | 键值表单 |
| 导航菜单 | navigation | 增删改排序 |
| 三大计划 | plans | 增删改 |
| 研究成果 | reports | PDF/图片上传 + 轮播设置 + 译者/原文链接 |
| 新闻/活动 | articles | 轮播设置 + tags 管理 |
| 研究员 | researchers | 照片上传 |
| 发起人 | founders | 照片上传 + 排序 |
| 手册/图书 | books | 封面上传 + 排序 |
| 酷残学院课程 | courses | 二维码上传 |
| 社群页面 | community_sections | 四区编辑 |
| 社交媒体 | social_links | 增删改排序 + 图标下拉选择 |
| 文件管理 | uploads | 浏览/删除 |

### 7.3 API 接口

| 端点 | 方法 | 说明 |
|------|------|------|
| /api/admin/content?type=<table> | GET | 列表/单条 |
| /api/admin/content | POST | 新增/更新 |
| /api/admin/content?type=<table>&id=<id> | DELETE | 删除 |
| /api/upload | POST | 上传文件 |

---

## 八、静态资源

| 路径 | 说明 |
|------|------|
| /static/style.css | 主样式表（含高对比度） |
| /static/a11y.js | 无障碍脚本 |
| /static/admin.js | 后台管理 SPA |
| /static/admin.html | 后台页面（内嵌） |
| /static/icons/ | 社交媒体 SVG 图标 |
| /static/LOGO.jpg | Logo |
| /static/brand-reference.jpg | 默认轮播图 |
| /static/concept-image.jpg | 概念图 |
| /static/uploads/ | 上传文件 |

---

## 九、无障碍设计（WCAG 2.1 AA）

- 颜色对比度 ≥ 4.5:1
- Skip Link
- 语义化 HTML
- 键盘可导航（含搜索输入）
- 字体缩放三档
- 高对比度模式
- localStorage 持久化
- Focus 样式
- 搜索按钮有 aria-label

---

## 十、技术架构

| 项目 | 选择 |
|------|------|
| 后端 | Python 3.10+ stdlib（http.server） |
| 数据库 | SQLite（LIKE 搜索） |
| 前台渲染 | 服务端渲染 HTML |
| 后台管理 | API + 前端 SPA |
| Tab 切换 | URL 参数 + 服务端渲染 |
| 搜索 | GET 参数 + 服务端 UNION 查询 |
| 部署 | Linux + Nginx + systemd |
| HTTPS | Let's Encrypt |

### 文件结构

```
cfi-site/
├── app.py
├── .env
├── DEPLOY.md
├── README.md
├── data/
│   ├── site.db
│   └── uploads/
├── deploy/
│   ├── cfi-site.service
│   └── nginx.conf
└── static/
    ├── style.css
    ├── a11y.js
    ├── admin.js
    ├── admin.html（内嵌）
    ├── icons/
    ├── LOGO.jpg
    ├── brand-reference.jpg
    └── concept-image.jpg
```

---

## 十一、未来迭代

| 功能 | 说明 |
|------|------|
| 英文版本 | 同一套结构，完整双语 |
| SEO 优化 | OG 标签、sitemap.xml |
| 上传预览 | 后台图片预览 |

---

## 十二、验收标准

### 功能验收

- [ ] 7 个一级页面 + 所有详情页正常渲染
- [ ] 首页轮播：有内容时轮播跳转，无内容时默认图
- [ ] 首页最新动态 UNION 混排，标签正确
- [ ] 活动动态仅 tags 含"活动"/"读书会"的 articles
- [ ] 研究成果「全部」分两区（上 reports 下 books）
- [ ] 文章详情底部相关报告（最多 3 条）
- [ ] 翻译文章显示译者+原文链接
- [ ] **全站搜索**
  - [ ] 导航栏搜索按钮点击展开输入框
  - [ ] 关键词搜索覆盖 4 种内容类型
  - [ ] 类型筛选 Tab 正常切换
  - [ ] 搜索结果按时间倒序混排
  - [ ] 关键词在结果中高亮（橙色底白字）
  - [ ] 搜索结果分页（10 条/页）
  - [ ] 无结果时显示友好提示
  - [ ] 移动端全屏搜索遮罩
- [ ] 关于页五区块完整
- [ ] 所有后台模块 CRUD（API + SPA）
- [ ] 社交媒体图标按钮 + 后台配置
- [ ] 文件上传下载

### 视觉验收

- [ ] 橙色按规范使用
- [ ] 等宽字体用于标签/日期/编号
- [ ] 4px 粗边框分隔区块
- [ ] 毛玻璃导航
- [ ] 研究员圆形照片
- [ ] 社交媒体 SVG 图标
- [ ] 搜索结果高亮正确渲染

### 无障碍验收

- [ ] WCAG 2.1 AA 对比度
- [ ] Skip Link
- [ ] 键盘可导航（含搜索）
- [ ] 三档字体缩放
- [ ] 高对比度模式
- [ ] 搜索按钮 aria-label

### 部署验收

- [ ] python app.py 直接启动
- [ ] 零第三方依赖
- [ ] Nginx + systemd

---

> **文档结束**
> V5.5 — 全部需求确认完毕，含搜索功能。
