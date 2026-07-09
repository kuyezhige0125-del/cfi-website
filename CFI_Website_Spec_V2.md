# 酷残未来研究院（CFI）网站制作需求文档

> 版本：V2.0 | 日期：2026-07-09
> 用途：供设计人员和 AI 开发者逐条复现的完整需求规格书

---

## 一、项目概述

### 1.1 机构信息

- **中文名**：酷残未来研究院
- **英文名**：Cripping Future Institute（CFI）
- **定位**：由残障人发起并领导的独立民间残障研究机构，兼有残障融合咨询与社群发展职能
- **核心理念**：以社群发展为手段进行知识生产，以知识生产为手段推动社群发展
- **品牌标语**：没有我们的参与，不要做有关我们的决定

### 1.2 网站性质

- **类型**：内容管理系统型网站（非纯静态，后台可编辑所有文字和图片/PDF）
- **语言**：第一版中文版（HTML lang="zh-CN"），架构预留英文版扩展能力
- **部署环境**：Linux 云服务器（Ubuntu 22.04 / Debian 12）+ Nginx 反向代理 + systemd 常驻进程
- **数据库**：SQLite（零维护，备份即拷贝文件）
- **技术栈**：Python 3.10+ 标准库（http.server），无任何第三方依赖

### 1.3 核心原则

1. **WCAG 2.1 AA 级无障碍**：颜色对比度达标、语义化 HTML、键盘可导航、屏幕朗读友好
2. **低视力友好模式**：右上角切换按钮，支持字体放大（正常/大/特大）和高对比度（黑底白字）
3. **后台可编辑所有栏目名称和内容**：包括导航菜单、三大计划、新闻、报告、研究员、课程等
4. **内容交叉关联**：报告、新闻、研究员之间可通过标签互相跳转
5. **极简高效**：无构建步骤、无框架依赖、单文件后端

---

## 二、前台页面架构

共 **6 个一级页面 + 若干详情页**，导航栏可在后台自定义：

| 页面 | 路由 | 说明 |
|------|------|------|
| 首页 | / | Hero + 核心陈述 + 三大计划概览 + 最新动态 + 支持我们 |
| 关于 | /about | 机构简介 / 背景与失语 / 核心方法论 / 战略愿景 |
| 计划 | /plans | 三大计划列表 |
| 计划详情 | /plans/<slug> | 单个计划的详细介绍 + 外链 |
| 产出 | /output | 研究报告（按类型Tab分类）+ 读书会/沙龙回顾 |
| 社群 | /community | 新闻动态 + 研究员名录 + 酷残学院 |
| 合作 | /contact | 联系方式 + 支持/捐助方式 |
| 新闻详情 | /articles/<slug> | 单篇新闻/文章正文 |
| 报告详情 | /reports/<slug> | 单份研究报告正文 + PDF下载 |
| 研究员详情 | /researchers/<slug> | 研究员照片 + 简介 + 发表作品列表 |

---

## 三、前台页面详细需求

### 3.1 全局组件

#### 3.1.1 顶部导航栏（sticky）

- **左侧**：圆形 Logo（48x48px）+ 机构名称（中 + EN）
- **中间**：导航菜单项（从数据库读取，后台可增删改排序）
- **右侧**：无障碍控制按钮组
  - A- 按钮：减小字体（Normal → Large → XLarge → Normal 循环）
  - A+ 按钮：增大字体
  - HC 按钮：高对比度模式切换（白色背景 ↔ 黑色背景）
- **行为**：sticky 定位，滚动时吸顶，毛玻璃背景效果
- **无障碍**：页面顶部有 skip-link（"跳到主要内容"），focus 时可见

#### 3.1.2 页脚

- 机构名称（中 + EN）+ 联系邮箱 + 后台入口链接
- 深色背景（#17130F）

#### 3.1.3 无障碍控制

