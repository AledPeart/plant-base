import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_paginate import Pagination, get_page_args

if os.path.exists("env.py"):
    import env

#Pagination shets per page
PER_PAGE = 6


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

#FUNCTIONS

#Pagination
# https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9

def paginated(sheets):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE

    return sheets[offset: offset + PER_PAGE]


def pagination_args(sheets):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    total = len(sheets)

    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap') 

    return Pagination(page=page, per_page=PER_PAGE, total=total)




@app.route("/")
@app.route("/get_sheets")
def get_sheets():
    sheets = list(mongo.db.sheets.find()) 
    sheets_paginated = paginated(sheets)
    pagination = pagination_args(sheets)
    # image = request.form.get("image")
    # placeholder_image = (static)

    return render_template("sheets.html", sheets=sheets_paginated, pagination=pagination,)


@app.route("/view_sheet/<sheet_id>")
def view_sheet(sheet_id):

    sheet = mongo.db.sheets.find_one({"_id":ObjectId(sheet_id)})
    categories = mongo.db.categories.find()
    return render_template("view_sheet.html", sheet=sheet, categories=categories)

    # activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    # user = mongo.db.users.find_one({"username": activity["created_by"]})
    # categories = list(mongo.db.categories.find())

    # return render_template("view_activity.html", activity=activity,
    #                        categories=categories, user=user)



@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    sheets = list(mongo.db.sheets.find({"$text": {"$search": query}})) 
    return render_template("sheets.html", sheets = sheets)



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #check if the username entered already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user: #if this variable is TRUE and that username aleady exists
            flash("That username already exists")
            return redirect(url_for("register")) #returns the user to the form so that hey can try again

        #confirms if users confirmation password matches the original Code sourced from https://code-institute-room.slack.com/archives/C7JQY2RHC/p1625910227318600
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        if confirm_password != password:
            flash("Your passwords do not match, please try again.")
            return redirect(url_for("register"))


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


@app.route("/add_sheet", methods=["GET", "POST"])
def add_sheet():
    if request.method == "POST":
        sheet = {
            "category_name": request.form.get("category_name"),
            "common_name": request.form.get("common_name"),
            "botanical_name": request.form.get("botanical_name"),
            "difficulty": request.form.get("difficulty"),
            "light": request.form.get("light"),
            "water": request.form.get("water"),
            "feed": request.form.get("feed"),
            "image": request.form.get("image"),
            "general_info": request.form.get("general_info"),
            "created_by": session["user"]
        }
        mongo.db.sheets.insert_one(sheet)
        flash("New Sheet Sucessfully Created")
        return redirect(url_for("get_sheets"))

    categories = mongo.db.categories.find()
    return render_template("add_sheet.html", categories=categories)



@app.route("/edit_sheet/<sheet_id>", methods = ["GET", "POST"])
def edit_sheet(sheet_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "common_name": request.form.get("common_name"),
            "botanical_name": request.form.get("botanical_name"),
            "difficulty": request.form.get("difficulty"),
            "light": request.form.get("light"),
            "water": request.form.get("water"),
            "feed": request.form.get("feed"),
            "general_info": request.form.get("general_info"),
            "created_by": session["user"]
        }
        mongo.db.sheets.update({"_id": ObjectId(sheet_id)}, submit)
        flash("Your Sheet Has Been Sucessfully Updated")
        return redirect(url_for("get_sheets"))

    sheet = mongo.db.sheets.find_one({"_id":ObjectId(sheet_id)})
    categories = mongo.db.categories.find()
    return render_template("edit_sheet.html", sheet=sheet, categories=categories)


@app.route("/delete_sheet/<sheet_id>")
def delete_sheet(sheet_id):
    mongo.db.sheets.remove({"_id": ObjectId(sheet_id)})
    flash("Sheet Successfully Deleted")
    return redirect(url_for("get_sheets"))
#need to add a delete confirmation warning



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

            


