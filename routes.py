import os
from flask import Flask
from flask_login import LoginManager
from flask_login import login_user, logout_user, login_required, current_user
from views import main_views
app = Flask(__name__, template_folder='templates')

app.secret_key = '7bc9b645bba64027bc9b645bba640269368993f2190db3369368993f2190db33'

app.add_url_rule('/',view_func=main_views.HomePageView.as_view('home_page'))

