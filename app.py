from flask import Flask, render_template

app = Flask(__name__)

myPost = [{
  "date" : "july 28",
  "postContent" : "-_-"},
  {
  "date" : "july 28",
  "postContent" : "-_-"}
  ]

@app.route("/")
def index():
 return  render_template("index.html",post=myPost)

@app.route("/resume") 
def resume():
  print("my Resume")

if __name__ == "__main__":
  app.run()

