from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/api/time", methods=["GET"])
def get_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"server_time": now})

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Backend running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
