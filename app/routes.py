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

@app.route('/data')
def data():
    items = []
    with open('app/static/data.jsonl') as f:
        for line in f:
            item = json.loads(line)
            items.append(item)
    return render_template('json.html', items=items)