from flask import render_template
from covador.flask import query_string

from . import app


@app.route('/')
def index():
    return render_template('ref-list.html')