- **字体缩放**：通过 CSS 变量 --font-scale 实现，三个档位
  - Normal: --font-scale: 1（基准 16px）
  - Large: --font-scale: 1.25（20px）
  - XLarge: --font-scale: 1.5（24px）
- **高对比度**：通过 body 添加 high-contrast class 实现，覆盖所有颜色变量
- **持久化**：用户偏好保存在 localStorage，下次访问自动恢复

### 3.2 首页（/）

从上到下依次展示以下区块：

#### 区块 1：Hero（首屏）

- **左侧**：
  - 英文机构名（小字号，大写，橙色 #DF4A16）
  - 大标题（首页大标题，来自后台设置）
  - 导语（首页导语，来自后台设置）
  - 两个按钮：「查看三大计划」（橙色实心）、「支持我们」（描边）
- **右侧**：
  - 品牌参考图（400px 宽）
  - 品牌标语（橙色背景卡片，居中显示）
- **布局**：grid 两列，左侧 1.3fr，右侧 0.7fr；最小高度 80vh
- **背景**：从左到右渐变，左侧纸色（#FFF8ED）占 60%，右侧橙色（#DF4A16）占 40%

#### 区块 2：核心陈述（Statement）

- 三列并排（桌面端），移动端堆叠
- 每列包含编号（01/02/03）、标题、正文
- 内容来自后台设置：关于标题+正文、背景标题+正文、方法论标题+正文
- 列之间有右边框分隔

#### 区块 3：三大计划（Band 深色背景区）

- 标题："三大行动计划"，上方小字 "Plans"
- 三张计划卡片并排（grid auto-fill, minmax 280px）
- 每张卡片：编号（01/02/03）、计划标题、副标题、摘要、"打开计划详情"链接
- 点击跳转到 /plans/<slug> 详情页

#### 区块 4：最新动态（Split Section）

- 标题："最新动态"，上方小字 "Updates"
- 新闻列表（按发布时间倒序），每条包含：
  - 标签（kicker，如"拾遗计划"）+ 发布日期
  - 新闻标题（可点击跳转）
  - 摘要

#### 区块 5：战略愿景（Vision Section）

- 橙色背景区域
- 上方小字 "Future Agenda"
- 愿景标题 + 正文（来自后台设置）

#### 区块 6：支持我们（Band 深色背景区）

- 标题："支持我们"，上方小字 "Support"
- 支持方式卡片（来自后台 supports 表）：标题 + 说明
- 联系方式栏：公众号 + 邮箱 + 客服

### 3.3 关于页（/about）

- **Hero 区**：大标题 "关于酷残未来研究院"
- **正文区**：机构简介正文
- **三列陈述区**：背景与失语 / 核心方法论 / 战略愿景（同首页区块 2）

### 3.4 计划页（/plans）

- **Hero 区**：大标题 "三大行动计划"
- **卡片网格**：三张计划卡片（同首页区块 3），每张可点击进入详情页

### 3.5 计划详情页（/plans/<slug>）

- **Hero 区**：标签 "行动计划" + 计划标题 + 副标题
- **正文区**：
  - 摘要（h2 标题）
  - 详细介绍（段落）
  - 外部链接按钮（如微信公众号文章）
  - "返回计划列表"按钮

### 3.6 产出页（/output）

- **Hero 区**：大标题 "研究与产出"
- **研究报告 Tab 区**：
  - Tab 按钮按报告类型分组（如"社群经验报告"、"政策倡导报告"等）
  - 每个 Tab 下显示该类型的报告卡片列表
  - 报告卡片：标题（可点击）、摘要、发布日期、PDF 下载按钮
  - 最后一个 Tab："读书会 & 沙龙回顾"，显示相关新闻
- **无障碍**：Tab 使用 
ole="tablist" + ria-selected + ria-pressed

### 3.7 社群页（/community）

三个子区块，每个区块有独立标题：

#### 子区块 1：新闻动态

- 新闻列表（同首页区块 4），按发布时间倒序

