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


class APIKey(object):
    r"""Represents an API Key.

    :param key_data: The raw key data from the API.
    :type key_data: dict

    :param cached: The raw key data from the API.
    :type cached: bool

    :param hypixel: The raw key data from the API.
    :type hypixel: PyPixel.Hypixel.Hypixel"""
    def __init__(self, key_data: dict, cached, hypixel):
        self.cached = cached
        self._hypixel = hypixel
        self.key = key_data['key']
        self.owner = key_data['owner']
        self.ratelimit = key_data['limit']
        self.request_past_minute = key_data['queriesInPastMin']
        self.total_requests = key_data['totalQueries']

    async def get_owner(self):
        r"""|coro|

        Gets the owner pf the key as a Player object.

        :return: The key's owner.
        :rtype: PyPixel.Player.Player"""
        return await self._hypixel.get_player(self.owner)

