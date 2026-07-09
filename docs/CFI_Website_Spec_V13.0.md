# 酷残未来研究院（CFI）网站需求文档 V13.0

> 版本：V13.0 | 日期：2026-07-10
> **独立完整需求文档，覆盖配色方案、页面结构、数据库、后台管理、API 全貌**

---

## 一、配色方案

### 1.1 配色表

| 角色 | 色值 | 用途 |
|------|------|------|
| 点缀色（Accent） | **#C7704F**（陶土橙） | 按钮背景、导航当前项底部标识线、超链接悬停态、标签链接、数字编号、浅色区卡片副标题、计划卡片标题（蒹葭/经纬/拾遗） |
| 背景色（Background） | **#F8F5F0**（暖米白） | 页面大面积底色，页头、导航、页脚及主要内容区背景 |
| 三大计划区背景 | **#F8F5F0**（暖米白） | 与页面背景统一，不设深色区块 |
| 正文色（Text） | **#4A3C31**（深褐色） | 正文文字，全站统一使用 |
| 辅助灰（Secondary） | **#6B6B6B** | 次级文字、日期、元信息 |
| 边框色（Border） | **#C4B9AE**（暖灰色） | 粗边框、卡片边框、分隔线、页脚上边框 |
| 卡片背景（Card） | **#F8F5F0**（暖米白） | 卡片内背景色 |
| 版权文字 | **#6B6B6B** | 页脚版权信息 |

### 1.2 WCAG AA 对比度

| 前景色 | 背景色 | 对比度 | 结果 |
|--------|--------|--------|------|
| #4A3C31 | #F8F5F0 | ~9:1 | ✅ 通过 |
| #C7704F | #F8F5F0 | ~4.6:1 | ✅ 通过 |
| #FFFFFF | rgba(0,0,0,0.7) | ~4.5:1 | ✅ 通过（轮播文字叠加层） |
| #6B6B6B | #F8F5F0 | ~4.8:1 | ✅ 通过 |

---

## 二、页面整体约束

### 2.1 最大宽度

整个页面由 .site-wrapper 包裹，设置 max-width: 1400px; margin: 0 auto; width: 100%;。
窗口宽度超过 1400px 时，页面居中不再拉伸，所有元素等比缩放，无背景断裂感。

### 2.2 字号缩放

- 基础字号：1rem（16px），由 CSS 变量 --font-scale 控制
- 导航栏 A- / A+ 按钮改变 data-font-size 属性
- mapping：level 1→1.0x，level 2→1.2x，level 3→1.4x
- 状态持久化到 localStorage

### 2.3 响应式断点

- 桌面端 >1024px：三列卡片，搜索框 160px
- 平板 768-1024px：两列卡片，搜索框 120px
- 移动端 <768px：汉堡菜单、单列卡片、页脚单列、容器内边距 12px
- 轮播高度：clamp(280px, 35vw, 480px) 平滑响应，移动端 clamp(200px, 40vw, 280px)

---

## 三、导航结构

### 3.1 一级导航项

导航栏 sticky 固定，背景 #F8F5F0，底部 2px 暖灰边框 #C4B9AE，内容区 1200px 居中。共 7 项 + 搜索框：

| 导航项 | 路由 | 说明 |
|--------|------|------|
| 首页 | / | 轮播 + 使命 + 三大计划 |
| 关于我们 | /about | 机构介绍 + 三大计划 + 发起人 |
| 最新动态 | /activities | 新闻动态 + 活动动态（分两区展示） |
| 研究成果 | /output | 研究报告 + 残障生命故事（分两区展示） |
| 资源与工具 | /resources | 酷残学院 + 工具手册/资源下载 |
| 研究力量 | /team | 研究员 + 社群行动者（分两列展示） |
| 合作与支持 | /contact | 联系方式 + 社交媒体 |

### 3.2 搜索功能

- 搜索范围：articles（文章）、reports（报告）、courses（课程）
- 命中字段：title、summary、content、tags
- 搜索结果按 created_at 倒序，标注类型标签
- 搜索路由：/search?q=关键词
- 搜索框白色背景，1px #C4B9AE 边框，搜索按钮 #C7704F 陶土橙

### 3.3 导航栏其他元素

- 机构 LOGO（圆形 48px）：左侧显示 LOGO.jpg + 机构名称"酷残未来研究院"
- 字号调节按钮 A-/A+
- 高对比度模式切换按钮 HC
- 移动端折叠为汉堡菜单

