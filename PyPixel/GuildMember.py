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


class GuildMember(object):
    r"""Represents a Hypixel guild member.

    :param memberdata: A dict containing the member's data.
    :type memberdata: dict"""

    def __init__(self, memberdata):
        self.uuid = memberdata['uuid'] if 'rank' in memberdata else None
        self.rank = memberdata['rank'] if 'rank' in memberdata else None
        self.joined = datetime.datetime.fromtimestamp(memberdata['joined'] / 1000.0) if 'joined' in memberdata else None
        self.quest_participation = memberdata['questParticipation'] if 'questParticipation' in memberdata else None
        self.xp_history = memberdata['expHistory'] if 'expHistory' in memberdata else None

    def __eq__(self, other):
        try:
            if other.uuid == self.uuid:
                return True
        except AttributeError:
            pass
        return False
