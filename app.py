from flask import Flask, flash, url_for, render_template, request
from markupsafe import escape
from search_engine import SearchEngine

# export FLASK_APP=app
app = Flask('MIPSE')
app.secret_key = 'foobar'

# initiate the search engine class
clip = SearchEngine('coco_dataset')

@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'GET':
		return render_template('main_page.html', query="")
	elif request.method == 'POST':
		query = request.form['query']
		return render_template('main_page.html',
													 query=query,
													 images=clip.search(query, image_count=100))
