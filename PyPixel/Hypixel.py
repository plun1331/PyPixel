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

import aiohttp
from typing import List, Tuple, Literal
from .Player import Player
from .Errors import PlayerNotFound, GuildNotFound
from .Cache import Cache
from .Guild import Guild
from .SkyBlockProfile import SkyBlockProfile


class Hypixel:
    r"""The main class that will be used for requesting information from the Hypixel API.

    :param api_key: Your Hypixel API key.
    :type api_key: str

    :param base_url: The base URL for the Hypixel API. Defaults to 'https://api.hypixel.net/'.
    :type base_url: str, optional

    :param clear_cache_after: How often the cache should clear in seconds.
    :type clear_cache_after: int, optional"""

    def __init__(self, *, api_key: str, base_url: str = "https://api.hypixel.net/", clear_cache_after: int = 300):
        self.api_key = str(api_key)
        b = str(base_url) if str(base_url).endswith('/') else str(base_url) + '/'
        self.base_url = b if b.startswith('https://') or b.startswith('http://') else 'https://' + b
        self.cache = Cache(int(clear_cache_after))

    async def get_player(self, uuid: str) -> Player:
        r"""|coro|
        
        Gets a player from the Hypixel API using the `/player` endpoint.
        
        :param uuid: The UUID you are requesting player data for.
        :type uuid: str

        :raises PyPixel.Errors.PlayerNotFound: The player couldn't be found.

        :return: The player from the API.
        :rtype: PyPixel.Player.Player"""

        url = self.base_url + '{0.base_url}player?key={0.api_key}&uuid={1}'.format(self, uuid)
        data, cached = await self._send(url)
        if not data['success']:
            raise PlayerNotFound(data['cause'])
        if not cached:
            await self.cache.cache(url, data)
        player = Player(data, cached, self)
        return player

    async def get_guild(self, arg: str, by: Literal['id', 'name', 'player']) -> Guild:
        r"""|coro|
        
        Gets a guild from the Hypixel API using the ``/guild`` endpoint.
        
        :param arg: The guild ID or name, or a player UUID.
        :type arg: str

        :param by: The type of 'arg' you provided.
        :type by: Literal['id', 'name', 'player']

        :raises TypeError: Invalid 'by' parameter.
        :raises PyPixel.Errors.GuildNotFound: The guild was not found.

        :return: The guild from the API.
        :rtype: PyPixel.Guild.Guild"""

        url = '{0.base_url}guild?key={0.api_key}&'.format(self)
        if by.lower() == 'id':
            url += 'id={0}'.format(arg)
        elif by.lower() == 'name':
            url += 'name={0}'.format(arg)
        elif by.lower() == 'player':
            url += 'player={0}'.format(arg)
        else:
            raise TypeError("Invalid input: " + by)
        data, cached = await self._send(url)
        if not data['success']:
            raise GuildNotFound(data['cause'])
        if not cached:
            await self.cache.cache(url, data)
        if by.lower() == 'player' and data['guild'] is None:
            raise GuildNotFound("Player {0} is not in a guild.".format(arg))
        guild = Guild(data, cached, self)
        return guild

    async def get_profiles(self, uuid: str) -> List[SkyBlockProfile]:
        r"""|coro|

        Gets a player's SkyBlock profiles from the Hypixel API using the `/skyblock/profiles` endpoint.

        :param uuid: The player's UUID.
        :type uuid: str

        :raises PyPixel.Errors.PlayerNotFound: The player's profiles could not be found.

        :return: A list containing the player's profiles.
        :rtype: List[PyPixel.SkyBlockProfile.SkyBlockProfile]"""

        url = '{0.base_url}skyblock/profiles?key={0.api_key}&uuid={1}'.format(self, uuid)
        data, cached = await self._send(url)
        if not data['success']:
            raise PlayerNotFound(data['cause'])
        if not cached:
            await self.cache.cache(url, data)
        profiles = []
        for profile in data['profiles']:
            profiles.append(SkyBlockProfile(profile, cached, self))
        return profiles

    async def get_name(self, uuid: str) -> str:
        r"""|coro|

        Gets a player's name from their UUID. This does not use the Hypixel API.

        :param uuid: The player's UUID.
        :type uuid: str

        :raises PyPixel.Errors.PlayerNotFound: The UUID is invalid.

        :return: The player's name.
        :rtype: str"""

        data, cached = await self._send("https://sessionserver.mojang.com/session/minecraft/profile/{0}".format(uuid))
        try:
            return data['name']
        except:
            raise PlayerNotFound

    async def get_uuid(self, name: str) -> str:
        r"""|coro|

        Get's a player's UUID from their name.

        :param name: The player's name.
        :type name: str

        :raises PyPixel.Errors.PlayerNotFound: The name is invalid.

        :return: The player's UUID.
        :rtype: str"""

        data, cached = await self._send("https://api.mojang.com/users/profiles/minecraft/{0}".format(name))
        try:
            return data['id']
        except:
            raise PlayerNotFound

    async def _send(self, url: str) -> Tuple[dict, bool]:
        r"""|coro|

        Sends a request to the specified url.

        :param url: The URL the request will be sent to.
        :type url: str

        :return: The json data from the API, and a boolean value indicating
            whether or not the data was retrieved from the cache.
        :rtype: Tuple[dict, bool]"""

        data = await self.cache.getFromCache(url)
        cached = True
        if data is None:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
            cached = False
        return data, cached
