from urllib import response
from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.vocablist import Vocablist
from app.models.word import Word
import google.auth
from google.cloud import translate_v2 as translate

words_bp = Blueprint("words", __name__, url_prefix="/words")
vocablists_bp = Blueprint("vocablists", __name__, url_prefix="/vocablists")
translation_bp = Blueprint("translation", __name__, url_prefix="/translation")


@translation_bp.route("", methods=["GET", "POST"])
def handle_translation():

    if request.method=="POST":
        request_body = request.get_json()

        translate_client = translate.Client()

        text=request_body["words"]
        target=request_body["lang"]
        source_language=request_body["original_lang"]
       
        result = translate_client.translate(text, source_language=source_language, target_language=target)

        return jsonify(result)
      

@vocablists_bp.route("", methods=["GET", "POST"])
def handle_vocablists():
    
    if request.method == "POST":

        request_body = request.get_json()

        new_vocablist = Vocablist(name=request_body["vocablist"]["name"], text=request_body["vocablist"]["text"])

        db.session.add(new_vocablist)
        db.session.commit()

        words_response = []
        
        for word in request_body["words"]:
            new_word = Word(selected_word=word
            ["selected_word"], translation=word["translation"], notes=word["notes"], link=word["link"], language=word["language"], vocablist_id=new_vocablist.id)
            
            db.session.add(new_word)
            db.session.commit()

            words_response.append({
                "id": new_word.id,
                "selected_word": new_word.selected_word,
                "translation": new_word.translation,
                "notes": new_word.notes,
                "link": new_word.link,
                "language": new_word.language,
                "vocablist_id": new_word.vocablist_id
            })

        return jsonify({"vocablist": {"id":new_vocablist.id, "name": new_vocablist.name, "text": new_vocablist.text}, "words": words_response}), 201
   
    if request.method == "GET": 
        vocablists = Vocablist.query.all()
        vocablists_response = []
        for vocablist in vocablists:
            vocablists_response.append({
                "id" : vocablist.id,
                "name" : vocablist.name,
                "text" : vocablist.text
            })

        return jsonify(vocablists_response), 200


@vocablists_bp.route("/<id>/words", methods=["GET", "DELETE"])
def handle_vocablists_words(id):
    vocablist = Vocablist.query.get(id)
    words = vocablist.words 
        
    if request.method == "DELETE":
        for word in words:
            db.session.delete(word)
    
        db.session.delete(vocablist)
        db.session.commit()
        return make_response(f"Vocablist #{id} and all words associated with it successfully deleted")

    if request.method == "GET":
        
        words_response = []

        for word in words:
            words_response.append({
                "id": word.id,
                "selected_word": word.selected_word,
                "translation": word.translation,
                "notes": word.notes,
                "link": word.link,
                "language": word.language,
                "vocablist_id": word.vocablist_id
            })
        
        return jsonify({"vocablist": {"id":vocablist.id, "name": vocablist.name, "text": vocablist.text}, "words": words_response}), 200


@words_bp.route("", methods=["GET", "POST"])
def handle_words():
    if request.method=="GET":
        words = Word.query.all()

        words_response=[]

        for word in words:
            words_response.append({
                "id": word.id,
                "selected_word": word.selected_word,
                "translation": word.translation,
                "notes": word.notes,
                "link": word.link,
                "language": word.language,
                "vocablist_id": word.vocablist_id
            })

        return jsonify(words_response)