#### 子区块 2：研究员名录

- 研究员卡片网格（auto-fill, minmax 260px）
- 每张卡片：圆形头像（100px，橙色边框）、姓名（可点击）、研究领域

#### 子区块 3：酷残学院

- 课程卡片网格（auto-fill, minmax 280px）
- 每张卡片：课程名称、课程介绍、报名二维码图片（160x160px）、学习材料链接按钮

### 3.8 合作页（/contact）

- **Hero 区**：大标题 "合作与捐助"
- **支持方式区**：支持卡片网格（同首页区块 6）
- **联系方式区**：
  - 公众号
  - 邮箱
  - 客服

### 3.9 新闻/报告/研究员详情页

通用结构：
- **Hero 区**：标签 + 标题 + 副标题/摘要
- **正文区**：Markdown 渲染的正文内容
- **操作区**：下载按钮（报告）/ 阅读原文链接（新闻）/ 返回列表按钮

---

## 四、后台管理系统

### 4.1 登录

- 路由：/admin
- 默认账号：dmin / CFI2026!Local
- 登录态通过 Cookie（cfi_session）维持，HttpOnly + SameSite=Lax
- 登录成功后显示管理面板，未登录显示登录表单

### 4.2 管理面板

顶部有 8 个 Tab，每个 Tab 对应一个管理模块：

| Tab | 模块 | 说明 |
|-----|------|------|
| 站点设置 | settings | 修改首页/关于/计划/愿景等所有固定文案 |
| 导航菜单 | navigation | 增删改导航栏菜单项，可自定义名称、链接、排序、启用/禁用 |
| 三大计划 | projects | 增删改三个计划的介绍内容 |
| 新闻动态 | articles | 增删改新闻/活动/读书会/沙龙回顾 |
| 研究报告 | reports | 增删改研究报告，支持上传 PDF |
| 研究员 | researchers | 增删改研究员信息，支持上传照片 |
| 酷残学院 | academies | 增删改课程信息，支持上传二维码 |
| 支持方式 | supports | 增删改捐助/合作方式说明 |

### 4.3 各模块字段详解

#### 站点设置（16 个字段）

| 字段名 | 类型 | 说明 | 默认值 |
|--------|------|------|--------|
| site_name | 文本 | 网站名称 | 酷残未来研究院 |
| site_en | 文本 | 英文名称 | Cripping Future Institute |
| hero_title | 文本 | 首页大标题 | 由残障者引领的知识生产生态 |
| hero_intro | 多行文本 | 首页导语 | 我们将社群沉淀的默会知识... |
| hero_quote | 文本 | 品牌标语 | 没有我们的参与，不要做有关我们的决定 |
| about_title | 文本 | 关于标题 | 关于酷残未来研究院 |
| about_body | 多行文本 | 关于正文 | 酷残未来研究院源于2023年... |
| background_title | 文本 | 背景标题 | 热闹背后的失语 |
| background_body | 多行文本 | 背景正文 | 有个体但无我们... |
| method_title | 文本 | 方法论标题 | 核心方法论：残障主体性 |
| method_body | 多行文本 | 方法论正文 | 研究是解放，也是翻译和杠杆... |
| vision_title | 文本 | 愿景标题 | 战略愿景：定标与设定议程 |
| vision_body | 多行文本 | 愿景正文 | 我们希望建立国内首个... |
| contact_public | 文本 | 公众号 | 公众号：酷残未来研究院 |
| contact_email | 文本 | 邮箱 | CFI@shshengbo.cn |
| contact_service | 文本 | 客服 | 客服：FreePWD |

#### 导航菜单

| 字段 | 类型 | 说明 |
|------|------|------|
| slug | 文本 | 链接标识（自动生成） |
| label | 文本 | 显示名称 |
| target | 文本 | 目标 URL |
| kind | 下拉 | internal（站内）/ external（外链） |
| order_num | 数字 | 排序号 |
| enabled | 开关 | 是否显示在导航栏 |

