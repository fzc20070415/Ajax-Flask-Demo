from flask import Flask, render_template, request
from flask import flash, redirect, url_for
import json
from werkzeug.utils import secure_filename
import os
import sys
# import VideoUploader

# Initiate flask
app = Flask(__name__)
app.SECRET_KEY = 'u0299Esd55Q00sdf20935'

VIDEO_EXT = set(['mp4', 'avi', 'png'])
app.config['MAX_CONTENT_LENGTH'] = 150 * 1024 * 1024


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
        print(request.form)
        print(request.files)
        file_list = request.files.getlist("file")
        print(file_list)
        for item in file_list:
            try:
                f = item
            except:
                print("ERROR:", sys.exc_info()[0])
                return render_template('upload.html', feedback="No file is uploaded.")

            basepath = os.path.dirname(__file__)
            if f and allowed_file(f.filename):
                upload_path = os.path.join(basepath, "cache", secure_filename(f.filename))
                f.save(upload_path)
                ### Receive in chunk ###
                # try:
                #     with open(upload_path) as p:
                #         p.seek(int(request.form['dzchunkbyteoffset']))
                #         p.write(file.stream.read())
                # except:
                #     print("Error(Upload):", sys.exc_info()[0])
                #
                # total_chunks = int(request.form['dztotalchunkcount'])
                #
                # if current_chunk + 1 == total_chunks:
                #     # This was the last chunk, the file should be complete and the size we expect
                #     if os.path.getsize(save_path) != int(request.form['dztotalfilesize']):
                #         print("Error(Upload): Size not match.")
                #         # return make_response(('Size mismatch', 500))
                #         Feedback = "File size not match. Try again."
                #         return render_template('upload.html', feedback=Feedback)
                #     else:
                #         print("Video uploaded")
                #         # log.info(f'File {file.filename} has been uploaded successfully')
                # else:
                #     # log.debug(f'Chunk {current_chunk + 1} of {total_chunks} '
                #               # f'for file {file.filename} complete')
                #     print("Error(Upload): Chunk size not match.")
                #     Feedback = "Chunk size not match. Try again."
                #     return render_template('upload.html', feedback=Feedback)
                ### End of Receive in Chunk ###
            else:
                print("Wrong extension.")
                Feedback = f.filename + ": The chosen file is not a video of supported format!"
                return render_template('upload.html', feedback=Feedback)

        # TODO: Analyze uploaded video
        # Use methods in VideoUploader

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
