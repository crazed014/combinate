from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to my app"



# run flask run --host=0.0.0.0