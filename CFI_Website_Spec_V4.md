# 酷残未来研究院（CFI）网站需求文档 V4

> 版本：V4.0 | 日期：2026-07-09
> 状态：设计定稿，待开始实现
> 基于 V3 视觉系统 + 结构深度对话定稿

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

- 学术感（Academic）— 严谨但不刻板
- 社群感（Community）— 有温度、有生命力
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
主色（点缀色）：#DF4A16 (橙色)   — 仅按钮/导航激活/标签链接/编号
背景色：        #FFF8ED (纸色)   — 大面积底色
深色背景：      #17130F (深褐)   — 页脚 / 深色区块
正文色：        #1A1A1A          — 正文文字
辅助灰：        #6B6B6B          — 次级文字 / 日期 / 元信息
边框色：        #2C2C2C          — 粗边框（学术感来源）
```

**橙色使用规范（仅限以下场景）：**
- 按钮（实心按钮背景）
- 导航栏当前激活状态
- 重要超链接悬停/激活态
- Hero 右侧色块区
- 高亮数字 / 编号

### 2.2 排版系统

| 层级 | 字重 | 字号（基准） | 字体 | 说明 |
|------|------|-------------|------|------|
| Hero 大标题 | Bold / 900 | clamp(2rem, 4vw, 3rem) | 系统无衬线 | 首页/页面主标题 |
| 区块标题 | Bold | 1.5rem | 系统无衬线 | 各区块标题 |
| 卡片标题 | Semibold | 1.125rem | 系统无衬线 | 计划/报告/新闻卡片 |
| 正文 | Regular | 1rem (16px) | 系统无衬线 | 正文段落 |
| 元信息/标签/日期/编号 | Regular | 0.875rem | Courier New / 等宽 | 标签、日期、编号 |
| 小字/脚注 | Regular | 0.75rem | 系统无衬线 | 版权/辅助信息 |

**等宽字体使用规范：**
- 字体栈：`"Courier New", "Noto Sans Mono CJK SC", "Source Han Mono", monospace`
- 使用场景：所有标签（Tags）、日期、编号（01/02/03）、页码、代码块
- 设计目的：营造"档案感"和"DIY 研究"气息，契合残障自组织的边缘叙事调性

### 2.3 间距系统

- 基础间距单位：8px
- 区块间距：64px（8 × 8）
- 卡片内边距：24px（3 × 8）
- 段落间距：16px（2 × 8）
- 列间距：32px（4 × 8）

### 2.4 边框系统

- **粗边框**（学术感来源）：区块分隔使用 4px 粗边框（颜色 `#2C2C2C`）
- **细边框**：卡片内部分隔使用 1px 边框（颜色 `#D4D0C8`）
- 卡片悬浮效果：轻微上移（-4px）+ 阴影加深

### 2.5 Logo 使用

- 文件：`static/LOGO.jpg`（圆形 Logo，中文 + 英文）
- 导航栏：48×48px，`object-fit: cover; border-radius: 50%`
- 页脚：64×64px
- 始终配套机构名称使用，不单独展示

---

## 三、信息架构（IA）

### 3.1 导航结构

一级导航（7 项，按顺序）：

```
首页 / → 关于 /about → 计划 /plans → 产出 /output → 社群 /community → 活动动态 /activities → 合作 /contact
```

### 3.2 各页面内容构成

#### 首页 `/`
| 区块 | 内容来源 |
|------|----------|
| Hero（首屏） | 标题+导语（site_settings）+ 品牌参考图 |
| 核心陈述（三列） | site_settings（关于/背景/方法论三组标题+正文） |
| 三大行动计划 | plans 表，3 张卡片 + 深色背景区 |
| 最新动态（混排） | articles + reports 按 created_at 混排，取最近 6 条 |
| 支持我们（捐款导向） | site_settings，突出捐款行动目标 |

#### 关于 `/about`
| 区块 | 内容 |
|------|------|
| 机构介绍 | 正文（site_settings） |
| 三大计划简介 | plans 表的简介卡片（点击跳转 /plans/xxx） |
| 社群学习 / 酷残学院 | 简介 + 跳转链接到 /academy |
| 团队介绍（发起人） | 可编辑内容块 |
| 研究员名录 | researchers 表，卡片网格展示 |

#### 计划 `/plans`
- 三大计划完整展示
- 每项标题、副标题、描述
- 如有 external_url 显示外部链接按钮
- 点击进入 `/plans/<slug>` 详情页

