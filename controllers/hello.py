from app import app

from flask import render_template


@app.route('/')
@app.route('/index')
def hello():
    return render_template('hello.html')
