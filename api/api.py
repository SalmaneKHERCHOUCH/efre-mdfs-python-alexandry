import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

file = 'alexandry/bibliotheque.json'

#Ensuite on le lit en le stockant dans data
with open(file, 'r',encoding='utf-8') as file:
    data = json.load(file)
    
#Il s'agit d'une route ou lorsque l'url est rentrée on retourne le texte ecrit
@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

#Il s'agit d'une route qui vas retourner tout notre JSON
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(data)

#Il s'agit d'une route qui va retourner un livre selon son ID
@app.route('/api/v1/resources/books/<int:id>', methods=['GET'])
def api_id(id):
    
    results = []

    for book in data:
        
        if book['Id'] == id:
            results.append(book)

    return jsonify(results)

#formulaire pour créer un livre
@app.route('/api/v1/resources/books/formulaire', methods=['GET'])
def form():
    return '<form action="/api/v1/resources/books/create"><label for="Titre">Titre:</label><br><input type="text" id="Titre" name="Titre"><br><label for="auteur">Auteur:</label><br><input type="text" id="auteur" name="auteur"><br><label for="edition">Edition:</label><br><input type="text" id="edition" name="edition"><br><label for="date">Date de publication:</label><br><input type="date" id="date" name="date"><br><label for="nbpages">Nombre de pages:</label><br><input type="number" id="nbpages" name="nbpages"><br><label for="genre1">Genre 1:</label><br><input type="text" id="genre1" name="genre"><br><label for="genre2">Genre 2:</label><br><input type="text" id="genre2" name="genre2"><br><br><input type="submit" value="Submit"></form>'

#appel du post après l'envoi du formulaire
@app.route('/api/v1/resources/books/create', methods=['GET', 'POST'])
def postBook():
    Titre = request.args.get('Titre')
    Auteur = request.args.get('auteur')
    Edition = request.args.get('edition')
    nb = request.args.get('nbpages')
    g1 = request.args.get('genre1')
    g2 = request.args.get('genre2')
    Id = len(data) + 1
    date = request.args.get('date')
    data.append({"Id":Id,"Titre":Titre,"Auteur":Auteur,"Edition":Edition,"Nombre de page":nb,"Date de publication":date,"genre":[g1,g2]})
    
    with open("alexandry/bibliotheque.json", "w",encoding='utf8') as file:
        json.dump(data, file,ensure_ascii=False,indent=4)
    
    return '<h2>Livre ajouté!</h2></br></br><a href="/">menu</a>'

@app.route('/api/v1/resources/books/delete/<int:id>',methods=['GET'])
def deleteBook(id):

    for book in data:

        if book['Id'] == id:
            data.remove(book)

    return '<h2>Livre supprimé!</h2>'

app.run()