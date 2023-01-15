from flask import Flask, render_template
from views import main_view, cart_view, search_view, detail_view, account

app = Flask(__name__)

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

#account
app.add_url_rule("/signup",view_func=account.SignupHandler.as_view("signup_page"))
app.add_url_rule("/login",view_func=account.LoginHandler.as_view("login_page"))


if __name__ == "__main__":
  app.run()