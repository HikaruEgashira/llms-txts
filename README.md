## 1. generate-llms-txt

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python: 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)

agnoを用いて与えられたキーワードを検索し、llms.txt形式で1ファイルにまとめるCLIツールです

## インストール

### 前提条件

- Python 3.10+
- Node.js（Playwrightの実行に必要）

### インストール手順

```bash
uv pip install -e .
uv pip install -e ".[dev]"
npx playwright install
```

## 使用方法

コマンドラインから以下のように実行します：

```bash
mise run generate-llms-txt "検索キーワード"
```

## 例

```bash
# "agno"に関する情報を検索して出力
mise run generate-llms-txt "agno.com"

# "claude"に関する情報を検索して、customフォルダに出力
mise run generate-llms-txt "claude" --output custom
```

## ライセンス

MIT License