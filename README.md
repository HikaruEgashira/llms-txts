## llms.txt

Opinioned llms.txt generator. powerd by Agno AI Agent.

## List

- [agno](./docs/agno)
- [whisk](./docs/whisk)

## Generate llms.txt

```bash
mise run generate-llms-txt "agno.com"

mise run generate-llms-txt "claude" --output docs/claude
```

## Setup

```bash
uv pip install -e .
uv pip install -e ".[dev]"
npx playwright install
```

## License

MIT License
