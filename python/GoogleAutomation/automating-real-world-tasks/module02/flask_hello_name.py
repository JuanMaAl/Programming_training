from flask import Flask

app = Flask("hello")

@app.route('/hello/<name>')
def hello_name(name):
	return f'Hello, {name}!'
