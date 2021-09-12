from nyaaabeou import app

import functools
import os
import sys
from flask import Flask, request, Response, abort, render_template, flash, redirect
from flask_login import current_user,login_user,login_required,LoginManager,UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, ValidationError
from flask_sqlalchemy import SQLAlchemy

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'secret'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text())
    password = db.Column(db.Text())
    def __init__(self,username,password):
        self.username = username
        self.password = password

db.create_all()
class LoginForm(FlaskForm):
    username = StringField('username',validators=[
        validators.DataRequired(message = 'must input'),
        validators.EqualTo('username',message = 'Username must match.')
        ])
    password = PasswordField('password', validators = [
        validators.DataRequired(message = 'must input'),
        validators.AnyOf(values = ['password'], message = 'missed'),
        validators.EqualTo('password',message = 'Password must match.')
        ])
    submit = SubmitField('login')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm() 
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data, password=form.password.data).one_or_none():
            user = User.query.filter_by(username=form.username.data).one_or_none()
            login_user(user)
            return redirect('/blog/blog.html')
        else:
            return 'Missed'

    return render_template(
        'login.html',
        title='Login',
        form = form
        )
