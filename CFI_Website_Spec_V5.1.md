# 酷残未来研究院（CFI）网站需求文档 V5.1

> 版本：V5.1 | 日期：2026-07-09
> 状态：定稿，待开始实现
> 基于 V5 + 首页轮播区整合一句话使命陈述 + 导航标签优化

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
首页 / → 关于 /about → 活动动态 /activities → 计划 /plans → 社群 & 学院 /community → 研究成果 /output → 合作 /contact
```

用户路径逻辑：吸引 → 了解 → 看动态 → 看项目 → 社群生态+学习 → 研究成果 → 参与支持

### 3.2 各页面内容构成

#### 首页 `/`
| 区块（从上到下） | 内容来源 | 说明 |
|------------------|----------|------|
| 轮播图 | articles + reports 中 is_featured=1 的记录 | 首屏大图轮播，图片上叠加大标题和"了解更多"链接 |
| 使命陈述 | site_settings（一行粗体大字 + 一行副标题） | 窄行居中或左对齐，一句话说清组织定位 |
| 三大行动计划 | plans 表，深色卡片区 | 3 张卡片 |
| 最新动态 | articles + reports 按时间混排，最近 6 条 | 每项标注 [新闻] / [报告] |
| 支持我们 | site_settings + 捐款引导 | CTA 导向捐款 |

**使命陈述的样式**（不是旧版两列 Hero）：
- 一行粗体大字标题（例如："用社群力量重塑未来"）
- 下方一行小字副标题（例如："由残障人发起并领导的独立民间研究机构"）
- 背景延续纸色，不做渐变或色块分割
- 上下间距 48px，不占首屏

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
| Tab（URL 参数切换） | 内容类型（report_type） | 有 PDF？ |
|---------------------|------------------------|----------|
| 研究报告 | research（含经纬计划） | ✅ |
| 翻译文章 | translation | ❌ 纯文字 |
| 手册/图书 | handbook（独立 books 表） | ✅ 下载地址/购买链接 |
| 未来扩展 | 预留 | 按需 |

- **Tab 切换方式：URL 参数**（`/output?type=research`），服务端只返回当前 Tab 数据
- **筛选方式：** Tab 切换 + 标签筛选并存
- 经纬计划产出：report_type='research' 且 tags 含"经纬计划"，不占独立 Tab

#### 研究成果详情 `/reports/<slug>`（研究报告/翻译文章）
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
| articles | 新闻/活动动态（tags 打标区分类型） | ✅ 已有，需新增轮播字段 |
| reports | 研究成果（research/translation 等） | ✅ 已有，需新增轮播字段 |
| researchers | 研究员 | ✅ 已有 |
| courses | 课程（挂在酷残学院下） | ✅ 已有 |
| founders | **发起人**（独立表） | 🆕 新增 |
| books | **手册/图书**（独立表） | 🆕 新增 |
| social_links | **社交媒体链接** | 🆕 新增 |
| community_sections | **社群页面结构化内容** | 🆕 新增 |

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
ALTER TABLE articles ADD COLUMN is_featured INTEGER DEFAULT 0;
ALTER TABLE articles ADD COLUMN featured_image TEXT DEFAULT '';
ALTER TABLE articles ADD COLUMN featured_sort_order INTEGER DEFAULT 0;

ALTER TABLE reports ADD COLUMN is_featured INTEGER DEFAULT 0;
ALTER TABLE reports ADD COLUMN featured_image TEXT DEFAULT '';
ALTER TABLE reports ADD COLUMN featured_sort_order INTEGER DEFAULT 0;
```

### 4.4 site_settings 新增默认键

