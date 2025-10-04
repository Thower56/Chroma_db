"""Example usage of ChromaDB with Ollama integration."""

import chromadb


def simple_embedding(text):
    """Simple hash-based embedding for demonstration (not for production)."""
    # Create a simple vector based on character frequencies
    vector = [0.0] * 384  # Standard embedding size
    for i, char in enumerate(text.lower()[:384]):
        vector[i] = float(ord(char)) / 255.0
    return vector


def main():
    """Main function demonstrating ChromaDB and Ollama integration."""
    print("=== ChromaDB with Ollama Example ===\n")
    
    # Initialize ChromaDB client with an ephemeral in-memory database
    client = chromadb.Client()
    
    # Create or get a collection
    collection = client.get_or_create_collection(
        name="example_collection",
        metadata={"description": "Example collection for ChromaDB with Ollama"}
    )
    
    # Example documents
    documents = [
        "This is a document about artificial intelligence.",
        "Machine learning is a subset of AI.",
        "Deep learning uses neural networks.",
    ]
    
    # Create simple embeddings for demonstration
    embeddings = [simple_embedding(doc) for doc in documents]
    
    print("Adding documents to the collection...")
    # Add documents to the collection with custom embeddings
    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=[f"doc_{i}" for i in range(len(documents))],
        metadatas=[{"source": f"document_{i}"} for i in range(len(documents))]
    )
    
    print(f"✓ Added {len(documents)} documents to the collection.\n")
    
    # Query the collection
    query_text = "What is AI?"
    query_embedding = simple_embedding(query_text)
    
    print(f"Querying: '{query_text}'")
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )
    
    print(f"\nTop {len(results['documents'][0])} results:")
    for i, doc in enumerate(results['documents'][0], 1):
        print(f"{i}. {doc}")
    
    # Get collection stats
    print(f"\nCollection '{collection.name}' contains {collection.count()} documents")
    
    print("\n" + "="*60)
    print("Integration with Ollama:")
    print("="*60)
    print("""
To integrate Ollama with ChromaDB in production:

1. Install and run Ollama:
   curl https://ollama.ai/install.sh | sh
   ollama pull llama2

2. Use Ollama to generate embeddings:
   import ollama
   response = ollama.embeddings(model='llama2', prompt='text')
   embedding = response['embedding']

3. Add to ChromaDB with Ollama embeddings:
   collection.add(
       documents=["Document text"],
       embeddings=[embedding],
       ids=["doc1"]
   )

4. Build a RAG (Retrieval Augmented Generation) system:
   # Query ChromaDB for relevant context
   results = collection.query(query_embeddings=[query_emb], n_results=3)
   context = " ".join(results['documents'][0])
   
   # Generate response with Ollama using context
   response = ollama.generate(
       model='llama2', 
       prompt=f"Context: {context}\\n\\nQuestion: {query}\\n\\nAnswer:"
   )
   print(response['response'])
""")


if __name__ == "__main__":
    main()
