# Getting Started

This guide will help you get started with the ChromaDB and Ollama integration project.

## Quick Start

### 1. Install Dependencies

```bash
# Install using Poetry
poetry install

# Or activate the virtual environment
poetry shell
```

### 2. Run the Example

```bash
poetry run python src/chroma_db/example.py
```

## Using ChromaDB

ChromaDB is an open-source embedding database that makes it easy to build AI applications with embeddings.

### Basic Usage

```python
import chromadb

# Create a client
client = chromadb.Client()

# Create a collection
collection = client.get_or_create_collection(name="my_collection")

# Add documents
collection.add(
    documents=["Document 1", "Document 2"],
    embeddings=[[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]],  # Optional: provide your own embeddings
    ids=["id1", "id2"]
)

# Query
results = collection.query(
    query_embeddings=[[0.1, 0.2, 0.3]],
    n_results=2
)
```

## Using Ollama

Ollama allows you to run large language models locally.

### Installation

```bash
# Install Ollama (Linux/MacOS)
curl https://ollama.ai/install.sh | sh

# Pull a model
ollama pull llama2
```

### Basic Usage

```python
import ollama

# Generate text
response = ollama.generate(
    model='llama2',
    prompt='Tell me about AI'
)
print(response['response'])

# Generate embeddings
embedding_response = ollama.embeddings(
    model='llama2',
    prompt='Some text to embed'
)
embedding = embedding_response['embedding']
```

## Combining ChromaDB and Ollama

Build a Retrieval Augmented Generation (RAG) system:

```python
import chromadb
import ollama

# Initialize ChromaDB
client = chromadb.Client()
collection = client.get_or_create_collection(name="knowledge_base")

# Add documents with Ollama embeddings
documents = ["AI is...", "Machine learning is..."]
for i, doc in enumerate(documents):
    embedding = ollama.embeddings(model='llama2', prompt=doc)['embedding']
    collection.add(
        documents=[doc],
        embeddings=[embedding],
        ids=[f"doc_{i}"]
    )

# Query and generate response
query = "What is AI?"
query_embedding = ollama.embeddings(model='llama2', prompt=query)['embedding']
results = collection.query(query_embeddings=[query_embedding], n_results=3)

# Use retrieved context to generate response
context = " ".join(results['documents'][0])
response = ollama.generate(
    model='llama2',
    prompt=f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
)
print(response['response'])
```

## Project Structure

```
Chroma_db/
├── src/
│   └── chroma_db/
│       ├── __init__.py         # Package initialization
│       └── example.py          # Example usage
├── pyproject.toml              # Poetry configuration
├── poetry.lock                 # Locked dependencies
├── README.md                   # Project overview
└── GETTING_STARTED.md          # This file
```

## Next Steps

1. Explore the [ChromaDB documentation](https://docs.trychroma.com/)
2. Read the [Ollama documentation](https://github.com/ollama/ollama)
3. Try building your own RAG application
4. Experiment with different embedding models and LLMs

## Troubleshooting

### ChromaDB Issues

- Ensure you have Python 3.9 or higher
- Try clearing the ChromaDB cache: `rm -rf ~/.cache/chroma`

### Ollama Issues

- Make sure Ollama is running: `ollama serve`
- Check available models: `ollama list`
- Pull a new model if needed: `ollama pull <model-name>`

## Additional Resources

- [ChromaDB GitHub](https://github.com/chroma-core/chroma)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [Poetry Documentation](https://python-poetry.org/docs/)
