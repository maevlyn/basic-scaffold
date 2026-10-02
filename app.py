import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# create the table once at startup
sqlite3.connect("names.db").execute("CREATE TABLE IF NOT EXISTS names (name TEXT)")


@app.route("/")
def home():
    return render_template("get-name.html")


# save to sqlite
@app.route("/save-db", methods=["POST"])
def save_db():
    with sqlite3.connect("names.db") as db:
        db.execute("INSERT INTO names VALUES (?)", (request.form["name"],))
    return redirect("/")


# save to text file
@app.route("/save-text", methods=["POST"])
def save_text():
    with open("names.txt", "a") as f:  # a stands for append
        f.write(request.form["name-text-file"] + "\n")
    return redirect("/")


# list all names from sqlite
@app.route("/names")
def names():
    rows = sqlite3.connect("names.db").execute("SELECT name FROM names").fetchall()
    names = (row[0] for row in rows)  # get the first element of the row
    return render_template("names.html", names=names)


@app.route("/names-text-file")
def names_text_file():
    with open("names.txt", "r") as f:  # r stands for read
        names = f.read().splitlines()
    return render_template("names.html", names=names)


app.run(debug=True, port=8000)
