from app import app, db, lm
from flask import render_template, flash, redirect, url_for
from app.models.tables import User
from flask_login import login_user, logout_user

from app.models.forms import LoginForm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/index/<user>")
@app.route("/", defaults={"user":None})
def index(user):
    return render_template('index.html', user=user)


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("index"))
            flash("Logged in.")

        else:
            flash("Invalid login.")   
        
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))



@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    i = User("vitorrios", "1234", "Vitor Rios", "vitor@gmail.com")
    db.session.add(i)
    db.session.commit()  
    return "OK"  
