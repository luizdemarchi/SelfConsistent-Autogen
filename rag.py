# rag.py
import chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="./rag_db")
collection = client.create_collection(
    name="wcag_rules",
    embedding_function=embedding_functions.DefaultEmbeddingFunction()
)

# Add your Markdown docs (run once)
def ingest_knowledge():
    for md_file in Path("knowledge/").glob("*.md"):
        text = md_file.read_text()
        collection.add(
            documents=text,
            ids=str(md_file),
            metadatas={"source": str(md_file)}
        )