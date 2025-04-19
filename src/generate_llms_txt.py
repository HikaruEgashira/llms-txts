import os
import click
import asyncio
from agno.agent import Agent
from agno.tools.mcp import MCPTools
from agno.models.anthropic import Claude
from agno.storage.agent.sqlite import SqliteAgentStorage
from mcp import StdioServerParameters
import shutil


async def write_file(file_path: str, content: str) -> None:
    """
    Asynchronously writes content to a file.
    Args:
        file_path (str): The relative path to the file where content will be written.
        content (str): The content to write to the file.
    Returns:
        None
    Note:
        This function overwrites any existing content in the file.
        The file is written using UTF-8 encoding.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


async def runAgent(keyword: str, output_folder: str):
    server_params = StdioServerParameters(
        command="npx",
        args=[
            "@playwright/mcp@latest",
            "--headless"
        ],
        env={
            "NODE_OPTIONS": "--no-warnings",
        },
    )

    async with MCPTools(server_params=server_params) as mcp_tools:
        agent = Agent(
            model=Claude(
                id="claude-3-7-sonnet-20250219",
                thinking={"type": "enabled", "budget_tokens": 1024},
            ),
            tools=[mcp_tools, write_file],
            storage=SqliteAgentStorage(
                table_name="agent_sessions", db_file="tmp/agent_storage.db"
            ),
            add_history_to_messages=True,
            num_history_responses=3,
            show_tool_calls=True,
            markdown=True,
            retries=2,
        )

        await agent.aprint_response(
            f'''You are research agent for expressing conceptual models in llms.txt.

        <reference>
        llms.txt specification: https://llmstxt.org/index.md
        working directory: {output_folder}
        </reference>

        <step>
        1. Check all hierarchies of llms.txt specification.
        2. Search keyword in bing.
        3. Crawl all hierarchies of official documentations.
        5. Create conceptual model in llms.txt
        6. Create concept_name.md files for each concept and summarize more detailed conceptual models for that concept.
        </step>

        <task>
        Create llms.txt for keyword:"{keyword}".
        </task>
        '''
        )


@click.command()
@click.argument("keyword", type=str)
@click.option("--output", "-o", default="out", help="Output folder name")
@click.option(
    "--force", "-f", is_flag=True, help="Remove existing output and tmp folders"
)
def main(keyword: str, output: str, force: bool) -> None:
    if force:
        if os.path.exists(output):
            shutil.rmtree(output)
        if os.path.exists("tmp"):
            shutil.rmtree("tmp")

    os.makedirs(output, exist_ok=True)
    asyncio.run(runAgent(keyword, output))
    click.echo(f"Search results saved to {output}")


if __name__ == "__main__":
    main()
