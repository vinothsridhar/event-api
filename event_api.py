import sys

from app import app, create_app

from config import config

#ENV = sys.argv[1]
ENV = "dev"

if __name__ == '__main__':
	create_app(config[ENV])
	app.run()