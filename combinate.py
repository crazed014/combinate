from flask import Flask, render_template
app = Flask(__name__)
viewcount = 0

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/viewed")
def viewed():
    global viewcount
    viewcount += 1
    return "This page has been served {} times since the last reboot.".format(str(viewcount))

#  flask run --host=0.0.0.0