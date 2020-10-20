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

from dataclasses import dataclass, field
from typing import Any

"""Dataclasses for paper and papers_table"""


@dataclass(order=True)
class Paper:
    """Paper.
        Dataclass for storing paper.
        id: Paper url
        title: Paper title
        summary: Short summary of paper.
    """

    id: int
    title: str
    summary: str


@dataclass(order=True)
class Cluster:
    """Cluster.
        topic: Topic
        paper_instance: Instance of Paper data classes.
    """

    topic: str
    paper_instance: Paper = field(default_factory=Paper)
