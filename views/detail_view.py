from flask import Flask, render_template
from flask.views import View


class DetailPageHandler(View):
    def dispatch_request(self):
        return render_template("product_detail.html")