---

## 四、首页布局

### 4.1 区块顺序

1. **轮播图（hero-carousel）**
2. **使命陈述（mission-statement）**
3. **三大计划（.section-dark .plans-grid-section）**
4. **页脚（site-footer）**

首页不包含"支持我们"区块。

### 4.2 轮播图

- 视觉风格：大图背景 + 白色文字叠加（标题 + 副标题）+ 底部导航圆点
- 高度：clamp(280px, 35vw, 480px)，响应式平滑缩放
- 背景图：cover 模式填充，无图时背景 #F8F5F0
- 文字叠加区：底部渐变遮罩（transparent → rgba(0,0,0,0.7)），文字白色
- 切换：左右箭头按钮 + 底部圆点导航 + 自动播放
- 圆点：12px 圆形，非活跃态 rgba(255,255,255,0.4)，活跃态 #C7704F
- **数据来源**：articles 表中 is_featured=1 且 is_published=1 的文章，按 featured_sort_order 排序
- **默认幻灯片**：无精选文章时展示标题"欢迎来到酷残未来研究院"，**副标题来自 site_settings 的 org_slogan 键值**（后台可编辑），背景图 static/default-carousel.jpg

### 4.3 使命陈述区

- 浅色区背景 #F8F5F0，居中展示
- **数据来源**：site_settings 表中 key='org_description'（后台可编辑）
- 字号 1.2rem，字重 500，行高 1.8，文字颜色 #4A3C31

### 4.4 三大计划

- 卡片网格 3 列响应式，gap 32px
- 每张卡片：背景 #F8F5F0，暖灰边框 4px solid #C4B9AE，内边距 40px，圆角 4px
- 卡片标题（计划名）：#4A3C31，字号 1.25rem，字重 700
- 卡片副标题：#C7704F 陶土橙，等宽字体 Courier New
- 卡片描述：#4A3C31，字号 0.95rem，行高 1.6
- hover：上移 4px + box-shadow 增强
- 整张卡片链接至 /plan/{slug} 详情页
- 数据来源：plans 表（is_active=1，按 sort_order 排序）
  - 蒹葭计划（jianjia-plan）
  - 经纬计划（jingwei-plan）
  - 拾遗计划（shiyi-plan）

---

## 五、页脚设计

### 5.1 结构

- 背景 #F8F5F0（与页面一致）
- 顶部与正文之间：**1px solid #C4B9AE 暖灰分隔线**
- 两列平行网格，gap 8px：

**左列（4 项）**：首页（/）、关于我们（/about）、最新动态（/activities）、合作与支持（/contact）
**右列（4 项）**：研究成果（/output）、资源与工具（/resources）、研究力量（/team）、后台管理（/login）

页脚不含 LOGO、机构简介、社交媒体链接。

### 5.2 样式

- padding：10px 0 6px（紧凑）
- 链接字号 0.75rem，颜色 #4A3C31，行高 1.4
- 底部版权：上边框 1px solid #C4B9AE，字号 0.7rem，颜色 #6B6B6B
- 内容：© 2026 酷残未来研究院 Cripping Future Institute. All rights reserved.

---

## 六、最新动态页面（/activities）

### 6.1 页面结构

标题"最新动态"，下方两个独立区域：

**区域一：新闻动态（article_type="news"）**
- 展示 articles 表中 is_published=1 AND article_type="news" 的记录
- 按 created_at 倒序
- 卡片显示：标题（可点击 /article/{slug}）、摘要、发布日期、标签

**区域二：活动动态（article_type="event"）**
- 展示 articles 表中 is_published=1 AND article_type="event" 的记录
- 格式同上

---

## 七、研究成果页面（/output）

### 7.1 页面结构

标题"研究成果"，下方两个独立区域：

**区域一：研究报告（report_type="research"）**
- 展示 reports 表中 is_published=1 AND report_type="research" 的记录
- 卡片显示：标题（可点击 /report/{slug}）、摘要、发布日期、标签、PDF 下载链接

**区域二：残障生命故事（report_type="life_story"）**
- 展示 reports 表中 is_published=1 AND report_type="life_story" 的记录
- 格式与研究报告相同

---

## 八、资源与工具页面（/resources）

### 8.1 页面结构

**区域一：酷残学院**
- 展示 courses 表中 is_active=1 的课程
- 课程卡片：标题、简介、讲师、二维码、外部链接

