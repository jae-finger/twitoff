# web_app/routes/admin_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

from web_app.models import db

import os

admin_routes = Blueprint("admin_routes", __name__)

API_KEY = os.getenv("API_KEY")


# GET /admin/db/reset?api_key=jon123
@admin_routes.route("/admin/db/reset")
def reset_db():
    # print("URL PARMS", dict(request.args))

    # if "api_key" in dict(request.args) and request.args["api_key"] == API_KEY:
    #     print(type(db))
    #     db.drop_all()
    #     db.create_all()
    #     # return jsonify({"message": "DB RESET OK"})
    #     return redirect("/tweets")
    # else:
    #     return redirect("/tweets")
    db.drop_all()
    db.create_all()
    # return jsonify({"message": "DB RESET OK"})
    return redirect("/tweets")
