from flask import Flask, jsonify
from flask_cors import CORS   # ✅ add this
from blog import get_all_posts, get_post_by_handle
from health import server_health_check

app = Flask(__name__)

# ✅ enable CORS
CORS(app)

@app.route('/')
def home():
    return "Hello, sptm april-25 v1"

@app.route('/health')
def health():
    return server_health_check()

@app.route('/api/posts')
def posts():
    return jsonify(get_all_posts())

@app.route('/api/post/<postHandle>')
def post_detail(postHandle):
    post = get_post_by_handle(postHandle)
    if post:
        return jsonify(post)
    return jsonify({"error": "Post not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
