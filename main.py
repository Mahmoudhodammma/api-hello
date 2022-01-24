import requests
from flask import *
app = Flask(__name__)
@app.route("https://apiflaskl.herokuapp.com/")
def f():
	return "Hello Word ! "
if __name__ =="__main__":
	app.run()
