# Import Flask class from flask module
# Flask is provided by the Flask package
from flask import Flask


# Create Flask application object
# app is our variable
# Flask() is Flask's class
app = Flask(__name__)


# Route 1
# "/" means Home Page
# When user visits http://127.0.0.1:5000/
# Flask runs home()
@app.route("/")
def home():

    # Send response back to browser
    return "Welcome to Flask Learning"


# Route 2
# When user visits http://127.0.0.1:5000/about
# Flask runs about()
@app.route("/about")
def about():

    return "This is About Page"


# Route 3
# When user visits http://127.0.0.1:5000/contact
# Flask runs contact()
@app.route("/contact")
def contact():

    return "Contact Page"


# Route 4
# Employee Page
@app.route("/employee")
def employee():

    return "Employee Management System"


# Start Flask web server
# Without this line website will not run
app.run()