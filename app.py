import os
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/') # Selects this page to open on app start
@app.route('/get_homepage') # Sets the link for index.html to be used with other pages
def get_homepage():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)