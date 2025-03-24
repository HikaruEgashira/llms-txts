# Basic Agent Example

This example demonstrates how to create and use a simple agent in Agno-AGI. The basic agent represents the simplest possible implementation - an agent without tools, memory, or knowledge that simply performs inference tasks.

## Overview

A basic agent in Agno-AGI consists of:
- A language model that powers the agent
- A description that defines the agent's persona and capabilities
- Optional instructions that guide the agent's behavior

This minimal configuration is perfect for simple conversational tasks, creative content generation, or basic information retrieval from the model's parametric knowledge.

## Implementation

Here's how to create a basic agent:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Create a basic agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    markdown=true  # Enable markdown formatting in responses
)

# Interact with the agent
agent.print_response("Tell me about a breaking news story from New York.", stream=true)
```

## Running the Example

To run this example:

1. Install the required dependencies:
   ```bash
   pip install agno openai
   ```

2. Set up your environment variables:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

3. Save the code to a file (e.g., `basic_agent.py`) and run it:
   ```bash
   python basic_agent.py
   ```

## Key Components

### Model Selection

The model is the foundation of the agent. In this example, we're using OpenAI's GPT-4o:

```python
model=OpenAIChat(id="gpt-4o")
```

You can substitute other models:

```python
# Using GPT-3.5-Turbo
model=OpenAIChat(id="gpt-3.5-turbo")

# Using Claude
from agno.models.anthropic import AnthropicChat
model=AnthropicChat(id="claude-3-opus-20240229")

# Using Gemini
from agno.models.google import GoogleChat
model=GoogleChat(id="gemini-1.5-pro")
```

### Agent Description

The description establishes the agent's persona and behavior:

```python
description="You are an enthusiastic news reporter with a flair for storytelling!"
```

This tells the agent how to "act" when responding to queries. Different descriptions will yield different response styles.

### Response Formatting

The `markdown=true` parameter enables markdown formatting in responses, making them more readable with headings, lists, and other formatting:

```python
markdown=true
```

### Streaming Responses

The `stream=true` parameter enables real-time streaming of responses:

```python
agent.print_response("Tell me about a breaking news story from New York.", stream=true)
```

This provides a more interactive experience as responses appear gradually rather than all at once.

## Limitations

The basic agent has several limitations:

1. **No External Information**: It can only access information from its training data
2. **No Tool Usage**: It cannot perform actions like web searches
3. **No Memory**: It doesn't remember previous interactions
4. **No Knowledge Base**: It cannot access domain-specific information

These limitations make it suitable for simple tasks but inadequate for more complex applications.

## Enhanced Basic Agent

You can enhance the basic agent with additional parameters:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Create a basic agent with more configuration
agent = Agent(
    model=OpenAIChat(
        id="gpt-4o",
        temperature=0.7,  # Control randomness (0.0-1.0)
        max_tokens=1000   # Limit response length
    ),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    instructions=[
        "Always structure your responses with a headline, summary, and details",
        "Include fictional quotes from witnesses or experts",
        "End with a question to engage the reader"
    ],
    markdown=true
)

# Interact with the agent
agent.print_response("Tell me about a breakthrough in renewable energy.", stream=true)
```

This enhanced basic agent includes:
- Model parameters for temperature and response length
- Detailed instructions that guide the agent's response format

## Next Steps

After mastering the basic agent, you can progress to:

1. [Adding tools to your agent](web_search_agent.md)
2. [Incorporating memory](../concepts/memory.md)
3. [Adding domain-specific knowledge](knowledge_agent.md)
4. [Creating multimodal agents](multimodal_agent.md)