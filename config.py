import json
from secret import *

ENV_VARIABLE_NAME = "EVENT_API_ENV"

ENV_DEV = "dev"

ENV_PROD = "prod"

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
	SQLALCHEMY_DATABASE_URI = "mysql://" + DEV_DB_USER + ":" + DEV_DB_PASSWORD + "@" + DEV_DB_HOST + "/" + DEV_DB_NAME

class ProdConfig(Config):
	"""
	Production Environment configurations
	"""

	DEBUG = False
	SQLALCHEMY_DATABASE_URI = "mysql://" + DB_USER + ":" + DB_PASSWORD +"@" + DB_HOST + "/" + DB_NAME

config = {
	ENV_DEV: DevConfig,
	ENV_PROD: ProdConfig
}