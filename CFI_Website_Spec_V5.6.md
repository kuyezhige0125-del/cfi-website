# 酷残未来研究院（CFI）网站需求文档 V5.6

> 版本：V5.6 | 日期：2026-07-09
> 状态：定稿，待开始实现
> 基于 V5.5 + bug 修复 + 最终 3 项确认

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
┌───────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [Logo] 酷残未来研究院 CFI  [首页] [关于] [活动动态] [计划] [社群&学院] [研究成果] [合作]  [🔍]  [A-] [A+] [HC] │
└───────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

搜索框位于导航栏右侧、无障碍按钮组左侧。

### 3.2 关键术语定义

| 术语 | 定义 | 表 |
|------|------|-----|
| 新闻 | 团队合作发布、招募公告、发起人参加外部活动 | articles（tags 不含"活动"且不含"读书会"） |
| 活动动态 | 研究院自主举办的活动 | articles（tags 含"活动"或"读书会"） |
| 读书会回顾 | 读书会的文字回顾记录 | articles（tags 含"读书会"） |
| 研究报告 | 正式学术/社群研究报告 | reports（report_type='research'） |
| 翻译文章 | 研究员翻译的海外文献 | reports（report_type='translation'） |
| 手册/图书 | 工具书、手册、出版物 | books |
| 课程 | 酷残学院下开设的课程 | courses |

### 3.3 各页面内容构成

#### 首页 `/`
轮播图 → 使命陈述 → 三大计划（深色区） → 最新动态（6 条混排） → 支持我们

首页标签显示逻辑：
```
article + tags 含"活动"/"读书会" → [活动]
article + 其他                     → [新闻]
report                             → [报告]
```

#### 关于 `/about`
机构介绍 → 三大计划简介 → 酷残学院简介 → 发起人（founders） → 研究员名录（全部展示）

4px 粗边框分隔。

#### 活动动态 `/activities`
articles 中 tags 含"活动"或"读书会"，分页 10 条/页。

#### 计划 `/plans` + `/plans/<slug>`

#### 社群 & 学院 `/community`
社群行动者 / 社群研究招募 / 社群学习资源 / 酷残学院入口卡片。

#### 酷残学院 `/academy` + `/academy/<slug>`

#### 研究成果 `/output`
- 默认「全部」，分两区（上 reports 下 books）
- Tab：全部 | 研究报告 | 翻译文章 | 手册/图书 | 未来扩展

#### 搜索 `/search`（详见第五章）

#### 各类详情页
- 文章详情：底部相关报告（同 tags，最多 3 条）
- 报告详情：PDF、翻译文章译者+原文链接
- 图书详情：封面 + 购买/下载链接

#### 合作 `/contact`
邮箱 + 社交媒体图标按钮（后台配） + 捐助文字。

---

## 四、数据库设计

### 4.1 表结构总览

| 表名 | 说明 | 状态 |
|------|------|------|
| site_settings | 网站键值配置 | ✅ 已有 |
| navigation | 导航菜单 | ✅ 已有 |
| plans | 三大计划 | ✅ 已有 |
| articles | 新闻 + 活动动态 + 读书会回顾 | ✅ 需新增字段 |
| reports | 研究成果 | ✅ 需新增字段 |
| researchers | 研究员 | ✅ 已有 |
| courses | 课程 | ✅ 已有 |
| founders | 发起人 | 🆕 新增 |
| books | 手册/图书（含 slug） | 🆕 新增 |
| social_links | 社交媒体链接 | 🆕 新增 |
| community_sections | 社群页面结构化内容 | 🆕 新增 |

### 4.2 新增表结构

#### founders
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
```

#### books（已修复：新增 slug 字段）
```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,         -- ← 修复：新增 slug
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
```

#### social_links
```sql
CREATE TABLE social_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    platform TEXT NOT NULL,
    url TEXT NOT NULL,
    icon TEXT DEFAULT '',
    sort_order INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1
);
```

#### community_sections
```sql
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

