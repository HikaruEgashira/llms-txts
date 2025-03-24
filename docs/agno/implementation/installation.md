# Installation Guide for Agno-AGI

This guide provides detailed instructions for installing and setting up Agno-AGI on various platforms, along with troubleshooting tips for common issues.

## Basic Installation

### Using pip

The simplest way to install Agno-AGI is using pip:

```bash
pip install -U agno
```

### Installation with Optional Dependencies

For full functionality, you can install Agno-AGI with optional dependencies:

```bash
# Full development installation
pip install -U "agno[dev]"

# Specific dependency groups
pip install -U "agno[tools]"  # All tool dependencies
pip install -U "agno[vectordb]"  # Vector database dependencies
pip install -U "agno[monitoring]"  # Monitoring dependencies
```

## Environment Setup

### API Keys Configuration

Agno-AGI requires API keys for various LLM providers. Set these as environment variables:

```bash
# For OpenAI
export OPENAI_API_KEY=your_api_key

# For Anthropic
export ANTHROPIC_API_KEY=your_api_key

# For Google
export GOOGLE_API_KEY=your_api_key

# For other providers
export MISTRAL_API_KEY=your_api_key
export AZURE_OPENAI_API_KEY=your_api_key
export OLLAMA_API_BASE=http://localhost:11434
```

### Persistent Configuration

For persistent configuration, add the environment variables to your shell profile:

```bash
# For bash
echo 'export OPENAI_API_KEY=your_api_key' >> ~/.bashrc

# For zsh
echo 'export OPENAI_API_KEY=your_api_key' >> ~/.zshrc
```

## Platform-Specific Instructions

### macOS

On macOS, you might need to install additional dependencies:

```bash
# Using Homebrew
brew install python@3.10

# For lancedb dependencies
brew install gcc
```

### Linux

On Linux systems, you may need to install system packages:

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y python3-dev python3-pip

# For lancedb dependencies
sudo apt-get install -y build-essential
```

### Windows

On Windows, we recommend using a virtual environment:

```powershell
# Create a virtual environment
python -m venv agno-env

# Activate the environment
.\agno-env\Scripts\activate

# Install Agno
pip install -U agno
```

## Docker Installation

Agno-AGI provides an official Docker image:

```bash
# Pull the latest image
docker pull agnoagi/agno:latest

# Run the container
docker run -p 8000:8000 -e OPENAI_API_KEY=your_api_key agnoagi/agno:latest
```

Or create your own Dockerfile:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV OPENAI_API_KEY=your_api_key

CMD ["python", "your_agent_script.py"]
```

## Tool-Specific Dependencies

Different tools require different dependencies:

```bash
# Web search tools
pip install duckduckgo-search

# Finance tools
pip install yfinance

# PDF processing
pip install pypdf

# Vector databases
pip install lancedb chroma-hnswlib pinecone-client

# Image processing
pip install pillow
```

## Troubleshooting

### Common Installation Issues

1. **Dependency Conflicts**
   
   If you encounter dependency conflicts:
   ```bash
   pip install -U agno --no-deps
   pip install -U <conflicting_package>
   ```

2. **Compilation Errors**
   
   For compilation errors with native extensions:
   ```bash
   # On Ubuntu/Debian
   sudo apt-get install -y python3-dev
   
   # On macOS
   xcode-select --install
   ```

3. **API Key Issues**
   
   Verify your API keys are correctly set:
   ```bash
   # Check if environment variable is set
   echo $OPENAI_API_KEY
   
   # Set it manually if needed
   export OPENAI_API_KEY=your_api_key
   ```

### Verifying Installation

To verify that Agno-AGI is installed correctly:

```python
import agno
print(agno.__version__)

# Test model access
from agno.models.openai import OpenAIChat
model = OpenAIChat(id="gpt-3.5-turbo")
# Should not raise an error if API key is correctly set
```

## Upgrading

To upgrade to the latest version:

```bash
pip install -U agno
```

To upgrade to a specific version:

```bash
pip install -U agno==1.2.0
```

## Development Installation

For contributing to Agno-AGI development:

```bash
# Clone the repository
git clone https://github.com/agno-agi/agno.git
cd agno

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest
```

## Next Steps

After successfully installing Agno-AGI, proceed to:

1. [Building your first agent](getting_started.md)
2. Exploring the [examples](../examples/basic_agent.md)
3. Setting up [monitoring](../advanced/monitoring.md) for your agents