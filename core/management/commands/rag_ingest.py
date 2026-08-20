from django.core.management.base import BaseCommand
import os
import sys
from pathlib import Path

class Command(BaseCommand):
    help = 'Ingest DSA topics into RAG vector database'

    def handle(self, *args, **options):
        # Add scripts directory to path
        script_dir = Path(__file__).resolve().parent.parent.parent.parent / 'scripts'
        if str(script_dir) not in sys.path:
            sys.path.insert(0, str(script_dir))
        
        try:
            from rag_parser import ingest_repo
            from rag_embedder import build_vector_db
            from rag_config import REPO_PATH
            
            self.stdout.write(self.style.SUCCESS('Ingesting DSA topics into RAG database...'))
            ingest_repo(REPO_PATH)
            self.stdout.write(self.style.SUCCESS('Building vector embeddings...'))
            build_vector_db()
            self.stdout.write(self.style.SUCCESS('RAG ingestion complete!'))
        except ImportError as e:
            self.stdout.write(self.style.ERROR(f'Failed to import RAG modules: {e}'))
            self.stdout.write(self.style.ERROR('Make sure scripts/rag_parser.py and scripts/rag_embedder.py exist'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'RAG ingestion failed: {e}'))