**区域二：工具手册（books.type="book"）**
- 展示 books 表中 is_active=1 AND type="book" 的记录
- 显示：封面图、标题、作者、简介、购买/下载链接

**区域三：资源与工具（books.type="tool"）**
- 展示 books 表中 is_active=1 AND type="tool" 的记录
- 显示：标题、简介、文件下载链接（file_url）、购买链接

---

## 九、研究力量页面（/team）

### 9.1 页面结构

标题"研究力量"，下方两个独立区域：

**区域一：研究员团队**
- 展示 researchers 表中 is_active=1 的记录
- 每人显示：照片（圆形 120px）、姓名、职称、简介
- **主要工作成果**：从 achievements 字段（JSON 数组）解析，每条显示为可点击链接标签（title→url）

**区域二：社群行动者团队**
- 展示 community_activists 表中 is_active=1 的记录
- 格式与研究员相同

---

## 十、其他页面

### 10.1 关于我们（/about）

- 机构介绍：site_settings.org_description
- 三大计划简介卡片，链接 /plan/{slug}
- 发起人团队：founders 表，照片 + 姓名 + 职称 + 简介

### 10.2 文章详情页（/article/{slug}）

- 标题、发布日期、标签、正文
- 优先使用 content 字段，为空则用 summary

### 10.3 报告详情页（/report/{slug}）

- 标题、发布日期、标签、PDF 下载链接、正文
- 标注类型标签（研究报告 / 残障生命故事）

### 10.4 计划详情页（/plan/{slug}）

- 标题、副标题、正文（content 或 description）

### 10.5 酷残学院（/academy）

- courses 表课程列表

### 10.6 合作与支持（/contact）

- 邮箱、地址、社交媒体链接

### 10.7 搜索结果页（/search?q=关键词）

- 跨 articles/reports/courses 搜索
- 按时间倒序，标注类型标签

---

## 十一、后台管理

### 11.1 登录

- 路由：/login
- 管理员凭据：admin / cfi2026（环境变量 CFI_ADMIN_USER / CFI_ADMIN_PASSWORD 可覆盖）
- Session HMAC-SHA256 签名，有效期 24 小时

### 11.2 可管理数据表（共 11 张）

| 表名 | 显示名称 | 可编辑字段 |
|------|----------|-----------|
| site_settings | 网站设置 | value（键值对，含 org_name、org_slogan、org_description、org_email 等） |
| navigation | 导航管理 | title、title_en、url、sort_order、is_external |
| plans | 计划管理 | title、subtitle、description、content、slug、tags、sort_order、is_active |
| articles | 文章管理 | title、slug、summary、content、tags、article_type（下拉：新闻/活动）、is_published、is_featured、featured_image、featured_sort_order |
| reports | 报告管理 | title、slug、summary、content、tags、report_type（下拉：研究报告/生命故事）、pdf_filename、translator、source_url、is_published、is_featured、featured_image |
| researchers | 研究员管理 | name、slug、title、bio、photo、tags、is_active、achievements（动态编辑器：多组 title+url） |
| courses | 课程管理 | title、slug、description、instructor、qr_code、external_url、is_active |
| founders | 发起人管理 | name、slug、title、bio、photo、sort_order、is_active |
| books | 工具手册管理 | title、slug、author、summary、cover_image、buy_url、download_url、file_url（PDF上传）、type（下拉：手册/工具）、tags、sort_order、is_active |
| community_activists | 社群行动者管理 | name、slug、title、bio、photo、tags、sort_order、is_active、achievements（动态编辑器） |
| social_links | 社交媒体管理 | platform、url、icon、sort_order、is_active |

### 11.3 字段控件类型

- text：普通文本输入框
- textarea：多行文本（字段名含 content）
- checkbox：复选框（字段名以 is_ 开头）
- number：数字输入框（sort_order、featured_sort_order）
- select：下拉选择框（article_type、report_type、type）
- achievements：动态编辑器（可添加/删除多组 title + url 对，提交时序列化为 JSON）
- upload：文件上传按钮（photo、qr_code、cover_image、pdf_filename、file_url、featured_image），上传后预览缩略图（图片类）

### 11.4 文件上传

- 接口：POST /api/upload
- 限制：图片 ≤5MB（jpg/png），PDF ≤20MB
- 自动填入文件名到文本框