#### 计划详情 `/plans/<slug>`
- 完整描述
- 外部链接（如有）
- 关联产出自动列出

#### 产出 `/output`
| Tab/分类 | 内容 | 格式 |
|----------|------|------|
| 社群研究报告 | report_type='research' | 有 PDF 下载 |
| 研究员翻译文章 | report_type='translation' | 纯文字 |
| 经纬计划产出 | report_type='jingwei' | 有 PDF 下载 |
| 读书会回顾 | report_type='reading' | 仅正文，无 PDF |
| 政策简报（未来） | 预留扩展 | — |
| 可视化数据（未来） | 预留扩展 | — |

**筛选方式：** 按标签/主题筛选 + 按类型 Tab 切换 并存
（用户可选择只看某类型，或在某类型内按标签筛选）

#### 社群 `/community`
| 区域 | 内容 |
|------|------|
| 社群行动者 | 介绍/列表 |
| 社群研究招募 | 招募信息 |
| 社群学习资源 | 学习资料列表 |
| 酷残学院入口 | 入口卡片，跳转到 /academy |

#### 活动动态 `/activities`
- articles 表中标记为活动的文章
- 展示日期、标题、摘要
- 按时间倒序
- 详情页 `/articles/<slug>`

#### 合作 `/contact`
- 联系邮箱
- 志愿者招募入口（文章/信息页）
- 社交媒体链接列表（微信公号、微博、Twitter/X 等）
- 支持/捐助信息（非核心，辅助展示）

#### 酷残学院 `/academy`
- 独立页面
- 课程列表（courses 表）
- 课程详情 `/academy/<slug>`

### 3.3 内容关联模型

```
研究员 ──(标签关联)──→ 报告/产出
     │
     └──(标签关联)──→ 新闻/活动（如有涉及该研究员）
     
新闻 ──(时间混排)──→ 首页最新动态
报告 ──(时间混排)──→ 首页最新动态

计划 ──(手动关联或标签)──→ 相关产出/报告
```

---

## 四、前台页面详细设计

### 4.1 全局组件

#### 4.1.1 顶部导航栏（sticky）

```
┌────────────────────────────────────────────────────────────────┐
│ [Logo] 酷残未来研究院 CFI  [首页] [关于] [计划] [产出] [社群] [活动动态] [合作] [A-] [A+] [HC] │
└────────────────────────────────────────────────────────────────┘
```

- 左侧：圆形 Logo（48×48）+ 中文名 + 英文缩写 CFI
- 中间：导航菜单项（从 navigation 表读取，后台可配置）
- 右侧：无障碍控制按钮组（A− / A+ / HC）
- 行为：sticky 吸顶，`backdrop-filter: blur(12px)` 毛玻璃
- 背景：`rgba(255, 248, 237, 0.9)`
- 激活态导航项：底部 3px 橙色实线 + 橙色文字
- 无障碍：顶部 `<a href="#main" class="skip-link">跳到主要内容</a>`

#### 4.1.2 页脚

- 两列：左列机构信息，右列联系方式 + 后台入口
- 背景：`#17130F`
- 文字：`#FFF8ED`
- 链接：`#DF4A16`

#### 4.1.3 无障碍控制系统

| 功能 | 实现 |
|------|------|
| 字体缩放三档 | CSS var `--font-scale`: 1 / 1.25 / 1.5 |
| 高对比度模式 | body class `.high-contrast` 覆盖颜色变量 |
| 持久化 | localStorage |

### 4.2 首页 `/`

#### 区块 1：Hero（80vh min-height）

**两列 Grid：左侧 1.3fr / 右侧 0.7fr**

左侧：
- 小字 `CRIPPING FUTURE INSTITUTE`（Courier New，大写，橙色）
- 大标题（site_settings `hero_title`，支持 HTML）
- 导语（site_settings `hero_subtitle`）
- 两个按钮：「查看三大计划」（实心橙底）「支持我们」（描边橙框）

右侧：
- 品牌参考图 `brand-reference.jpg`（400px 宽）
- 品牌标语卡片（橙色底白字）

背景：左侧 60% `#FFF8ED` → 右侧 40% `#DF4A16`

#### 区块 2：核心陈述

三列并排，列间 4px 粗边框分隔，编号 Courier New 橙色

#### 区块 3：三大计划（深色背景 `#17130F`）

