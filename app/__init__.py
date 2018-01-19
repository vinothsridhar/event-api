from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

db = SQLAlchemy()

#creating app
def create_app(config):
	app.config.from_object(config)

	db.init_app(app)

	#logging
	handler = RotatingFileHandler(app.config['LOG_PATH'], maxBytes=10000, backupCount=1)
	handler.setLevel(logging.INFO)
	app.logger.addHandler(handler)

	app.logger.info(app.config)

	app.logger.info("app created successfully")

	from app import routes

	from app import models

	from models import initdb

	#init models
	with app.app_context():
		initdb()