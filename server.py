from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/status")
def status():
    current_time = datetime.strftime(datetime.now(), '%Y/%m/%d %H:%m')
    return {
        'status': True,
        'name': 'SkillMessenger',
        'time': current_time}

app.run()