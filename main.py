# import health
from health import server_health_check
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Hi"

@app.route('/health')
def health():
    report = server_health_check()
    return report

app.run()




