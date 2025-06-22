## llms.txt

Opinioned llms.txt generator. powerd by Agno AI Agent.

## List

- [agno](./docs/agno)
- [whisk](./docs/whisk)

## Usage

### Using uvx (Recommended)

```bash
# ローカルディレクトリから実行
uvx --from . generate-llms-txt "agno.com"

# GitHub（SSH）から直接実行
uvx --from "git+ssh://git@github.com/HikaruEgashira/llms-txts.git" generate-llms-txt "agno.com"
```

### Using pipx

```bash
# ローカルからインストール
pipx install .

# GitHub（SSH）からインストール
pipx install git+ssh://git@github.com/HikaruEgashira/llms-txts.git

# 実行
generate-llms-txt "agno.com"
```

### Options

```bash
generate-llms-txt --help
# Usage: generate-llms-txt [OPTIONS] KEYWORD
# 
# Options:
#   -o, --output TEXT  Output folder name
#   -f, --force        Remove existing output and tmp folders
#   --help             Show this message and exit.
```

## Development

### Generate llms.txt

```bash
mise run generate-llms-txt "agno.com"

mise run generate-llms-txt "claude" --output docs/claude
```

### Setup

```bash
uv pip install -e .
uv pip install -e ".[dev]"
npx playwright install
```

## License

MIT License
