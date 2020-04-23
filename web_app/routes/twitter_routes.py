# web_app/routes/twitter_routes.py

from flask import Blueprint, jsonify # , request, render_template #, flash, redirect

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/tweets.json")
def list_tweets():
    tweets = [
        {"id": 1, "tweet_text": "Tweet 1"},
        {"id": 2, "tweet_text": "Tweet 2"},
        {"id": 3, "tweet_text": "Tweet 3"},
    ]
    return jsonify(tweets)