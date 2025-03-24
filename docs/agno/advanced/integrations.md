# Integrations

Agno-AGI integrates with numerous third-party services, frameworks, and platforms to extend its capabilities and facilitate seamless incorporation into existing systems. This document outlines the key integrations available and how to implement them.

## Model Provider Integrations

### OpenAI

Agno-AGI offers comprehensive integration with OpenAI's models:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat, OpenAICompletion

# Chat models
agent = Agent(
    model=OpenAIChat(
        id="gpt-4o",
        temperature=0.7,
        api_key="your_api_key"  # Or use OPENAI_API_KEY environment variable
    ),
    description="You are a helpful assistant."
)

# Completion models
agent = Agent(
    model=OpenAICompletion(
        id="text-davinci-003",
        temperature=0.7
    ),
    description="You are a helpful assistant."
)
```

### Anthropic

Integration with Anthropic's Claude models:

```python
from agno.agent import Agent
from agno.models.anthropic import AnthropicChat

agent = Agent(
    model=AnthropicChat(
        id="claude-3-opus-20240229",
        temperature=0.7,
        api_key="your_api_key"  # Or use ANTHROPIC_API_KEY environment variable
    ),
    description="You are a helpful assistant."
)
```

### Google

Integration with Google's models:

```python
from agno.agent import Agent
from agno.models.google import GoogleChat

agent = Agent(
    model=GoogleChat(
        id="gemini-1.5-pro",
        temperature=0.7,
        api_key="your_api_key"  # Or use GOOGLE_API_KEY environment variable
    ),
    description="You are a helpful assistant."
)
```

### Other Model Providers

Agno-AGI also integrates with:

- **Mistral AI**: `from agno.models.mistral import MistralChat`
- **Cohere**: `from agno.models.cohere import CohereChat`
- **Azure OpenAI**: `from agno.models.azure import AzureOpenAIChat`
- **Ollama**: `from agno.models.ollama import OllamaChat`
- **Hugging Face**: `from agno.models.huggingface import HuggingFaceTextGeneration`

## Vector Database Integrations

### LanceDB

```python
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.embedder.openai import OpenAIEmbedder

vector_db = LanceDb(
    uri="tmp/lancedb",
    table_name="documents",
    search_type=SearchType.hybrid,
    embedder=OpenAIEmbedder(id="text-embedding-3-small")
)
```

### ChromaDB

```python
from agno.vectordb.chroma import ChromaDb
from agno.embedder.openai import OpenAIEmbedder

vector_db = ChromaDb(
    path="tmp/chromadb",
    collection_name="documents",
    embedder=OpenAIEmbedder(id="text-embedding-3-small")
)
```

### Pinecone

```python
from agno.vectordb.pinecone import PineconeDb
from agno.embedder.openai import OpenAIEmbedder

vector_db = PineconeDb(
    api_key="your_pinecone_api_key",
    environment="us-west1-gcp",
    index_name="documents",
    embedder=OpenAIEmbedder(id="text-embedding-3-small")
)
```

### Other Vector Databases

Agno-AGI also integrates with:

- **Weaviate**: `from agno.vectordb.weaviate import WeaviateDb`
- **Qdrant**: `from agno.vectordb.qdrant import QdrantDb`
- **Milvus**: `from agno.vectordb.milvus import MilvusDb`
- **FAISS**: `from agno.vectordb.faiss import FaissDb`

## Storage Integrations

### Redis

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.redis import RedisStorage
from agno.memory.conversation import ConversationMemory

storage = RedisStorage(
    redis_url="redis://localhost:6379/0",
    namespace="agent-memory"
)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful assistant with memory.",
    storage=storage,
    memory=ConversationMemory(),
    session_id="user-123"
)
```

### PostgreSQL

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.postgres import PostgresStorage
from agno.memory.conversation import ConversationMemory

storage = PostgresStorage(
    connection_string="postgresql://user:password@localhost:5432/dbname",
    table_name="agent_memory"
)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful assistant with memory.",
    storage=storage,
    memory=ConversationMemory(),
    session_id="user-123"
)
```

### Other Storage Options

Agno-AGI also integrates with:

- **MongoDB**: `from agno.storage.mongodb import MongoStorage`
- **File System**: `from agno.storage.filesystem import FileSystemStorage`
- **DynamoDB**: `from agno.storage.dynamodb import DynamoDBStorage`
- **SQLite**: `from agno.storage.sqlite import SQLiteStorage`

## Web Framework Integrations

### FastAPI

```python
from fastapi import FastAPI, Depends, HTTPException
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from pydantic import BaseModel

app = FastAPI()

# Create agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful API assistant.",
    markdown=true
)

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_agent(query: Query):
    try:
        response = agent.get_response(query.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### Flask

```python
from flask import Flask, request, jsonify
from agno.agent import Agent
from agno.models.openai import OpenAIChat

app = Flask(__name__)

# Create agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful API assistant.",
    markdown=true
)

@app.route("/ask", methods=["POST"])
def ask_agent():
    data = request.json
    question = data.get("question")
    
    if not question:
        return jsonify({"error": "Question is required"}), 400
    
    try:
        response = agent.get_response(question)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
```

## Cloud Platform Integrations

### AWS Lambda

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
import json

# Create agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful serverless assistant.",
    markdown=true
)

def lambda_handler(event, context):
    try:
        # Parse the input
        body = json.loads(event.get("body", "{}"))
        question = body.get("question")
        
        if not question:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Question is required"})
            }
        
        # Get response from agent
        response = agent.get_response(question)
        
        return {
            "statusCode": 200,
            "body": json.dumps({"response": response})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
```

### Docker

Agno-AGI provides Docker integration for containerized deployment:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV OPENAI_API_KEY=your_api_key

CMD ["python", "app.py"]
```

## Monitoring Integrations

### Agno.com Platform

Agno-AGI integrates with the Agno.com platform for comprehensive monitoring:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.monitoring.agno import AgnoMonitoring

# Create monitoring
monitoring = AgnoMonitoring(
    api_key="your_agno_api_key",
    project="my-project"
)

# Create agent with monitoring
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful assistant.",
    monitoring=monitoring,
    session_id="user-123"
)
```

### Prometheus

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.monitoring.prometheus import PrometheusMonitoring

# Create monitoring
monitoring = PrometheusMonitoring(
    metrics_port=8000,
    metrics_path="/metrics"
)

# Create agent with monitoring
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a helpful assistant.",
    monitoring=monitoring
)
```

## Integration Best Practices

When implementing Agno-AGI integrations:

1. **Security**: Securely manage API keys and credentials
2. **Error Handling**: Implement robust error handling for integration failures
3. **Caching**: Consider caching strategies for performance optimization
4. **Monitoring**: Track integration performance and reliability
5. **Fallbacks**: Implement fallback mechanisms for critical integrations
6. **Testing**: Thoroughly test integrations in isolation and combination
7. **Documentation**: Document integration details for maintainers

## Custom Integration Development

Agno-AGI provides base classes for developing custom integrations:

```python
from agno.models.base import BaseModel
from typing import Dict, Any, Optional

class CustomModel(BaseModel):
    """Custom model integration for Agno-AGI."""
    
    def __init__(self, id: str, api_key: Optional[str] = null, **kwargs):
        super().__init__(id=id, **kwargs)
        self.api_key = api_key or os.environ.get("CUSTOM_API_KEY")
        
    def generate(self, messages: list, **kwargs) -> Dict[str, Any]:
        """Generate response from custom model."""
        # Implementation details
        pass
```