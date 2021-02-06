from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import redirect
from flask_script import Manager

# window
# set FLASK_APP=hello.py
# linux
# export FLASK_APP=hello.py

app = Flask(__name__)

@app.route('/')
def index():
	# response = make_response('<h1>This document carries a cookie!</h1>')
	# response.set_cookie('answer','42')
	# return response
	# return redirect('http://www.baidu.com')

	# return '<h1>Bad Request</h1>', 400
	return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
	
# def sendtemplate():
# 	return render_template('hello.html')

@app.route('/info',methods=['GET',])
def sendinfo_tem():
	#获取到传入url参数id对应的值，例如/info?id=666
	sendid = request.args.get('id')
	return render_template("hello.html",u=sendid)

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>'%name

@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello, %s</h1>' % user.name

manager = Manager(app)

if __name__ == "__main__":
	# app.run(host='0.0.0.0',port=8080)
	# app.run(debug=True)
	manager.run()