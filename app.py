import json
import os
from random import choice

from flask import Flask, jsonify, request
from redis import Redis


REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
SAMPLE_GIFS_IDS = [
    "8FGM7VT9bre1TqKRds",
    "fjxMDSKaAWv45IvfHo",
    "2A6YmvLNhJXSMzBM2G",
]

app = Flask(__name__)
redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

# This is supposed to be a GET endpoint, but Slack
# only sends POST requests in the 'slash command' feature
@app.route("/dale_gif", methods=["POST"])
def get_dale_gif():
    return jsonify({
        "response_type": "in_channel",
        "attachments": [{
            "title": "Vamo dale",
            "image_url": "https://media.giphy.com/media/" + __random_gif() + "/giphy.gif"
        }]
    })


@app.route("/register_dale_gif", methods=["POST"])
def register_dale_gif():
    data = request.get_json()
    gif_id = data.get("gif_id")

    if gif_id:
        if not __gif_already_exists(gif_id):
            __add_gifs([gif_id])
            return "OK", 201
        return "gif_id supplied is already registered", 404
    return "No gif_id supplied", 404


def __random_gif():
    if not __all_gifs():
        __add_gifs(SAMPLE_GIFS_IDS)
    return choice(__all_gifs())

def __gif_already_exists(gif_id):
    return gif_id in __all_gifs()

def __all_gifs():
    return [gif.decode() for gif in redis.lrange("GifsList", 0, -1)]

def __add_gifs(gif_ids):
    redis.lpush("GifsList", *gif_ids)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
