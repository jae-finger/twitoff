# web_app/routes/home_routes.py

from flask import Blueprint, render_template
from web_app.models import db, User


home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def hello_world():
    user_names = User.query.all()
    return render_template("prediction_form.html", users=user_names)

@home_routes.route("/about")
def about():
    print("YOU VISITED THE ABOUT PAGE")
    return "About Me (TODO)"