import os
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/') # Selects this page to open on app start
@app.route('/get_homepage') # Sets the link for index.html to be used with other pages
def get_homepage():
    return render_template("index.html")

@app.route('/get_recipes') # Sets the link for addrecipes.html to be used with other pages
def get_recipes():
    return render_template("recipe.html")

@app.route('/get_addrecipes') # Sets the link for recipes.html to be used with other pages
def get_addrecipes():
    return render_template("addrecipe.html")

@app.route('/get_amendrecipes') # Sets the link for amend recipes.html to be used with other pages
def get_amendrecipes():
    return render_template("amendrecipe.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)