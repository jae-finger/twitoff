# web_app/routes/twitter_routes.py

from flask import Blueprint, jsonify, render_template #, request, flash, redirect

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/tweets.json")
def list_tweets():
    tweets = [
        {"id": 1, "tweet_text": "Tweet 1"},
        {"id": 2, "tweet_text": "Tweet 2"},
        {"id": 3, "tweet_text": "Tweet 3"},
    ]
    return jsonify(tweets)

@twitter_routes.route("/tweets")
def list_tweets_for_humans():
    tweets = [
        {"id": 1, "tweet_text": "Tweet 1"},
        {"id": 2, "tweet_text": "Tweet 2"},
        {"id": 3, "tweet_text": "Tweet 3"},
    ]
    return render_template("tweets.html", message="Here are some tweets for ya'.", tweets=tweets)