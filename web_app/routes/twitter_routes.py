# web_app/routes/twitter_routes.py

from flask import Blueprint, jsonify, render_template, request, flash, redirect
from web_app.models import User, db, Tweet, parse_records

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/tweets.json")
def list_tweets():
    tweet_list = Tweet.query.all()
    tweets_response = parse_records(tweet_list)
    return jsonify(tweets_response)

@twitter_routes.route("/tweets")
def list_tweets_for_humans():
    tweets_list = Tweet.query.all()
    return render_template("tweets.html", message="Here are some tweets for ya'.", tweets=tweets_list)

@twitter_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@twitter_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form)) #> {"tweet_text": "?, "user_name": "?"}

    new_tweet = Tweet(tweet_text=request.form["tweet_text"], user_name=request.form["user_name"])
    new_user = User(user_name=request.form["user_name"])
    db.session.add(new_user)
    db.session.add(new_tweet)
    db.session.commit()

    return jsonify({
        "message": "TWEET CREATED OK",
        "tweet": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")
      