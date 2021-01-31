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

from .SkyBlockProfileMember import ProfileMember
from contextlib import suppress


class SkyBlockProfile(object):
    r"""Represents a SkyBlock profile.

    :param profiledata: The profile's data from the API.
    :type profiledata: dict

    :param cached: A boolean indicating if the profile's data was retrieved from the cache.
    :type cached: bool

    :param hypixel: The Hypixel class used to get the profile.
    :type hypixel: PyPixel.Hypixel.Hypixel"""

    def __init__(self, profiledata: dict, cached, hypixel):
        self._hypixel = hypixel
        self.cached = cached
        self.name = profiledata['cute_name']
        self.id = profiledata['profile_id']
        self.members = []
        for member in profiledata['members']:
            self.members.append(ProfileMember(member, profiledata['members'][member], self._hypixel))
        with suppress(KeyError):
            self.community_upgrades = profiledata['community_upgrades']
        with suppress(KeyError):
            self.bank_balance = profiledata['banking']['balance']
        with suppress(KeyError):
            self.bank_transactions = profiledata['banking']['transactions']

    def __eq__(self, other):
        if isinstance(other, SkyBlockProfile):
            if other.id == self.id:
                return True
        return False

    def __str__(self):
        return self.name