**首页轮播（无结果时显示默认图，不轮播）：**
```sql
SELECT id, title, slug, featured_image, featured_sort_order, 'article' AS ct
FROM articles WHERE is_featured=1 AND is_published=1
UNION ALL
SELECT id, title, slug, featured_image, featured_sort_order, 'report' AS ct
FROM reports WHERE is_featured=1 AND is_published=1
ORDER BY featured_sort_order ASC;
```

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

## 五、搜索功能

### 5.1 搜索入口

导航栏右侧搜索图标按钮 `🔍`（aria-label="搜索"）。

- **桌面端：** 点击后导航栏内展开输入框（宽度约 200px），回车或点击图标提交
- **移动端：** 点击后全屏遮罩，顶部输入框 + 取消按钮

### 5.2 搜索范围

| 类型 | 表 | 搜索字段 | 摘要字段 | 详情路由 |
|------|-----|---------|---------|---------|
| 新闻/活动 | articles | title, content, tags | content（前 200 字） | /articles/<slug> |
| 研究成果 | reports | title, content, tags | content（前 200 字） | /reports/<slug> |
| 手册/图书 | books | title, author, summary, tags | summary（全文，通常不长） | /books/<slug> |
| 课程 | courses | title, description, instructor | description（全文） | /academy/<slug> |

### 5.3 搜索路由

```
/search?q=关键词                    → 全部类型
/search?q=关键词&type=article       → 仅新闻/活动
/search?q=关键词&type=report        → 仅研究成果
/search?q=关键词&type=book          → 仅手册/图书
/search?q=关键词&type=course        → 仅课程
/search                              → 空搜索页，显示搜索框 + "请输入关键词"
```

### 5.4 搜索逻辑

1. 关键词按空格分词
2. 每个分词必须至少匹配一个搜索字段（AND 逻辑）
3. 使用 SQLite `LIKE` 查询
4. **结果总数限制：最多 30 条，分 3 页展示（每页 10 条）**
5. 四种类型按时间倒序混排

### 5.5 搜索结果页设计

```
┌─ 搜索 ────────────────────────────────────────────────┐
│                                                        │
│  🔍 [___________________关键词________________]        │
│                                                        │
│  搜索结果：共 X 条                                     │
│                                                        │
│  [全部] [新闻/活动] [研究成果] [手册/图书] [课程]      │
│  ────────────────────────────────────────────────      │
│                                                        │
│  [活动]  2026-05-20                                    │
│  标题文本  ← 关键词<mark>高亮</mark>                    │
│  摘要截取前 200 字...                                   │
│  ────────────────────────────────────────────────      │
│                                                        │
│  [报告]  2026-04-15                                    │
│  标题文本                                                │
│  摘要截取前 200 字...                                   │
│  ────────────────────────────────────────────────      │
│                                                        │
│  [图书]  2026-03-01                                    │
│  标题文本                                                │
│  手册/图书用 summary 全文作为摘要                        │
│  ────────────────────────────────────────────────      │
│                                                        │
│  [课程]  —                                             │
│  课程名称                                                │
│  课程用 description 全文作为摘要                         │
│  ────────────────────────────────────────────────      │
│                                                        │
│  ← 上一页    第 1 页 / 共 N 页    下一页 →             │
└────────────────────────────────────────────────────────┘
```

### 5.6 关键词高亮

搜索结果中的标题和摘要，匹配到的关键词用 `<mark class="search-highlight">` 包裹。

```css
.search-highlight { background: #DF4A16; color: #fff; padding: 0 4px; border-radius: 2px; }
.high-contrast .search-highlight { background: #FF6B35; color: #000; }
```

### 5.7 空搜索页

访问 `/search` 不带 `?q=` 参数时：
- 显示搜索框（可输入）
- 显示「请输入关键词」提示
- 无结果列表

### 5.8 无结果状态

搜索无匹配时显示：「未找到与 "关键词" 相关的内容」
保持搜索框和类型筛选 Tab 可见，方便调整后重新搜索。

---

## 六、前台页面详情

### 6.1 全局组件

**顶部导航栏：** Logo + 导航项 + 🔍 + A− / A+ / HC。sticky 吸顶，毛玻璃效果。

**页脚：** #17130F 背景，机构信息 + 邮箱 + 后台入口。

**无障碍：** 字体缩放三档、高对比度模式、localStorage 持久化、Skip Link。

