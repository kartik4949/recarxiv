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
"""

"""Recommender System builder function."""

import json
import yaml
from bunch import Bunch

from core.fetch import Fetch


class ClusterTopic:
    def __init__(self):
        with open("config/config.yml", "r") as ymlfile:
            # SafeLoader usage.
            cfg = yaml.load(ymlfile, yaml.SafeLoader)

        self.config = {
            "max_result": cfg["max_result"],
            "topic_score": cfg["topic_score"],
            "threshold": cfg["threshold"],
            "base_url": cfg["base_url"],
        }
        self.config = Bunch(self.config)
        self.fetch = Fetch(self.config)

    @staticmethod
    def format_json(papers):
        json_out = {"payload": []}
        for topic, paper_data in papers.items():
            topic_data = []
            _paper_dict = []
            for paper, score in paper_data:
                _paper_dict.append(
                    {
                        "title": paper.title,
                        "url": paper.id,
                        "summary": paper.summary,
                        "author": "",
                        "score": score,
                    }
                )
            json_out["payload"].append({topic: _paper_dict})
        return json_out

    def __call__(self, profile):
        papers = self.fetch._get_clusterd_papers(profile)
        papers_json = self.format_json(papers)
        return papers_json
