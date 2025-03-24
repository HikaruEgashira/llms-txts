# Web Search Agent Example

This example demonstrates how to create an agent in Agno-AGI that can search the web for information. By integrating web search capabilities, the agent can access up-to-date information beyond its training data, provide more accurate responses, and verify facts.

## Overview

A web search agent in Agno-AGI consists of:
- A language model that powers the agent
- A description that defines the agent's persona and capabilities
- Web search tools that allow the agent to query the internet
- Instructions that guide how the agent uses search capabilities

This configuration is ideal for research assistance, answering current events questions, fact-checking, and providing up-to-date information.

## Implementation

Here's how to create a web search agent:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# Create a web search agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a research assistant who provides accurate and up-to-date information.",
    tools=[DuckDuckGoTools()],  # Add web search capability
    instructions=[
        "When you don't know something or need current information, use web search.",
        "Always cite your sources when providing information from the web.",
        "Summarize search results clearly and concisely."
    ],
    show_tool_calls=true,  # Show when tools are being used
    markdown=true
)

# Interact with the agent
agent.print_response("What are the latest developments in fusion energy?", stream=true)
```

## Running the Example

To run this example:

1. Install the required dependencies:
   ```bash
   pip install agno openai duckduckgo-search
   ```

2. Set up your environment variables:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

3. Save the code to a file (e.g., `web_search_agent.py`) and run it:
   ```bash
   python web_search_agent.py
   ```

## Key Components

### Web Search Tool

The DuckDuckGoTools integrates DuckDuckGo search capabilities into the agent:

```python
tools=[DuckDuckGoTools()]
```

This tool provides several methods:
- `search`: Performs a general web search
- `search_news`: Searches specifically for news articles
- `lookup`: Gets quick answers from DuckDuckGo's instant answers feature

### Tool Visibility

The `show_tool_calls=true` parameter makes the agent's tool usage visible in the output:

```python
show_tool_calls=true
```

This helps users understand when and how the agent is using web search to answer questions.

### Instructions

The instructions guide how the agent uses its search capabilities:

```python
instructions=[
    "When you don't know something or need current information, use web search.",
    "Always cite your sources when providing information from the web.",
    "Summarize search results clearly and concisely."
]
```

These instructions ensure the agent uses search appropriately and cites sources.

## Alternative Search Tools

Agno-AGI supports several search tools beyond DuckDuckGo:

```python
# Using Google Search (requires API key)
from agno.tools.google import GoogleSearchTools
tools=[GoogleSearchTools(api_key="your_google_api_key")]

# Using Bing Search (requires API key)
from agno.tools.bing import BingSearchTools
tools=[BingSearchTools(api_key="your_bing_api_key")]

# Using SerpAPI (requires API key)
from agno.tools.serpapi import SerpApiTools
tools=[SerpApiTools(api_key="your_serpapi_key")]
```

## Advanced Usage

### Combining Multiple Search Tools

You can combine multiple search tools for more comprehensive results:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools

# Create an agent with multiple search tools
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a comprehensive research assistant.",
    tools=[
        DuckDuckGoTools(),  # Web search
        WikipediaTools()    # Wikipedia-specific search
    ],
    instructions=[
        "Use Wikipedia for background information and established facts.",
        "Use web search for current events and recent developments.",
        "Always cite your sources."
    ],
    show_tool_calls=true,
    markdown=true
)
```

### Customizing Search Parameters

You can customize the search parameters when creating the tools:

```python
from agno.tools.duckduckgo import DuckDuckGoTools

# Custom search parameters
tools=[
    DuckDuckGoTools(
        max_results=5,        # Number of results to return
        time_period="d",      # Time period (d=day, w=week, m=month)
        region="us-en"        # Region and language
    )
]
```

## Best Practices

When implementing web search agents:

1. **Instruct Citation**: Always instruct the agent to cite sources
2. **Verify Information**: Use multiple sources for important facts
3. **Handle Ambiguity**: Teach the agent to acknowledge uncertainty
4. **Consider Privacy**: Be mindful of privacy implications of searches
5. **Rate Limiting**: Be aware of search API rate limits

## Next Steps

After implementing a web search agent, you can enhance it by:

1. [Adding knowledge bases](knowledge_agent.md) for domain-specific information
2. [Implementing memory](../concepts/memory.md) to remember previous searches
3. [Adding more tools](../concepts/tools.md) for expanded capabilities
4. [Creating multimodal agents](multimodal_agent.md) that can process images and other media