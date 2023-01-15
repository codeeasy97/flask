from flask import Flask, render_template
from flask.views import View

class CartPageHandler(View):
    def dispatch_request(self):
        return render_template("cart.html")


class CheckoutPageHandler(View):
    def dispatch_request(self):
        return render_template("checkout.html")

class WishlistHandler(View):
    def dispatch_request(self):
        return render_template("wishlist.html")