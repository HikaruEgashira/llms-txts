# Multimodal Agent Example

This example demonstrates how to create an agent in Agno-AGI that can work with multiple modalities - processing and generating content across text, images, audio, and video. Multimodal agents can understand complex inputs and produce rich, varied outputs, making them ideal for creative applications, content analysis, and advanced user interactions.

## Overview

A multimodal agent in Agno-AGI consists of:
- A language model with multimodal capabilities
- A description that defines the agent's persona and capabilities
- Tools for working with different media types
- Instructions that guide how the agent handles multimodal content

This configuration allows the agent to process rich inputs and generate diverse outputs, creating more engaging and comprehensive interactions.

## Implementation

Here's how to create a multimodal agent that can process images:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# Create an agent that can understand images
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),  # GPT-4o has vision capabilities
    description="You are a visual analysis assistant who can understand images and provide detailed descriptions.",
    tools=[DuckDuckGoTools()],  # Add web search capability
    instructions=[
        "When analyzing images, be detailed and descriptive.",
        "If you need more information about what's in the image, use web search.",
        "Explain technical concepts in simple terms."
    ],
    show_tool_calls=true,
    markdown=true
)

# Path to a local image
image_path = "path/to/your/image.jpg"

# Interact with the agent using an image
agent.print_response(
    {
        "text": "What's in this image and can you explain what's happening?",
        "images": [image_path]  # Can accept local paths or URLs
    },
    stream=true
)
```

## Running the Example

To run this example:

1. Install the required dependencies:
   ```bash
   pip install agno openai duckduckgo-search pillow
   ```

2. Set up your environment variables:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

3. Save the code to a file (e.g., `multimodal_agent.py`) and run it:
   ```bash
   python multimodal_agent.py
   ```

## Key Components

### Multimodal Model

The model must support the modalities you want to work with:

```python
model=OpenAIChat(id="gpt-4o")  # GPT-4o supports images
```

Different models support different modalities:
- GPT-4o: Text + Images
- Claude 3: Text + Images
- Gemini Pro: Text + Images + Audio + Video

### Multimodal Input

Inputs to multimodal agents use a dictionary format:

```python
{
    "text": "What's in this image and can you explain what's happening?",
    "images": [image_path]  # Can be a local path or URL
}
```

Agno-AGI supports multiple input modalities:
- Text: Primary communication
- Images: Visual content for analysis
- Audio: Sound files for analysis (with supporting models)
- Video: Video files for analysis (with supporting models)

## Multimodal Output Generation

Agents can also generate multimodal content using appropriate tools:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.dalle import DallEImageGeneration

# Create an agent that can generate images
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a creative assistant who can generate images based on descriptions.",
    tools=[DallEImageGeneration()],  # Add image generation capability
    instructions=[
        "When asked to create images, use the DALL-E tool to generate them.",
        "Provide detailed prompts to the image generation tool.",
        "Explain your creative choices."
    ],
    show_tool_calls=true,
    markdown=true
)

# Request image generation
agent.print_response("Create an image of a futuristic city with flying cars and tall glass buildings.", stream=true)
```

## Advanced Multimodal Capabilities

### Audio Response Generation

You can create agents that generate audio responses:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tts import TextToSpeechTool

# Create an agent that can generate audio responses
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful assistant who can speak responses aloud.",
    tools=[TextToSpeechTool()],  # Add text-to-speech capability
    instructions=[
        "When the user asks you to speak your response, use the text-to-speech tool.",
        "Keep spoken responses concise and clear."
    ],
    show_tool_calls=true,
    markdown=true
)

# Request audio response
agent.print_response("Tell me about the solar system and speak your response.", stream=true)
```

### Video Analysis

With models that support video analysis:

```python
from agno.agent import Agent
from agno.models.google import GoogleChat

# Create an agent that can analyze videos (Gemini supports video)
agent = Agent(
    model=GoogleChat(id="gemini-1.5-pro"),
    description="You are a video analysis assistant who can understand and describe video content.",
    instructions=[
        "When analyzing videos, describe the key events and elements.",
        "Pay attention to both visual and audio content.",
        "Summarize the overall narrative or purpose of the video."
    ],
    markdown=true
)

# Video path or URL
video_path = "path/to/your/video.mp4"

# Interact with the agent using a video
agent.print_response(
    {
        "text": "What's happening in this video?",
        "video": video_path
    },
    stream=true
)
```

## Best Practices

When implementing multimodal agents:

1. **Model Selection**: Choose models that support your required modalities
2. **Input Preparation**: Ensure images and other media are properly formatted
3. **Error Handling**: Include fallbacks for cases where media processing fails
4. **Output Diversity**: Consider how to balance different output modalities
5. **Performance**: Be aware of the increased processing requirements
6. **Privacy**: Consider privacy implications of processing visual/audio content

## Next Steps

After implementing a multimodal agent, you can enhance it by:

1. [Adding knowledge bases](knowledge_agent.md) for domain-specific expertise
2. [Implementing memory](../concepts/memory.md) to remember user preferences
3. [Building agent teams](agent_team.md) with specialized multimodal capabilities
4. [Creating complex workflows](../advanced/workflows.md) that incorporate multiple modalities