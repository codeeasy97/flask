from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"


@app.route("/about")
def about():
  return "Hello About!"

@app.route("/contact")
def contact():
  return "Hello Contact!"

if __name__ == "__main__":
  app.run()