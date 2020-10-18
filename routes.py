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

import os
from flask import Flask
from flask_login import LoginManager
from flask_login import login_user, logout_user, login_required, current_user
from views import main_views
app = Flask(__name__, template_folder='templates')

app.secret_key = '7bc9b645bba64027bc9b645bba640269368993f2190db3369368993f2190db33'

# Recarxiv Homepage Route
app.add_url_rule('/',view_func=main_views.HomePageView.as_view('home_page_view'))

