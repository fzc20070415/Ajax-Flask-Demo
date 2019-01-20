from flask import Flask, render_template, request
import json

# Initiate flask
app = Flask(__name__)
app.SECRET_KEY = 'u0299Esd55Q00sdf20935'


# Direct to index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test2')
def test():
    return "This is test2."

# Registration
@app.route('/register', methods=['POST'])
def primary_func():
    username = request.form['Username']
    password = request.form['Pwd']
    print(username + " " + password + "received")
    return render_template('register.html')

# def advanced_inple():
#     # Add to database
#     # display webpage    

if __name__ == '__main__':
    app.run(port=7000, debug=True)
