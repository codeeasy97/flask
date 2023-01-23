from flask import Flask, render_template, redirect, url_for, session
from flask.views import View
import re

class SignupHandler(View):
    methods = ["GET", "POST"]
    def dispatch_request(self):
        return render_template("signup.html")

class LoginHandler(View):
    def dispatch_request(self):
        return render_template("login.html")

class ProfileHandler(View):
    def dispatch_request(self):
        return render_template("account/profile.html")

class LogoutHandler(View):
    def dispatch_request(self):
        session["is_authenticated"] = None
        session["name"] = None
        del session["is_authenticated"]
        del session["name"]
        return redirect(url_for("home_page"))