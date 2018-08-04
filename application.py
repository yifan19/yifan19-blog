from flask import Flask, render_template, request, redirect
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

    textBoxAmount = int((request.values.get("textBoxAmount")))
    for i in range(1,textBoxAmount+1):

      itemDescription = (request.values.get("shoppingItem" + str(i)),)

      if (itemDescription[0]):
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

@app.route("/blog")
@app.route("/blog/<text>")
def blog(text=""):
  print(text)
  return render_template("fail.html",displayText=text)

@app.route("/removeItem", methods=["post"])
def removeItem():
  itemId = (request.values.get("removeItem"),)
  if itemId:
    db.execute(""" UPDATE "shoppingList" SET "active" = '0' WHERE itemID = ?;""",itemId)
    dbConnect.commit()

  return redirect("/shop")

@app.route("/feedback", methods=["get", "post"])
def feedback():
  if request.method == "post":
    return "bye"
  else:
    return "bye"
if __name__ == "__main__":
  app.run()

