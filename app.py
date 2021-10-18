import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_sheets")


def get_sheets():
    sheets = mongo.db.sheets.find()
    return render_template("sheets.html", sheets = sheets)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #check if the username entered already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user: #if this variable is TRUE and that userbname aleady exists
            flash("That username already exists")
            return redirect(url_for("register")) #returns the user to the form so that hey can try again

        register = {                #this is the 'else' that creates a dictionary stored in the variable 'register' to insert into the db
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))        #it would be good to add a second user password field later on
        }
        mongo.db.users.insert_one(register) 

        #put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successfully Completed")

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

            


