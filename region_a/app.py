from flask import Flask, jsonify

app = Flask(__name__)

REGION = "region-a"


@app.route("/")
def home():

    return jsonify({
        "message": "Hello from Region A",
        "region": REGION
    })


@app.route("/health")
def health():

    return jsonify({
        "status": "healthy",
        "region": REGION
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
