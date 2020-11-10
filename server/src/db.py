""" Contains database logic. """

import contextlib
import os
import sqlite3

from flask import current_app

from src import const


@contextlib.contextmanager
def connect():
    conn = sqlite3.connect(
        current_app.config['DATABASE'],
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    conn.row_factory = sqlite3.Row

    yield conn

    conn.close()


def init_db():
    os.makedirs(const.DATA_DIR, exist_ok=True)

    with connect() as conn, open(const.DB_SCHEMA) as f:
        conn.executescript(f.read())


def init_app(_):
    init_db()
