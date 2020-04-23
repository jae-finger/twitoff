# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print('You found the page. GJ!')
    return f"Hello World! -- I made this on 04/22/20"

@home_routes.route("/about")
def about():
    return "About me"