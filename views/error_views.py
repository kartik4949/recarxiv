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

""" Flask App Error Views """

from flask import (
    Flask,
    render_template,
)

app = Flask(__name__, template_folder="././templates")


def server_error_500(e):
    return render_template("errors/500.html"), 500


def server_error_404(e):
    return render_template("errors/404.html"), 404


def server_error_405(e):
    return render_template("errors/405.html"), 405
