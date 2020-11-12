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

""" Flask App Routes """

from flask import Flask
from views import main_views

app = Flask(__name__, template_folder="templates")

# Recarxiv Homepage Route
app.add_url_rule("/", view_func=main_views.HomePageView.as_view("home_page_view"))
# Fetch User Suggestions
app.add_url_rule(
    "/suggestions",
    view_func=main_views.FetchUserSuggestionHandler.as_view("fetch_user_suggestions"),
)
# User Selected Topics Ajax Call
app.add_url_rule(
    "/suggestions/topics/ajax",
    view_func=main_views.UserSuggestedTopicHandler.as_view(
        "user_selected_topic_handler"
    ),
)
# Recommender System
app.add_url_rule(
    "/suggested/arxiv/<arxiv_base64>",
    view_func=main_views.RecommendedArxiv.as_view("recommended_Arxiv"),
)
