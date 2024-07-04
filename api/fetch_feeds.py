from flask import Flask, jsonify
import feedparser

app = Flask(__name__)


# Function to fetch RSS feed and store it in a variable
def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    entries = feed.entries
    return entries


# Endpoint to fetch RSS feed
@app.route("/fetch", methods=["GET"])
def fetch():
    url = "https://www.xataka.com/feedburner.xml"  
    feed_data = fetch_rss_feed(url)
    return jsonify(feed_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
