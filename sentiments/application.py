from flask import Flask, redirect, render_template, request, url_for

import helpers
from analyzer import Analyzer
import sys, os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)
    numTweets = len(tweets)
     
    if (numTweets == 0):
        screen_name = "ERROR: {} is not a valid twitter handle".format(screen_name)
        positive = negative = 0
        neutral = 1
        chart = helpers.chart(positive, negative, neutral)
        return render_template("search.html", chart=chart, screen_name=screen_name)   
    
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    
    analyzer = Analyzer(positives, negatives)
    
    posCount = negCount = neuCount = 0
    for tweet in tweets:
        score = analyzer.analyze(tweet)
        if score > 0.0:
            posCount += 1
        elif score < 0.0:
            negCount += 1
        else:
            neuCount += 1

    positive = posCount/numTweets
    negative = negCount/numTweets
    neutral = neuCount/numTweets

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
