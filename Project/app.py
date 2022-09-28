from flask import Flask

app = Flask(__name__)

@app.route("/generate/")
def configGenerate():
    return "<p>My super service</p>"