#### 三大计划

| 字段 | 类型 | 说明 |
|------|------|------|
| slug | 文本 | 链接标识 |
| title | 文本 | 标题 |
| subtitle | 文本 | 副标题 |
| summary | 多行文本 | 摘要 |
| detail | 多行文本 | 详细介绍 |
| link_label | 文本 | 外链按钮文字 |
| link_url | 文本 | 外链 URL |
| sort_order | 数字 | 排序 |

#### 新闻动态（articles）

| 字段 | 类型 | 说明 |
|------|------|------|
| slug | 文本 | 链接标识 |
| title | 文本 | 标题 |
| kicker | 文本 | 标签（如"拾遗计划"、"读书会回顾"） |
| summary | 多行文本 | 摘要 |
| body | 多行文本 | 正文（Markdown 格式） |
| external_url | 文本 | 原文链接（如微信公众号） |
| published_at | 日期 | 发布日期 |
| is_published | 开关 | 是否发布 |

#### 研究报告（reports）

| 字段 | 类型 | 说明 |
|------|------|------|
| slug | 文本 | 链接标识 |
| title | 文本 | 标题 |
| summary | 多行文本 | 摘要 |
| body | 多行文本 | 正文（Markdown 格式） |
| report_type | 文本 | 报告类型（7种分类） |
| pdf_filename | 文本 | PDF 文件名 |
| published_at | 日期 | 发布日期 |
| is_published | 开关 | 是否发布 |
| tags | 文本 | 标签（逗号分隔） |
| plan_slug | 文本 | 关联计划（可选） |
| author_ids | 文本 | 关联研究员 ID（逗号分隔） |

**7种报告类型**：
1. 社群经验报告
2. 政策倡导报告
3. 自我叙事报告
4. 残障行动者案例研究
5. 残障口述史
6. 残障学术研究报告
7. 核心领域路线图报告

#### 研究员（researchers）

| 字段 | 类型 | 说明 |
|------|------|------|
| slug | 文本 | 链接标识 |
| name | 文本 | 姓名 |
| photo | 文本 | 照片文件名 |
| bio | 多行文本 | 个人简介 |
| research_areas | 文本 | 研究领域 |
| contact_info | 文本 | 联系方式 |
| sort_order | 数字 | 排序 |

#### 酷残学院（academies）

| 字段 | 类型 | 说明 |
|------|------|------|
| slug | 文本 | 链接标识 |
| title | 文本 | 课程名称 |
| description | 多行文本 | 课程介绍 |
| material | 文本 | 学习材料链接 |
| qr_code | 文本 | 报名二维码文件名 |
| sort_order | 数字 | 排序 |

#### 支持方式（supports）

| 字段 | 类型 | 说明 |
|------|------|------|
| title | 文本 | 标题 |
| description | 多行文本 | 说明 |
| sort_order | 数字 | 排序 |

### 4.4 图片/PDF 上传

- **接口**：POST /api/upload（需登录）
- **格式**：multipart/form-data
- **存储路径**：data/uploads/
- **支持的格式**：图片（jpg/png）、PDF
- **文件名处理**：去除特殊字符，保留字母数字和下划线
- **返回**：{"ok": true, "filename": "saved_filename.jpg"}

> **注意**：当前后台界面中图片/PDF 字段仅接受文件名文本输入，尚未集成上传按钮。需要在前端添加文件选择器和上传触发逻辑，上传后自动回填文件名字段。

---

## 五、视觉设计规范

### 5.1 色彩系统

| 角色 | 色值 | 用途 |
|------|------|------|
| 主色 - 橙 | #DF4A16 | Logo、按钮、链接 hover、强调元素 |
| 深橙 | #B93410 | 辅助文字、hover 态 |
| 墨色 - 黑 | #17130F | 正文、深色区块背景 |
| 灰度 -  muted | #645C54 | 次要文字、日期、标签 |
| 纸色 - 背景 | #FFF8ED | 页面主背景（暖纸色） |
| 白色 | #FFFFFF | 卡片背景 |

