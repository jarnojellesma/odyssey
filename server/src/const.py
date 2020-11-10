""" Contains constant, static properties. """
import os

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SRC_DIR)
DATA_DIR = os.path.join(ROOT_DIR, ".data")
RESOURCES_DIR = os.path.join(ROOT_DIR, "resources")
DB_SCHEMA = os.path.join(RESOURCES_DIR, "schema.sql")
DB_PATH = os.path.join(DATA_DIR, "server.db")
