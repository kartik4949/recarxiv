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

import string
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from unidecode import unidecode
from nltk.stem import WordNetLemmatizer


"""Data PreProcessor Class"""


class Processor:
    """Processor.
        Helper class for preprocessing of text data.
    """

    @classmethod
    def tokenize(cls, corpus):
        """tokenize.
            Tokenizer for word tokenize with preprocessing.

        Args:
            corpus: List of words.
        """
        corpus = corpus.lower()
        # collecting a list of stop words from nltk and punctuation form
        stopset = stopwords.words("english") + list(string.punctuation)
        # remove stop words and punctuations from string.
        corpus = " ".join(
            [i for i in word_tokenize(corpus) if i not in stopset]
        )
        # remove non-ascii characters
        corpus = unidecode(corpus)
        corpus = corpus.split(" ")
        return corpus

    @classmethod
    def lemmatize(cls, words):
        """lemmatize.
            Lemmatizate the list of words.

        Args:
            words: List of words to lemmatize.
        """
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(w) for w in words]
        return words

    def __call__(self, text):
        corpus = self.tokenize(text)
        words = self.lemmatize(corpus)
        return words
