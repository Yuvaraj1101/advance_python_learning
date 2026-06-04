# Import Flask
from flask import Flask

# Create Flask App
app = Flask(__name__)


# Employee API
@app.route("/employee")
def employee():

    # Return Dictionary
    return {
        "id": 101,
        "name": "Yuvaraj",
        "department": "Data Analytics"
    }


# Start Server
app.run()