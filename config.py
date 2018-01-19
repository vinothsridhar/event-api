import json
from secret import *

class Config(object):
	"""
	Common Configurations
	"""

	LOG_PATH = 'error.log'


class DevConfig(Config):
	"""
	Development Environment Configurations
	"""

	DEBUG = True
	SQLALCHEMY_ECHO = True
	SECRET_KEY = DEV_DB_PASSWORD
	SQLALCHEMY_DATABASE_URI = "mysql://" + DEV_DB_USER + "@" + DEV_DB_HOST + "/" + DEV_DB_NAME

class ProdConfig(Config):
	"""
	Production Environment configurations
	"""

	DEBUG = False
	SECRET_KEY = DB_PASSWORD
	SQLALCHEMY_DATABASE_URI = "mysql://" + DB_USER + "@" + DB_HOST + "/" + DB_NAME

config = {
	'dev': DevConfig,
	'prod': ProdConfig
}