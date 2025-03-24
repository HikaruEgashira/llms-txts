# Getting Started with Agno-AGI

This guide will help you build your first Agno-AGI agent, explaining the core concepts and basic implementation patterns.

## Prerequisites

Before getting started with Agno-AGI, ensure you have:

1. **Python 3.9+** installed on your system
2. **API keys** for the LLM provider(s) you plan to use (e.g., OpenAI, Anthropic)
3. Basic familiarity with Python programming

## Installation

Install Agno-AGI using pip:

```bash
pip install -U agno
```

For development installation with all dependencies:

```bash
pip install -U "agno[dev]"
```

## Environment Setup

Set up your environment variables for the LLM providers you'll use:

```bash
# For OpenAI
export OPENAI_API_KEY=your_api_key_here

# For Anthropic
export ANTHROPIC_API_KEY=your_api_key_here

# For Google
export GOOGLE_API_KEY=your_api_key_here
```

## Creating Your First Agent

Let's create a simple agent that responds to basic queries:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Create a basic agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful assistant with a friendly personality.",
    markdown=true
)

# Test the agent
agent.print_response("Hello! What can you do for me?", stream=true)
```

Save this code to a file (e.g., `first_agent.py`) and run it:

```bash
python first_agent.py
```

## Adding Tools to Your Agent

Let's enhance our agent by adding a web search capability:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# Install required dependencies
# pip install duckduckgo-search

# Create an agent with web search capability
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful research assistant.",
    tools=[DuckDuckGoTools()],
    show_tool_calls=true,  # Show when tools are being used
    markdown=true
)

# Test the agent with a question that requires searching
agent.print_response("What are the latest developments in quantum computing?", stream=true)
```

## Creating an Agent with Knowledge

Now, let's create an agent with domain-specific knowledge:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType

# Install required dependencies
# pip install lancedb tantivy pypdf

# Create a knowledge base from a PDF
knowledge = PDFUrlKnowledgeBase(
    urls=["https://path/to/your/document.pdf"],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="documents",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)

# Create an agent with knowledge
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a subject matter expert.",
    knowledge=knowledge,
    instructions=[
        "Search your knowledge base for information",
        "If the knowledge base doesn't have the answer, say so"
    ],
    markdown=true
)

# Load the knowledge base (do this once)
if agent.knowledge is not null:
    agent.knowledge.load()

# Test the agent with domain-specific questions
agent.print_response("Tell me about the specific topic in the document", stream=true)
```

## Building a Multi-Agent Team

Finally, let's create a team of specialized agents:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

# Install required dependencies
# pip install duckduckgo-search yfinance

# Create specialist agents
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=true,
    markdown=true,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=true, analyst_recommendations=true)],
    instructions="Use tables to display data",
    show_tool_calls=true,
    markdown=true,
)

# Create a team with a coordinator
agent_team = Agent(
    mode="coordinate",
    members=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-4o"),
    success_criteria="A comprehensive report with clear sections and data-driven insights.",
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=true,
    markdown=true,
)

# Test the team with a complex query
agent_team.print_response("What's the market outlook for AI chip manufacturers?", stream=true)
```

## Next Steps

After getting familiar with the basics of Agno-AGI, consider exploring:

1. **Additional Tools**: Explore the range of tools available in Agno-AGI
2. **Custom Tools**: Create your own tools for specific use cases
3. **Memory Integration**: Add memory capabilities to your agents
4. **Advanced Workflows**: Build more complex agent workflows
5. **Monitoring**: Set up monitoring for your agents on agno.com

Refer to the [Agno-AGI documentation](https://docs.agno.com) for comprehensive information on all these topics.