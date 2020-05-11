import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/') # Selects this page to open on app start
@app.route('/get_homepage') # Sets the link for index.html to be used with other pages
def get_homepage():
    return render_template("index.html")



@app.route('/get_recipes') # Sets the link for addrecipes.html to be used with other pages
def get_recipes():
    return render_template("recipe.html", recipe_lists=mongo.db.recipe_lists.find())



@app.route('/get_addrecipes') # Sets the link for recipes.html to be used with other pages
def get_addrecipes():
    return render_template("addrecipe.html", add_recipe=mongo.db.recipe_lists.find())



@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    addrecipe =  mongo.db.recipe_lists
    addrecipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))



@app.route('/get_amendrecipes') # Sets the link for amend recipes.html to be used with other pages
def get_amendrecipes():
    return render_template("amendrecipe.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)