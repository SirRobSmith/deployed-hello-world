"""
app.py

An extraordinarily simple 'hello world' application which uses flask to 
create a simple /hello-world end-point. This project exists largely to 
show an example pipeline for deploying code to a GCP Cloud-Run instance. 

"""
import os
import json
import logging
from google.cloud import secretmanager


# Initalise the connection to Secrets Manager
secrets_client = secretmanager.SecretManagerServiceClient()

# Pull all of the relevant secrets, we get the reference for the secret with the environment variable SECRET_REF
SECRET_REF          = os.environ['SECRET_REF']
secret_data_raw     = secrets_client.access_secret_version(request={"name": SECRET_REF})
secret_decoded      = secret_data_raw.payload.data.decode("UTF-8")
secrets_data        = json.loads(secret_decoded)


from flask import Flask

app = Flask(__name__)

@app.route("/hello-world")
def hello_world():
    return "<p>Hello, World 123!</p>"
 
