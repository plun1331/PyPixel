# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2021 plun1331

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import datetime
from contextlib import suppress


class GuildRank(object):
    r"""Represents a Hypixel guild rank.
    
    :param rankdata: A dict containing the rank's data.
    :type rankdata: dict"""

    def __init__(self, rankdata):
        with suppress(KeyError):
            self.name = rankdata['name']
        with suppress(KeyError):
            self.default = rankdata['default']
        with suppress(KeyError):
            self.tag = rankdata['tag']
        with suppress(KeyError):
            self.created = datetime.datetime.fromtimestamp(rankdata['created'] / 1000)
        with suppress(KeyError):
            self.priority = rankdata['priority']

    def __eq__(self, other):
        try:
            if other.priority == self.priority:
                return True
        except AttributeError:
            pass
        return False

    def __ge__(self, other):
        try:
            if self.priority >= other.priority:
                return True
        except AttributeError:
            pass
        return False

    def __le__(self, other):
        try:
            if self.priority <= other.priority:
                return True
        except AttributeError:
            pass
        return False

    def __gt__(self, other):
        try:
            if self.priority > other.priority:
                return True
        except AttributeError:
            pass
        return False

    def __lt__(self, other):
        try:
            if self.priority < other.priority:
                return True
        except AttributeError:
            pass
        return False

    def __str__(self):
        return self.name
