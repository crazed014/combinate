import os

from flask import Flask, render_template, request
from flask_dropzone import Dropzone

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    DROPZONE_ALLOWED_FILE_CUSTOM = True,
    DROPZONE_ALLOWED_FILE_TYPE = '.csv, .txt',
    DROPZONE_MAX_FILES=2,
    DROPZONE_DEFAULT_MESSAGE = "Click or Drag your two CSV files to upload."
)


dropzone = Dropzone(app)



@app.route('/', methods=['POST', 'GET'])
def upload():
    global filecount
    filecount = 0 
    if request.method == 'POST':
        for key, f in request.files.items():
            if key.startswith('file'):
                f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
                filecount += 1
    if filecount < 2:
        app.config.update(DROPZONE_REDIRECT_VIEW='second')
        print("Didn't upload second csv, redirecting. CSV count is: {}".format(str(filecount)))
    else:
        app.config.update(DROPZONE_REDIRECT_VIEW='completed')
        print("Did upload second csv, redirecting. CSV count is: {}".format(str(filecount)))
    return render_template('welcome.html', title="Combinate")

@app.route('/second')
def second():
    return '<h1>The Redirected Page</h1><p>Upload not complete.</p>'

@app.route('/completed')
def completed():
    return '<h1>The Redirected Page</h1><p>Upload completed.</p>'

if __name__ == '__main__':
    app.run(debug=True)