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
		#calculate best images here
		images = [
			'https://images.ctfassets.net/hrltx12pl8hq/3MbF54EhWUhsXunc5Keueb/60774fbbff86e6bf6776f1e17a8016b4/04-nature_721703848.jpg?fit=fill&w=480&h=270',
			'https://media.istockphoto.com/photos/concept-of-an-open-magic-book-open-pages-with-water-and-land-and-picture-id1279460648?b=1&k=20&m=1279460648&s=170667a&w=0&h=uZa830sWo8hlFN0Y7FnQ14giNC0Z2EBNuTMuNJeJhQg=',
			'https://static.scientificamerican.com/sciam/cache/file/7A715AD8-449D-4B5A-ABA2C5D92D9B5A21_source.png',
			'https://www.inside-digital.de/img/Stiftung-Warentest-6-Gaming-Laptops-im-Test-1200x900.jpg',
			'https://www.3mdeutschland.de/wps/wcm/connect/c4c6a37e-9bad-4235-87b9-875e980a177e/4/giraffe_mobileimage2.jpg?MOD=AJPERES',
			'https://www.proshop.de/Images/915x900/2626563_c4315db873db.png',
			'https://miro.medium.com/max/640/1*UIsJisgPsdZh1O7fTFZx3A.jpeg',
		]*8

		return render_template('main_page.html',
													 query=query,
													 images=images)
