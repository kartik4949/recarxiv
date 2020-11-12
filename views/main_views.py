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
import base64
from flask.views import View
from flask import (
    render_template,
    request,
    jsonify,
    Flask,
)

from core import builder
from . import topics

app = Flask(__name__, template_folder="././templates")
SUGGESTIONS = topics.SUGGESTIONS


class HomePageView(View):
    """Recarxiv Homepage View Handler"""

    methods = ["GET"]

    def dispatch_request(self):
        return render_template("homepage/homepage.html")


class FetchUserSuggestionHandler(View):
    """User Suggestions Input"""

    methods = ["GET"]

    def dispatch_request(self):
        return render_template("App/FetchSuggestionPage.html", suggestions=SUGGESTIONS)


class UserSuggestedTopicHandler(View):
    """Fetch user suggested topics and return success"""

    methods = ["POST"]

    def dispatch_request(self):
        fetch_topics = request.form.get("selected")
        selected = fetch_topics.split(",")
        url_string = ""
        for names in selected:
            url_string += names + "-"
        encoded_strign = base64.b64encode(bytes(url_string, "utf-8"))
        return jsonify(
            {"message": "success", "url": str(encoded_strign.decode("UTF-8", "ignore"))}
        )


class RecommendedArxiv(View):
    """Recommend Papers based on selected topics"""

    methods = ["GET"]

    def dispatch_request(self, arxiv_base64):
        selected_topics = (
            base64.b64decode(arxiv_base64).decode("UTF-8", "ignore").split("-")[:-1]
        )
        user_profile = []
        for index in selected_topics:
            user_profile.append(SUGGESTIONS[index])
        clustertopic = builder.ClusterTopic()
        payload = clustertopic(user_profile)
        return render_template("App/RecommendArxiv.html", payload=payload)
