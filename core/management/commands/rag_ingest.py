from django.core.management.base import BaseCommand
import sys
from pathlib import Path

from config import settings


class Command(BaseCommand):
    help = 'Ingest DSA topics into the RAG vector database (SQLite + ChromaDB)'

    def handle(self, *args, **options):
        script_dir = Path(settings.BASE_DIR) / 'scripts'
        if str(script_dir) not in sys.path:
            sys.path.insert(0, str(script_dir))

        try:
            from rag_parser import ingest_repo
            from rag_embedder import build_vector_db
            from rag_config import REPO_PATH

            self.stdout.write(self.style.SUCCESS('Parsing DSA topics into SQLite...'))
            ingest_repo(REPO_PATH)

            self.stdout.write(self.style.SUCCESS('Building vector embeddings (ChromaDB)...'))
            build_vector_db()

            self.stdout.write(self.style.SUCCESS('✅ RAG ingestion complete'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'RAG ingestion failed: {e}'))