from app import db

class Vocablist(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    text = db.Column(db.String)
    words = db.relationship("Word", back_populates="vocablist")

   