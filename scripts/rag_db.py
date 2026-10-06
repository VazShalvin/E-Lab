import sqlite3
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.rag_config import DB_PATH


def get_conn():
    return sqlite3.connect(DB_PATH)


def init_db():
    """Create both tables: repo_questions (parsed) + generated_questions (adapted output)."""
    conn = get_conn()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS repo_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            filename TEXT NOT NULL,
            title TEXT,
            problem_desc TEXT,
            solution_code TEXT,
            test_cases TEXT,
            difficulty TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        );
        CREATE INDEX IF NOT EXISTS idx_repo_topic ON repo_questions(topic);

        CREATE TABLE IF NOT EXISTS generated_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            module_name TEXT NOT NULL,
            topic TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            prompt TEXT NOT NULL,
            solution TEXT,
            test_cases TEXT,
            reference_ids TEXT,
            status TEXT DEFAULT 'pending',
            created_at TEXT DEFAULT (datetime('now'))
        );
        CREATE INDEX IF NOT EXISTS idx_gen_module ON generated_questions(module_name);
    """)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print(f"Database initialized at {DB_PATH}")
