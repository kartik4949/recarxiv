import flask
from flask.views import View, MethodView
from flask import render_template, request, redirect, url_for, flash, jsonify, Flask, make_response, Response, send_file
app = Flask(__name__,template_folder='././templates')

class HomePageView(View):
    def dispatch_request(self):
        return render_template('homepage/homepage.html')