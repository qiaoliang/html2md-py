# html-to-markdown

一个现代化的、完全类型安全的 Python 库，用于将 HTML 转换为 Markdown。这个库是 [markdownify](https://pypi.org/project/markdownify/) 的完全重写版本，具有现代化的代码库、严格的类型安全性和 Python 3.9+ 支持。

## 特性

- 完整的类型安全，严格遵循 MyPy 规范
- 函数式 API 设计
- 全面的测试覆盖
- 可配置的转换选项
- 命令行工具支持
- 支持预配置的 BeautifulSoup 实例
- 严格的语义版本控制

## 项目结构

```
html-to-markdown/
├── html_to_markdown/          # 主包目录
│   ├── cli.py                # 命令行接口
│   ├── converters.py         # HTML 到 Markdown 的转换器
│   ├── processing.py         # 核心处理逻辑
│   ├── utils.py             # 工具函数
│   ├── constants.py         # 常量和默认值
│   └── scripts.py           # CLI 入口点
├── tests/                    # 测试套件
│   ├── cli_test.py          # CLI 测试
│   ├── integration_test.py  # 集成测试
│   ├── module_test.py       # 模块测试
│   └── conftest.py          # 测试配置
├── pyproject.toml           # 项目配置
└── README.md               # 说明文件
```

## 安装

### 使用 pip

```shell
pip install html-to-markdown
```

### 使用 Poetry

```shell
poetry add html-to-markdown
```

### 开发环境安装

1. 克隆仓库：
   ```shell
   git clone https://github.com/yourusername/html-to-markdown.git
   cd html-to-markdown
   ```

2. 安装依赖：
   ```shell
   poetry install
   ```

3. 安装预提交钩子：
   ```shell
   pre-commit install && pre-commit install --hook-type commit-msg
   ```

## 快速开始

使用单个函数调用将 HTML 转换为 Markdown：

```python
from html_to_markdown import convert_to_markdown

html = '''
<article>
    <h1>欢迎</h1>
    <p>这是一个<strong>示例</strong>，包含一个<a href="https://example.com">链接</a>。</p>
    <ul>
        <li>项目 1</li>
        <li>项目 2</li>
    </ul>
</article>
'''

markdown = convert_to_markdown(html)
print(markdown)
```

输出：

```markdown
# 欢迎

这是一个**示例**，包含一个[链接](https://example.com)。

* 项目 1
* 项目 2
```

### 使用 BeautifulSoup

如果你需要更多对 HTML 解析的控制，可以传入预配置的 BeautifulSoup 实例：

```python
from bs4 import BeautifulSoup
from html_to_markdown import convert_to_markdown

# 使用你喜欢的解析器配置 BeautifulSoup
soup = BeautifulSoup(html, 'lxml')  # 注意：lxml 需要额外安装
markdown = convert_to_markdown(soup)
```

## 高级用法

### 自定义转换选项

该库提供了丰富的自定义选项：

```python
from html_to_markdown import convert_to_markdown

html = '<div>你的内容...</div>'
markdown = convert_to_markdown(
    html,
    heading_style="atx",  # 使用 # 样式的标题
    strong_em_symbol="*",  # 使用 * 表示粗体/斜体
    bullets="*+-",  # 定义列表符号
    wrap=True,  # 启用文本换行
    wrap_width=100,  # 设置换行宽度
    escape_asterisks=True,  # 转义 * 字符
    code_language="python"  # 默认代码块语言
)
```

### 配置选项

| 选项                | 类型  | 默认值         | 描述                                                |
|---------------------|-------|----------------|-----------------------------------------------------|
| `autolinks`         | bool  | `True`         | 自动将 URL 转换为 Markdown 链接                     |
| `bullets`           | str   | `'*+-'`        | 用于列表项的符号                                    |
| `code_language`     | str   | `''`           | 代码块的默认语言                                    |
| `heading_style`     | str   | `'underlined'` | 标题样式（`'underlined'`、`'atx'`、`'atx_closed'`）|
| `escape_asterisks`  | bool  | `True`         | 转义 * 字符                                         |
| `escape_underscores`| bool  | `True`         | 转义 _ 字符                                         |
| `wrap`              | bool  | `False`        | 启用文本换行                                        |
| `wrap_width`        | int   | `80`           | 文本换行宽度                                        |

完整的配置选项列表，请参见下面的[配置](#配置)部分。

## 命令行使用

直接从命令行转换 HTML 文件：

```shell
# 转换文件
html_to_markdown input.html > output.md

# 处理标准输入
cat input.html | html_to_markdown > output.md

# 使用自定义选项
html_to_markdown --heading-style atx --wrap --wrap-width 100 input.html > output.md
```

### 命令行示例

1. 使用 ATX 标题样式：
   ```shell
   html_to_markdown input.html --heading-style atx > output.md
   ```

2. 使用下划线表示强调：
   ```shell
   html_to_markdown input.html --strong-em-symbol _ > output.md
   ```

3. 设置代码块语言：
   ```shell
   html_to_markdown input.html --code-language python > output.md
   ```

4. 自定义列表符号：
   ```shell
   html_to_markdown input.html --bullets "•-" > output.md
   ```

5. 移除特定标签：
   ```shell
   html_to_markdown input.html --strip script style > output.md
   ```

查看所有可用选项：
```shell
html_to_markdown --help
```

## 从 Markdownify 迁移

对于使用 Markdownify 的现有项目，提供了兼容层：

```python
# 旧代码
from markdownify import markdownify as md

# 新代码 - 功能相同
from html_to_markdown import markdownify as md
```

`markdownify` 函数是 `convert_to_markdown` 的别名，提供相同的功能。

## 配置

完整的配置选项列表：

- `autolinks`：自动将有效的 URL 转换为 Markdown 链接
- `bullets`：用于列表项的符号
- `code_language`：代码块的默认语言
- `code_language_callback`：用于确定代码块语言的函数
- `convert`：要转换的 HTML 标签列表（None = 所有支持的标签）
- `default_title`：为链接等元素使用默认标题
- `escape_asterisks`：转义 * 字符
- `escape_misc`：转义其他 Markdown 字符
- `escape_underscores`：转义 _ 字符
- `heading_style`：标题样式（underlined/atx/atx_closed）
- `keep_inline_images_in`：保留内联图片的标签
- `newline_style`：处理换行的样式（spaces/backslash）
- `strip`：要从输出中移除的标签
- `strong_em_symbol`：用于粗体/斜体文本的符号（* 或 _）
- `sub_symbol`：用于下标文本的符号
- `sup_symbol`：用于上标文本的符号
- `wrap`：启用文本换行
- `wrap_width`：文本换行宽度
- `convert_as_inline`：将内容作为内联元素处理

## 贡献

本库欢迎贡献。欢迎提交问题或 PR。在提交 PR 之前最好先讨论问题，以避免失望。

### 本地开发

1. 克隆仓库
2. 安装系统依赖
3. 使用 `poetry install` 安装完整依赖
4. 安装预提交钩子：
   ```shell
   pre-commit install && pre-commit install --hook-type commit-msg
   ```
5. 进行修改并提交 PR

## 许可证

本库使用 MIT 许可证。

## 致谢

特别感谢 [markdownify](https://pypi.org/project/markdownify/) 项目的原作者和贡献者。 