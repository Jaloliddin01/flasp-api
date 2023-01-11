from flask import abort, make_response
from config import db
from models import Person, PersonSchema, people_schema, person_schema


def read_all():
    people = Person.query.all()
    return people_schema.dump(people)


def read_one(lname):
    person = Person.query.filter(Person.lname == lname).one_or_none()

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(404, f"Person with last name {lname} not found")

def create(person):
    new_person = person_schema.load(person, session=db.session)
    db.session.add(new_person)
    db.session.commit()
    return person_schema.dump(new_person), 201

def update(lname, person):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        update_person = person_schema.load(person, session=db.session)
        print(update_person)
        if update_person.fname:
            existing_person.fname = update_person.fname
        if update_person.lname:
            existing_person.lname = update_person.lname
        if update_person.votes:
            existing_person.votes = update_person.votes
        if update_person.occupation:
            existing_person.occupation = update_person.occupation
        if update_person.company:
            existing_person.company = update_person.company
        if update_person.liked:
            existing_person.liked = update_person.liked
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(404, f"Person with last name {lname} not found")

def delete(lname):
    existing_person = Person.query.filter(Person.lname == lname).all()

    if len(existing_person):
        for person in existing_person:
            db.session.delete(person)
            db.session.commit()
            return make_response(f"Person {lname} was successfully deleted", 200)
    else:
        abort(404, f"Person with last name {id} not found")