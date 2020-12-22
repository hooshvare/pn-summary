# coding=utf-8
# Copyright 2020 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python2, python3
"""A library for tokenizing text."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
import six
import string
import hazm

PERSIAN_ALPHA = "\u0621-\u0628\u062A-\u063A\u0641-\u0642\u0644-\u0648\u064E-\u0651\u0655\u067E\u0686\u0698\u06A9\u06AF\u06BE\u06CC"  # noqa: E501
PERSIAN_DIGIT = "\u06F0-\u06F9"

COMMON_ARABIC_ALPHA = "\u0629\u0643\u0649-\u064B\u064D\u06D5"
COMMON_ARABIC_DIGIT = "\u0660-\u0669"


def tokenize(text, stemmer, lang='en'):
    """Tokenize input text into a list of tokens.

    This approach aims to replicate the approach taken by Chin-Yew Lin in
    the original ROUGE implementation.

    Args:
      text: A text blob to tokenize.
      stemmer: An optional stemmer.
      lang: Handling text language.

    Returns:
      A list of string tokens extracted from input text.
    """

    # Persian alphabet and numbers + english one
    _rgx = "a-z0-9"
    if lang == 'fa':
        _rgx += PERSIAN_ALPHA + PERSIAN_DIGIT
        _rgx += COMMON_ARABIC_ALPHA + COMMON_ARABIC_DIGIT

    # Convert everything to lowercase.
    text = text.lower()

    # Replace any non-alpha-numeric characters with spaces.
    text = re.sub(r"[^" + _rgx + "+]", " ", six.ensure_str(text))

    tokens = re.split(r"\s+", text)
    if stemmer:
        # Only stem words more than 3 characters long.
        tokens = [stemmer.stem(x) if len(x) > 3 else x for x in tokens]

    # One final check to drop any empty or invalid tokens.
    tokens = [x for x in tokens if re.match(r"^[" + _rgx + "]+$", six.ensure_str(x))]

    return tokens

# stemmer = hazm.Stemmer()
# text = "اصلاح نويسه ها و استفاده از نیم‌فاصله پردازش را آسان مي كند"
# t = tokenize(text, None, 'fa')
# print(t)
# text = "اصلاح نویسه‌ها و استفاده از نیم‌فاصله پردازش را آسان می‌کند"
# t = tokenize(text, stemmer, 'fa')
# print(t)
