from flask import Flask, jsonify, make_response
import feedparser
from feedgen.feed import FeedGenerator

app = Flask(__name__)


# Function to fetch RSS feed and store it in a variable
def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    entries = feed.entries
    return entries


def create_feed():
    fg = FeedGenerator()
    fg.id("http://lernfunk.de/media/654321")
    fg.title("Some Testfeed")
    fg.author({"name": "John Doe", "email": "john@example.de"})
    fg.link(href="http://example.com", rel="alternate")
    fg.logo("http://ex.com/logo.jpg")
    fg.subtitle("This is a cool feed!")
    fg.link(href="http://larskiesow.de/test.atom", rel="self")
    fg.language("en")
    rssfeed = fg.rss_str(pretty=True)  # Get the RSS feed as string
    return rssfeed


# # Endpoint to fetch RSS feed
# @app.route("/fetch", methods=["GET"])
# def fetch():
#     url = "https://www.xataka.com/feedburner.xml"
#     feed_data = fetch_rss_feed(url)
#     return jsonify(feed_data)


# TODO Voy a empezar trayendo un feed de xataka por ejemplo y guardandolo en unidades individuales en una base de datos para luego compilarlos
# y devolver el feed reconstruido.
# Despues de eso puedo seguir con hacer lo mismo para una lista de feeds.


# Code from https://www.reddit.com/r/flask/comments/evjcc5/question_on_how_to_generate_a_rss_feed/
@app.route("/rss")
def rss():
    fg = FeedGenerator()
    fg.id("http://lernfunk.de/media/654321")
    fg.title("Some Testfeed")
    fg.author({"name": "John Doe", "email": "john@example.de"})
    fg.link(href="http://example.com", rel="alternate")
    fg.logo("http://ex.com/logo.jpg")
    fg.subtitle("This is a cool feed!")
    fg.link(href="http://larskiesow.de/test.atom", rel="self")
    fg.language("en")

    response = make_response(fg.rss_str())
    response.headers.set("Content-Type", "application/rss+xml")

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
