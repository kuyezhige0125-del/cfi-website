# 酷残未来研究院（CFI）网站需求文档 V5.2

> 版本：V5.2 | 日期：2026-07-09
> 状态：定稿，待开始实现
> 基于 V5.1 + 6 项结构问题最终确认

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

## 二、视觉设计系统（与 V5.1 一致）

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
| 新闻 | 团队合作发布、招募公告、发起人参加外部活动 | articles 表（不加"活动"标签） |
| 活动动态 | 研究院自主举办的活动（读书会、沙龙、工作坊等） | articles 表（tags 含"活动"或"读书会"） |
| 读书会回顾 | 读书会的文字回顾记录 | articles 表（tags 含"读书会"→自动归入活动动态） |

**首页"最新动态"混排以上所有类型 + 研究成果。**

### 3.3 各页面内容构成

#### 首页 `/`
| 区块（从上到下） | 内容来源 | 说明 |
|------------------|----------|------|
| 轮播图 | articles + reports 中 is_featured=1 的记录 | 首屏大图轮播，图片上叠加大标题和"了解更多"链接 |
| 使命陈述 | site_settings（一行粗体大字 + 一行副标题） | 窄行居中或左对齐，纸色背景 |
| 三大行动计划 | plans 表，深色卡片区 | 3 张卡片 |
| 最新动态 | articles + reports 按时间混排，最近 6 条 | 每项标注 [新闻] / [活动] / [报告] 标签 |
| 支持我们 | site_settings | 文字指引"联系我们获取捐赠方式"，无图片/外链 |

**使命陈述的样式：**
- 一行粗体大字标题（如："用社群力量重塑未来"）
- 下方一行副标题（如："由残障人发起并领导的独立民间研究机构"）
- 纸色背景，无渐变/色块分割
- 上下间距 48px，不占首屏

**支持我们的样式：**
- 标题 + 一段说明文字
- 不做二维码、不做外链按钮
- 仅文字引导："如您有意支持我们的工作，请联系……"

#### 关于 `/about`
| 区块（从上到下） | 内容来源 |
|------------------|----------|
| 机构介绍 | site_settings（ about_body ） |
| 三大计划简介 | plans 表，带跳转链接 /plans/xxx |
| 社群学习/酷残学院简介 | site_settings（ academy_intro ），带跳转 /academy |
| 团队介绍（发起人） | founders 表，照片+姓名+头衔+简介 |
| 研究员名录 | researchers 表，卡片网格 |

区块之间 4px 粗边框分隔。

#### 活动动态 `/activities`
- articles 表中 **tags 含"活动"或"读书会"** 的记录
- 按 created_at 时间倒序
- 分页，每页 10 条
- 每项：日期（Courier New）+ 标题 + 摘要截断
- 读书会回顾自然出现在此

#### 计划 `/plans`
- 三大计划卡片展示
- 点击进详情 `/plans/<slug>`

#### 计划详情 `/plans/<slug>`
- 完整描述 + 外部链接（如有）
- 关联研究成果自动列出（通过标签匹配）

#### 社群 & 学院 `/community`
| 区域 | 内容 | 数据来源 |
|------|------|----------|
| 社群行动者 | 结构化人物/介绍列表 | community_sections |
| 社群研究招募 | 结构化招募信息 | community_sections |
| 社群学习资源 | 结构化资源链接列表 | community_sections |
| 酷残学院入口 | 入口卡片 → /academy | 静态/配置 |

#### 酷残学院 `/academy`
- 独立页面，课程列表
- 课程详情 `/academy/<slug>`

#### 研究成果 `/output`
| Tab（URL 参数切换） | 内容来源 | 有 PDF？ |
|---------------------|----------|----------|
| 全部（默认） | 所有类型混排 | — |
| 研究报告 | reports 表 report_type='research' | ✅ |
| 翻译文章 | reports 表 report_type='translation' | ❌ 纯文字 |
| 手册/图书 | books 表 | ✅ 下载/购买链接 |
| 未来扩展 | 预留 | 按需 |

