import os

from app import app, create_app

from app.config import config, ENV_PROD, ENV_VARIABLE_NAME

ENV = os.getenv(ENV_VARIABLE_NAME, ENV_PROD)

if __name__ == '__main__':
	create_app(config[ENV])
	app.run()