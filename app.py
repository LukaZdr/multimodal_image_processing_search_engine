from flask import Flask, flash, url_for, render_template, request
from markupsafe import escape

# export FLASK_APP=app
app = Flask('MIPSE')
app.secret_key = 'foobar'

@app.route('/', methods=['GET', 'POST'])
def hallo():
	if request.method == 'GET':
		return render_template('main_page.html', query="")
	elif request.method == 'POST':
		query = request.form['query']
		return render_template('main_page.html', query=query)
