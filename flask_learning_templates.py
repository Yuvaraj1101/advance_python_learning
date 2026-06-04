# Import Flask class
from flask import Flask

# Import render_template function
from flask import render_template


# Create Flask Application
app = Flask(__name__)


# Home Route
# If user visits "/"
# Flask runs home()
@app.route("/")
def home():

    # Load home.html
    return render_template("home.html")


# About Route
# If user visits "/about"
# Flask runs about()
@app.route("/about")
def about():

    # Load about.html
    return render_template("about.html")


# Start Flask Server
app.run()