**关键变化：**
- 默认 Tab 为「全部」（`/output` → `type=all`）
- **经纬计划产出不再是独立类目**，全部归为"研究报告"（report_type='research'），在正文中标注即可
- **读书会回顾不再在研究成果页**，移至活动动态页（articles 表）
- Tab 切换：URL 参数 + 服务端渲染
- 筛选：Tab 切换 + 标签筛选并存

#### 研究成果详情 `/reports/<slug>`
- 标题 + 日期 + 标签 + 正文
- PDF 下载（如有）
- 翻译文章额外显示：译者、原文链接（如有）

#### 手册/图书详情 `/books/<slug>`
- 封面图 + 书名 + 作者 + 推荐语 + 购买链接 + 下载按钮

#### 合作 `/contact`
- 联系邮箱
- **（已取消：志愿者招募入口）**
- 社交媒体链接（social_links 表，后台可编辑）
- 支持/捐助信息（文字说明，指向联系获取方式）

---

## 四、数据库设计

### 4.1 表结构总览

| 表名 | 说明 | 状态 |
|------|------|------|
| site_settings | 网站键值配置 | ✅ 已有 |
| navigation | 导航菜单 | ✅ 已有 |
| plans | 三大计划 | ✅ 已有 |
| articles | 新闻 + 活动动态 + 读书会回顾（tags 打标区分） | ✅ 已有，需新增轮播字段 |
| reports | 研究成果（research / translation） | ✅ 已有，需新增轮播字段 |
| researchers | 研究员 | ✅ 已有 |
| courses | 课程（挂在酷残学院下） | ✅ 已有 |
| founders | 发起人（独立表） | 🆕 新增 |
| books | 手册/图书（独立表） | 🆕 新增 |
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
-- articles：首页轮播支持
ALTER TABLE articles ADD COLUMN is_featured INTEGER DEFAULT 0;
ALTER TABLE articles ADD COLUMN featured_image TEXT DEFAULT '';
ALTER TABLE articles ADD COLUMN featured_sort_order INTEGER DEFAULT 0;

-- reports：首页轮播支持 + 翻译文章扩展
ALTER TABLE reports ADD COLUMN is_featured INTEGER DEFAULT 0;
ALTER TABLE reports ADD COLUMN featured_image TEXT DEFAULT '';
ALTER TABLE reports ADD COLUMN featured_sort_order INTEGER DEFAULT 0;
ALTER TABLE reports ADD COLUMN translator TEXT DEFAULT '';
ALTER TABLE reports ADD COLUMN source_url TEXT DEFAULT '';
```

### 4.4 site_settings 新增默认键

```python
# 首页
"mission_title": "用社群力量重塑未来",
"mission_subtitle": "由残障人发起并领导的独立民间研究机构",
"support_body": "如您有意支持我们的工作，请联系我们获取捐赠方式。",

# 关于页
"about_body": "（机构详细介绍文本）",
"academy_intro": "（酷残学院简介文本）",
```

### 4.5 首页轮播查询

```sql
SELECT id, title, slug, featured_image, featured_sort_order, 'article' AS content_type
FROM articles WHERE is_featured=1 AND is_published=1
UNION ALL
SELECT id, title, slug, featured_image, featured_sort_order, 'report' AS content_type
FROM reports WHERE is_featured=1 AND is_published=1
ORDER BY featured_sort_order ASC;
```

### 4.6 首页最新动态查询

```sql
SELECT id, title, slug, created_at, 'article' AS content_type, tags
FROM articles WHERE is_published=1
UNION ALL
SELECT id, title, slug, created_at, 'report' AS content_type, tags
FROM reports WHERE is_published=1
ORDER BY created_at DESC LIMIT 6;
```

**前端标签显示逻辑：**
- content_type='article' 且 tags 含"活动"→ 显示 `[活动]`
- content_type='article' 且 tags 不含"活动"→ 显示 `[新闻]`
- content_type='report' → 显示 `[报告]`

### 4.7 活动动态页查询

```sql
SELECT * FROM articles
WHERE is_published=1
  AND (tags LIKE '%活动%' OR tags LIKE '%读书会%')
