from flask import Flask, render_template

app = Flask(__name__)

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
  {"item": "mushrooms"}
  {"item": "bananas"}

 ]

  
@app.route("/")
def index():
 return render_template("index.html",post=myPost)

@app.route("/shop")
def shoppingList():
  return render_template("shoppingList.html",
                          myList=myList)
@app.route("/resume") 
def resume():
  print("my Resume")

if __name__ == "__main__":
  app.run()

