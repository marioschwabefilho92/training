from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    text = "Mario POD on port 5000"
    return text

app.run(host='0.0.0.0', port=5000)