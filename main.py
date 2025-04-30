import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

port = int(os.environ.get("PORT", 10000))  # Render usa esta variable
app.run(host="0.0.0.0", port=port)