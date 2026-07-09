# 酷残未来研究院（CFI）网站需求文档 V5.3

> 版本：V5.3 | 日期：2026-07-09
> 状态：定稿，待开始实现
> 基于 V5.2 + 最终 3 项确认 + 首页标签逻辑 bug 修复

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

### 1.3 品牌视觉调性关键词

- 学术感 — 严谨但不刻板
- 社群感 — 有温度、有生命力
- 酷残/Crip — 去污名化、边缘叙事、DIY 研究气质
- 克制 — 不商业化、不过度设计

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

### 3.1 导航结构（7 项）

```
首页 / → 关于 /about → 活动动态 /activities → 计划 /plans → 社群 & 学院 /community → 研究成果 /output → 合作 /contact
```

用户路径逻辑：吸引 → 了解 → 看动态 → 看项目 → 社群生态+学习 → 研究成果 → 参与支持

### 3.2 关键术语定义

| 术语 | 定义 | 存储位置 |
|------|------|----------|
| 新闻 | 团队合作发布、招募公告、发起人参加外部活动 | articles 表（tags 不含"活动"或"读书会"） |
| 活动动态 | 研究院自主举办的活动（读书会、沙龙、工作坊等） | articles 表（tags 含"活动"或"读书会"） |
| 读书会回顾 | 读书会的文字回顾记录 | articles 表（tags 含"读书会"→自动归入活动动态） |
| 研究报告 | 正式学术/社群研究报告 | reports 表 report_type='research' |
| 翻译文章 | 研究员翻译的海外文献 | reports 表 report_type='translation' |
| 手册/图书 | 工具书、手册、出版物 | books 表 |

### 3.3 各页面内容构成

#### 首页 `/`
| 区块（从上到下） | 内容来源 | 说明 |
|------------------|----------|------|
| 轮播图 | articles + reports 中 is_featured=1 的记录 | 首屏大图轮播，图片上叠加大标题和"了解更多"链接 |
| 使命陈述 | site_settings（一行粗体大字 + 一行副标题） | 窄行居中或左对齐，纸色背景 |
| 三大行动计划 | plans 表，深色卡片区 | 3 张卡片 |
| 最新动态 | articles + reports 按时间混排，最近 6 条 | 每项标注 [新闻] / [活动] / [报告] |
| 支持我们 | site_settings | 文字指引联系获取捐赠方式 |

**首页标签显示逻辑（已修复）：**
```
content_type='article' AND tags 含"活动"或"读书会" → [活动]
content_type='article' AND tags 不含"活动"且不含"读书会" → [新闻]
content_type='report' → [报告]
```

#### 关于 `/about`
| 区块（从上到下） | 内容来源 |
|------------------|----------|
| 机构介绍 | site_settings（about_body） |
| 三大计划简介 | plans 表，带跳转链接 /plans/xxx |
| 社群学习/酷残学院简介 | site_settings（academy_intro），带跳转 /academy |
| 团队介绍（发起人） | founders 表，照片+姓名+头衔+简介 |
| 研究员名录 | researchers 表，卡片网格 |

区块之间 4px 粗边框分隔。

#### 活动动态 `/activities`
- articles 表中 tags 含"活动"或"读书会"的记录
- 时间倒序，分页每页 10 条
- 每项：日期（Courier New）+ 标题 + 摘要截断

#### 计划 `/plans`
- 三大计划卡片展示
- 详情 `/plans/<slug>`

#### 计划详情 `/plans/<slug>`
- 完整描述 + 外部链接（如有）
- 关联研究成果列表（相同标签）

#### 社群 & 学院 `/community`
| 区域 | 数据来源 |
|------|----------|
| 社群行动者 | community_sections |
| 社群研究招募 | community_sections |
| 社群学习资源 | community_sections |
| 酷残学院入口卡片 → /academy | 静态/配置 |

