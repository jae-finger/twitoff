# web_app/routes/twitter_routes.py

from flask import Blueprint, jsonify, render_template, request, flash, redirect
from web_app.models import User, db, Tweet, parse_records
from web_app.services.twitter_service import api as twitter_api
from web_app.services.basilica_service import connection as basilica_connection

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
    # new_tweet = Tweet(tweet_text=request.form["tweet_text"], user_name=request.form["user_name"])
    user_name=request.form["user_name"]
    # db.session.add(new_user)
    # db.session.add(new_tweet)
    # db.session.commit()

    # flash(f"New tweet by '{user_name}' created successfully!", "dark")
    return redirect(f"/users/{user_name}/fetch")

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user_data(screen_name):
    # print("Fetching:", screen_name)

    # 1. Fetch user info
    user = twitter_api.get_user(screen_name)
    
    # 2. Store user info in DB
    db_user = User.query.get(user.id) or User(id=user.id)
    db_user.screen_name = user.screen_name
    db_user.name = user.name
    db_user.location = user.location
    db_user.followers_count = user.followers_count
    db.session.add(db_user)
    db.session.commit()
    

    # 3. Fetch their tweets
    users_tweets = twitter_api.user_timeline(screen_name, tweet_mode="extended", count=200, exclude_replies=True, include_rts=False)

    # 4. Fetch embedding for tweet
    tweet_texts = [tweets.full_text for tweets in users_tweets]
    embeddings = list(basilica_connection.embed_sentences(tweet_texts, model="twitter"))
    # print("EMBEDDINGS", len(embeddings))
    
    # 5. Store tweets in database with embedding
    for index, tweets in enumerate(users_tweets):
        db_tweet = Tweet.query.get(tweets.id) or Tweet(id=tweets.id)
        db_tweet.user_id = tweets.author.id
        db_tweet.full_text = tweets.full_text
        embedding = embeddings[index]
        print(len(embedding))
        db_tweet.embedding = embedding
        db.session.add(db_tweet)

    db.session.commit()

    # return jsonify({"user": user._json, "num_tweets": len(users_tweets)})
    return redirect("/tweets")