### 11.5 API 端点

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/{table} | 获取列表 |
| GET | /api/{table}/{id} | 获取单条 |
| POST | /api/{table} | 新增 |
| PUT | /api/{table}/{id} | 编辑 |
| DELETE | /api/{table}/{id} | 删除 |
| POST | /api/upload | 文件上传 |

所有 API 返回 JSON，需 Session 认证。

---

## 十二、数据库完整定义

### 12.1 表结构

**site_settings**
| 列 | 类型 | 约束 |
|----|------|------|
| key | TEXT | PRIMARY KEY |
| value | TEXT | NOT NULL DEFAULT '' |

种子数据：org_name（酷残未来研究院）、org_name_en（Cripping Future Institute）、org_slogan（以社群发展为手段进行知识生产）、org_description（以社群发展为手段进行知识生产，以知识生产为手段推动社群发展）、org_email、org_address、org_donation_info

**navigation**
| 列 | 类型 | 约束 |
|----|------|------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| title | TEXT | NOT NULL |
| title_en | TEXT | DEFAULT '' |
| url | TEXT | NOT NULL DEFAULT '/' |
| sort_order | INTEGER | NOT NULL DEFAULT 0 |
| is_external | INTEGER | NOT NULL DEFAULT 0 |

种子数据：7 条导航记录。

**plans**
| 列 | 类型 | 约束 |
|----|------|------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| title | TEXT | NOT NULL |
| subtitle | TEXT | DEFAULT '' |
| description | TEXT | NOT NULL DEFAULT '' |
| content | TEXT | DEFAULT '' |
| slug | TEXT | UNIQUE NOT NULL |
| tags | TEXT | DEFAULT '' |
| external_url | TEXT | DEFAULT '' |
| sort_order | INTEGER | NOT NULL DEFAULT 0 |
| is_active | INTEGER | NOT NULL DEFAULT 1 |
| created_at | TEXT | DEFAULT CURRENT_TIMESTAMP |
| updated_at | TEXT | DEFAULT CURRENT_TIMESTAMP |

种子数据：蒹葭/经纬/拾遗三条计划。

**articles**
| 列 | 类型 | 约束 |
|----|------|------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| title | TEXT | NOT NULL |
| slug | TEXT | UNIQUE NOT NULL |
| summary | TEXT | DEFAULT '' |
| content | TEXT | NOT NULL DEFAULT '' |
| tags | TEXT | DEFAULT '' |
| article_type | TEXT | NOT NULL DEFAULT 'news'（'news'=新闻, 'event'=活动） |
| is_published | INTEGER | NOT NULL DEFAULT 1 |
| is_featured | INTEGER | DEFAULT 0（首页轮播精选标记） |
| featured_image | TEXT | DEFAULT ''（轮播图片路径） |
| featured_sort_order | INTEGER | DEFAULT 0（轮播排序号） |
| created_at | TEXT | DEFAULT CURRENT_TIMESTAMP |
| updated_at | TEXT | DEFAULT CURRENT_TIMESTAMP |

**reports**
| 列 | 类型 | 约束 |
|----|------|------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| title | TEXT | NOT NULL |
| slug | TEXT | UNIQUE NOT NULL |
| summary | TEXT | DEFAULT '' |
| content | TEXT | NOT NULL DEFAULT '' |
| tags | TEXT | DEFAULT '' |
| report_type | TEXT | DEFAULT 'research'（'research'=研究报告, 'life_story'=残障生命故事） |
| pdf_filename | TEXT | DEFAULT '' |
| is_published | INTEGER | NOT NULL DEFAULT 1 |
| is_featured | INTEGER | DEFAULT 0 |
| featured_image | TEXT | DEFAULT '' |
| featured_sort_order | INTEGER | DEFAULT 0 |
| translator | TEXT | DEFAULT '' |
| source_url | TEXT | DEFAULT '' |
| created_at | TEXT | DEFAULT CURRENT_TIMESTAMP |
| updated_at | TEXT | DEFAULT CURRENT_TIMESTAMP |

**researchers**
| 列 | 类型 | 约束 |
|----|------|------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| name | TEXT | NOT NULL |
| slug | TEXT | UNIQUE NOT NULL |
| title | TEXT | DEFAULT '' |
| bio | TEXT | DEFAULT '' |
| photo | TEXT | DEFAULT '' |
| tags | TEXT | DEFAULT '' |
| achievements | TEXT | DEFAULT ''（JSON：[{"title":"...","url":"..."}]） |
| is_active | INTEGER | NOT NULL DEFAULT 1 |
| created_at | TEXT | DEFAULT CURRENT_TIMESTAMP |

