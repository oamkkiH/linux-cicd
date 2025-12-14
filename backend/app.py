from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({
        "status": "ok",
        "message": "CI/CD demo backend running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "timestamp": time.time()})

@app.route("/api/time")
def api_time():
    return jsonify({"server_time": time.ctime()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
