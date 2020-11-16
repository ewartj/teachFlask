import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, literal

from app import app

# out functions in new py script?

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    Same hello world, but better structure
    """
    string = 'Hello, World!'
    return render_template("index.html", string = string)