
from flask import Flask
app=Flask(__name__)

@app.route("/")
def greet():
  return "Hello World to fg me"



if __name__==("__main__"):
   app.run(host="0.0.0.0",debug=True)
