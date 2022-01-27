from app import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    selected_word = db.Column(db.String)
    translation = db.Column(db.String)
    notes = db.Column(db.String)
    link = db.Column(db.String)
    language = db.Column(db.String)
    vocablist_id = db.Column(db.Integer, db.ForeignKey('vocablist.id'))
    vocablist = db.relationship("Vocablist", back_populates="words")

    

