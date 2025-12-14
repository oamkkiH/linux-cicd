from flask import Flask, jsonify
from datetime import datetime
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "cicd-backend"}), 200

@app.route("/api/time")
def server_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    app.logger.info(f"Time request served: {now}")
    return jsonify({"server_time": now})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
