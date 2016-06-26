import os
from flask import Flask, render_template, request

from settings import APP_ROOT

application = Flask(__name__)
application.debug = True

@application.route('/')
def index():
	return render_template('index.html')	

@application.route('/mothersday2016')
def mothersday2016():
	poem = ['The fish has too many bones,', 'and the watermelon too many seeds.']
	with open(os.path.join(APP_ROOT, 'mothersday2016poems/poem1.txt')) as f:
		poem = f.read().strip().split('\n')
	balpreet = request.args.get('balpreet', '')
	return render_template('mothersday2016.html', balpreet=balpreet, poem=poem)

if __name__ == '__main__':
	application.run(host='0.0.0.0')
