from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}> Person(name: {})'.format(self.id, self.name)

    @property
    def serialized(self):
        """Return Person in serializable format"""
        return {
            'id': self.id,
            'name': self.name,
        }