ORDER BY created_at DESC;
```

---

## 五、前台页面详细设计

### 5.1 全局组件

#### 5.1.1 顶部导航栏（sticky）

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [Logo] 酷残未来研究院 CFI  [首页] [关于] [活动动态] [计划] [社群&学院] [研究成果] [合作] [A-] [A+] [HC] │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

- Logo（48×48）+ 中文名 + CFI
- 导航项从 navigation 表读取
- 右侧无障碍按钮组
- sticky 吸顶，backdrop-filter: blur(12px)，底色 rgba(255,248,237,0.9)
- 激活态：底部 3px 橙色实线 + 橙色文字

#### 5.1.2 页脚

- 背景 #17130F，文字 #FFF8ED，链接 #DF4A16
- 机构信息（中+英）+ 联系邮箱 + 后台入口

#### 5.1.3 无障碍控制

| 功能 | 实现 |
|------|------|
| 字体缩放三档 | CSS var --font-scale: 1 / 1.25 / 1.5 |
| 高对比度模式 | body class .high-contrast |
| 持久化 | localStorage |
| Skip Link | 页面顶部，focus 时可见 |

### 5.2 首页 `/`

#### 轮播区（首屏）
- 全屏宽度，固定高度 400px（移动端 250px）
- 自动轮播，底部指示器圆点 + 左右箭头
- 每张图片左下角叠加标题文字 + "了解更多"链接
- 点击跳转到对应内容详情页
- **后台操作**：编辑文章/报告时设置"在首页轮播"开关 + 上传轮播图（建议 16:9）+ 排序序号
- 不足 2 张时仍正常显示（单张不轮播）

#### 使命陈述区
- 一行粗体大标题（mission_title）
- 一行副标题（mission_subtitle）
- 窄行，纸色背景，上下 padding 48px

#### 三大计划（深色背景区 #17130F）
- 三张卡片（编号 + 标题 + 副标题 + 描述摘要）
- 点击进 /plans/<slug>

#### 最新动态
- 最近 6 条混排
- 每项：日期（Courier New）+ `[新闻]` / `[活动]` / `[报告]` 标签 + 标题
- 底部「查看全部动态 →」（跳转 /activities）

#### 支持我们
- 标题 + 说明文字
- **仅文字引导**：不显示二维码、不做外链按钮
- 如："如您有意支持我们的工作，请联系 contact@crippingfuture.org"

### 5.3 关于 `/about`

区块从上到下，4px 粗边框分隔：
1. 机构介绍
2. 三大计划简介卡片
3. 社群学习/酷残学院简介 → /academy
4. 发起人（founders 表，照片+姓名+头衔+简介）
5. 研究员名录（researchers 卡片网格，圆形照片）

### 5.4 活动动态 `/activities`

- articles 表中 tags 含"活动"或"读书会"的记录
- 时间倒序，分页 10 条/页
- 每项：日期（Courier New）+ 标题 + 摘要

### 5.5 计划 `/plans`

三大计划卡片，详情 `/plans/<slug>`。

### 5.6 计划详情 `/plans/<slug>`

完整描述 + 外部链接 + 关联产出。

### 5.7 社群 & 学院 `/community`

四个区域（community_sections）：
- 社群行动者
- 社群研究招募
- 社群学习资源
- 酷残学院入口卡片 → /academy

### 5.8 酷残学院 `/academy`

课程列表，详情 `/academy/<slug>`。

### 5.9 研究成果 `/output`

- 默认显示全部（type=all）
- Tab 行：全部 | 研究报告 | 翻译文章 | 手册/图书 | 未来扩展
- 当前 Tab 下可按标签筛选
- 每项：标题 + 摘要 + 标签（Courier New）+ 日期 + PDF 下载（如有）

### 5.10 研究成果详情 `/reports/<slug>`

- 标题 + 日期 + 标签
- 完整正文
- PDF 下载（如有）
- 翻译文章额外显示：译者、原文链接

### 5.11 手册/图书详情 `/books/<slug>`

封面图 + 书名 + 作者 + 推荐语 + 购买链接 + 下载按钮。

### 5.12 合作 `/contact`

- 联系邮箱
- 社交媒体链接（social_links 表）
- 支持/捐助文字说明

---

## 六、后台管理系统

### 6.1 管理模块

| 模块 | 管理对象 | 说明 |
|------|----------|------|
| 网站设置 | site_settings | 所有键值对编辑 |
| 导航菜单 | navigation | 增删改排序 |
| 三大计划 | plans | 增删改 |
| 研究成果 | reports | 增删改，含 PDF/图片上传 + 轮播设置 + 译者字段 |
| 新闻/活动 | articles | 增删改，含轮播设置（通过 tags 区分新闻/活动） |
| 研究员 | researchers | 增删改，含照片上传 |
| 发起人 | founders | 增删改，含照片上传 + 排序 |
| 手册/图书 | books | 增删改，含封面上传 + 排序 |
| 酷残学院课程 | courses | 增删改，含二维码上传 |
| 社群页面 | community_sections | 编辑四个区域内容 |
| 社交媒体 | social_links | 增删改 + 排序 |
| 文件管理 | uploads | 浏览/删除上传文件 |

### 6.2 管理面板导航顺序

```
网站设置 | 导航菜单 | 三大计划 | 研究成果 | 新闻/活动
手册/图书 | 研究员 | 发起人 | 酷残学院课程
社群页面 | 社交媒体 | 文件管理
```

### 6.3 API 接口

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
- 语义化 HTML（h1-h6, nav, main, footer, article, section）
- 键盘可导航
- 字体缩放三档（CSS var + JS）
- 高对比度模式
- localStorage 持久化
- Focus 样式（2px outline + 2px offset）

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
| 全站搜索 | 覆盖新闻 + 活动 + 研究成果 + 课程 |
| SEO 优化 | OG 标签、sitemap.xml |
| 上传预览 | 后台图片预览 |
| 新一级页面 | 数据结构已预留 |

---

## 十一、验收标准

### 11.1 功能验收

- [ ] 7 个一级页面 + 所有详情页正常渲染
- [ ] 首页轮播图正常展示 + 可点击跳转
- [ ] 使命陈述区正确显示
- [ ] 首页最新动态 = articles + reports 按时间 UNION 混排，标注正确类型标签
- [ ] 活动动态页仅显示 tags 含"活动"/"读书会"的 articles
- [ ] 研究成果页默认「全部」，Tab 切换 + 标签筛选正常
- [ ] 研究成果详情页：报告有 PDF，翻译文章显示译者
- [ ] 关于页五个区块完整
- [ ] 发起人管理（founders）CRUD
- [ ] 手册/图书管理（books）CRUD + 封面上传
- [ ] 社交媒体后台可编辑排序
- [ ] 社群页面内容通过 community_sections 管理
- [ ] 文章/报告可设置首页轮播
- [ ] 所有后台模块 CRUD
- [ ] 文件上传下载

### 11.2 视觉验收

- [ ] 橙色严格按规范使用
- [ ] 等宽字体用于标签/日期/编号
- [ ] 深色区块正确渲染
- [ ] 4px 粗边框分隔区块
- [ ] 毛玻璃导航栏
- [ ] 研究员圆形照片裁切

### 11.3 无障碍验收

- [ ] WCAG 2.1 AA 对比度
- [ ] Skip Link
- [ ] 键盘可导航
- [ ] Focus 样式
- [ ] 字体缩放三档
- [ ] 高对比度模式

### 11.4 部署验收

- [ ] python app.py 直接启动
- [ ] 零第三方依赖
- [ ] Nginx + systemd

---

> **文档结束**
> V5.2 — 全部需求细节确认完毕。
