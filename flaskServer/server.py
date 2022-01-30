from flask import Flask, render_template
# flask automatically converts routes to html

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, SUGANTHI!</p>"

# To create a blog
@app.route("/blog") # you can name it anything
def blog():
    return "<p>Just blogs!!!!</p>"
# you can create as many routes

# passing html file
@app.route("/html")
def html(): # Make sure to put the html files in templates folder, or won't work
    return render_template('index.html')

# Static files = css & js (never changes in background)
# Make sure to put the these files in static folder, or won't work

# Passing param in route
@app.route("/<username>/<int:id>")
def param(username=None, id=None):
    return render_template('index.html', name = username, num = id)
                                    # Make sure to set {{ assigned variable }} on html file, not parameter
