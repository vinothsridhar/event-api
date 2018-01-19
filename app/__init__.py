from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

db = SQLAlchemy()

migrate = Migrate(app, db)

#creating app
def create_app(config):
	app.config.from_object(config)

	db.init_app(app)

	#logging
	handler = RotatingFileHandler(app.config['LOG_PATH'], maxBytes=10000, backupCount=1)
	handler.setLevel(logging.INFO)
	app.logger.addHandler(handler)

	app.logger.info("app created successfully")

from app import routes

from app import models