**高对比度模式覆盖**：
- 墨色 → #000
- 纸色 → #FFF
- 主橙 → #FF6B35
- 深色区块 → #000 白字

### 5.2 字体

- **正文**：微软雅黑 / PingFang SC / Noto Sans CJK SC / Arial
- **等宽/标签**：Courier New（用于日期、标签等）
- **字号层级**：
  - H1: 36px-72px（响应式 clamp）
  - H2: 28px
  - H3: 19-22px
  - 正文: 16px（可缩放至 20px / 24px）
  - 辅助文字: 13-14px

### 5.3 布局

- **最大宽度**：1200px（居中）
- **内边距**：响应式 clamp(18px, 5vw, 64px)
- **卡片**：白色背景 + 2px 实线边框 + 圆角 4px
- **按钮**：最小高度 44px（触摸友好），两种样式（实心/描边）
- **网格**：uto-fill, minmax(260px, 1fr) 自适应

### 5.4 响应式断点

- **桌面**：> 900px，多列布局
- **平板**：600-900px，减少列数
- **手机**：< 560px，单列堆叠

### 5.5 风格关键词

- **基底**：暖纸色 + 粗边框（2px solid）→ 学术感
- **点缀**：橙色 + 等宽字体标签 → 赛博朋克感
- **理念**：CF/残废的语义彩蛋 → 颠覆与重构
- **禁止**：暗黑底色全屏、霓虹光效、花哨动画

---

## 六、无障碍设计（WCAG 2.1 AA）

### 6.1 强制要求

1. **Skip Link**：页面顶部隐藏链接，focus 时显示 "跳到主要内容"
2. **语义化 HTML**：正确使用 <header>, <nav>, <main>, <footer>, <section>, <article>, <h1>-<h6>
3. **ARIA 属性**：
   - 导航：ria-label="主导航"
   - Tab 切换：
ole="tablist", ria-selected, ria-pressed
   - 无障碍按钮：ria-label, 	itle
   - 图片：lt 文本
4. **键盘导航**：所有交互元素可通过 Tab 键聚焦，Enter/Space 可触发
5. **焦点可见**：:focus-visible 显示橙色 3px 轮廓
6. **颜色对比度**：所有文字与背景的对比度 ≥ 4.5:1（AA 级）
7. **字体缩放**：支持 150% 缩放而不丢失内容或功能
8. **打印样式**：隐藏导航、按钮、无障碍控件；黑白输出

### 6.2 低视力友好模式

- **字体缩放**：三档切换（Normal / Large / XLarge），通过 CSS 变量实现
- **高对比度**：黑底白字 + 橙色强调，覆盖所有页面元素
- **持久化**：localStorage 保存用户偏好

---

## 七、数据库 Schema

### 7.1 表结构

