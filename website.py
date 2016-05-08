from __future__ import division, absolute_import, print_function, unicode_literals
from flask import Flask, render_template, request

website = Flask(__name__)

@website.route('/')
def index():
	return render_template('index.html')	

@website.route('/mothersday2016')
def mothersday2016():
	poem = ['The fish has too many bones,', 'and the watermelon too many seeds.']
	with open('mothersday2016poems/default.txt') as f:
		poem = f.read().strip().split('\n')
	balpreet = request.args.get('balpreet', '')
	return render_template('mothersday2016.html', balpreet=balpreet, poem=poem)

if __name__ == '__main__':
	website.run(host='0.0.0.0')
