import requests
from flask import *
app = Flask(__name__)
@app.route("https://api-flaskb.herokuapp.com/e")
def f():
	return "Hello Word ! "
app.run()