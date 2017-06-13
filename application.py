from flask import Flask, render_template

import config
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db.init_app(app)


with app.app_context():
    db.create_all()
    db.session.commit()


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

from views import general
from views import persons

app.register_blueprint(general.mod)
app.register_blueprint(persons.mod)

if __name__ == '__main__':
    app.run()
