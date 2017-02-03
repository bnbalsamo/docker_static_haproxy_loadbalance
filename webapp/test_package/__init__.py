from flask import Flask
from socket import gethostname

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World (from {})".format(gethostname())

if __name__ == "main":
    app.run()
