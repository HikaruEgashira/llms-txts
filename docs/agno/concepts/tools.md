# Tools

Tools in Agno-AGI enable agents to interact with the external world, access information, and perform actions beyond their inherent capabilities. Tools expand what agents can do, allowing them to search the web, access databases, generate images, and much more.

## Core Concept

Tools are function-like interfaces that agents can invoke to:
- Retrieve information from external sources
- Perform actions in external systems
- Process or generate different types of content
- Interact with APIs and services

Agno-AGI implements tools as Python classes with well-defined interfaces that describe their capabilities to the agent. When an agent needs to use a tool, it generates a structured call that the Agno framework interprets and executes.

## Tool Categories

Agno-AGI tools generally fall into several categories:

1. **Information Retrieval Tools**: Search engines, knowledge bases, etc.
2. **Content Generation Tools**: Image generation, audio creation, etc.
3. **Utility Tools**: Math calculations, code execution, etc.
4. **API Integration Tools**: Weather services, news APIs, etc.
5. **Database Tools**: Query and manipulation of structured data

## Built-in Tools

Agno-AGI includes numerous built-in tools:

- **DuckDuckGoTools**: Web search functionality
- **YFinanceTools**: Financial data and stock information
- **WikipediaTools**: Access to Wikipedia content
- **PythonREPLTools**: Python code execution
- **FileTools**: File operations (read, write, list)
- **ImageTools**: Image processing and generation
- **CalendarTools**: Calendar operations and scheduling
- **MathTools**: Mathematical calculations
- **URLTools**: URL operations and web content fetching

## Tool Integration

Integrating tools with an agent follows a simple pattern:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

# Create an agent with multiple tools
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a research assistant",
    tools=[
        DuckDuckGoTools(),  # Web search
        YFinanceTools(stock_price=true)  # Financial data
    ],
    show_tool_calls=true,  # Shows tool calls in output
    markdown=true
)

# The agent can now use these tools
agent.print_response("What's the current price of AAPL stock?", stream=true)
```

## Custom Tools

Developers can create custom tools by subclassing `BaseTool`:

```python
from agno.tools.base import BaseTool
from pydantic import Field
from typing import Dict, Any

class WeatherTool(BaseTool):
    """Tool to get weather information for a location."""
    
    name = "weather_tool"
    
    def get_weather(self, location: str = Field(..., description="The location to get weather for")) -> Dict[str, Any]:
        """Get the current weather for a location."""
        # Implementation details
        return {"temperature": 72, "conditions": "sunny", "location": location}
```

## Tool Composition

Agno-AGI supports tool composition through:

1. **Tool Groups**: Combining related tools into functional groups
2. **Tool Hierarchies**: Creating relationships between tools
3. **Multi-Agent Tool Use**: Distributing tools across specialized agents

## Design Considerations

When working with tools in Agno-AGI:

1. **Tool Complexity**: Balance between simplicity and functionality
2. **Tool Selection**: Provide only tools relevant to the agent's purpose
3. **Error Handling**: Robust handling of tool failures
4. **Authentication**: Secure management of API keys and credentials
5. **Rate Limiting**: Respect API rate limits and quotas