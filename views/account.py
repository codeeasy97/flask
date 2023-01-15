from flask import Flask, render_template
from flask.views import View


class SignupHandler(View):
    methods = ["GET", "POST"]
    def dispatch_request(self):
        return render_template("signup.html")

class LoginHandler(View):
    def dispatch_request(self):
        return render_template("login.html")