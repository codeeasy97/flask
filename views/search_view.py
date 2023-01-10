from flask import Flask, render_template
from flask.views import View

class SearchPageHandler(View):
    def dispatch_request(self):
        return render_template("search.html")