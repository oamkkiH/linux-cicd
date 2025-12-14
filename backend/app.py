from flask import Flask, jsonify
from datetime import datetime
import platform
import pytz

app = Flask(__name__)

@app.get("/api/time")
def get_time():
    tz = pytz.timezone("Europe/Helsinki")
    now = datetime.now(tz)

    return jsonify({
        "status": "ok",
        "time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "timestamp": int(now.timestamp()),
        "timezone": "Europe/Helsinki",
        "server": platform.node()
    })
