# 酷残未来研究院（CFI）网站需求文档 V5.4

> 版本：V5.4 | 日期：2026-07-09
> 状态：定稿，待开始实现
> 基于 V5.3 + 最终 4 项确认

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

### 3.2 关键术语定义

| 术语 | 定义 | 存储位置 |
|------|------|----------|
| 新闻 | 团队合作发布、招募公告、发起人参加外部活动 | articles 表（tags 不含"活动"且不含"读书会"） |
| 活动动态 | 研究院自主举办的活动 | articles 表（tags 含"活动"或"读书会"） |
| 读书会回顾 | 读书会的文字回顾记录 | articles 表（tags 含"读书会"） |
| 研究报告 | 正式学术/社群研究报告 | reports 表 report_type='research' |
| 翻译文章 | 研究员翻译的海外文献 | reports 表 report_type='translation' |
| 手册/图书 | 工具书、手册、出版物 | books 表 |

### 3.3 各页面内容构成

#### 首页 `/`
| 区块（从上到下） | 内容来源 | 说明 |
|------------------|----------|------|
| 轮播图 | articles + reports 中 is_featured=1 的记录；无内容时显示 brand-reference.jpg | 首屏大图轮播，图片上叠加大标题和"了解更多"链接 |
| 使命陈述 | site_settings（一行粗体大字 + 一行副标题） | 窄行纸色背景 |
| 三大行动计划 | plans 表，深色卡片区 | 3 张卡片 |
| 最新动态 | articles + reports UNION 混排，最近 6 条 | 每项标注 [新闻] / [活动] / [报告] |
| 支持我们 | site_settings | 纯文字指引联系获取捐赠方式 |

**首页标签显示逻辑：**
```
content_type='article' AND tags 含"活动"或"读书会" → [活动]
content_type='article' AND 其他 → [新闻]
content_type='report' → [报告]
```

#### 关于 `/about`
| 区块（从上到下） | 内容来源 |
|------------------|----------|
| 机构介绍 | site_settings（about_body） |
| 三大计划简介 | plans 表 → /plans/xxx |
| 社群学习/酷残学院简介 | site_settings（academy_intro）→ /academy |
| 团队介绍（发起人） | founders 表，照片+姓名+头衔+简介 |
| 研究员名录 | researchers 表，全部展示不截断，滚动即可 |

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

**「全部」Tab：分两区展示**
- 上半区：研究报告 + 翻译文章（reports 表，标题+摘要+标签+PDF）
- 下半区：手册/图书（books 表，封面小图+书名+作者+链接）

**单类型 Tab：** 仅显示对应类型，单区列表
**所有场景下均可按标签筛选。**

#### 研究成果详情 `/reports/<slug>`
- 标题 + 日期 + 标签
- 完整正文
- PDF 下载（如有）
- 翻译文章额外显示：译者 + 原文链接

#### 文章详情 `/articles/<slug>`
- 标题 + 日期
- 完整正文
- 底部：相关报告列表（相同标签的 reports，最多 3 条），标题如"延伸阅读"

#### 手册/图书详情 `/books/<slug>`
- 封面图 + 书名 + 作者 + 推荐语 + 购买链接 + 下载按钮

#### 合作 `/contact`
- 联系邮箱
- 社交媒体链接：**图标按钮**（SVG 图标，后台 staff 通过 social_links 表自行配置）
- 支持/捐助文字说明

---

## 四、数据库设计

### 4.1 表结构总览

