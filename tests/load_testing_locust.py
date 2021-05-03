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
import base64
import random

from locust import HttpUser, task

from app.schemas import topics

""" locust file for load testing. """


class LoadTesting(HttpUser):
    """ LoadTesting Class for load testing recommendation api. """

    @task
    def load_test_recommendation(self):
        """ load test task. """
        selected = [str(random.randint(1, len(topics.SUGGESTIONS) - 1))]
        url_string = ""
        for names in selected:
            url_string += names + "-"
        encoded_str = base64.b64encode(bytes(url_string, "utf-8"))
        encoded_str = str(encoded_str.decode("UTF-8", "ignore"))
        self.client.get(f"/suggested/arxiv/{encoded_str}")
