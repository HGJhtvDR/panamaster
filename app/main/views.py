from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/company')
def company():
    return render_template('company.html')

@main.route('/services')
def services():
    return render_template('services.html') 