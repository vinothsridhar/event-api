from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from db import db
from time import strftime, gmtime

#app build version
__version__ = strftime('%Y-%m-%d-%H%M', gmtime())

app = Flask(__name__)

#creating app
def create_app(config):
	app.config.from_object(config)

	db.init_app(app)

	#logging
	handler = RotatingFileHandler(app.config['LOG_PATH'], maxBytes=10000, backupCount=1)
	handler.setLevel(logging.INFO)
	app.logger.addHandler(handler)

	app.logger.info(app.config)

	from app import routes

	#init models
	with app.app_context():
		from app import models
		# db.drop_all()
		db.create_all()

	app.logger.info("app created successfully")