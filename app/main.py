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

""" FastAPI routes."""
import base64

from fastapi import Request, Form, FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException


from core import builder
from .schemas import topics

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")
SUGGESTIONS = topics.SUGGESTIONS


@app.get("/", name="home_page_view", response_class=HTMLResponse)
def HomePageView(request: Request):
    """Recarxiv Homepage View Handler"""
    return templates.TemplateResponse(
        "homepage/homepage.html",
        {"request": request},
    )


@app.get("/suggestions", name="fetch_user_suggestions", response_class=HTMLResponse)
def FetchUserSuggestionHandler(request: Request):
    """User Suggestions Input"""
    return templates.TemplateResponse(
        "app/FetchSuggestionPage.html",
        {"request": request, "suggestions": SUGGESTIONS},
    )


@app.post(
    "/suggestions/topics/ajax",
    name="user_selected_topic_handler",
)
def UserSuggestedTopicHandler(request: Request, selected: str = Form(...)):
    """Fetch user suggested topics and return success"""
    selected = selected.split(",")
    url_string = ""
    for names in selected:
        url_string += names + "-"
    encoded_strign = base64.b64encode(bytes(url_string, "utf-8"))
    return JSONResponse(
        content={
            "message": "success",
            "url": str(encoded_strign.decode("UTF-8", "ignore")),
        }
    )


@app.get(
    "/suggested/arxiv/{arxiv_base64}",
    name="recommended_Arxiv",
    response_class=HTMLResponse,
)
def RecommendedArxiv(request: Request, arxiv_base64: str):
    """Recommend Papers based on selected topics"""
    selected_topics = (
        base64.b64decode(arxiv_base64).decode("UTF-8", "ignore").split("-")[:-1]
    )
    user_profile = [
        topic for topic in map(lambda idx: SUGGESTIONS[int(idx)], selected_topics)
    ]
    clustertopic = builder.ClusterTopic()
    payload = clustertopic(user_profile)
    return templates.TemplateResponse(
        "app/RecommendArxiv.html", {"request": request, "payload": payload}
    )


if __name__ == "__main__":
    app.run()