**community_activists**
| 列 | 类型 | 约束 |
|----|------|------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| name | TEXT | NOT NULL |
| slug | TEXT | UNIQUE NOT NULL |
| title | TEXT | DEFAULT '' |
| bio | TEXT | DEFAULT '' |
| photo | TEXT | DEFAULT '' |
| tags | TEXT | DEFAULT '' |
| achievements | TEXT | DEFAULT ''（JSON 同上） |
| sort_order | INTEGER | NOT NULL DEFAULT 0 |
| is_active | INTEGER | NOT NULL DEFAULT 1 |
| created_at | TEXT | DEFAULT CURRENT_TIMESTAMP |

**courses**
| 列 | 类型 | 约束 |
|----|------|------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| title | TEXT | NOT NULL |
| slug | TEXT | UNIQUE NOT NULL |
| description | TEXT | DEFAULT '' |
| instructor | TEXT | DEFAULT '' |
| qr_code | TEXT | DEFAULT '' |
| external_url | TEXT | DEFAULT '' |
| is_active | INTEGER | NOT NULL DEFAULT 1 |
| created_at | TEXT | DEFAULT CURRENT_TIMESTAMP |

**founders**
| 列 | 类型 | 约束 |
|----|------|------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| name | TEXT | NOT NULL |
| slug | TEXT | UNIQUE NOT NULL |
| title | TEXT | DEFAULT '' |
| bio | TEXT | DEFAULT '' |
| photo | TEXT | DEFAULT '' |
| sort_order | INTEGER | NOT NULL DEFAULT 0 |
| is_active | INTEGER | NOT NULL DEFAULT 1 |
| created_at | TEXT | DEFAULT CURRENT_TIMESTAMP |

**books**
| 列 | 类型 | 约束 |
|----|------|------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| title | TEXT | NOT NULL |
| slug | TEXT | UNIQUE NOT NULL |
| author | TEXT | DEFAULT '' |
| summary | TEXT | DEFAULT '' |
| cover_image | TEXT | DEFAULT '' |
| buy_url | TEXT | DEFAULT '' |
| download_url | TEXT | DEFAULT '' |
| file_url | TEXT | DEFAULT ''（工具类文件/PDF 路径） |
| type | TEXT | NOT NULL DEFAULT 'book'（'book'=手册/图书, 'tool'=工具/资源） |
| tags | TEXT | DEFAULT '' |
| sort_order | INTEGER | NOT NULL DEFAULT 0 |
| is_active | INTEGER | NOT NULL DEFAULT 1 |
| created_at | TEXT | DEFAULT CURRENT_TIMESTAMP |

**social_links**
| 列 | 类型 | 约束 |
|----|------|------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| platform | TEXT | NOT NULL |
| url | TEXT | NOT NULL DEFAULT '' |
| icon | TEXT | DEFAULT '' |
| sort_order | INTEGER | NOT NULL DEFAULT 0 |
| is_active | INTEGER | NOT NULL DEFAULT 1 |

---

## 十三、非功能需求

### 13.1 技术栈

- 后端：Python 3 标准库 http.server（单文件 app.py）
- 数据库：SQLite（data/site.db）
- 前端：嵌入式 HTML + static/style.css + static/admin.js + static/a11y.js
- 文件上传存储：data/uploads/ 目录
- 轮播默认图生成：PIL（ensure_default_carousel）

### 13.2 无障碍

- skip-link 跳转到主要内容
- 语义化 HTML（header、main、nav、section、article、footer）
- aria-label 标注关键交互（轮播、导航、搜索）
- 高对比度模式切换（data-high-contrast）
- 字号缩放（A-/A+，--font-scale 变量）
- WCAG AA 对比度合规

### 13.3 安全

- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- Referrer-Policy: strict-origin-when-cross-origin
- 所有输出 HTML 转义（esc 函数）
- 参数化 SQL 查询
- Session HMAC-SHA256 签名
- 文件上传类型白名单（仅 jpg/jpeg/png/pdf）

### 13.4 部署

- 端口：7021（环境变量 CFI_PORT）
- 绑定：127.0.0.1（环境变量 CFI_HOST）
- 管理员：admin / cfi2026（环境变量可覆盖）
- 启动：python app.py
- 前台：http://127.0.0.1:7021/
- 后台：http://127.0.0.1:7021/login
