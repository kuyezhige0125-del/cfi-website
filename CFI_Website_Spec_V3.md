# 酷残未来研究院（CFI）网站需求文档 V3

> 版本：V3.0 | 日期：2026-07-09
> 状态：待确认
> 基于 V2 规格书 + Gemini 设计参考 + 视觉系统深化

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

### 1.2 品牌视觉调性关键词

- 学术感（Academic）— 严谨但不刻板
- 社群感（Community）— 有温度、有生命力
- 酷残/Crip — 去污名化、边缘叙事、DIY 研究气质
- 克制 — 不商业化、不过度设计

### 1.3 设计参考来源

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
主色：      #DF4A16 (橙色)   — 仅作为功能性点缀色，不大面积平铺
背景色：    #FFF8ED (纸色)   — 大面积底色，减少视觉疲劳
深色背景：  #17130F (深褐)   — 页脚 / 深色区块
正文色：    #1A1A1A          — 正文文字
辅助灰：    #6B6B6B          — 次级文字 / 日期 / 元信息
边框色：    #2C2C2C          — 粗边框（学术感来源之一）
```

**橙色使用规范（仅限以下场景）：**
- 按钮（实心按钮背景）
- 导航栏当前激活状态
- 重要超链接悬停/激活态标签
- Hero 右侧色块区
- 高亮数字 / 编号

### 2.2 排版系统

| 层级 | 字重 | 字号（基准） | 说明 |
|------|------|-------------|------|
| Hero 大标题 | Bold / 900 | clamp(2rem, 4vw, 3rem) | 首页/页面主标题 |
| 区块标题 | Bold | 1.5rem | 各区块标题 |
| 卡片标题 | Semibold | 1.125rem | 计划/报告/新闻卡片 |
| 正文 | Regular | 1rem (16px) | 正文段落 |
| 元信息 / 标签 / 日期 / 编号 | Regular | 0.875rem | **使用 Courier New 字体** |
| 小字 / 脚注 | Regular | 0.75rem | 版权/辅助信息 |

**字体选择：**
- 正文字体：系统无衬线字体（-apple-system, "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif）
- **等宽字体用于**：所有标签（Tags）、日期、编号（01/02/03）、页码、代码块 → `"Courier New", "Noto Sans Mono CJK SC", monospace`
- 等宽字体目的：营造"档案感"和"DIY 研究"气息，契合残障自组织的边缘叙事调性

### 2.3 间距系统

- 基础间距单位：8px
- 区块间距：64px (8 × 8)
- 卡片内边距：24px (3 × 8)
- 段落间距：16px (2 × 8)
- 列间距：32px (4 × 8)

### 2.4 边框系统

- 粗边框（学术感来源）：区块分隔使用 4px 粗边框（颜色 #2C2C2C）
- 细边框：卡片内部分隔使用 1px 边框（颜色 #D4D0C8）
- 卡片悬浮效果：轻微上移（-4px）+ 阴影加深（border 不变）

### 2.5 Logo 使用

- 文件：`static/LOGO.jpg`（圆形 Logo，中文 + 英文）
- 导航栏：48×48px 圆形裁切
- 页脚：64×64px
- 始终保留完整 Logo（不单独使用图标）

---

## 三、技术架构

### 3.1 技术选型

| 项目 | 选择 | 理由 |
|------|------|------|
| 后端 | Python 3.10+ 标准库（http.server） | 零第三方依赖，部署简单 |
| 数据库 | SQLite | 零维护，备份即拷贝 |
| 前端渲染 | 后端生成 HTML（无框架） | 极简，无需构建步骤 |
| 部署 | Nginx 反向代理 + systemd | 稳定可靠 |
| HTTPS | Let's Encrypt / Certbot | 免费自动续签 |

### 3.2 路由设计

| 页面 | 路由 | 类型 | 说明 |
|------|------|------|------|
| 首页 | `/` | 一级页面 | Hero + 核心陈述 + 三大计划 + 动态 + 支持 |
| 关于 | `/about` | 一级页面 | 机构简介 / 背景 / 方法论 / 愿景 |
| 计划 | `/plans` | 一级页面 | 三大计划列表 |
| 计划详情 | `/plans/<slug>` | 详情页 | 单个计划详情 |
| 产出 | `/output` | 一级页面 | 研究报告（按类型 Tab 分类）+ 读书会/沙龙 |
| 社群 | `/community` | 一级页面 | 新闻动态 + 研究员名录 + 酷残学院 |
| 合作 | `/contact` | 一级页面 | 联系方式 + 支持方式 |
| 新闻详情 | `/articles/<slug>` | 详情页 | 单篇新闻正文 |
| 报告详情 | `/reports/<slug>` | 详情页 | 研究报告 + PDF 下载 |
| 研究员详情 | `/researchers/<slug>` | 详情页 | 照片 + 简介 + 发表列表 |
| 管理员登录 | `/admin` | 后台 | 登录页面 |
| 管理后台 | `/admin/dashboard` | 后台 | 管理仪表盘 |
| API 数据 | `/api/admin/content` | API | JSON 数据接口 |
| API 上传 | `/api/upload` | API | 文件上传 |
| 静态文件 | `/static/*` | 静态 | CSS/JS/图片 |

---

## 四、前台页面详细设计

### 4.1 全局组件

#### 4.1.1 顶部导航栏（sticky）

**布局：**
```
┌─────────────────────────────────────────────────────┐
│ [Logo] 酷残未来研究院 CFI  [首页] [关于] [计划] ... [A-] [A+] [HC] │
└─────────────────────────────────────────────────────┘
```

**规范：**
- 左侧：圆形 Logo（48×48 + object-fit: cover）+ 中文名 + 英文缩写
- 中间：导航菜单项（从数据库 `navigation` 表读取，后台可增删改排序）
- 右侧：无障碍控制按钮组
  - `A−`：减小字体（Normal → Large → XLarge → Normal 循环）
  - `A+`：增大字体
  - `HC`：高对比度切换
- 行为：sticky 定位，滚动吸顶，`backdrop-filter: blur(12px)` 毛玻璃效果
- 背景：底色 `rgba(255, 248, 237, 0.9)`，blur 效果
- 激活态导航项：底部 3px 橙色实线 + 橙色文字
- 无障碍：顶部 `<a href="#main" class="skip-link">跳到主要内容</a>`，focus 时可见

#### 4.1.2 页脚

**布局：**
```
┌─────────────────────────────────────────────────────┐
│ 酷残未来研究院 Cripping Future Institute             │
│ contact@crippingfuture.org                          │
│ [后台管理]                                           │
│ © 2026 Cripping Future Institute                    │
└─────────────────────────────────────────────────────┘
```

**规范：**
- 背景色：`#17130F`
- 文字色：`#FFF8ED`
- 链接色：`#DF4A16`
- 内边距：40px 上下
- 两列布局：左列机构信息，右列联系方式和链接

#### 4.1.3 无障碍控制系统

| 功能 | 实现方式 |
|------|----------|
| 字体缩放 | CSS 变量 `--font-scale`，三档：1 / 1.25 / 1.5 |
| 高对比度 | body class `.high-contrast`，覆盖所有颜色变量 |
| 持久化 | localStorage 保存偏好，下次访问自动恢复 |

high-contrast 模式下覆盖规则：
```css
.high-contrast { --bg: #000; --text: #fff; --border: #fff; --accent: #FF6B35; }
```

#### 4.1.4 Skip Link

- 页面第一个可聚焦元素
- 默认隐藏（position: absolute + left: -9999px）
- focus 时显示：从顶部滑入
- 跳转到 `<main id="main">` 元素

### 4.2 首页 `/`

#### 区块 1：Hero（首屏，80vh min-height）

**布局：两列 Grid，左侧 1.3fr / 右侧 0.7fr**

**左侧内容：**
- 小字：`CRIPPING FUTURE INSTITUTE`（Courier New，大写，橙色 `#DF4A16`，0.875rem）
- 大标题：来自后台设置 `hero_title`（支持 HTML，如"用社群力量<br>重塑未来"）
- 导语：来自后台设置 `hero_subtitle`
- 两个按钮：
  - 「查看三大计划」— 实心按钮（背景 `#DF4A16`，白色文字）
  - 「支持我们」— 描边按钮（边框 `#DF4A16`，透明背景）

**右侧内容：**
- 品牌参考图（400px 宽，`brand-reference.jpg`）
- 下方品牌标语卡片（橙色背景 `#DF4A16`，白色文字）

**背景：**
- 左侧 60% 纸色 `#FFF8ED`
- 右侧 40% 橙色 `#DF4A16`（渐变过渡）

#### 区块 2：核心陈述（Statement）

**布局：三列并排，移动端堆叠**

```
┌─────────────┬──────────────┬─────────────┐
│ 01           │ 02           │ 03           │
│ 关于我们     │ 背景与失语   │ 核心方法论   │
│ ……           │ ……           │ ……           │
└─────────────┴──────────────┴─────────────┘
```

- 编号使用 Courier New，橙色 `#DF4A16`，粗体
- 列之间使用 4px 粗边框（`#2C2C2C`）分隔
- 内容来自 site_settings（statement_01_title/body、statement_02_title/body、statement_03_title/body）

#### 区块 3：三大计划（深色背景 `#17130F`）

- 小标题标记："PLANS"（Courier New，橙色）
- 区块标题："三大行动计划"
- 三张卡片（Grid，`repeat(auto-fill, minmax(280px, 1fr))`，gap 24px）
- 每张卡片内容：
  - 编号（Courier New，大号，橙色）
  - 计划标题 + 副标题
  - 简短描述（截断）
  - 「了解更多 →」链接
- 卡片背景 `#2A2724`，边框 `#3D3935`
- 数据来源：`plans` 表，按 sort_order 排序

#### 区块 4：最新动态（Latest）

- 小标题标记："NEWS"（Courier New，橙色）
- 区块标题："最新动态"
- 展示最近 3-4 条已发布的 articles
- 每项：日期（Courier New，灰色）+ 标题 + 摘要截断
- 底部链接：「查看全部动态 →」

#### 区块 5：支持我们（Support）

- 小标题标记："SUPPORT"（Courier New，橙色）
- 区块标题："支持我们"
- 正文来自 site_settings `support_body`
- 联系/捐助方式说明
- 深色背景或纸色背景可配置

### 4.3 关于 `/about`

**区块结构（从上到下）：**

1. **Hero 小标题**："关于 — ABOUT"
2. **机构简介**：大标题（来自 site_settings `about_title`）+ 正文（`about_body`）
3. **背景与失语**：标题 + 正文（`background_title` + `background_body`）
4. **核心方法论**：标题 + 正文（`methodology_title` + `methodology_body`）
5. **战略愿景**：标题 + 正文（`vision_title` + `vision_body`）
6. 每个区块之间用 4px 粗边框分隔

### 4.4 计划 `/plans`

- 页面标题："三大行动计划"
- 计划卡片网格展示（所有 plans，按 sort_order 排序）
- 每张卡片内容：编号、标题、副标题、描述、外链（如有则显示「外部链接 →」）
- 点击卡片进入 `/plans/<slug>` 详情页

### 4.5 计划详情 `/plans/<slug>`

- 返回链接：「← 返回计划列表」
- 编号 + 标题 + 副标题
- 完整描述（支持段落）
- 如有 external_url，显示「查看外部项目 →」按钮（新标签打开）

### 4.6 产出 `/output`

**Tab 切换结构（纯前端 CSS Tab 或后端参数）：**

| Tab | 内容 |
|-----|------|
| 研究报告 | `report_type='research'` 的报告列表 |
| 读书会 | `report_type='reading'` 的报告列表 |
| 沙龙回顾 | `report_type='salon'` 的报告列表 |

**每项显示：**
- 标题（可点击进入详情）
- 摘要
- 标签（Courier New 风格标签）
- 日期（Courier New）
- 如有 PDF 则显示下载按钮

### 4.7 报告详情 `/reports/<slug>`

- 返回链接 + 面包屑
- 标题 + 发表日期
- 标签（可点击，跳转到 `/output?tag=<tagname>`）
- 完整正文（支持段落、引用）
- PDF 下载按钮（如有 `pdf_filename`）
- 相关报告：相同标签的其他报告

### 4.8 社群 `/community`

**分三个子区域：**

#### 区域 1：新闻动态
- 最新新闻列表（articles）
- 每项：日期 + 标题
- 「查看全部新闻 →」

#### 区域 2：研究员名录
- 研究员卡片网格（researchers，is_active=1）
- 每张卡片：照片（圆形裁切，120×120px）、姓名、title 头衔、标签
- 点击进入 `/researchers/<slug>` 详情页

#### 区域 3：酷残学院（Courses）
- 课程卡片列表
- 每张卡片：标题、讲师、简介
- 如有 QR code 则展示二维码
- 如有 external_url 则显示「前往学习 →」按钮

### 4.9 研究员详情 `/researchers/<slug>`

- 照片（大图，300px，圆形或圆角）
- 姓名 + 头衔
- 标签列表
- 个人简介 bio
- 关联作品：在 reports 表中搜索 tags 包含该研究员标签的报告列表

### 4.10 合作 `/contact`

- 联系邮箱
- 支持/捐助说明（来自 site_settings `support_body`）
- 其他联系方式（可后台配置）

---

## 五、后台管理系统

### 5.1 登录

- 路由：`/admin`
- 表单：用户名 + 密码
- 验证方式：Session（SECRET_KEY 签名）
- 失败提示：模糊提示（"用户名或密码错误"）

### 5.2 管理面板 `/admin/dashboard`

**左侧导航：9 个管理模块**

| 模块 | 说明 |
|------|------|
| 网站设置 | 编辑 site_settings 所有键值对 |
| 导航菜单 | 增删改导航项 + 排序 |
| 三大计划 | 增删改 plans |
| 新闻动态 | 增删改 articles |
| 研究报告 | 增删改 reports |
| 研究员 | 增删改 researchers |
| 酷残学院 | 增删改 courses |
| 文件管理 | 浏览/删除已上传文件 |
| 其他 | 占位 |

**每个模块：**
- 表格列表显示所有条目
- 「新增」按钮
- 每条记录：编辑按钮 + 删除按钮（带确认弹窗）
- 表单均为纯文本/文本域输入，兼容简单 HTML
- 报告类型：下拉选择（research/reading/salon）
- 研究员照片 / 课程二维码 / 报告 PDF：文本输入 + 「上传」按钮

### 5.3 API 接口

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/admin/content?type=<table>` | GET | 获取指定表所有数据（JSON） |
| `/api/admin/content?type=<table>&id=<id>` | GET | 获取单条数据 |
| `/api/admin/content` | POST | 保存数据（JSON body） |
| `/api/admin/content?type=<table>&id=<id>` | DELETE | 删除数据 |
| `/api/upload` | POST | 文件上传（multipart/form-data） |

### 5.4 上传功能

- 支持类型：图片（jpg/png ≤5MB）、PDF（≤20MB）
- 上传到 `data/uploads/` 目录
- 文件名：`{uuid}.{ext}` 避免冲突
- 返回 JSON：`{"ok":true, "filename":"abc123.jpg"}`

---

## 六、数据库设计

### 6.1 表结构

已定义在 `_gen_all.py`，共 7 张表：

1. **site_settings** (key TEXT PK, value TEXT)
2. **navigation** (id, title, title_en, url, sort_order, is_external)
3. **plans** (id, title, subtitle, description, slug UNIQUE, external_url, sort_order, is_active, created_at, updated_at)
4. **articles** (id, title, slug UNIQUE, summary, content, tags, is_published, created_at, updated_at)
5. **reports** (id, title, slug UNIQUE, summary, content, tags, report_type, pdf_filename, is_published, created_at, updated_at)
6. **researchers** (id, name, slug UNIQUE, title, bio, photo, tags, is_active, created_at)
7. **courses** (id, title, slug UNIQUE, description, instructor, qr_code, external_url, is_active, created_at)

### 6.2 默认数据

- 导航：首页、关于、计划、产出、社群、合作
- site_settings：hero_title、hero_subtitle、三个陈述、愿景、支持文案、footer_email

---

## 七、静态资源

| 路径 | 说明 | 状态 |
|------|------|------|
| `/static/style.css` | 主样式表（含高对比度模式） | ❌ 待编写 |
| `/static/a11y.js` | 无障碍脚本 | ❌ 待编写 |
| `/static/admin.js` | 后台管理前端脚本 | ❌ 待编写 |
| `/static/LOGO.jpg` | 圆形 Logo（48×48 / 64×64） | ✅ 已就位 |
| `/static/brand-reference.jpg` | 品牌参考图（Hero 区域用） | ✅ 已就位 |
| `/static/concept-image.jpg` | 概念布局图 | ✅ 已就位 |
| `/static/uploads/` | 用户上传文件目录 | ❌ 待创建 |

### Logo 信息

- 文件：`static/LOGO.jpg`
- 尺寸：原始约 500×500px 正方形
- 内容："酷残未来研究院" + "Cripping Future Institute"
- 使用方式：
  - 导航栏：48×48px，`object-fit: cover; border-radius: 50%`
  - 页脚：64×64px，同上
  - 始终配套机构名称使用，不单独展示

---

## 八、无障碍设计（WCAG 2.1 AA）

### 8.1 已覆盖

- ✅ 颜色对比度：所有前景/背景组合 ≥ 4.5:1
- ✅ Skip Link
- ✅ 语义化 HTML（h1-h6、nav、main、footer、article、section）
- ✅ 键盘可导航
- ✅ 字体缩放三档（CSS var + JS 切换）
- ✅ 高对比度模式
- ✅ localStorage 持久化偏好
- ✅ Focus 样式可见（2px outline + 2px offset）
- ✅ 图片 alt 属性

### 8.2 待补充

- ARIA labels 和 landmarks
- 屏幕朗读测试
- 打印样式

---

## 九、部署方案

### 9.1 服务器要求

- OS：Ubuntu 22.04 / Debian 12
- Python 3.10+
- Nginx + systemd + Certbot

### 9.2 目录结构（部署后）

```
/opt/cfi-site/
├── app.py              # 主程序
├── .env                # 环境变量
├── data/
│   ├── site.db         # SQLite 数据库
│   └── uploads/        # 上传文件
├── static/
│   ├── style.css
│   ├── a11y.js
│   ├── admin.js
│   ├── LOGO.jpg
│   ├── brand-reference.jpg
│   └── concept-image.jpg
├── deploy/
│   ├── cfi-site.service
│   └── nginx.conf
├── DEPLOY.md
└── README.md
```

### 9.3 环境变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| CFI_ENV | development | 运行环境 |
| CFI_HOST | 127.0.0.1 | 监听地址 |
| CFI_PORT | 7010 | 监听端口 |
| CFI_ADMIN_USER | admin | 管理员用户名 |
| CFI_ADMIN_PASSWORD | cfi2026 | 管理员密码 |
| CFI_SECRET | 自动生成 | Session 密钥 |

### 9.4 Nginx 反向代理

```nginx
server {
    listen 80;
    server_name your-domain.com;
    client_max_body_size 20m;
    location / {
        proxy_pass http://127.0.0.1:7010;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 9.5 systemd 服务

```ini
[Unit]
Description=CFI Website
After=network.target

[Service]
Type=simple
WorkingDirectory=/opt/cfi-site
EnvironmentFile=/opt/cfi-site/.env
ExecStart=/usr/bin/python3 /opt/cfi-site/app.py
User=www-data
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

---

## 十、未包含（后续迭代）

| 功能 | 说明 |
|------|------|
| 英文版本 | 全站中英双语，路由 `/en/...` |
| 搜索功能 | 全站搜索 + 按类型筛选 + 分页 |
| SEO 优化 | 独立 title/description、OG 标签、sitemap.xml、robots.txt |
| 上传按钮前端 | 后台文件上传按钮 + 图片预览 |

---

## 十一、验收标准

### 11.1 功能检查

- [ ] 6 个一级页面 + 所有详情页正常渲染
- [ ] 后台 9 个管理模块均可 CRUD
- [ ] 导航菜单后台可自定义
- [ ] 字体缩放（3 档）准确生效
- [ ] 高对比度模式所有页面覆盖
- [ ] 偏好 localStorage 持久化
- [ ] 研究报告 PDF 上传和下载
- [ ] 图片上传

### 11.2 视觉检查

- [ ] 橙色仅出现在规范允许的场景
- [ ] 等宽字体（Courier New）用于标签/日期/编号
- [ ] 首页 Hero 布局正确（两列 + 渐变色）
- [ ] 核心陈述三列 + 4px 粗边框分隔
- [ ] 三大计划深色卡片区
- [ ] 研究员圆形照片裁切
- [ ] 毛玻璃导航栏效果
- [ ] 页脚深色背景

### 11.3 无障碍检查

- [ ] WCAG 2.1 AA 对比度达标
- [ ] Skip Link 可见且可用
- [ ] 键盘 Tab 顺序正确
- [ ] Focus 样式清晰可见

### 11.4 部署检查

- [ ] Python 标准库零依赖
- [ ] `python app.py` 直接启动
- [ ] Nginx + systemd 可正常工作

---

> **文档结束**
> 本文档为 V3 版完整需求规格书。请确认后开始实现。
