from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
  return render_template("home.html")


@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/help")
def help():
  return render_template("help.html")

#faq page
@app.route("/faq")
def faq():
  return render_template("faq.html")

#cart page
@app.route("/cart")
def cart():
  return render_template("cart.html")

#checkout page
@app.route("/checkout")
def checkout():
  return render_template("checkout.html")

#product search page
@app.route("/search")
def search():
  return render_template("search.html")

#product detail page
@app.route("/product-detail")
def productDetail():
  return render_template("product_detail.html")



if __name__ == "__main__":
  app.run()