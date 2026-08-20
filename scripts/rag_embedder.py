import sqlite3
import chromadb
from sentence_transformers import SentenceTransformer
from db import get_conn
from config import CHROMA_PATH, EMBED_MODEL_NAME

COLLECTION_NAME = "leetcode_questions"

# Lazy-load so Streamlit doesn't load it on every import
_embed_model = None


def get_embed_model():
    global _embed_model
    if _embed_model is None:
        print(f"Loading embedding model: {EMBED_MODEL_NAME} ...")
        _embed_model = SentenceTransformer(EMBED_MODEL_NAME)
        print("Embedding model ready.")
    return _embed_model


def build_vector_db():
    """Embed all repo_questions into ChromaDB."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, topic, title, problem_desc FROM repo_questions"
    )
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No questions found. Run parser.py first.")
        return

    model = get_embed_model()

    client = chromadb.PersistentClient(path=CHROMA_PATH)

    # Delete + recreate for clean rebuild
    try:
        client.delete_collection(name=COLLECTION_NAME)
    except Exception:
        pass

    collection = client.create_collection(name=COLLECTION_NAME)

    for qid, topic, title, desc in rows:
        text = f"Topic: {topic}. Title: {title}. Problem: {desc[:500]}"
        embedding = model.encode(text).tolist()
        collection.add(
            ids=[str(qid)],
            embeddings=[embedding],
            metadatas=[{"topic": topic, "title": title}],
            documents=[text],
        )

    print(f"Embedded {len(rows)} questions into ChromaDB at {CHROMA_PATH}")


def retrieve_similar(topic_query: str, n_results: int = 5):
    """Retrieve top-N questions similar to the faculty's topic request."""
    model = get_embed_model()
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    try:
        collection = client.get_collection(name=COLLECTION_NAME)
    except Exception:
        raise RuntimeError(
            "Vector DB not found. Run: python embedder.py"
        )

    query_embedding = model.encode(topic_query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
    )
    return results


if __name__ == "__main__":
    build_vector_db()
