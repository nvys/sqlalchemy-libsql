import sys
from unittest.mock import patch

def patch_libsql():
    if sys.version_info >= (3, 12):
        import sqlite3
        with patch.object(sqlite3, 'SQLITE_BUSY_TIMEOUT', sqlite3.SQLITE_BUSY):
            yield
    else:
        yield
