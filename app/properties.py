import os

from config import ENV_VARIABLE_NAME
from app import __version__
from db import db

env = os.getenv(ENV_VARIABLE_NAME, None)
build_version = __version__

def is_db_connected():
	try:
		db.session.query("1").from_statement("SELECT 1").all()
		return True
	except:
		return False