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

@vocablists_bp.route("/<id>/words", methods=["GET", "POST", "DELETE"])
def handle_vocablists_words(id):
    vocablist = Vocablist.query.get(id)

    if request.method == "POST":
        request_body = request.get_json()
        # if len(request_body["message"]) > 40:
        #     return jsonify(details="Message length must be 40 characters or less"), 400

        words_response = []

        new_word = Word(message=request_body["message"], likes_count=0, board=board)

        for word in words:
            words_response.append({
                "id" : word.id,
                "selected_word" : word.selected_word,
                "translation" : word.translation,
                "notes" : word.notes,
                "link" : word.link,
                "language" : word.language,
                "vocablist_id": word.vocablist_id
            })
        
            db.session.add(new_word)


        new_vocablist = Vocablist(name=request_body["name"], text=request_body["text"])

        db.session.add(new_vocablist)
        db.session.commit()

        return jsonify({"card":{"board_id": new_card.board_id, "card_id": new_card.id, "likes_count": new_card.likes_count, "message": new_card.message}}), 201
    
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
        
        return jsonify(words_response), 200

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


