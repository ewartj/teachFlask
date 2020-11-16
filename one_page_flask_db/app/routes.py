import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, literal

from app import app
from app.models import Schools

# out functions in new py script?

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    The home page. This will display a sql table (sequenced runs)
    """
    show = Schools.query.count()
    lists = Schools.query.all()
    return render_template("index.html", count=show, schools=lists)

@app.route('/runs/<slug>')
def detail(slug):
    """
    A page that will display more information about a sample
    """
    school = Schools.query.filter_by(Name=slug).first()
    return render_template("detail.html", school=school)

