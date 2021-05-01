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

import collections

from tqdm import tqdm
import feedparser
import urllib.request as libreq

from core.papers import Paper
from core.similarity import Processor

"""Below are helper functions to fetch and cluster papers based on user."""


class Fetch:
    def __init__(self, config: dict):
        """init fetch class"""
        self.BASE_URL = config.base_url
        self.MAX_R = config.max_result
        self.THRESHOLD = config.threshold
        self.topic_score = config.topic_score

    def _get_parsed_data(self):
        """_get_parsed_data.
        reads query url from arxiv endpoint.
        """
        # Search parameters
        _category = "cat:cs.CV+OR+cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.NE+OR+cat:stat.ML"
        query = "search_query=%s&sortBy=lastUpdatedDate&start=%i&max_results=%i" % (
            _category,
            0,
            self.MAX_R,
        )

        with libreq.urlopen(self.BASE_URL + query) as url:
            r = url.read()
        parse = feedparser.parse(r)
        return parse

    def _get_clusterd_papers(self, user_profile: list):
        """_get_clusterd_papers.

        Args:
            user_profile (list): user_profile also called interests.
        """
        processor = Processor()
        parse = self._get_parsed_data()
        _papers_list = []
        for _, paper in enumerate(parse.entries):
            _paper = Paper(id=paper.id, title=paper.title, summary=paper.summary)
            _papers_list.append(_paper)
        topic_cluster = collections.defaultdict(lambda: "Paper doesn't exists")
        _ = [topic_cluster.update({t: []}) for t in user_profile]
        for _, paper in tqdm(enumerate(_papers_list)):
            title = processor(paper.title)
            summary = processor(paper.summary)
            for interest in user_profile:
                topic = processor(interest)
                intersect_summary = set(topic).intersection(set(summary))
                intersect = set(topic).intersection(set(title))
                _score_topic = (len(intersect) / len(topic)) * self.topic_score
                if _score_topic != self.topic_score:
                    _score_topic *= 1.5
                if not _score_topic:
                    _score_topic += len(intersect_summary) ** 2 / 2
                else:
                    _score_topic += len(intersect_summary) / self.topic_score

                _score_topic = min(_score_topic, self.topic_score)

                if _score_topic > self.THRESHOLD:
                    topic_cluster.get(interest).append([paper, _score_topic])
        return topic_cluster
