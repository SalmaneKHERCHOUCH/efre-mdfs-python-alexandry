import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

file = 'alexandry/bibliotheque.json'

with open(file, 'r',encoding='utf-8') as file:
    data = json.load(file)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return data

app.run()