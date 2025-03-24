# Agent Team Example

This example demonstrates how to create a team of specialized agents in Agno-AGI that work together to solve complex problems. Agent teams distribute cognitive load across multiple specialized agents, enabling more sophisticated problem-solving by combining different expertise, tools, and knowledge bases.

## Overview

An agent team in Agno-AGI consists of:
- A coordinator agent that manages the overall workflow
- Multiple specialist agents with different capabilities
- A communication protocol between agents
- A task distribution mechanism
- A result synthesis process

This configuration is ideal for complex tasks that require multiple types of expertise, access to different tools, or handling of diverse knowledge domains.

## Implementation

Here's how to create a team of agents:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

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
    tools=[YFinanceTools(stock_price=true, analyst_recommendations=true, company_info=true)],
    instructions="Use tables to display data",
    show_tool_calls=true,
    markdown=true,
)

# Create a coordinator agent with team members
agent_team = Agent(
    mode="coordinate",  # Operating in coordination mode
    members=[web_agent, finance_agent],  # Team members
    model=OpenAIChat(id="gpt-4o"),
    success_criteria="A comprehensive financial news report with clear sections and data-driven insights.",
    instructions=[
        "Always include sources", 
        "Use tables to display data",
        "First gather general market information, then get specific financial data"
    ],
    show_tool_calls=true,
    markdown=true,
)

# Use the team to solve a complex problem
agent_team.print_response("What's the market outlook and financial performance of AI semiconductor companies?", stream=true)
```

## Running the Example

To run this example:

1. Install the required dependencies:
   ```bash
   pip install agno openai duckduckgo-search yfinance
   ```

2. Set up your environment variables:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

3. Save the code to a file (e.g., `agent_team.py`) and run it:
   ```bash
   python agent_team.py
   ```

## Key Components

### Specialist Agents

Each specialist agent focuses on a specific domain or function:

```python
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=true,
    markdown=true,
)
```

Important attributes for specialist agents:
- `name`: Identifies the agent within the team
- `role`: Describes the agent's function to the coordinator
- `tools`: Provides capabilities specific to the agent's role
- `instructions`: Guides the agent's behavior in its specialized role

### Coordinator Agent

The coordinator agent manages the team's workflow:

```python
agent_team = Agent(
    mode="coordinate",  # Operating in coordination mode
    members=[web_agent, finance_agent],  # Team members
    model=OpenAIChat(id="gpt-4o"),
    success_criteria="A comprehensive financial news report with clear sections and data-driven insights.",
    instructions=[
        "Always include sources", 
        "Use tables to display data",
        "First gather general market information, then get specific financial data"
    ],
    show_tool_calls=true,
    markdown=true,
)
```

Key aspects of the coordinator:
- `mode="coordinate"`: Specifies that this agent coordinates others
- `members`: Lists the specialist agents in the team
- `success_criteria`: Defines what constitutes successful task completion
- `instructions`: Guides the overall workflow and output format

## Advanced Team Configurations

### Multiple Levels of Coordination

You can create hierarchical team structures:

```python
# First-level specialist teams
research_team = Agent(
    mode="coordinate",
    members=[web_agent, academic_agent],
    name="Research Team",
    role="Gather and analyze information",
    model=OpenAIChat(id="gpt-4o"),
)

analysis_team = Agent(
    mode="coordinate",
    members=[finance_agent, data_analyst_agent],
    name="Analysis Team",
    role="Process and visualize data",
    model=OpenAIChat(id="gpt-4o"),
)

# Top-level coordinator
executive_team = Agent(
    mode="coordinate",
    members=[research_team, analysis_team, writing_agent],
    model=OpenAIChat(id="gpt-4o"),
    success_criteria="A comprehensive report with research, analysis, and clear recommendations.",
)
```

### Dynamic Task Allocation

Advanced teams can dynamically allocate tasks:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Create a pool of specialists
specialists = [
    web_agent,
    finance_agent,
    legal_agent,
    technical_agent,
    creative_agent
]

# Create a dynamic team that selects appropriate specialists
dynamic_team = Agent(
    mode="dynamic",  # Dynamically selects team members
    member_pool=specialists,
    max_members=3,  # Maximum number of specialists to use per task
    model=OpenAIChat(id="gpt-4o"),
    selection_criteria="Select specialists based on the specific requirements of the task.",
)

# The dynamic team will select the most relevant specialists
dynamic_team.print_response("Evaluate the legal and financial implications of a tech startup acquisition.", stream=true)
```

## Team Communication Patterns

Agno-AGI supports different team communication patterns:

1. **Hub-and-Spoke**: Coordinator communicates with each specialist individually
2. **Sequential**: Output from one agent becomes input to the next
3. **Parallel**: Multiple agents work simultaneously on different aspects
4. **Deliberative**: Agents debate and critique each other's work
5. **Hybrid**: Combinations of the above patterns

## Best Practices

When implementing agent teams:

1. **Clear Role Definition**: Each agent should have a well-defined role
2. **Complementary Skills**: Ensure team members have complementary capabilities
3. **Task Decomposition**: Break complex tasks into manageable components
4. **Information Flow**: Design efficient information sharing between agents
5. **Output Integration**: Ensure coherent synthesis of individual contributions
6. **Error Handling**: Include mechanisms for handling failures in individual agents
7. **Resource Management**: Consider the computational cost of multiple agents

## Next Steps

After implementing an agent team, you can enhance it by:

1. [Adding shared knowledge](knowledge_agent.md) across the team
2. [Implementing team memory](../concepts/memory.md) for long-term collaboration
3. [Creating more sophisticated workflows](../advanced/workflows.md)
4. [Implementing deliberative systems](../advanced/reasoning.md) where agents critique each other's work