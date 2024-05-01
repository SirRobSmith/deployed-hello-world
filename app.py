"""
app.py

An extraordinarily simple 'hello world' application which uses flask to 
create a simple /hello-world end-point. This project exists largely to 
show an example pipeline for deploying code to a GCP Cloud-Run instance. 

"""

from flask import Flask

app = Flask(__name__)

@app.route("/hello-world")
def hello_world():
    return "<p>Hello, World 123!</p>"
 
