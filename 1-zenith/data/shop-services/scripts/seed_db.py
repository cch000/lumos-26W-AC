"""(Re)build data/zenith.db from the CSV export in data/.

    python scripts/seed_db.py
The app also builds the DB on first start if it does not exist.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import db  # noqa: E402

if __name__ == "__main__":
    db.seed(force=True)
    conn = db.get_conn()
    for table in ("products", "orders", "order_items"):
        print(table, conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0])
