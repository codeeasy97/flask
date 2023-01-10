from flask import Flask, render_template
from flask.views import View


class HomePageHander(View):
    def dispatch_request(self):
        return render_template("home.html")

class AboutPageHander(View):
    def dispatch_request(self):
        return render_template("about.html")

class ContactPageHander(View):
    def dispatch_request(self):
        return render_template("contact.html")

class HelpPageHander(View):
    def dispatch_request(self):
        return render_template("help.html")

class FaqPageHander(View):
    def dispatch_request(self):
        return render_template("faq.html")