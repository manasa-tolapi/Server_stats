# import health
from health import server_health_check
from flask import Flask, jsonify
from blog import get_all_posts, get_post_by_handle

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, sptm april-25 v1"

@app.route('/health')
def health():
    report = server_health_check()
    return report


# ✅ API 1: Get all posts (title, short-desc, image)
@app.route('/posts')
def posts():
    return jsonify(get_all_posts())


# ✅ API 2: Get single post by handle
@app.route('/post/<postHandle>')
def post_detail(postHandle):
    post = get_post_by_handle(postHandle)
    if post:
        return jsonify(post)
    return jsonify({"error": "Post not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