#### 酷残学院 `/academy`
- 课程列表
- 课程详情 `/academy/<slug>`

#### 研究成果 `/output`
- 默认显示「全部」（type=all）
- Tab 行：全部 | 研究报告 | 翻译文章 | 手册/图书 | 未来扩展

**「全部」Tab 的展示方式（分两区）：**
```
┌─ 上半区 ─────────────────────────────────┐
│ 研究报告 / 翻译文章（reports 表）         │
│ ┌─ 卡片列表 ──────────────────────────┐ │
│ │ 标题 | 摘要 | 标签 | 日期 | PDF下载 │ │
│ └────────────────────────────────────┘ │
├─ 下半区 ─────────────────────────────────┤
│ 手册 / 图书（books 表）                  │
│ ┌─ 卡片列表 ──────────────────────────┐ │
│ │ 封面小图 | 书名 + 作者 | 推荐语 | 链接 │ │
│ └────────────────────────────────────┘ │
└──────────────────────────────────────────┘
```

**非全部 Tab 时**：只显示对应类型，单区列表。

#### 研究成果详情 `/reports/<slug>`
- 标题 + 日期 + 标签
- 完整正文
- PDF 下载（如有）
- 翻译文章额外显示：译者、原文链接

#### 文章详情 `/articles/<slug>`
- 标题 + 日期
- 完整正文
- **底部：相关报告列表**（相同标签的 reports，最多 3 条）
  - 如标题 "延伸阅读" 或 "相关研究成果"
  - 仅在有匹配时显示

#### 手册/图书详情 `/books/<slug>`
- 封面图 + 书名 + 作者 + 推荐语 + 购买链接 + 下载按钮

#### 合作 `/contact`
- 联系邮箱
- 社交媒体链接（social_links 表）
- 支持/捐助文字说明

---

## 四、数据库设计

### 4.1 表结构总览

| 表名 | 说明 | 状态 |
|------|------|------|
| site_settings | 网站键值配置 | ✅ 已有 |
| navigation | 导航菜单 | ✅ 已有 |
| plans | 三大计划 | ✅ 已有 |
| articles | 新闻 + 活动动态 + 读书会回顾（tags 打标区分） | ✅ 已有，需新增字段 |
| reports | 研究成果（research / translation） | ✅ 已有，需新增字段 |
| researchers | 研究员 | ✅ 已有 |
| courses | 课程 | ✅ 已有 |
| founders | 发起人 | 🆕 新增 |
| books | 手册/图书 | 🆕 新增 |
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

#### books
```sql
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
-- articles
ALTER TABLE articles ADD COLUMN is_featured INTEGER DEFAULT 0;
ALTER TABLE articles ADD COLUMN featured_image TEXT DEFAULT '';
ALTER TABLE articles ADD COLUMN featured_sort_order INTEGER DEFAULT 0;

-- reports
ALTER TABLE reports ADD COLUMN is_featured INTEGER DEFAULT 0;
ALTER TABLE reports ADD COLUMN featured_image TEXT DEFAULT '';
ALTER TABLE reports ADD COLUMN featured_sort_order INTEGER DEFAULT 0;
ALTER TABLE reports ADD COLUMN translator TEXT DEFAULT '';
ALTER TABLE reports ADD COLUMN source_url TEXT DEFAULT '';
```

### 4.4 site_settings 默认键

```python
{
    # 首页
    "mission_title": "用社群力量重塑未来",
    "mission_subtitle": "由残障人发起并领导的独立民间研究机构",
    "support_body": "如您有意支持我们的工作，请联系我们获取捐赠方式。",
    # 关于页
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
SELECT * FROM reports
WHERE is_published=1
  AND (tags LIKE '%标签A%' OR tags LIKE '%标签B%')
  -- 取文章 tags 的每个分词逐一 match
ORDER BY created_at DESC LIMIT 3;
```

---

## 五、前台页面详细设计

### 5.1 全局组件

