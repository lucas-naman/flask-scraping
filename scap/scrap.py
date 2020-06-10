from flask import Blueprint, jsonify
import requests
from bs4 import BeautifulSoup
from .database import db
from .modelscrap import Scrap

scrap = Blueprint("scrap", __name__)

@scrap.route("/<word>", methods=["GET"])
def _scrap(word):

    if not word:
        return jsonify(failed="I need a word try /scrap/pain")

    # Create the collection
    doc_ref = db.collection(u'images').document(word)

    # Scrap
    url = "https://fr.wikipedia.org/wiki/" + word
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    images = soup.find_all("img")    
    if not images:
        return jsonify(failed="True")

    # Create a list of images Url
    listUrl = []
    for cnt, image in enumerate(images):
        listUrl.append(image["src"][2:])
        if cnt >= 9:
            break

    # Push into the DataBase
    doc_ref.set(Scrap(word, listUrl).to_dict())

    # Return the nice message
    return jsonify(goto="/geturls/" + word, success="Got em")
    