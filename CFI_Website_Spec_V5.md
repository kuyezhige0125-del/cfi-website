# 酷残未来研究院（CFI）网站需求文档 V5

> 版本：V5.0 | 日期：2026-07-09
> 状态：定稿，待开始实现
> 基于 V4 + 结构深度追问 + 首页重构

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

### 1.4 设计参考来源

| 参考站点 | 借鉴方向 |
|----------|----------|
| [Disability Visibility Project](https://disabilityvisibilityproject.com/) | 大量文本的清晰信息层级、极简排版、搜索/分类逻辑 |
| [Vera List Center](https://www.veralistcenter.org/) | 粗体大字标题 + 粗边框、模块化 Grid 布局、学术排版 |
| [Keleketla! Library](https://keleketla.org/) | 社群活力的非商业审美、去中心化内容组织 |
| [Data & Society](https://datasociety.net/) | 研究报告展示范式、研究员-出版物交叉关联、专业性体现 |

---

## 二、视觉设计系统（与 V4 一致）

### 2.1 色彩系统

```
点缀色：      #DF4A16 (橙色)   — 仅按钮/导航激活/标签链接/编号
背景色：      #FFF8ED (纸色)   — 大面积底色
深色背景：    #17130F (深褐)   — 页脚 / 深色区块
正文色：      #1A1A1A          — 正文文字
辅助灰：      #6B6B6B          — 次级文字/日期/元信息
边框色：      #2C2C2C          — 粗边框
```

橙色仅限：按钮背景、导航激活态、链接悬停态、Hero 色块区、数字/编号。

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
首页 / → 关于 /about → 活动动态 /activities → 计划 /plans → 社群 /community → 产出 /output → 合作 /contact
```

用户路径逻辑：吸引 → 了解 → 看动态 → 看项目 → 社群生态 → 研究成果 → 参与支持

### 3.2 各页面内容构成

#### 首页 `/`
| 区块（从上到下） | 内容来源 | 说明 |
|------------------|----------|------|
| 轮播图 | articles + reports 中 is_featured=1 的记录 | 多图轮播，点击进详情 |
| 最新动态 | articles + reports 按时间混排，最近 6 条 | 文字列表，每项标注 [新闻] / [报告] |
| 三大行动计划 | plans 表，深色卡片区 | 3 张卡片 |
| 支持我们 | site_settings + 捐款引导 | CTA 导向捐款 |

**首页不设 Hero 区。** 首屏即轮播图。

#### 关于 `/about`
| 区块（从上到下） | 内容来源 |
|------------------|----------|
| 机构介绍 | site_settings（ about_body ） |
| 三大计划简介 | plans 表，带跳转链接 /plans/xxx |
| 社群学习/酷残学院简介 | site_settings，带跳转链接 /academy |
| 团队介绍（发起人） | founders 表，照片+简介 |
| 研究员名录 | researchers 表，卡片网格 |

区块之间 4px 粗边框分隔。

#### 活动动态 `/activities`
- articles 列表（通过 tags 打标区分普通新闻 vs 活动回顾）
- 时间倒序，分页（每页 10 条）
- 每项：日期 + 标题 + 摘要

#### 计划 `/plans`
- 三大计划完整展示卡片
- 点击进详情 `/plans/<slug>`

#### 计划详情 `/plans/<slug>`
- 完整描述 + 外部链接（如有）
- 关联产出自动列出

#### 社群 `/community`
| 区域 | 内容 | 数据来源 |
|------|------|----------|
| 社群行动者 | 结构化人物/介绍列表 | community_sections |
| 社群研究招募 | 结构化招募信息 | community_sections |
| 社群学习资源 | 结构化资源链接列表 | community_sections |
| 酷残学院入口 | 入口卡片 → /academy | 静态/配置 |

#### 酷残学院 `/academy`
- 独立页面，课程列表
- 课程详情 `/academy/<slug>`

#### 产出 `/output`
| Tab（URL 参数切换） | 内容类型（report_type） | 有 PDF？ |
|---------------------|------------------------|----------|
| 研究报告 | research（含经纬计划） | ✅ |
| 翻译文章 | translation | ❌ 纯文字 |
| 手册/图书 | handbook（独立 books 表） | ✅ 下载地址/购买链接 |
| 未来扩展 | 预留 | 按需 |

- **Tab 切换方式：URL 参数**（`/output?type=research`），服务端只返回当前 Tab 数据
- **筛选方式：** Tab 切换 + 标签筛选并存
- 经纬计划产出：report_type='research' 且 tags 含"经纬计划"，不占独立 Tab

#### 产出详情 `/reports/<slug>`（研究报告/翻译文章）
- 标题 + 日期 + 标签 + 正文 + PDF 下载（如有）

#### 手册/图书详情
- 书名 + 作者 + 封面图 + 推荐语 + 购买链接 + 下载地址
- 独立详情页 `/books/<slug>`

#### 合作 `/contact`
- 联系邮箱
- 志愿者招募入口
- 社交媒体链接（social_links 表，后台可编辑）
- 支持/捐助信息

---

## 四、数据库设计

### 4.1 表结构总览

| 表名 | 说明 | 状态 |
|------|------|------|
| site_settings | 网站键值配置 | ✅ 已有 |
| navigation | 导航菜单 | ✅ 已有 |
| plans | 三大计划 | ✅ 已有 |
| articles | 新闻/活动动态（tags 打标区分类型） | ✅ 已有，需新增字段 |
| reports | 产出（research/translation/reading 等） | ✅ 已有，需新增字段 |
| researchers | 研究员 | ✅ 已有 |
| courses | 课程（挂在酷残学院下） | ✅ 已有 |
| founders | **发起人**（独立表） | 🆕 新增 |
| books | **手册/图书**（独立表） | 🆕 新增 |
| social_links | **社交媒体链接**（后台可编辑排序） | 🆕 新增 |
| community_sections | **社群页面结构化内容** | 🆕 新增 |

### 4.2 新增表结构

#### founders（发起人表）
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

#### books（手册/图书表）
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

#### social_links（社交媒体链接表）
```sql
CREATE TABLE social_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    platform TEXT NOT NULL,
    url TEXT NOT NULL,
    icon TEXT DEFAULT '',          -- 图标名如 'wechat' / 'weibo' / 'twitter'
    sort_order INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1
);
```

#### community_sections（社群页面内容区）
```sql
CREATE TABLE community_sections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    section_key TEXT UNIQUE NOT NULL,   -- 'activists' / 'recruitment' / 'resources'
    title TEXT NOT NULL,
    content TEXT DEFAULT '',
    sort_order INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1
);
```

### 4.3 现有表新增字段

#### articles 新增字段
```sql
-- 用于首页轮播
ALTER TABLE articles ADD COLUMN is_featured INTEGER DEFAULT 0;
ALTER TABLE articles ADD COLUMN featured_image TEXT DEFAULT '';
ALTER TABLE articles ADD COLUMN featured_sort_order INTEGER DEFAULT 0;
```

#### reports 新增字段
```sql
-- 用于首页轮播
ALTER TABLE reports ADD COLUMN is_featured INTEGER DEFAULT 0;
ALTER TABLE reports ADD COLUMN featured_image TEXT DEFAULT '';
ALTER TABLE reports ADD COLUMN featured_sort_order INTEGER DEFAULT 0;
```

### 4.4 首页轮播查询

```sql
SELECT id, title, slug, featured_image, featured_sort_order, 'article' AS content_type
FROM articles WHERE is_featured=1 AND is_published=1
UNION ALL
SELECT id, title, slug, featured_image, featured_sort_order, 'report' AS content_type
FROM reports WHERE is_featured=1 AND is_published=1
ORDER BY featured_sort_order ASC;
```

### 4.5 首页最新动态混排查询

```sql
SELECT id, title, slug, 'article' AS content_type, created_at
FROM articles WHERE is_published=1
UNION ALL
SELECT id, title, slug, 'report' AS content_type, created_at
FROM reports WHERE is_published=1
ORDER BY created_at DESC LIMIT 6;
```

---

## 五、前台页面详细设计

### 5.1 全局组件

#### 5.1.1 顶部导航栏（sticky）

```
┌────────────────────────────────────────────────────────────────────────────────┐
│ [Logo] 酷残未来研究院 CFI  [首页] [关于] [活动动态] [计划] [社群] [产出] [合作] [A-] [A+] [HC] │
└────────────────────────────────────────────────────────────────────────────────┘
```

- Logo（48×48）+ 中文名 + CFI
- 导航项从 navigation 表读取
- 右侧无障碍按钮组
- sticky 吸顶，`backdrop-filter: blur(12px)`，底色 `rgba(255,248,237,0.9)`
- 激活态：底部 3px 橙色实线 + 橙色文字

#### 5.1.2 页脚

- 背景 `#17130F`，文字 `#FFF8ED`，链接 `#DF4A16`
- 机构信息 + 联系方式 + 后台入口

#### 5.1.3 无障碍控制

- 字体缩放三档（--font-scale: 1 / 1.25 / 1.5）
- 高对比度模式（.high-contrast class）
- localStorage 持久化
- Skip Link（focus 时可见）

### 5.2 首页 `/`

#### 轮播区
- 多张图片自动轮播（CSS + 少量 JS）
- 每张图片点击 → 跳转到对应文章/报告详情页
- 图片下方或覆盖显示标题
- 后台：在文章/报告编辑页面设置"在首页轮播"开关 + 上传轮播图 + 排序序号

#### 最新动态
- 混排列表，6 条
- 每项：日期 | [新闻/报告] 标签 | 标题
- 底部「查看全部动态 →」（跳转 /activities）

#### 三大计划
- 深色背景区（#17130F）
- 三张卡片（编号 + 标题 + 副标题 + 描述）
- 点击进 /plans/<slug>

#### 支持我们
- 捐款 CTA
- 说明文字 + 联系方式

### 5.3 关于 `/about`

区块从上到下，4px 粗边框分隔：

1. **机构介绍** — site_settings about_body
2. **三大计划** — plans 简介卡片 → /plans
3. **社群学习/酷残学院** — 简介 → /academy
4. **团队（发起人）** — founders 表，每张含照片+姓名+头衔+简介
5. **研究员名录** — researchers 卡片网格（圆形照片 + 姓名 + 头衔）

### 5.4 活动动态 `/activities`

- articles 列表（tags 含"活动"标记为活动动态）
- 时间倒序，分页 10 条/页
- 每项：日期 + 标题 + 摘要

### 5.5 计划 `/plans`

三大计划卡片展示，详情 `/plans/<slug>`。

### 5.6 社群 `/community`

四个区域，数据来自 community_sections 表：
- 社群行动者
- 社群研究招募
- 社群学习资源
- 酷残学院入口卡片

### 5.7 酷残学院 `/academy`

课程列表，课程详情 `/academy/<slug>`。

### 5.8 产出 `/output`

- URL 参数切换 Tab：`/output?type=research` / `?type=translation` / `?type=handbook` / `?type=all`
- 当前 Tab 下可按标签筛选
- 每项展示标题、摘要、标签、日期、PDF下载（如有）

### 5.9 手册/图书详情 `/books/<slug>`

- 封面图（大图）
- 书名 + 作者
- 推荐语
- 购买链接按钮 + 下载按钮

### 5.10 合作 `/contact`

- 联系邮箱
- 志愿者招募入口
- 社交媒体链接列表（social_links 表）
- 支持/捐助信息

---

## 六、后台管理系统

### 6.1 新增管理模块

| 模块 | 表 | 说明 |
|------|-----|------|
| 发起人管理 | founders | 增删改 + 照片上传 + 排序 |
| 手册/图书管理 | books | 增删改 + 封面上传 + 排序 |
| 社群页面管理 | community_sections | 编辑四个区域内容 |
| 社交媒体管理 | social_links | 增删改 + 排序 |

### 6.2 现有模块新增功能

| 模块 | 新增功能 |
|------|----------|
| 文章编辑 | 新增"首页轮播"开关 + 轮播图上传 + 排序序号 |
| 报告编辑 | 新增"首页轮播"开关 + 轮播图上传 + 排序序号 |
| 网站设置 | 新增 about_body、academy_intro 等键值 |

### 6.3 管理面板左侧导航

```
网站设置 | 导航菜单 | 三大计划 | 产出/报告 | 新闻/活动
手册/图书 | 研究员 | 发起人 | 酷残学院课程
社群页面 | 社交媒体 | 文件管理
```

---

## 七、静态资源

| 路径 | 说明 |
|------|------|
| /static/style.css | 主样式表（含高对比度模式） |
| /static/a11y.js | 无障碍脚本 |
| /static/admin.js | 后台管理脚本 |
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
- Focus 可见

---

## 九、技术架构

| 项目 | 选择 |
|------|------|
| 后端 | Python 3.10+ stdlib（http.server） |
| 数据库 | SQLite |
| 前端 | 服务端渲染 HTML |
| Tab 切换 | URL 参数 + 服务端渲染 |
| 部署 | Linux + Nginx + systemd |
| HTTPS | Let's Encrypt |

---

## 十、未来迭代

| 功能 | 说明 |
|------|------|
| 英文版本 | 同一套结构，完整双语 |
| 全站搜索 | 覆盖新闻 + 报告 + 课程 |
| SEO 优化 | OG 标签、sitemap.xml |
| 上传预览 | 后台图片预览 |

---

> **文档结束**
> V5.0 — 结构定稿，可开始实现。
