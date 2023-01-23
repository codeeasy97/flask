from flask import Flask, render_template, request, session
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