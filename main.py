# import health
from health import server_health_check
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, sptm"

@app.route('/health')
def health():
    report = server_health_check()
    return report

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