`sql
-- 站点设置（Key-Value 结构）
CREATE TABLE settings (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- 三大计划
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    subtitle TEXT NOT NULL,
    summary TEXT NOT NULL,
    detail TEXT NOT NULL,
    link_label TEXT NOT NULL,
    link_url TEXT NOT NULL,
    sort_order INTEGER NOT NULL DEFAULT 0
);

-- 导航菜单
CREATE TABLE navigation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT UNIQUE NOT NULL,
    label TEXT NOT NULL,
    target TEXT NOT NULL,
    kind TEXT NOT NULL DEFAULT 'internal',
    order_num INTEGER NOT NULL DEFAULT 0,
    enabled INTEGER NOT NULL DEFAULT 1
);

-- 新闻动态
CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    kicker TEXT NOT NULL,
    summary TEXT NOT NULL,
    body TEXT NOT NULL,
    external_url TEXT NOT NULL DEFAULT '',
    published_at TEXT NOT NULL,
    is_published INTEGER NOT NULL DEFAULT 1
);

-- 研究报告
CREATE TABLE reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    summary TEXT NOT NULL,
    body TEXT NOT NULL,
    report_type TEXT NOT NULL DEFAULT '其他',
    pdf_filename TEXT NOT NULL DEFAULT '',
    published_at TEXT NOT NULL,
    is_published INTEGER NOT NULL DEFAULT 1,
    tags TEXT NOT NULL DEFAULT '',
    plan_slug TEXT NOT NULL DEFAULT '',
    author_ids TEXT NOT NULL DEFAULT ''
);

-- 研究员
CREATE TABLE researchers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    photo TEXT NOT NULL DEFAULT '',
    bio TEXT NOT NULL,
    research_areas TEXT NOT NULL DEFAULT '',
    contact_info TEXT NOT NULL DEFAULT '',
    sort_order INTEGER NOT NULL DEFAULT 0
);

-- 酷残学院
CREATE TABLE academies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    material TEXT NOT NULL DEFAULT '',
    qr_code TEXT NOT NULL DEFAULT '',
    sort_order INTEGER NOT NULL DEFAULT 0
);

-- 支持方式
CREATE TABLE supports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    sort_order INTEGER NOT NULL DEFAULT 0
);
`

### 7.2 种子数据（首次初始化）

- **settings**：16 条预设文案
- **projects**：3 条（拾遗计划、蒹葭计划、经纬计划）
- **navigation**：5 条（关于、计划、产出、社群、合作）
- **articles**：2 条（口述史、社群行动报告）
- **supports**：3 条（非限定资助、专项项目资助、小微/志愿者支持）
- **reports / researchers / academies**：空（通过后台添加）

---

## 八、API 接口

### 8.1 公开接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | / | 首页 |
| GET | /about | 关于页 |
| GET | /plans | 计划列表 |
| GET | /plans/<slug> | 计划详情 |
| GET | /output | 产出页 |
| GET | /reports/<slug> | 报告详情 |
| GET | /community | 社群页 |
| GET | /researchers/<slug> | 研究员详情 |
| GET | /contact | 合作页 |
| GET | /articles/<slug> | 新闻详情 |
| GET | /api/health | 健康检查 {"ok": true} |

### 8.2 认证接口

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | /api/login | 登录，返回 Cookie |
| POST | /api/logout | 登出 |

请求体：{"username": "...", "password": "..."}
响应：{"ok": true} + Set-Cookie

### 8.3 管理接口（需登录）

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/admin/content | 获取所有内容（JSON） |
| POST | /api/admin/content | 保存所有内容（JSON） |
| POST | /api/upload | 上传文件（multipart/form-data） |

### 8.4 静态资源

| 路径 | 说明 |
|------|------|
| /static/style.css | 主样式表 |
| /static/a11y.js | 无障碍脚本 |
| /static/admin.js | 后台管理脚本 |
| /static/LOGO.jpg | Logo |
| /static/brand-reference.jpg | 品牌参考图 |
| /static/uploads/<file> | 用户上传的文件 |

---

## 九、部署配置

### 9.1 服务器要求

- 操作系统：Ubuntu 22.04 / Debian 12
- Python：3.10+
- Web 服务器：Nginx（反向代理）
- 进程管理：systemd
- HTTPS：Let's Encrypt / Certbot

### 9.2 环境变量（.env）

`ash
CFI_ENV=production
CFI_HOST=127.0.0.1
CFI_PORT=7010
CFI_ADMIN_USER=admin
CFI_ADMIN_PASSWORD=<强密码>
`

### 9.3 Nginx 配置

`
ginx
server {
    listen 80;
    server_name your-domain.com;
    client_max_body_size 20m;
    location / {
        proxy_pass http://127.0.0.1:7010;
        proxy_set_header Host System.Management.Automation.Internal.Host.InternalHost;
        proxy_set_header X-Real-IP ;
    }
}
`

