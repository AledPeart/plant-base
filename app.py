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
    sheets = list(mongo.db.sheets.find()) 
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
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #check if the username entered exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user: 
            #if this variable is TRUE need to ensure passwords match
            if check_password_hash(
                 existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else: 
                #invalid password match
                flash("Incorrect username and/or password entered")
                return redirect(url_for("login"))

        else:
            #username doesn't exist
            flash("Incorrect username and/or password entered")
            return redirect(url_for("login"))

    return render_template("login.html") 


@app.route("/profile/<username>", methods = ["GET", "POST"])
def profile(username):
    #grabs the session users username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:      
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout") 
def logout():
    #remove user from session cookies
    flash("You have been logged out")
    session.pop("user") 
    return redirect(url_for("login"))


@app.route("/add_sheet")
def add_sheet():
    categories = mongo.db.categories.find()
    return render_template("add_sheet.html", categories=categories)




if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

            


