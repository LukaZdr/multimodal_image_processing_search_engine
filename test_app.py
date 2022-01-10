from flask import Flask, flash, url_for, render_template
from markupsafe import escape

# export FLASK_APP=hello
app = Flask('hello')
app.secret_key = "super secret key"

@app.route('/')
@app.route('/<name>')
def hallo(name=None):
    flash('test')
    return render_template("greetings.html", name=name)

@app.route('/other_page')
def other_page():
    return 'other_page'

@app.route('/param_page/<int:id>')
def show_id(id):
    # converter types
    """
    string  | (default) accepts any text without a slash
    int     | accepts positive integers
    float   | accepts positive floating point values
    path    | like string but also accepts slashes
    uuid    | accepts UUID strings
    """
    return f"This is your id: {escape(id)}"