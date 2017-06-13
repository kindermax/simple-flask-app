from flask import Blueprint, jsonify, request, escape
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

from models import Person, db

mod = Blueprint('persons', __name__, url_prefix='/api')


@mod.route('/add_person', methods=['POST'])
def save_person():
    name = request.form['name']
    if not name:
        return
    try:
        person = Person(name)
        db.session.add(person)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'person': escape(name)}), 409

    return jsonify({'person': escape(name)}), 201


@mod.route('/delete_person', methods=['POST'])
def delete_person():
    name = request.form['name']
    if name:
        count = Person.query.filter_by(name=name).delete()
        db.session.commit()
        if not count:
            return jsonify({'person': escape(name)}), 400
    return jsonify({'person': escape(name)}), 200


@mod.route('/random_persons', methods=['GET'])
def get_persons():
    rand_count = 3
    persons = db.session.query(Person).order_by(func.random()).limit(rand_count).all()
    return jsonify({'persons': [p.serialized for p in persons]}), 200
