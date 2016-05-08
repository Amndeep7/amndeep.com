from flask import Flask, render_template, request

website = Flask(__name__)

@website.route('/')
def index():
	return render_template('index.html')	

@website.route('/mothersday2016')
def mothersday2016():
	balpreet = request.args.get('balpreet', '')
	return render_template('mothersday2016.html', balpreet=balpreet)

if __name__ == '__main__':
	website.run(host='0.0.0.0')
