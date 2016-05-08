from flask import Flask, render_template
website = Flask(__name__)

@website.route('/')
def index():
	return render_template('index.html')	

if __name__ == '__main__':
	website.run(host='0.0.0.0')
