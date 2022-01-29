from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.vocablist import Vocablist
from app.models.word import Word

words_bp = Blueprint("words", __name__, url_prefix="/words")
vocablists_bp = Blueprint("vocablists", __name__, url_prefix="/vocablists")

# 1 /vocablists - lists all vocab lists
# 2 /vocablists/id - displays vocab list (so text and words) for vocab list with a specific id -BUT HOW CAN ACCES WORD MODEL WITH THIS ROUTE??

# 3 /words-lists all words irregardless of vocab list (currently not a target feature)

# 4 /words/vocablists/<vocablist_id> - returns all words associated with specified vocablists id -RELATED TO #2 ABOVE, HOW ACCESS VOCABLIST INFO THROUGH WORD ROUTE

# vocablists/vocablist_id/words
# 

@vocablists_bp.route("", methods=["GET", "POST"])
def handle_vocablists():
    # if request.method == "POST":
    #     request_body = request.get_json()
    #     # if "title" not in request_body or  request_body["title"] == "":
    #     #     return jsonify(details="Invalid request, a title is required."), 400
    #     # if "owner" not in request_body or request_body["owner"] == "":
    #     #     return jsonify(details="Invalid request, an owner is required."), 400

    #     new_vocablist = Vocablist(name=request_body["name"], text=request_body["text"])



    #     db.session.add(new_vocablist)
    #     db.session.commit()
        

    #     return jsonify({"vocablist":{"vocablist_id": new_vocablist.id, "text": new_vocablist.text, "name": new_vocablist.name}}), 201

    # to save/post vocab list and all its words
    if request.method == "POST":

        request_body = request.get_json()

        new_vocablist = Vocablist(name=request_body["vocablist"]["name"], text=request_body["vocablist"]["text"])

        db.session.add(new_vocablist)
        db.session.commit()
        
        # request body is a dictionary
        # if len(request_body["message"]) > 40:
        #     return jsonify(details="Message length must be 40 characters or less"), 400

        words_response = []

    # new vocab list is object not dictionary

        
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
                

            #     for i in range(len(request_body["words"])):
            # for word in request_body["words"]:
            #     new_word = Word(selected_word=word[i]
            #     ["selected_word"], translation=word[i]["translation"], notes=word[i]["notes"], link=word[i]["link"], language=word[i]["language"], vocablist_id=new_vocablist.id)
                

            #     db.session.add(new_word)
            #     db.session.commit()

            #     words_response.append({
            #         "id": word.id,
            #         "selected_word": word.selected_word,
            #         "translation": word.translation,
            #         "notes": word.notes,
            #         "link": word.link,
            #         "language": word.language,
            #         "vocablist_id": word.vocablist_id
            #     })
        # vocablist_response = {"vocablist": {"id":new_vocablist.id, "name": new_vocablist.name, "text": new_vocablist.text}}
            
    # information give in request body to database
        # {"vocablist": {"name": vocablist.name, "text": vocablist.text},
        # "words": [{
        #         "selected_word" : word.selected_word,
        #         "translation" : word.translation,
        #         "notes" : word.notes,
        #         "link" : word.link,
        #         "language" : word.language,
        #         "vocablist_id": word.vocablist_id
        #     },
        #     {
        #         "selected_word" : word.selected_word,
        #         "translation" : word.translation,
        #         "notes" : word.notes,
        #         "link" : word.link,
        #         "language" : word.language,
        #         "vocablist_id": word.vocablist_id
        #     }
            
        # ]}
        

        

        return jsonify({"vocablist": {"id":new_vocablist.id, "name": new_vocablist.name, "text": new_vocablist.text}, "words": words_response}), 201

    # Use this endpoint's GET request to just get a list of vocab list names (to display on select a vocab list page)
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


# @boards_bp.route("/<id>", methods=["DELETE"]) 
# def handle_board(id):
#     board = Board.query.get(id)
#     if request.method == "DELETE":
#         db.session.delete(board)
#         db.session.commit()
#         return make_response(f"Board #{id} successfully deleted")


# vocablists/vocablist_id/words

@vocablists_bp.route("/<id>/words", methods=["GET", "DELETE"])
def handle_vocablists_words(id):
    vocablist = Vocablist.query.get(id)

    #CREATE DELETE ROUTE-so if hit delete button will delete all words and text associated with vocab list ID
    
    #call to use to get all info needed to display a specific vocab list
    if request.method == "GET":
        
        words = vocablist.words 
        words_response = []

        for word in words:
            words_response.append({
                "id": word.id,
                "selected_word": word.selected_word,
                "translation": word.translation,
                "notes" : word.notes,
                "link" : word.link,
                "language": word.language,
                "vocablist_id": word.vocablist_id
            })
        
        return jsonify({"vocablist": {"id":vocablist.id, "name": vocablist.name, "text": vocablist.text}, "words": words_response}), 200

# @cards_bp.route("/<id>", methods=["DELETE", "PATCH"])
# def handle_cards(id):
#     card = Card.query.get(id)
    
#     if request.method == "DELETE":
#         db.session.delete(card)
#         db.session.commit()
#         return make_response(f"Card #{id} successfully deleted")
#     if request.method == "PATCH":
#         card.likes_count += 1
    
#         db.session.commit()

#         return jsonify({"likes_count": card.likes_count }), 200


