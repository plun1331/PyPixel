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
from .utils import HypixelUtils


class AchievementData(object):
    r"""Represents Hypixel achievement data.

    :param data: The raw data from the API.
    :type data: dict

    :param cached: Whether or not the data was retrieved from the cache.
    :type cached: bool"""

    def __init__(self, data, cached):
        self.raw = data
        self.cached = cached
        self.last_updated = datetime.datetime.fromtimestamp(
            data['lastUpdated'] / 1000
        )
        achievements = data['achievements']
        self.games = [AchievementGame(game, achievements[game]) for game in achievements]


class AchievementGame(object):
    r"""Represents a game with achievements.

    :param name: The name of the game.
    :type name: str

    :param data: The game's achievement data.
    :type data: dict"""

    def __init__(self, name, data):
        self.name = HypixelUtils.getGameName(name)
        self.total_points = data['total_points']
        self.one_time = [OneTime(data['one_time'][achievement]) for achievement in data['one_time']]
        self.tiered = [Tiered(data['tiered'][achievement]) for achievement in data['tiered']]

    def __str__(self):
        return self.name


class Achievement(object):
    r"""Represents a Hypixel achievement.

    :param data: The achievement's data.
    :type data: dict"""

    def __init__(self, data):
        self.name = data['name']
        self.description = data['description']

    def __str__(self):
        return self.name


class OneTime(Achievement):
    r"""Represents a one-time achievement.

    :param data: The achievement's data.
    :type data: dict"""

    def __init__(self, data):
        super().__init__(data)
        self.points = data['points'] if 'points' in data else None
        self.percent_unlocked_game = data['gamePercentUnlocked'] if 'gamePercentUnlocked' in data else None
        self.percent_unlocked_global = data['globalPercentUnlocked'] if 'globalPercentUnlocked' in data else None


class Tiered(Achievement):
    r"""Represents a tiered achievement.

    :param data: The achievement's data.
    :type data: dict"""

    def __init__(self, data):
        super().__init__(data)
        self.tiers = [AchievementTier(tier) for tier in data['tiers']]


class AchievementTier(object):
    r"""Represents an achievement tier in a tiered achievement.

    :param data: The tier's data.
    :type data: dict"""

    def __init__(self, data):
        self.tier = data['tier']
        self.points = data['points']
        self.amount = data['amount']
