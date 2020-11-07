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
from . import constants
from core import builder
import base64

app = Flask(__name__,template_folder='././templates')
SUGGESTIONS = constants.SUGGESTIONS

class HomePageView(View):
    '''Recarxiv Homepage View Handler'''
    methods = ['GET']
    def dispatch_request(self):
        return render_template('homepage/homepage.html')

class FetchUserSuggestionHandler(View):
    '''User Suggestions Input'''
    methods = ['GET']
    def dispatch_request(self):
        return render_template('App/FetchSuggestionPage.html',suggestions=SUGGESTIONS)

class UserSuggestedTopicHandler(View):
    '''Fetch user suggested topics and return success'''
    methods = ['POST']
    def dispatch_request(self):
        fetch_topics = request.form.get("selected")
        selected = fetch_topics.split(',')
        url_string = ''
        for names in selected:
            url_string += names + '-'
        encoded_strign = base64.b64encode(bytes(url_string, 'utf-8'))
        return jsonify({"message":"success",'url':str(encoded_strign.decode('UTF-8','ignore'))})

class RecommendedArxiv(View):
    '''Recommend Papers based on selected topics'''
    methods = ['GET']
    def dispatch_request(self,arxiv_base64):
        selected_topics = base64.b64decode(arxiv_base64).decode('UTF-8', 'ignore').split('-')[:-1]
        payload = builder.recommender_builder(selected_topics)
        # payload - JSON format
        return render_template('App/RecommendArxiv.html',payload=payload)