| 表名 | 说明 | 状态 |
|------|------|------|
| site_settings | 网站键值配置 | ✅ 已有 |
| navigation | 导航菜单 | ✅ 已有 |
| plans | 三大计划 | ✅ 已有 |
| articles | 新闻 + 活动动态 + 读书会回顾 | ✅ 已有，需新增字段 |
| reports | 研究成果 | ✅ 已有，需新增字段 |
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
    platform TEXT NOT NULL,      -- 显示名称，如"微信公众号"
    url TEXT NOT NULL,           -- 链接地址
    icon TEXT DEFAULT '',        -- 图标标识，如 'wechat' / 'weibo' / 'twitter' / 'email'
    sort_order INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1
);
```

可用图标集合（内置 SVG，后台下拉选择）：`wechat` `weibo` `twitter` `email` `website` `github` `bilibili` `douyin` `link`

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

**首页轮播：**
```sql
SELECT id, title, slug, featured_image, featured_sort_order, 'article' AS ct
FROM articles WHERE is_featured=1 AND is_published=1
UNION ALL
SELECT id, title, slug, featured_image, featured_sort_order, 'report' AS ct
FROM reports WHERE is_featured=1 AND is_published=1
ORDER BY featured_sort_order ASC;
```
无结果时页面渲染默认图 `brand-reference.jpg`（不轮播）。

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

## 五、前台页面详细设计

### 5.1 全局组件

#### 顶部导航栏（sticky）
- Logo 48×48 + 中文名 + CFI
- 导航项来自 navigation 表
- sticky 吸顶，backdrop-filter: blur(12px)，底色 rgba(255,248,237,0.9)
- 激活态：底部 3px 橙色实线 + 橙色文字
- 移动端：汉堡菜单 + 滑出侧栏

#### 页脚
- 背景 #17130F，文字 #FFF8ED，链接 #DF4A16

#### 无障碍控制
- 字体缩放三档（--font-scale: 1 / 1.25 / 1.5）
- 高对比度模式（.high-contrast）
- localStorage 持久化
- Skip Link

### 5.2 首页 `/`

#### 轮播区（首屏）
- 全屏宽度，固定高度 400px（移动端 250px）
- 自动轮播 5s，鼠标悬停暂停
- 淡入淡出切换，底部指示器圆点 + 左右箭头
- 图片左下角黑色半透明渐变 + 标题 + "了解更多"
- **无轮播内容时**：显示 `brand-reference.jpg` 作为默认首图，不轮播

#### 使命陈述 → 三大计划 → 最新动态 → 支持我们

### 5.3 关于 `/about`

五区块 4px 粗边框分隔。研究员全部展示不截断。

### 5.4 活动动态 `/activities`

tags 含"活动"或"读书会"的 articles，分页 10 条。

### 5.5 计划 `/plans` + 详情 `/plans/<slug>`

### 5.6 社群 & 学院 `/community`

四区：行动者 / 招募 / 学习资源 / 学院入口。

### 5.7 酷残学院 `/academy`

课程列表，详情 `/academy/<slug>`。

### 5.8 研究成果 `/output`

- 全部 Tab：上 reports 下 books 分两区
- 单 Tab：仅当前类型
- 可按标签筛选

### 5.9 详情页

- 文章详情：底部相关报告（同标签，最多 3 条）
- 报告详情：PDF / 译者+原文链接
- 图书详情：封面+购买/下载链接

### 5.10 合作 `/contact`

- 邮箱 + 社交媒体图标按钮（后台配） + 捐助文字

---

## 六、后台管理系统

### 6.1 技术方案：API + 前端 SPA

后端提供 JSON API，`admin.js` 通过 fetch 调用，页面不刷新。

### 6.2 管理模块

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

### 6.3 API 接口

| 端点 | 方法 | 说明 |
|------|------|------|
| /api/admin/content?type=<table> | GET | 列表/单条 |
| /api/admin/content | POST | 新增/更新 |
| /api/admin/content?type=<table>&id=<id> | DELETE | 删除 |
| /api/upload | POST | 上传文件 |

---

## 七、静态资源

| 路径 | 说明 |
|------|------|
| /static/style.css | 主样式表（含高对比度） |
| /static/a11y.js | 无障碍脚本 |
| /static/admin.js | 后台管理 SPA |
| /static/admin.html | 后台页面（内嵌） |
| /static/icons/ | 社交媒体 SVG 图标集合 |
| /static/LOGO.jpg | Logo |
| /static/brand-reference.jpg | 默认轮播图 + 品牌参考图 |
| /static/concept-image.jpg | 概念布局图 |
| /static/uploads/ | 上传文件目录 |

### 图标集合

`/static/icons/` 下内置以下 SVG 图标，social_links 表的 icon 字段对应文件名（不含扩展名）：

```
wechat.svg  weibo.svg  twitter.svg  email.svg
website.svg  github.svg  bilibili.svg  douyin.svg
link.svg（通用链接）
```

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
| 前台渲染 | 服务端渲染 HTML |
| 后台管理 | API + 前端 SPA |
| Tab 切换 | URL 参数 + 服务端渲染 |
| 部署 | Linux + Nginx + systemd |
| HTTPS | Let's Encrypt |

### 文件结构

```
cfi-site/
├── app.py                    # 主程序
├── .env                      # 环境变量
├── DEPLOY.md                 # 部署文档
├── README.md                 # 项目说明
├── data/
│   ├── site.db              # SQLite
│   └── uploads/             # 上传文件
├── deploy/
│   ├── cfi-site.service     # systemd
│   └── nginx.conf           # Nginx
└── static/
    ├── style.css
    ├── a11y.js
    ├── admin.js
    ├── admin.html（内嵌）
    ├── icons/               # 社交媒体 SVG 图标
    ├── LOGO.jpg
    ├── brand-reference.jpg
    └── concept-image.jpg
```

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
- [ ] 首页轮播：有内容时轮播+跳转，无内容时显示默认图
- [ ] 首页最新动态 UNION 混排，标签正确
- [ ] 活动动态仅显示 tags含"活动"/"读书会"的 articles
- [ ] 研究成果「全部」分两区（上 reports 下 books）
- [ ] 文章详情底部显示相关报告
- [ ] 翻译文章显示译者+原文链接
- [ ] 关于页五区块 + 研究员全部展示
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

### 无障碍验收

- [ ] WCAG 2.1 AA 对比度
- [ ] Skip Link
- [ ] 键盘可导航
- [ ] 三档字体缩放
- [ ] 高对比度模式

### 部署验收

- [ ] python app.py 直接启动
- [ ] 零第三方依赖
- [ ] Nginx + systemd

---

> **文档结束**
> V5.4 — 全部需求细节确认完毕，可开始实现。