三张卡片（grid auto-fill minmax 280px），每张含编号、标题、副标题、描述摘要

#### 区块 4：最新动态（混排）

- articles + reports UNION 按 created_at 取最近 6 条
- 每项：日期（Courier New）+ 标题 + 类型标记 [新闻] / [报告]
- 底部：「查看全部动态 →」（跳转 /activities）

#### 区块 5：支持我们（捐款导向）

- 突出的行动号召，指向捐款/支持方式
- 核心行动目标：推动访客捐款

### 4.3 关于 `/about`

从上到下：
1. 页面标题 + 机构介绍正文
2. **三大计划简介** — 三张小型卡片，带跳转 `/plans/xxx`
3. **社群学习 / 酷残学院** — 简介 + 跳转 `/academy`
4. **团队介绍（发起人）** — 照片 + 简介正文
5. **研究员名录** — researchers 卡片网格（照片、姓名、头衔）

每个区块之间 4px 粗边框分隔。

### 4.4 计划 `/plans`

三大计划完整展示卡片，点击进详情。

### 4.5 计划详情 `/plans/<slug>`

完整信息 + 外链（如有）+ 关联产出自动列出。

### 4.6 产出 `/output`

**Tab 切换 + 标签筛选并存：**

Tab 行：研究报告 | 翻译文章 | 经纬产出 | 读书会回顾 | （+ 未来扩展）

当前 Tab 下可按标签（tags）筛选。

每项展示：标题、摘要、类型标签（Courier New）、日期、PDF 下载按钮（如有）。

### 4.7 产出详情 `/reports/<slug>`

- 标题 + 日期 + 标签
- 完整正文（含 HTML）
- PDF 下载（如有 `pdf_filename`）
- 相关产出（相同标签的其他报告）

### 4.8 社群 `/community`

四个区域：

1. **社群行动者** — 介绍性文字（site_settings）
2. **社群研究招募** — 招募信息（可编辑）
3. **社群学习资源** — 资源链接/文档列表
4. **酷残学院入口** — 卡片形式，跳转 `/academy`

### 4.9 酷残学院 `/academy`

- 页面标题 + 简介
- 课程列表（courses 表，is_active=1）
- 每张课程卡片：标题、讲师、简介、二维码（如有）、外部链接按钮（如有）
- 课程详情 `/academy/<slug>`

### 4.10 活动动态 `/activities`

- articles 列表（时间倒序）
- 每项：日期（Courier New）+ 标题 + 摘要
- 分页（每页 10 条）

### 4.11 新闻详情 `/articles/<slug>`

- 标题 + 日期
- 正文
- 如有相关报告，底部列出

### 4.12 研究员详情 `/researchers/<slug>`

- 照片（300px，圆角）
- 姓名 + 头衔
- 标签
- 个人简介
- 关联产出列表（相同标签的 reports）

### 4.13 合作 `/contact`

- 联系邮箱
- 志愿者招募入口
- 社交媒体链接（微信公众号、微博、Twitter/X 等）

---

## 五、后台管理系统

### 5.1 登录 `/admin`

用户名/密码表单，Session 认证。

### 5.2 管理面板 `/admin/dashboard`

左侧导航：

| 模块 | 管理对象 | 说明 |
|------|----------|------|
| 网站设置 | site_settings | 所有键值对编辑 |
| 导航菜单 | navigation | 增删改排序 |
| 三大计划 | plans | 增删改 |
| 产出/报告 | reports | 增删改，含 PDF 上传 |
| 新闻/活动 | articles | 增删改 |
| 研究员 | researchers | 增删改，含照片上传 |
| 酷残学院课程 | courses | 增删改，含二维码上传 |
| 社群内容 | community_sections | 社群页面各区域内容 |
| 文件管理 | uploads | 浏览/删除上传文件 |
| 其他 | — | 占位（未来扩展） |

每个模块：列表 + 新增 + 编辑 + 删除（带确认）。

