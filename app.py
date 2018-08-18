import os
from random import choice

from flask import Flask, jsonify
from redis import Redis


app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

SAMPLE_GIFS_IDS = [
    "8FGM7VT9bre1TqKRds",
    "fjxMDSKaAWv45IvfHo",
    "2A6YmvLNhJXSMzBM2G",
]

@app.route("/dale_gif", methods=["POST"])
def dale_gif():
    return jsonify({
        "response_type": "in_channel",
        "attachments": [{
            "title": "Vamo dale",
            "image_url": "https://media.giphy.com/media/" + choice(__get_all_gifs()) + "/giphy.gif"
        }]
    })


def __get_all_gifs():
    if not redis.lrange("GifsList", 0, -1):
        redis.lpush("GifsList", *SAMPLE_GIFS_IDS)
    return [gif.decode() for gif in redis.lrange("GifsList", 0, -1)]


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
