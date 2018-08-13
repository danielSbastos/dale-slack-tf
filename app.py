from random import choice

from flask import Flask, jsonify


app = Flask(__name__)

GIFS_IDS = [
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
            "image_url": "https://media.giphy.com/media/" + choice(GIFS_IDS) + "/giphy.gif"
        }]
    })


if __name__ == '__main__':
    app.run()
