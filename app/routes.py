from app import app
from flask import render_template


@app.route('/')
def index():

    context = {
        "head": "My favorite Artists"
    }
    return render_template('index.html', **context)

@app.route('/artists')
def artists():
    return render_template('artists.html')