from flask import Flask, render_template, request, flash, session, redirect, url_for
from views import main_view, cart_view, search_view, detail_view, account
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)
app.secret_key = 'ksdfjslfdsm898sdfdmfsmdf@Hhejvwh'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'multishop'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

app.add_url_rule("/",view_func=main_view.HomePageHander.as_view('home_page'))
app.add_url_rule("/about",view_func=main_view.AboutPageHander.as_view('about_page'))
app.add_url_rule("/contact",view_func=main_view.ContactPageHander.as_view('contact_page'))
app.add_url_rule("/help",view_func=main_view.HelpPageHander.as_view('help_page'))
app.add_url_rule("/faq",view_func=main_view.FaqPageHander.as_view('faq_page'))

#cart
app.add_url_rule("/cart",view_func=cart_view.CartPageHandler.as_view("cart_page"))
app.add_url_rule("/checkout",view_func=cart_view.CheckoutPageHandler.as_view("checkout_page"))
app.add_url_rule("/wishlist",view_func=cart_view.WishlistHandler.as_view("wishlist_page"))

#product search page
app.add_url_rule("/search",view_func=search_view.SearchPageHandler.as_view("search_page"))
app.add_url_rule("/product-detail",view_func=detail_view.DetailPageHandler.as_view("detail_page"))

@app.route('/signup', methods=['GET', 'POST'])
def register():
  if request.method == "POST":
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    mobile = request.form["mobile"]
    password = request.form["password"]
    confirm_password = request.form["confirm_password"]
    print(first_name,last_name,email,mobile,password, confirm_password)
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM accounts WHERE email = %s', (email,))
    account = cursor.fetchone()
    if account:
      flash("Account already exists!","danger")
    else:
      cursor.execute('INSERT INTO accounts(first_name,last_name, email, mobile, password) VALUES (%s, %s, %s, %s, %s)', (first_name, last_name, email, mobile, password))
      mysql.connection.commit()
      flash("You have successfully registered!","success")
  return render_template("signup.html")


@app.route("/login", methods=["GET","POST"])
def login():
  if request.method == "POST":
    email = request.form['email']
    password = request.form['password']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM accounts WHERE email = %s', (email,))
    check_email = cursor.fetchone()
    if check_email:
      cursor.execute('SELECT * FROM accounts WHERE email = %s and password=%s', (email,password))
      account = cursor.fetchone()
      if account:
        session["is_authenticated"]  = True
        session["name"] = account["first_name"]
        flash("You are successfully loggedin!", "success")
        return redirect(url_for("profile_page"))
      else:
        flash("Your password is incorrect!", "danger")
    else:
      flash("You are not registered with us!", "danger")
  return render_template("login.html")

#account
# app.add_url_rule("/signup",view_func=account.SignupHandler.as_view("signup_page"))
# app.add_url_rule("/login",view_func=account.LoginHandler.as_view("login_page"))
app.add_url_rule("/logout",view_func=account.LogoutHandler.as_view("logout_page"))
app.add_url_rule("/profile",view_func=account.ProfileHandler.as_view("profile_page"))

if __name__ == "__main__":
  app.run()