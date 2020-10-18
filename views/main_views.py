"""
   Copyright 2020 Kartik Sharma, Saurabh Saxena
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

  ==============================================================================

"""

""" Flask App Main Views """

import flask
from flask.views import View, MethodView
from flask import render_template, request, redirect, url_for, flash, jsonify, Flask, make_response, Response, send_file
app = Flask(__name__,template_folder='././templates')

class HomePageView(View):
    '''Recarxiv Homepage View Handler'''
    methods = ['GET']
    def dispatch_request(self):
        return render_template('homepage/homepage.html')