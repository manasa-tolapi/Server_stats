# blog.py

blog_posts = [
    {
        "handle": "post-1",
        "title": "Getting Started with Flask",
        "short_desc": "A beginner-friendly guide to Flask.",
        "full_desc": "Flask is a lightweight WSGI web application framework in Python...",
        "image": "https://example.com/images/flask.png"
    },
    {
        "handle": "post-2",
        "title": "Understanding REST APIs",
        "short_desc": "Learn the basics of REST architecture.",
        "full_desc": "REST APIs are a way for systems to communicate over HTTP...",
        "image": "https://example.com/images/rest.png"
    },
    {
        "handle": "post-3",
        "title": "Python Tips & Tricks",
        "short_desc": "Boost your Python productivity.",
        "full_desc": "Here are some lesser-known Python tips and tricks...",
        "image": "https://example.com/images/python.png"
    },
    {
        "handle": "post-4",
        "title": "Deploying Flask Apps",
        "short_desc": "How to deploy your Flask app.",
        "full_desc": "Deploying Flask apps can be done using Gunicorn, Docker...",
        "image": "https://example.com/images/deploy.png"
    },
    {
        "handle": "post-5",
        "title": "Working with Databases",
        "short_desc": "Intro to databases with Flask.",
        "full_desc": "Flask supports multiple databases like SQLite, PostgreSQL...",
        "image": "https://example.com/images/db.png"
    },
    {
        "handle": "post-6",
        "title": "Flask vs Django",
        "short_desc": "Compare two popular frameworks.",
        "full_desc": "Flask and Django are both powerful, but they serve different needs...",
        "image": "https://example.com/images/flask-django.png"
    },
    {
        "handle": "post-7",
        "title": "API Security Basics",
        "short_desc": "Keep your APIs secure.",
        "full_desc": "Security is critical when exposing APIs. Use authentication...",
        "image": "https://example.com/images/security.png"
    }
]


def get_all_posts():
    return [
        {
            "handle": post["handle"],
            "title": post["title"],
            "short_desc": post["short_desc"],
            "image": post["image"]
        }
        for post in blog_posts
    ]


def get_post_by_handle(handle):
    for post in blog_posts:
        if post["handle"] == handle:
            return {
                "title": post["title"],
                "full_desc": post["full_desc"],
                "image": post["image"]
            }
    return None
