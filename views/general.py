from flask import render_template, Blueprint

mod = Blueprint('general', __name__)


@mod.route('/')
def index():
    return render_template('index.html')



