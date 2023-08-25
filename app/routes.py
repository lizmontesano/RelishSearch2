import json

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    items = []
    with open('app/static/data.jsonl') as f:
        for line in f:
            item = json.loads(line)
            items.append(item)
    return render_template('index.html', items=items)

@app.route('/api')
def api():
    with open('/static/data.jsonl', mode='r') as my_file:
        text = my_file.read()
        return text
