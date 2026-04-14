from flask import Flask, jsonify
import os, socket, redis
app = Flask(__name__)
cache = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)
@app.route("/")
def index():
    visits = cache.incr("visits")
    return f"<h1>GitHub Cloud Lab</h1><p>Visits: {visits}</p>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
