import json
import os
from random import choice

from flask import Flask, jsonify, request
from redis import Redis


REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
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
def dale_gif():
    gif_id = request.form.get("text")
    if gif_id:
        return __register_gif(gif_id)
    return __random_gif()


def __register_gif(gif_id):
    if gif_id:
        if not __gif_already_exists(gif_id):
            __add_gifs([gif_id])
            return "Gif id `" + gif_id + "` registered!", 201
        return "gif_id supplied is already registered.", 404
    return "No gif_id supplied.", 404


def __random_gif():
    if not __all_gifs():
        __add_gifs(SAMPLE_GIFS_IDS)
    return jsonify({
        "response_type": "in_channel",
        "attachments": [{
            "title": "Vamo dale",
            "image_url": "https://media.giphy.com/media/" + choice(__all_gifs()) + "/giphy.gif"
        }]
    })

def __gif_already_exists(gif_id):
    return gif_id in __all_gifs()

def __all_gifs():
    return [gif.decode() for gif in redis.lrange("GifsList", 0, -1)]

def __add_gifs(gif_ids):
    redis.lpush("GifsList", *gif_ids)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
