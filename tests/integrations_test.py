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

"""simple integrations tests."""
import pytest
import logging
from bunch import Bunch

from core.fetch import Fetch
from core.similarity import Processor

config = {
    "max_result": 100,
    "topic_score": 10.0,
    "threshold": 1.0,
    "base_url": "http://export.arxiv.org/api/query?",
}

config = Bunch(config)
fetch = Fetch(config)
p = Processor()


def test_sanity_fetching_integration():
    user_profile = ["computer vision"]
    papers = fetch._get_clusterd_papers(user_profile)
    assert len(papers) > 0


@pytest.mark.parametrize(
    ["text", "num_tokens"],
    [
        pytest.param("computer vision is great", 3),
        pytest.param("object detection", 2),
    ],
)
def test_sanity_check_processor(text, num_tokens):
    tokens = p(text)
    assert len(tokens) == num_tokens


if __name__ == "__main__":
    logging.set_verbosity(logging.WARNING)
