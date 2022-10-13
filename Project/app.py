from flask import Flask, request
## import our module that creates the config file.
from modules import generate_template
import json

app = Flask(__name__)

@app.route('/generate/<env>', methods = ['GET', 'POST'])

def configGenerate(env):
    # Invoke our custom code and catch any error
    try:
        generate_template.get_template(env)
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    except:
        return json.dumps({'success':False}), 500, {'ContentType':'application/json'}
