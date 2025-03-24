# Knowledge-based Agent Example

This example demonstrates how to create an agent in Agno-AGI with access to domain-specific knowledge. Knowledge-based agents can reference specialized information beyond their training data, making them ideal for domain-specific applications, technical support, and expert systems.

## Overview

A knowledge-based agent in Agno-AGI consists of:
- A language model that powers the agent
- A description that defines the agent's persona and capabilities
- A knowledge base containing domain-specific information
- A vector database for storing and retrieving knowledge
- Instructions that guide how the agent uses its knowledge

This configuration allows the agent to provide accurate, domain-specific information by referencing authoritative sources rather than relying solely on its parametric knowledge.

## Implementation

Here's how to create a knowledge-based agent:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.tools.duckduckgo import DuckDuckGoTools

# Create a knowledge base from PDFs
knowledge = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],  # Example PDF
    vector_db=LanceDb(
        uri="tmp/lancedb",  # Storage location
        table_name="recipes",  # Table name
        search_type=SearchType.hybrid,  # Search method
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),  # Embedding model
    ),
)

# Create a knowledge-based agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a Thai cuisine expert!",
    instructions=[
        "Search your knowledge base for Thai recipes.",
        "If the question is better suited for the web, search the web to fill in gaps.",
        "Prefer the information in your knowledge base over the web results."
    ],
    knowledge=knowledge,  # Attach knowledge base
    tools=[DuckDuckGoTools()],  # Add web search as fallback
    show_tool_calls=true,
    markdown=true
)

# Load the knowledge base (usually done once)
if agent.knowledge is not null:
    agent.knowledge.load()

# Interact with the agent
agent.print_response("How do I make Tom Kha Gai soup?", stream=true)
agent.print_response("What is the history of Thai curry?", stream=true)
```

## Running the Example

To run this example:

1. Install the required dependencies:
   ```bash
   pip install agno openai lancedb tantivy pypdf duckduckgo-search
   ```

2. Set up your environment variables:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

3. Save the code to a file (e.g., `knowledge_agent.py`) and run it:
   ```bash
   python knowledge_agent.py
   ```

## Key Components

### Knowledge Base

The knowledge base contains domain-specific information:

```python
knowledge = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="recipes",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)
```

Agno-AGI supports various knowledge sources:
- PDFs
- Web pages
- Markdown files
- Custom document types

### Vector Database

The vector database stores and retrieves knowledge efficiently:

```python
vector_db=LanceDb(
    uri="tmp/lancedb",
    table_name="recipes",
    search_type=SearchType.hybrid,
    embedder=OpenAIEmbedder(id="text-embedding-3-small"),
)
```

Agno-AGI supports multiple vector databases:
- LanceDb
- ChromaDb
- Pinecone
- Weaviate
- Qdrant
- Custom implementations

### Knowledge Loading

Knowledge bases must be loaded before use:

```python
if agent.knowledge is not null:
    agent.knowledge.load()
```

This process:
1. Loads the documents
2. Chunks them into manageable segments
3. Creates embeddings
4. Stores them in the vector database

### Agentic RAG

Agno-AGI uses Agentic RAG by default, where the agent actively determines:
- When to search the knowledge base
- What queries to use for retrieval
- How to incorporate retrieved information into responses

## Alternative Knowledge Sources

Agno-AGI supports several knowledge sources:

```python
# Using web pages as knowledge
from agno.knowledge.url import UrlKnowledgeBase
knowledge = UrlKnowledgeBase(
    urls=["https://example.com/documentation.html"],
    vector_db=vector_db
)

# Using local files
from agno.knowledge.file import FileKnowledgeBase
knowledge = FileKnowledgeBase(
    files=["path/to/local/document.pdf"],
    vector_db=vector_db
)

# Using GitHub repositories
from agno.knowledge.github import GitHubKnowledgeBase
knowledge = GitHubKnowledgeBase(
    repos=["username/repo"],
    vector_db=vector_db
)
```

## Advanced Usage

### Custom Chunking Strategies

You can customize how documents are chunked:

```python
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.chunker.recursive import RecursiveChunker

knowledge = PDFUrlKnowledgeBase(
    urls=["https://example.com/document.pdf"],
    vector_db=vector_db,
    chunker=RecursiveChunker(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
)
```

### Multiple Knowledge Bases

Agents can have access to multiple knowledge bases:

```python
from agno.agent import Agent
from agno.knowledge.composite import CompositeKnowledgeBase

# Combine multiple knowledge bases
composite_knowledge = CompositeKnowledgeBase(
    knowledge_bases=[
        pdf_knowledge,
        url_knowledge,
        github_knowledge
    ]
)

agent = Agent(
    model=model,
    knowledge=composite_knowledge,
    description="You are an expert with access to multiple knowledge sources."
)
```

## Best Practices

When implementing knowledge-based agents:

1. **Document Quality**: Use high-quality, authoritative sources
2. **Chunking Strategy**: Optimize chunk size for your content type
3. **Search Configuration**: Balance semantic and keyword search
4. **Knowledge Updates**: Plan for regular updates to knowledge bases
5. **Fallback Mechanisms**: Provide alternative information sources
6. **Citation**: Ensure the agent cites sources properly

## Next Steps

After implementing a knowledge-based agent, you can enhance it by:

1. [Implementing memory](../concepts/memory.md) to remember user preferences
2. [Adding more tools](../concepts/tools.md) for expanded capabilities
3. [Creating multimodal agents](multimodal_agent.md) that can process images
4. [Building agent teams](agent_team.md) with specialized knowledge domains