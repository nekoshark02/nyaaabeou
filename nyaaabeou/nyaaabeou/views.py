"""
Routes and views for the flask application.
"""
# coding :utf-8
from flask import render_template,Flask
from nyaaabeou import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title = 'home'
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title = 'contact'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title = 'about'
    )