#### 顶部导航栏（sticky）

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [Logo] 酷残未来研究院 CFI  [首页] [关于] [活动动态] [计划] [社群&学院] [研究成果] [合作] [A-] [A+] [HC] │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

- Logo 48×48 + 中文名 + CFI
- 导航项来自 navigation 表
- sticky 吸顶，backdrop-filter: blur(12px)，底色 rgba(255,248,237,0.9)
- 激活态：底部 3px 橙色实线 + 橙色文字
- 移动端：汉堡菜单 + 滑出侧栏

#### 页脚
- 背景 #17130F，文字 #FFF8ED，链接 #DF4A16
- 机构信息 + 邮箱 + 后台入口

#### 无障碍控制
- 字体缩放三档：--font-scale: 1 / 1.25 / 1.5
- 高对比度模式：.high-contrast class
- localStorage 持久化
- Skip Link（focus 时可见）

### 5.2 首页 `/`

#### 轮播区（首屏）
- 全屏宽度，固定高度 400px（移动端 250px）
- 自动轮播 5s，鼠标悬停暂停
- 淡入淡出切换，底部指示器圆点 + 左右箭头
- 每张图左下角黑色半透明渐变叠加文字 + "了解更多"
- 不足 2 张时单张显示不轮播
- 后台：编辑文章/报告时设"在首页轮播"+上传轮播图（建议 16:9）+排序

#### 使命陈述
- mission_title（大粗体）+ mission_subtitle
- 纸色背景，上下 padding 48px

#### 三大计划（#17130F 深色区）
- 三张卡片，编号+标题+副标题+描述，点击 /plans/<slug>

#### 最新动态
- 6 条混排，标注 [新闻]/[活动]/[报告]
- 底部 "查看全部动态 →"→ /activities

#### 支持我们
- 纯文字引导，无二维码无外链按钮

### 5.3 关于 `/about`

五区块 4px 粗边框分隔。

### 5.4 活动动态 `/activities`

tags 含"活动"或"读书会"的 articles，分页 10 条。

### 5.5 计划 `/plans`

三大计划卡片，详情 `/plans/<slug>`。

### 5.6 社群 & 学院 `/community`

四区：行动者 / 招募 / 学习资源 / 学院入口。

### 5.7 酷残学院 `/academy`

课程列表，详情 `/academy/<slug>`。

### 5.8 研究成果 `/output`

- **全部 Tab：分两区** — 上 reports 下 books
- 单 Tab：仅当前类型
- 全部场景下均可按标签筛选

### 5.9 详情页

- 文章详情：底部相关报告（同标签，最多 3 条）
- 报告详情：PDF 下载 / 翻译文章译者+原文链接
- 图书详情：封面+购买/下载链接
- 计划详情：关联产出列表

### 5.10 合作 `/contact`

邮箱 + 社交媒体 + 捐助文字。

---

## 六、后台管理系统

### 6.1 技术方案：API + 前端 SPA

- **后端**：提供 RESTful JSON API（已有 `/api/admin/content` 端点）
- **前端**：`static/admin.js` + `admin.html` 通过 fetch 调用 API
- **页面不刷新**：新增/编辑/删除操作后前端更新 DOM
- **登录**：Session 认证，API 请求携带凭证

### 6.2 管理模块

| 模块 | 管理对象 | 特殊功能 |
|------|----------|----------|
| 网站设置 | site_settings | 键值表单 |
| 导航菜单 | navigation | 拖拽排序 |
| 三大计划 | plans | 增删改 |
| 研究成果 | reports | PDF/图片上传 + 轮播设置 + 译者字段 |
| 新闻/活动 | articles | 轮播设置（tags 管理区分类型） |
| 研究员 | researchers | 照片上传 |
| 发起人 | founders | 照片上传 + 排序 |
| 手册/图书 | books | 封面上传 + 排序 |
| 酷残学院课程 | courses | 二维码上传 |
| 社群页面 | community_sections | 四区编辑 |
| 社交媒体 | social_links | 增删改排序 |
| 文件管理 | uploads | 浏览/删除 |

