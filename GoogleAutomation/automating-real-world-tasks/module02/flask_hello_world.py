# This is not an executable code block
from flask import Flask

app = Flask("myapp")

@app.route('/')
def hello_world():
	return 'Hello, World!'
