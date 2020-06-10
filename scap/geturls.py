from flask import Blueprint, jsonify
from .database import db
from .modelscrap import Scrap

geturls = Blueprint("geturls", __name__)

@geturls.route("/<word>", methods=["GET"])
def _geturls(word):

    if not word:
        return jsonify(failed="I need a word try /geturls/pain")

    doc_ref = db.collection(u'images').document(word)

    doc = doc_ref.get()

    return jsonify(doc.to_dict())

    