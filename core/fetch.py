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
from tqdm import tqdm

from papers import Paper
from similarity import Processor

"""Below are helper functions to fetch and cluster papers based on user."""


def _get_parsed_data():
    """_get_parsed_data.
        reads query url from arxiv endpoint.
    """
    BASE_URL = "http://export.arxiv.org/api/query?"
    MAX_RESULTS = 1000

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
        user_profile (list): user_profile also called interests.
    """
    # TODO(kartik4949) : Make config file for hyperparameters.
    THRESHOLD = 1.0
    processor = Processor()
    parse = _get_parsed_data()
    _papers_list = []
    for key, paper in enumerate(parse.entries):
        _paper = Paper(id=paper.id, title=paper.title, summary=paper.summary)
        _papers_list.append(_paper)
    topic_cluster = {t: [] for t in user_profile}
    for key, paper in tqdm(enumerate(_papers_list)):
        title = processor(paper.title)
        summary = processor(paper.summary)
        for interest in user_profile:
            topic = processor(interest)
            intersect_summary = set(topic).intersection(set(summary))
            intersect = set(topic).intersection(set(title))
            _score_topic = (len(intersect) / len(topic)) * 10.0
            if _score_topic != 10.0:
                _score_topic *= 1.5
            if not _score_topic:
                _score_topic += len(intersect_summary) ** 2 / 2
            else:
                _score_topic += len(intersect_summary) / 10.0

            _score_topic = min(_score_topic, 10.0)

            if _score_topic > THRESHOLD:
                topic_cluster.get(interest).append([paper, _score_topic])
        return topic_cluster


if __name__ == "__main__":
    user_profile = ["instance segmentation", "object detection"]
    _get_clusterd_papers(user_profile)