### 6.3 管理面板导航

```
网站设置 | 导航菜单 | 三大计划 | 研究成果 | 新闻/活动
手册/图书 | 研究员 | 发起人 | 酷残学院课程
社群页面 | 社交媒体 | 文件管理
```

### 6.4 API 接口

| 端点 | 方法 | 说明 |
|------|------|------|
| /api/admin/content?type=<table> | GET | 获取列表 |
| /api/admin/content?type=<table>&id=<id> | GET | 获取单条 |
| /api/admin/content | POST | 新增/更新 |
| /api/admin/content?type=<table>&id=<id> | DELETE | 删除 |
| /api/upload | POST | 上传文件 |

---

## 七、静态资源

| 路径 | 说明 |
|------|------|
| /static/style.css | 主样式表（含高对比度） |
| /static/a11y.js | 无障碍脚本 |
| /static/admin.js | 后台管理 SPA 脚本 |
| /static/admin.html | 后台管理页面（内嵌在 app.py） |
| /static/LOGO.jpg | Logo |
| /static/brand-reference.jpg | 品牌参考图 |
| /static/concept-image.jpg | 概念布局图 |
| /static/uploads/ | 上传文件目录 |

---

## 八、无障碍设计（WCAG 2.1 AA）

- 颜色对比度 ≥ 4.5:1
- Skip Link
- 语义化 HTML
- 键盘可导航
- 字体缩放三档
- 高对比度模式
- localStorage 持久化
- Focus 样式（2px outline + 2px offset）

---

## 九、技术架构

| 项目 | 选择 |
|------|------|
| 后端 | Python 3.10+ stdlib（http.server） |
| 数据库 | SQLite |
| 前端渲染 | 服务端渲染前台 HTML |
| 后台管理 | API + 前端 SPA（admin.js） |
| Tab 切换 | URL 参数 + 服务端渲染 |
| 部署 | Linux + Nginx + systemd |
| HTTPS | Let's Encrypt |

---

## 十、未来迭代

| 功能 | 说明 |
|------|------|
| 英文版本 | 同一套结构，完整双语 |
| 全站搜索 | 新闻 + 活动 + 研究成果 + 课程 |
| SEO 优化 | OG 标签、sitemap.xml |
| 上传预览 | 后台图片预览 |

---

## 十一、验收标准

### 功能验收

- [ ] 7 个一级页面 + 所有详情页正常渲染
- [ ] 首页轮播图展示 + 跳转正常
- [ ] 首页最新动态混排 UNION，标签正确（活动/新闻/报告）
- [ ] 活动动态页仅显示 tags 含"活动"或"读书会"的 articles
- [ ] 研究成果「全部」Tab：上 reports 下 books 分两区
- [ ] 研究成果单 Tab 只显示对应类型
- [ ] 文章详情页底部显示相关报告（最多 3 条）
- [ ] 翻译文章显示译者 + 原文链接
- [ ] 关于页五区块完整
- [ ] 所有后台模块 CRUD（API + SPA）
- [ ] 文件上传下载
- [ ] 所有用户偏好持久化

### 视觉验收

- [ ] 橙色按规范使用
- [ ] 等宽字体用于标签/日期/编号
- [ ] 4px 粗边框分隔区块
- [ ] 毛玻璃导航
- [ ] 研究员圆形照片

### 无障碍验收

- [ ] WCAG 2.1 AA
- [ ] Skip Link
- [ ] 键盘可导航
- [ ] 三档字体缩放
- [ ] 高对比度模式

### 部署验收

- [ ] python app.py 启动
- [ ] 零第三方依赖
- [ ] Nginx + systemd

---

> **文档结束**
> V5.3 — 全部需求细节确认完毕，可开始实现。
