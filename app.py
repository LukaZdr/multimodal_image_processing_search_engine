from flask import Flask, flash, url_for, render_template, request
from markupsafe import escape
from search_engine import SearchEngine

# export FLASK_APP=app
app = Flask('MIPSE')
app.secret_key = 'foobar'
app.config['TEMPLATES_AUTO_RELOAD'] = True

# initiate the search engine class
coco_clip = SearchEngine('coco_dataset')
unsplash_clip = SearchEngine('unsplash_dataset')

search_engines = {
	'Coco': coco_clip,
	'Unsplash': unsplash_clip
}

@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'GET':
		return render_template('main_page.html', query="")
	elif request.method == 'POST':
		query = request.form['query']
		search_engine = request.form['dataset']
		image_count = int(request.form['image_count'])
		return render_template('main_page.html',
								query=query,
								search_engine=search_engine,
								images=search_engines[search_engine].search(query, image_count=image_count),
								image_count=image_count)
