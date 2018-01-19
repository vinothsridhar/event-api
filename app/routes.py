from app import app

@app.route('/')
@app.route('/index')
def index():
	app.logger.info("inside index")
	return 'Hello, World!'