from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb

chroma_client = chromadb.PersistentClient(path='./chromadb')
try:
    collection = chroma_client.get_collection('documents')
except:
    collection = chroma_client.create_collection('documents')

def store_document(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=500,
        add_start_index=True
    )

    chunks = splitter.split_text(text)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks, show_progress_bar=True)

    for i, embedding in enumerate(embeddings):
        collection.add(documents=[chunks[i]], embeddings=[embedding], ids=[str(i)])

def query(query, n=5):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([query])[0]

    results = collection.query(query_embedding, n_results=n)
    return results