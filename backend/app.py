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
    return jsonify({
        "status": "healthy",
        "timestamp": time.time()
    })

@app.route("/api/time")
def api_time():
    # Return Europe/Helsinki local time
    helsinki_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return jsonify({"server_time": helsinki_time})

if __name__ == "__main__":
    # Run backend on port 5005 for Docker
    app.run(host="0.0.0.0", port=5005)