### 5.3 API 接口

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/admin/content?type=<table>` | GET | 获取列表 |
| `/api/admin/content?type=<table>&id=<id>` | GET | 获取单条 |
| `/api/admin/content` | POST | 新增/更新 |
| `/api/admin/content?type=<table>&id=<id>` | DELETE | 删除 |
| `/api/upload` | POST | 上传文件 |

---

## 六、数据库设计

### 6.1 表结构

7 张表 + 1 张扩展：

| 表名 | 主要字段 | 说明 |
|------|----------|------|
| site_settings | key TEXT PK, value TEXT | 网站所有配置键值 |
| navigation | id, title, title_en, url, sort_order, is_external | 导航菜单 |
| plans | id, title, subtitle, description, slug UNIQUE, external_url, sort_order, is_active, created_at, updated_at | 三大计划 |
| articles | id, title, slug UNIQUE, summary, content, tags, is_published, created_at, updated_at | 新闻/活动动态 |
| reports | id, title, slug UNIQUE, summary, content, tags, **report_type**, pdf_filename, is_published, created_at, updated_at | 产出（type 扩展预留：research/translation/jingwei/reading/等） |
| researchers | id, name, slug UNIQUE, title, bio, photo, tags, is_active, created_at | 研究员 |
| courses | id, title, slug UNIQUE, description, instructor, qr_code, external_url, is_active, created_at | 课程（挂在酷残学院下） |
| community_sections | id, section_key TEXT UNIQUE, title, content, sort_order | 社群页面各区域内容 |

### 6.2 report_type 取值与对应展示

| report_type | 显示名称 | 有 PDF？ |
|-------------|----------|----------|
| research | 社群研究报告 | ✅ 有 |
| translation | 研究员翻译文章 | ❌ 纯文字 |
| jingwei | 经纬计划产出 | ✅ 有 |
| reading | 读书会回顾 | ❌ 仅正文 |
| *未来扩展* | 政策简报 / 可视化数据 | 按需 |

### 6.3 首页混排查询

```sql
SELECT id, title, slug, 'article' AS content_type, created_at FROM articles WHERE is_published=1
UNION ALL
SELECT id, title, slug, 'report' AS content_type, created_at FROM reports WHERE is_published=1
ORDER BY created_at DESC LIMIT 6;
```

---

## 七、静态资源

| 路径 | 说明 |
|------|------|
| `/static/style.css` | 主样式表（含高对比度模式） |
| `/static/a11y.js` | 无障碍脚本 |
| `/static/admin.js` | 后台管理脚本 |
| `/static/LOGO.jpg` | Logo |
| `/static/brand-reference.jpg` | 品牌参考图 |
| `/static/concept-image.jpg` | 概念布局图 |
| `/static/uploads/` | 上传文件目录 |

---

## 八、无障碍设计（WCAG 2.1 AA）

- 颜色对比度 ≥ 4.5:1
- Skip Link（focus 时可见）
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
| 后端 | Python 3.10+ 标准库（http.server） |
| 数据库 | SQLite |
| 前端 | 后端生成 HTML |
| 部署 | Linux + Nginx 反向代理 + systemd |
| HTTPS | Let's Encrypt / Certbot |

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

### Nginx + systemd

详见 V3 文档保持不变。

---

## 十一、未来迭代（本次未包含）

| 功能 | 说明 |
|------|------|
| 英文版本 | 完整双语，同一套导航结构 |
| 全站搜索 | 覆盖新闻 + 报告 + 课程 |
| SEO 优化 | title/description、OG 标签、sitemap.xml |
| 上传预览 | 后台图片预览 |
| 新一级页面 | 数据结构已预留扩展（新增 navigation 记录即可） |

---

## 十二、验收标准

### 12.1 功能验收

- [ ] 7 个一级页面 + 所有详情页正常渲染
- [ ] 首页最新动态 = 新闻+报告按时间混排
- [ ] 产出页 Tab + 标签筛选并存
- [ ] 酷残学院独立页面 `/academy` + 课程详情
- [ ] 活动动态独立页面 `/activities`
- [ ] 后台所有模块可 CRUD
- [ ] PDF 上传下载
- [ ] 字体缩放 + 高对比度全站覆盖

### 12.2 视觉验收

- [ ] 橙色仅限规范允许场景
- [ ] 等宽字体用于标签/日期/编号
- [ ] Hero 两列 + 渐变色
- [ ] 4px 粗边框分隔区块
- [ ] 深色区块正确渲染

### 12.3 无障碍验收

- [ ] WCAG 2.1 AA 对比度达标
- [ ] Skip Link 可用
- [ ] 键盘可操作

### 12.4 部署验收

- [ ] `python app.py` 直接启动
- [ ] 零第三方依赖
- [ ] Nginx + systemd 正常工作

---

> **文档结束**
> V4.0 — 结构定稿，随时可开始实现。
