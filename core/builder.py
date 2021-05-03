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
import logging
from urllib.error import URLError
from bunch import Bunch

from core.fetch import Fetch

# Create a custom logger
logging.config.fileConfig("core_logging.conf", disable_existing_loggers=False)

# get root logger
core_logger = logging.getLogger(__name__)


class ClusterTopic:
    """ Cluster Topic Class. """

    def __init__(self):
        try:
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
        except FileNotFoundError:
            core_logger.critical("FileNotFoundError config.yml for core functions")
            raise Exception("config.yml file not found!!")
        else:
            core_logger.info("successfully opened yaml!")

    @staticmethod
    def format_json(papers):
        json_out = {"payload": []}
        for topic, paper_data in papers.items():
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
        try:
            papers = self.fetch._get_clusterd_papers(profile)
        except URLError:
            core_logger.error("Network is not reachable!")
            raise Exception("Network issue in fetching papers!!")
        else:
            core_logger.info("papers fetched successfully!!")
        papers_json = self.format_json(papers)
        core_logger.info("papers formatted successfully!!")
        return papers_json