```python
"mission_title": "用社群力量重塑未来",
"mission_subtitle": "由残障人发起并领导的独立民间研究机构"

# 关于页
"about_body": "（机构详细介绍文本）"
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

### 4.6 首页最新动态混排查询

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
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [Logo] 酷残未来研究院 CFI  [首页] [关于] [活动动态] [计划] [社群&学院] [研究成果] [合作] [A-] [A+] [HC] │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

- Logo（48×48）+ 中文名 + CFI
- 导航项从 navigation 表读取（默认值即为以上 7 项）
- 右侧无障碍按钮组
- sticky 吸顶，backdrop-filter: blur(12px)，底色 rgba(255,248,237,0.9)
- 激活态：底部 3px 橙色实线 + 橙色文字

#### 5.1.2 页脚

- 背景 #17130F，文字 #FFF8ED，链接 #DF4A16
- 机构信息 + 联系方式 + 后台入口

#### 5.1.3 无障碍控制

- 字体缩放三档（--font-scale: 1 / 1.25 / 1.5）
- 高对比度模式（.high-contrast class 覆盖颜色变量）
- localStorage 持久化
- Skip Link（focus 时可见）

### 5.2 首页 `/`

#### 轮播区（首屏）
- 多张图片自动轮播（纯 CSS + 少量 JS）
- 每张图片上叠加标题文字 + "了解更多"链接
- 点击跳转到对应文章/报告详情页
- **后台操作**：文章/报告编辑页面设置"在首页轮播"开关 + 上传轮播图（建议 16:9 宽幅） + 排序序号

#### 使命陈述区
- 一行粗体大标题（site_settings mission_title）
- 一行副标题（site_settings mission_subtitle）
- 窄行居中或左对齐，纸色背景，无额外装饰
- 上下 padding 48px

#### 三大计划（深色背景区 #17130F）
- 三张卡片（编号 + 标题 + 副标题 + 描述摘要）
- 点击进 /plans/<slug>

#### 最新动态
- articles + reports UNION 按 created_at 取最近 6 条
- 每项：日期（Courier New）| [新闻] / [报告] 标签 | 标题
- 底部「查看全部动态 →」（跳转 /activities）

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

### 5.6 计划详情 `/plans/<slug>`

完整描述 + 外部链接 + 关联产出列表。

### 5.7 社群 & 学院 `/community`

四个区域，数据来自 community_sections 表：
- 社群行动者
- 社群研究招募
- 社群学习资源
- 酷残学院入口卡片

### 5.8 酷残学院 `/academy`

课程列表，课程详情 `/academy/<slug>`。

### 5.9 研究成果 `/output`

- URL 参数切换 Tab：`/output?type=research` / `?type=translation` / `?type=handbook` / `?type=all`
- 当前 Tab 下可按标签筛选
- 每项展示标题、摘要、标签、日期、PDF下载（如有）

### 5.10 手册/图书详情 `/books/<slug>`

封面图 + 书名 + 作者 + 推荐语 + 购买链接 + 下载按钮。

### 5.11 合作 `/contact`

- 联系邮箱
- 志愿者招募入口
- 社交媒体链接列表（social_links 表）
- 支持/捐助信息

---

## 六、后台管理系统

### 6.1 管理模块

| 模块 | 管理对象 | 说明 |
|------|----------|------|
| 网站设置 | site_settings | 所有键值对编辑（含使命陈述、关于正文等） |
| 导航菜单 | navigation | 增删改排序 |
| 三大计划 | plans | 增删改 |
| 研究成果 | reports | 增删改，含 PDF 上传 + 轮播设置 |
| 新闻/活动 | articles | 增删改，含轮播设置 |
| 研究员 | researchers | 增删改，含照片上传 |
| 发起人 | founders | 增删改，含照片上传 + 排序 |
| 手册/图书 | books | 增删改，含封面上传 + 排序 |
| 酷残学院课程 | courses | 增删改，含二维码上传 |
| 社群页面 | community_sections | 编辑四个区域内容 |
| 社交媒体 | social_links | 增删改 + 排序 |
| 文件管理 | uploads | 浏览/删除上传文件 |

### 6.2 管理面板左侧导航顺序

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
    ├── LOGO.jpg
    ├── brand-reference.jpg
    └── concept-image.jpg
```

---

## 十、部署配置

### 环境变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| CFI_ENV | development | 运行环境 |
| CFI_HOST | 127.0.0.1 | 监听地址 |
| CFI_PORT | 7010 | 监听端口 |
| CFI_ADMIN_USER | admin | 管理员用户 |
| CFI_ADMIN_PASSWORD | cfi2026 | 管理员密码 |
| CFI_SECRET | 自动生成 | Session 密钥 |

### Nginx 反向代理 + systemd 服务

与 V3 配置一致，无变化。

---

## 十一、未来迭代

| 功能 | 说明 |
|------|------|
| 英文版本 | 同一套结构，完整双语 |
| 全站搜索 | 覆盖新闻 + 研究成果 + 课程 |
| SEO 优化 | OG 标签、sitemap.xml |
| 上传预览 | 后台图片预览 |
| 新一级页面 | 数据结构已预留（新增 navigation 记录 + 新表即可） |

---

## 十二、验收标准

### 12.1 功能验收

- [ ] 7 个一级页面 + 所有详情页正常渲染
- [ ] 首页轮播图正常展示且可点击跳转
- [ ] 使命陈述区正确显示大标题+副标题
- [ ] 首页最新动态 = 新闻+报告按时间混排（UNION）
- [ ] 研究成果页 Tab 切换 + 标签筛选并存（URL 参数）
- [ ] 关于页五人区完整（机构/计划/学院/发起人/研究员）
- [ ] 发起人管理（founders 表）可 CRUD
- [ ] 手册/图书管理（books 表）可 CRUD + 封面上传
- [ ] 社交媒体链接后台可编辑排序
- [ ] 社群页面内容通过 community_sections 管理
- [ ] 文章/报告可设置首页轮播
- [ ] 所有后台模块可 CRUD
- [ ] PDF 上传下载

### 12.2 视觉验收

- [ ] 橙色仅限规范允许场景
- [ ] 等宽字体用于标签/日期/编号
- [ ] 深色区块正确渲染
- [ ] 4px 粗边框分隔区块
- [ ] 研究员圆形照片裁切
- [ ] 毛玻璃导航栏
- [ ] 页脚深色背景

### 12.3 无障碍验收

- [ ] WCAG 2.1 AA 对比度达标
- [ ] Skip Link 可见可用
- [ ] 键盘可操作
- [ ] Focus 样式可见
- [ ] 字体缩放三档覆盖全站
- [ ] 高对比度模式覆盖全站

### 12.4 部署验收

- [ ] python app.py 直接启动
- [ ] 零第三方依赖
- [ ] Nginx + systemd 正常工作

---

> **文档结束**
> V5.1 — 结构定稿，可开始实现。
