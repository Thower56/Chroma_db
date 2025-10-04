# Chroma DB

A Python project integrating ChromaDB with Ollama for vector database operations and AI model interactions.

## Features

- **ChromaDB**: Open-source embedding database for building AI applications
- **Ollama**: Run large language models locally
- **Poetry**: Modern dependency management and packaging

## Prerequisites

- Python 3.9 or higher
- Poetry (for dependency management)
- Ollama (optional, for local LLM support)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Thower56/Chroma_db.git
cd Chroma_db
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. (Optional) Install Ollama:
   - Visit [Ollama's website](https://ollama.ai/) for installation instructions
   - Pull a model: `ollama pull llama2`

## Usage

Run the example script:
```bash
poetry run python src/chroma_db/example.py
```

## Project Structure

```
Chroma_db/
├── src/
│   └── chroma_db/
│       ├── __init__.py
│       └── example.py
├── pyproject.toml
├── README.md
└── .gitignore
```

## Dependencies

- **chromadb**: ^0.5.0 - Vector database for embeddings
- **ollama**: ^0.4.5 - Python client for Ollama

## Development

This project uses Poetry for dependency management. To add new dependencies:

```bash
poetry add <package-name>
```

For development dependencies:
```bash
poetry add --group dev <package-name>
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.