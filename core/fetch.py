"""
   copyright 2020 kartik sharma, saurabh saxena

   licensed under the apache license, version 2.0 (the "license");
   you may not use this file except in compliance with the license.
   you may obtain a copy of the license at

       http://www.apache.org/licenses/license-2.0

   unless required by applicable law or agreed to in writing, software
   distributed under the license is distributed on an "as is" basis,
   without warranties or conditions of any kind, either express or implied.
   see the license for the specific language governing permissions and
   limitations under the license.
"""

import feedparser
import urllib.request as libreq

from papers import paper, paper_table

"""Below are helper functions to fetch and cluster papers based on user."""


def _get_parsed_data():
    """_get_parsed_data.
        reads query url from arxiv endpoint.
    """
    BASE_URL = "http://export.arxiv.org/api/query?"
    MAX_RESULTS = 10

    # Search parameters
    _category = "cat:cs.CV+OR+cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.NE+OR+cat:stat.ML"
    query = (
        "search_query=%s&sortBy=lastUpdatedDate&start=%i&max_results=%i"
        % (_category, 0, MAX_RESULTS)
    )

    with libreq.urlopen(BASE_URL + query) as url:
        r = url.read()
    parse = feedparser.parse(r)
    return parse


def _get_clusterd_papers(user_profile: list):
    """_get_clusterd_papers.

    Args:
        user_profile (list): user_profile with interests.
    """
    # TODO(kartik4949) : Complete the remaining.
    parse = _get_parsed_data()
    for key, paper in enumerate(parse.entries):
        paper_url = paper.id


if __name__ == "__main__":
    user_profile = [
        "computer vision",
        "instance segmentation",
        "object detection",
    ]
    _get_clusterd_papers(user_profile)
