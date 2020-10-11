from flask import Flask, render_template
from flask_dropzone import Dropzone
import os

app = Flask(__name__)
dropzone = Dropzone(app)
viewcount = 0

basedir = os.path.abspath(os.path.dirname(__file__))

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_MAX_FILES=3,
    DROPZONE_UPLOAD_ON_CLICK=True
)
@app.route("/")
def welcome():
    return render_template("welcome.html", title="Combinate", formtext="Drag your first CSV here.")

@app.route("/viewed")
def viewed():
    global viewcount
    viewcount += 1
    return "This page has been served {} times since the last reboot.".format(str(viewcount))

@app.route('/uploads', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('/srv/combinate/files/', f.filename))

    return render_template("welcome.html", title="Combinate", formtext="Drag your second CSV here.")
#  flask run --host=0.0.0.0