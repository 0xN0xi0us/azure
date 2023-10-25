from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><!--Takeover by n0xi0us--> </html>"
