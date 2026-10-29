# rein-paper-template

[English](README.md) | 简体中文

Rein Protocol Foundation 的 LaTeX 论文模板，适合录用后的作者版本、技术报告与预印本。使用官网现有 R 标识、Foundation 英文全称与暖黑/橙色配色。

## 模板效果预览

以下为单栏与双栏模板的首页截图，点击图片可查看大图。

| 单栏 · 作者–年份引用 | 双栏 · 数字引用 |
| --- | --- |
| [![单栏论文模板首页预览](docs/previews/single-column.png)](docs/previews/single-column.png) | [![双栏论文模板首页预览](docs/previews/double-column.png)](docs/previews/double-column.png) |
| [查看完整单栏 PDF](output/REIN-single-column.pdf) | [查看完整双栏 PDF](output/REIN-double-column.pdf) |

## 从 GitHub 创建自己的论文仓库

点击本仓库的 **Use this template → Create a new repository**，即可在自己的账号或组织下创建论文仓库。

## 直接使用

下载 `output/REIN-complete-Overleaf-kit.zip` 并上传 Overleaf。选择 **pdfLaTeX**：

- `main.tex`：单栏，作者–年份引用。
- `main-double.tex`：双栏，数字引用。

只需要一种版式时，下载对应的 `REIN-single-column-Overleaf.zip` 或 `REIN-double-column-Overleaf.zip`，其入口均为 `main.tex`。`output/` 同时提供两份 PDF 预览。

## 改成自己的论文

1. 编辑 `paper-info-single.tex` 或 `paper-info-double.tex`：题目、真实作者、单位、邮箱、短标题、关键词。
2. 将 `\reinstatus{RESEARCH TEMPLATE}` 改为 `\reinstatus{AUTHOR ACCEPTED MANUSCRIPT}`，填写真实版本号。模板本身没有录用声明。
3. 用实际论文替换 `sections/single/` 或 `sections/double/` 中的教学示例；替换 `references.bib`、插图与实验结果。
4. 在正文添加真实会议/期刊名称、年份、DOI 及需要的出版说明。按出版方允许的作者版本与格式要求上传；本模板不替代会议官方 camera-ready 样式。
5. 按需启用 `\reinproject[标签]{URL}`、`\reingithub{URL}`、`\reindataset[标签]{URL}`。这些链接默认不显示，不要把机构首页误作论文实验资源。

Foundation 官网：https://rein-protocol.org 。示例作者和邮箱均为占位符，不代表实际作者或研究成果。

## 可选功能

- `\reinorcid{真实 ORCID}`：在作者名后添加 ORCID 链接。
- `\reinpartner{机构名称}{assets/partner-logo.pdf}`：添加合作机构 Logo；默认隐藏。
- `\reinacknowledgments{...}`：致谢。
- `anonymous` 类选项：隐藏模板管理的作者、机构、Logo、资源链接、致谢与身份元数据。正文、自引和自带图片仍需自行检查。
- `monochrome` 类选项：正文使用灰度配色；正式 Logo 保留原始品牌颜色。

共享类为 `reinpaper.cls`，命令前缀为 `\rein`；公式中的 `\star` 仍是数学符号。

## 本地编译与打包

### 先安装依赖

这些工具**并非操作系统默认自带**，脚本也不会自动安装它们。

- **Python 3**：通过 [python.org](https://www.python.org/downloads/) 或系统包管理器安装。两个脚本仅使用 Python 标准库，不需要 `pip install` 或 `requirements.txt`。
- **TeX 工具链**：选择下面一种方案。LaTeX 宏包和字体不是 Python 库。
- **Git**：仅克隆仓库需要；也可下载并解压仓库 ZIP。

**方案 A：TeX Live / MacTeX（pdfLaTeX）。** macOS 安装完整的 [MacTeX](https://tug.org/mactex/)；Linux 或 Windows 按 [TeX Live 安装指南](https://tug.org/texlive/quickinstall.html)选择 full scheme。完整发行版包含模板使用的宏包和字体，精简安装可能缺包。安装后重新打开终端，确保 TeX 可执行文件目录位于 `PATH`。

编译前检查：

```bash
python3 --version
latexmk -v
pdflatex --version
bibtex --version
```

Windows 如果使用 Python launcher，将所有命令中的 `python3` 替换为 `py -3`。

**方案 B：Tectonic。** 按[官方安装说明](https://tectonic-typesetting.github.io/book/latest/installation/)安装。macOS 已有 Homebrew 时可运行：

```bash
brew install tectonic
tectonic --version
```

Tectonic 编译时会下载所需 TeX 资源，首次编译需要联网。`--offline` 只使用缓存，资源不完整时会失败。Tectonic 与 pdfLaTeX 使用不同引擎，字体和换行可能存在差异。

### 编译 PDF

```bash
git clone https://github.com/rein-protocol-foundation/rein-paper-template.git
cd rein-paper-template
python3 scripts/build.py
```

脚本优先选择 `latexmk`，未找到时才选择 Tectonic。也可显式指定：

```bash
python3 scripts/build.py --engine tectonic
```

若缺少 `.sty` 文件或字体，请通过 TeX 发行版的包管理器安装（不是 `pip`），或使用上述完整发行版。编译日志位于 `build/<layout>/compile.log`。若缺少可执行文件，先安装并配置 `PATH`，再重试。

### 打包 Overleaf（可选）

```bash
python3 scripts/package.py
```

打包**只需要 Python 3**，不会编译或刷新 PDF。修改论文后若需要更新 PDF 预览，应先运行编译步骤。中间文件保存在忽略的 `build/`，PDF 和 ZIP 写入 `output/`。Overleaf 包仅包含英文内容，不包含私有资料、构建缓存或他人的论文。

使用 Overleaf 时，直接上传提供的 ZIP 并选择 **pdfLaTeX** 即可，无需在本机安装 Python 或 TeX。

## 来源

上游来源、固定版本与授权状态见 [PROVENANCE.md](PROVENANCE.md)。来源说明不出现在论文排版中。此目录独立于网站代码，不依赖 Node.js 或 Next.js。
