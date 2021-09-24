import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

file = 'alexandry/bibliotheque.json'

#Ensuite on le lit en le stockant dans data
with open(file, 'r',encoding='utf-8') as file:
    data = json.load(file)
    print("On veut voir notre fichier json", data)
    
#Il s'agit d'une route ou lorsque l'url est rentrée on retourne le texte ecrit
@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

#Il s'agit d'une route qui vas retourner tout notre JSON
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return data

#Il s'agit d'une route qui vas retourner un livre selon son ID
@app.route('/api/v1/resources/books/<int:id>', methods=['GET'])
def api_id(id):
    
    results = []

    for book in data:
        
        if book['Id'] == id:
            results.append(book)

    return jsonify(results)

app.run()