### 9.4 systemd 服务

`ini
[Service]
WorkingDirectory=/opt/cfi-site
ExecStart=/usr/bin/python3 /opt/cfi-site/app.py
User=www-data
Restart=always
`

---

## 十、待实现功能（本次未包含）

以下功能在当前版本中**尚未实现**，需在后续迭代中补充：

### 10.1 后台图片/PDF 上传按钮

**现状**：后台界面中 photo（研究员照片）、qr_code（课程二维码）、pdf_filename（报告 PDF）字段仅为纯文本输入框，用户需手动输入文件名。

**需求**：
- 在上述字段旁添加「上传」按钮
- 点击后弹出文件选择器
- 选择文件后调用 POST /api/upload 接口
- 上传成功后自动将返回的文件名填入文本框
- 支持图片预览（photo / qr_code 字段）
- 限制文件大小（图片 ≤ 5MB，PDF ≤ 20MB）
- 限制文件类型（图片：jpg/png；文档：pdf）

### 10.2 英文版本

**现状**：所有文案硬编码在中文，site_en 字段仅用于显示英文名称。

**需求**：
- 后台增加语言切换开关
- 所有可编辑字段支持中英文双版本
- 前台根据 URL 参数或浏览器语言自动切换
- 路由支持 /en/about 等英文路径

### 10.3 搜索功能

**现状**：无搜索能力。

**需求**：
- 全站搜索（新闻、报告、研究员）
- 按关键词 + 类型筛选
- 搜索结果分页展示

### 10.4 SEO 优化

**现状**：基本 meta 标签。

**需求**：
- 每页独立 title / description / keywords
- Open Graph 标签（社交媒体分享）
- sitemap.xml 自动生成
- robots.txt

---

## 十一、文件结构

`
cfi-site/
├── app.py                    # 主程序（Python，无第三方依赖）
├── .env                      # 环境变量（部署时创建）
├── .env.example              # 环境变量模板
├── .env.production.example   # 生产环境模板
├── DEPLOY.md                 # 部署文档
├── README.md                 # 项目说明
├── data/
│   ├── site.db              # SQLite 数据库
│   └── uploads/             # 上传文件目录
├── deploy/
│   ├── cfi-site.service     # systemd 服务配置
│   └── nginx.conf           # Nginx 配置模板
└── static/
    ├── style.css            # 主样式表（含高对比度模式）
    ├── a11y.js              # 无障碍切换脚本
    ├── admin.js             # 后台管理前端
    ├── admin.html           # 后台管理页面（内嵌在 app.py 中）
    ├── LOGO.jpg             # 机构 Logo
    └── brand-reference.jpg  # 品牌参考图
`

---

## 十二、开发验收标准

### 12.1 功能验收

- [ ] 前台所有 6 个一级页面正常渲染
- [ ] 所有详情页（计划/新闻/报告/研究员）正常渲染
- [ ] 后台登录/登出功能正常
- [ ] 后台 8 个管理模块均可增删改查
- [ ] 导航菜单可在后台自定义
- [ ] 研究报告支持 PDF 上传和下载
- [ ] 字体缩放（三档）功能正常
- [ ] 高对比度模式切换正常
- [ ] 所有用户偏好（字体/对比度）localStorage 持久化

### 12.2 无障碍验收

- [ ] WCAG 2.1 AA 颜色对比度达标
- [ ] Skip Link 可用
- [ ] 所有交互元素键盘可操作
- [ ] 屏幕朗读软件可正确播报
- [ ] 打印样式正常

### 12.3 部署验收

- [ ] 无第三方依赖（仅 Python 标准库）
- [ ] python app.py 可直接启动
- [ ] Nginx + systemd 配置可正常工作
- [ ] HTTPS 证书可自动续签
- [ ] 数据库文件可独立备份

---

> **文档结束**
> 本文档为完整需求规格书，设计人员和 AI 开发者可据此逐条复现实现。