### 6.2-6.10 各页面

与 V5.5 保持一致，无变化。

---

## 七、后台管理系统

### 7.1 技术方案：API + 前端 SPA

后端提供 JSON API，admin.js 通过 fetch 调用，页面不刷新。

### 7.2 管理模块

| 模块 | 管理对象 | 特殊功能 |
|------|----------|----------|
| 网站设置 | site_settings | 键值表单 |
| 导航菜单 | navigation | 增删改排序 |
| 三大计划 | plans | 增删改 |
| 研究成果 | reports | PDF/图片上传 + 轮播设置 + 译者 |
| 新闻/活动 | articles | 轮播设置 + tags |
| 研究员 | researchers | 照片上传 |
| 发起人 | founders | 照片上传 + 排序 |
| 手册/图书 | books | 封面上传 + 排序（slug 自动生成） |
| 酷残学院课程 | courses | 二维码上传 |
| 社群页面 | community_sections | 四区编辑 |
| 社交媒体 | social_links | 增删改排序 + 图标下拉 |
| 文件管理 | uploads | 浏览/删除 |

### 7.3 API

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
| /static/style.css | 主样式表 |
| /static/a11y.js | 无障碍脚本 |
| /static/admin.js | 后台管理 SPA |
| /static/admin.html | 后台页面（内嵌） |
| /static/icons/ | 社交媒体 SVG 图标集 |
| /static/LOGO.jpg | Logo |
| /static/brand-reference.jpg | 默认轮播图 |
| /static/concept-image.jpg | 概念图 |
| /static/uploads/ | 上传文件 |

---

## 九、无障碍设计（WCAG 2.1 AA）

- 颜色对比度 ≥ 4.5:1
- Skip Link
- 语义化 HTML
- 键盘可导航（含搜索）
- 字体缩放三档
- 高对比度模式
- localStorage 持久化
- Focus 样式（2px outline + 2px offset）
- 搜索按钮 aria-label="搜索"

---

## 十、技术架构

| 项目 | 选择 |
|------|------|
| 后端 | Python 3.10+ stdlib（http.server） |
| 数据库 | SQLite（LIKE 搜索，限 30 条） |
| 前台渲染 | 服务端渲染 HTML |
| 后台管理 | API + 前端 SPA |
| Tab 切换 | URL 参数 + 服务端渲染 |
| 部署 | Linux + Nginx + systemd |
| HTTPS | Let's Encrypt |

### 文件结构

```
cfi-site/
├── app.py
├── .env
├── DEPLOY.md
├── README.md
├── data/site.db + data/uploads/
├── deploy/cfi-site.service + nginx.conf
└── static/（style.css, a11y.js, admin.js, icons/, 图片等）
```

---

## 十一、验收标准

### 功能验收

- [ ] 7 个一级页面 + 所有详情页正常渲染
- [ ] 首页轮播 + 使命陈述 + 三大计划 + 最新动态混排 + 支持我们
- [ ] 活动动态仅 tags 含"活动"/"读书会"的 articles
- [ ] 研究成果「全部」分两区（上 reports 下 books）
- [ ] 文章详情底部相关报告（同 tags，最多 3 条）
- [ ] 翻译文章显示译者 + 原文链接
- [ ] **搜索**
  - [ ] 导航栏搜索按钮展开输入框
  - [ ] 空搜索页显示"请输入关键词"
  - [ ] 关键词搜索覆盖 4 种类型（articles/reports/books/courses）
  - [ ] 类型筛选 Tab 正常切换
  - [ ] 结果按时间倒序混排，限 30 条 3 页
  - [ ] 关键词在标题和摘要中高亮
  - [ ] 无结果时友好提示
  - [ ] 移动端全屏遮罩
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
- [ ] 搜索高亮橙色底白字

### 无障碍验收

- [ ] WCAG 2.1 AA
- [ ] Skip Link
- [ ] 键盘可导航（含搜索）
- [ ] 三档字体缩放
- [ ] 高对比度模式

### 部署验收

- [ ] python app.py 直接启动
- [ ] 零第三方依赖
- [ ] Nginx + systemd

---

> **文档结束**
> V5.6 — 全部需求确认完毕，可实现。
