import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DSA_TOPICS_DIR = BASE_DIR / "data" / "DSA_Topics"

OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:11434/api/chat')
MODEL_NAME = os.environ.get('OLLAMA_MODEL', 'qwen2.5-coder:3b')

EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
RETRIEVAL_COUNT = 3
GENERATION_TEMPERATURE = 0.4
GENERATION_CTX = 4096
