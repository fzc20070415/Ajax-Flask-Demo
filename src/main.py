from flask import Flask, render_template, request
from flask import flash, redirect, url_for
import json
from werkzeug.utils import secure_filename
import os
import sys

# Initiate flask
app = Flask(__name__)
app.SECRET_KEY = 'u0299Esd55Q00sdf20935'

VIDEO_EXT = set(['mp4', 'avi', 'png'])
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024


# Direct to index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test2')
def test():
    print("Test2 detected.")
    return "This is test2."

# Registration
@app.route('/register', methods=['POST'])
def primary_func():
    username = request.form['Username']
    password = request.form['Pwd']
    print(username, password, "received")
    return render_template('register.html')

# Video Upload
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in VIDEO_EXT

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        print('Uploading videos...')

        # Retrieve uploaded video
        try:
            f = request.files['file']
        except:
            print("ERROR:", sys.exc_info()[0])
            return render_template('upload.html', feedback="No file is uploaded.")

        basepath = os.path.dirname(__file__)
        if f and allowed_file(f.filename):
            upload_path = os.path.join(basepath, "uploads", secure_filename(f.filename))
            f.save(upload_path)
            print("Video uploaded")
        else:
            print("Wrong extension.")
            Feedback = f.filename + ": The chosen file is not a video of supported format!"
            return render_template('upload.html', feedback=Feedback)

        # TODO: Analyze uploaded video
        

        return render_template('upload_succeed.html')
    return render_template('upload.html', feedback="")

# @app.route('/upload_succeed', methods=['POST'])
# def upload_video():
#     print('Video uploaded.')
#     return render_template('upload_succeed.html')


# def advanced_inple():
#     # Add to database
#     # display webpage

if __name__ == '__main__':
    app.run(port=7000, debug=True)
