from flask import Flask, render_template

from settings import APP_ROOT

application = Flask(__name__)
application.debug = True


@application.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	application.run(host='0.0.0.0')
