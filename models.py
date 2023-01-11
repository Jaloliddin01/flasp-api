from datetime import datetime
from config import db, ma

class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), default=f"Tantiboyev")
    fname = db.Column(db.String(32), default=f"Bekorchibek")
    votes = db.Column(db.Integer, default=0)
    occupation = db.Column(db.String(32), default="Toza havo qorovuli")
    company = db.Column(db.String(32), default="Mahalla darvozasi yoni")
    liked = db.Column(db.Integer, default=0)

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session

person_schema = PersonSchema()
people_schema = PersonSchema(many=True)