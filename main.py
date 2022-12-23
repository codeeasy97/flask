from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
  return render_template("home.html")


@app.route("/about")
def about():
  return "Hello About!"

@app.route("/contact")
def contact():
  return "Hello Contact!"

if __name__ == "__main__":
  app.run()