from flask import Flask, flash, url_for, render_template
from markupsafe import escape

# export FLASK_APP=app
app = Flask('MIPSE')
app.secret_key = "foobar"

@app.route('/')
@app.route('/<query>')
def hallo(query=None):
	return render_template("main_page.html", name=query)