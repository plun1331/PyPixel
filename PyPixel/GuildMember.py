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

class GuildMember:
    r"""Represents a Hypixel guild member.
    
    Parameters
    -----------
    memberdata: :class:`dict`
        A dict containing the member's data."""
    def __init__(self, memberdata):
        with suppress(KeyError):
            self.uuid = memberdata['uuid']
        with suppress(KeyError):
            self.rank = memberdata['rank']
        with suppress(KeyError):
            self.joined = datetime.datetime.fromtimestamp(memberdata['joined'] / 1000.0)
        with suppress(KeyError):
            self.quest_participation = memberdata['questParticipation']
        with suppress(KeyError):
            self.xp_history = memberdata['expHistory']