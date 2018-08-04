from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
dbConnect = sqlite3.connect("data.db")
db = dbConnect.cursor()

myPost = [{
  "date" : "july 28",
  "postContent" : "-_-"},
  {
  "date" : "july 28",
  "postContent" : "-_-"}
  ]

myList = [
  {"item": "eggs"},
  {"item": "juice"},
  {"item": "onion"},
  {"item": "apples"},
  {"item": "absorbing towel"},
  {"item": "avocados"},
  {"item": "mushrooms"},
  {"item": "bananas"}

 ]


@app.route("/")
def index():
 return render_template("index.html",post=myPost)

@app.route("/shop", methods=["get", "post"])
def shoppingList():
  if request.method == "POST":
    itemDescription = (request.values.get("shoppingItem"),)

    db.execute(""" INSERT INTO "shoppingList"("description") VALUES(?)""",
      itemDescription)

    dbConnect.commit()

    return render_template("index.html")
  else:

    db.execute(""" SELECT * FROM "shoppingList" WHERE "active" = 1
                             ORDER BY "requestTime" """)
    shoppingList = db.fetchall()

    return render_template("shoppingList.html",
                          myList=shoppingList)
@app.route("/resume")
def resume():
  print("my Resume")

if __name__ == "__main__":
  app.run()

