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
import sys

import aiohttp
import asyncio
from typing import List, Tuple, Literal, Optional

from .AuctionPage import AuctionPage
from .Player import Player
from .Errors import PlayerNotFound, GuildNotFound, APIError, NotFound, ClientError, KeyNotFound, PyPixelError
from .Cache import Cache
from .Guild import Guild
from .SkyBlockProfile import SkyBlockProfile
from .Key import APIKey
from .Achievements import AchievementData


class Hypixel:
    r"""The main class that will be used for requesting information from the Hypixel API.

    :param api_key: Your Hypixel API key.
    :type api_key: str

    :param base_url: The base URL for the Hypixel API. Defaults to 'https://api.hypixel.net/'.
    :type base_url: Optional[str]

    :param clear_cache_after: How often the cache should clear in seconds.
    :type clear_cache_after: Optional[int]

    :param user_agent: The user agent to use for requests.
                        This is formatted with your Python version and aiohttp version.
    :type user_agent: Optional[str]"""

    def __init__(self, *, api_key: str, base_url: str = "https://api.hypixel.net/", clear_cache_after: int = 300,
                 user_agent: str = None):
        self.api_key = str(api_key)
        b = str(base_url) if str(base_url).endswith('/') else str(base_url) + '/'
        self.base_url: str = b if b.startswith('https://') or b.startswith('http://') else 'https://' + b
        self.cache = Cache(int(clear_cache_after))
        try:
            loop = asyncio.new_event_loop()
            loop.run_until_complete(self.get_key())
        except KeyNotFound:
            raise ValueError("The API Key {0} is invalid.".format(self.api_key))
        self.session = aiohttp.ClientSession()
        if user_agent is None:
            user_agent = 'PyPixel (https://github.com/plun1331/PyPixel) Python/{0[0]}.{0[1]}.{0[2]} aiohttp/{1}'
        self.user_agent: str = user_agent.format(sys.version_info, aiohttp.__version__)

    async def get_player(self, uuid: str) -> Player:
        r"""|coro|
        
        Gets a player from the Hypixel API using the `/player` endpoint.
        
        :param uuid: The UUID you are requesting player data for.
        :type uuid: str

        :raises PyPixel.Errors.PlayerNotFound: The player couldn't be found.

        :return: The player from the API.
        :rtype: PyPixel.Player.Player"""

        url = '{0.base_url}player?uuid={1}'.format(self, uuid)
        try:
            data, cached = await self._send(url)
        except NotFound as e:
            reason = e.data['cause'] if e.data is not None else 'None'
            raise PlayerNotFound(
                reason,
                e.url,
                e.data
            )
        if not data['success']:
            raise PlayerNotFound(
                data['cause'],
                url,
                data
            )
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

        url = '{0.base_url}guild?'.format(self)
        if by.lower() == 'id':
            url += 'id={0}'.format(arg)
        elif by.lower() == 'name':
            url += 'name={0}'.format(arg)
        elif by.lower() == 'player':
            url += 'player={0}'.format(arg)
        else:
            raise TypeError("Invalid input: " + by)
        try:
            data, cached = await self._send(url)
        except NotFound as e:
            reason = e.data['cause'] if e.data is not None else 'None'
            raise GuildNotFound(
                reason,
                e.url,
                e.data
            )
        if not data['success']:
            raise GuildNotFound(
                data['cause'],
                url,
                data
            )
        if not cached:
            await self.cache.cache(url, data)
        if by.lower() == 'player' and data['guild'] is None:
            raise GuildNotFound(
                "Player {0} is not in a guild.".format(arg),
                url,
                data
            )
        guild = Guild(
            data,
            cached,
            self
        )
        return guild

    async def get_profiles(self, uuid: str) -> List[SkyBlockProfile]:
        r"""|coro|

        Gets a player's SkyBlock profiles from the Hypixel API using the `/skyblock/profiles` endpoint.

        :param uuid: The player's UUID.
        :type uuid: str

        :raises PyPixel.Errors.PlayerNotFound: The player's profiles could not be found.

        :return: A list containing the player's profiles.
        :rtype: List[PyPixel.SkyBlockProfile.SkyBlockProfile]"""

        url = '{0.base_url}skyblock/profiles?&uuid={1}'.format(self, uuid)
        try:
            data, cached = await self._send(url)
        except NotFound as e:
            reason = e.data['cause'] if e.data is not None else 'None'
            raise PlayerNotFound(
                reason,
                url,
                e.data
            )
        if not data['success']:
            raise PlayerNotFound(
                data['cause'],
                url,
                data
            )
        if not cached:
            await self.cache.cache(url, data)
        profiles = []
        for profile in data['profiles']:
            profiles.append(SkyBlockProfile(profile, cached, self))
        return profiles

    async def get_auctions(self, page: int = 0) -> AuctionPage:
        r"""
        |coro|

        Gets a page of auctions from the Hypixel API.

        This does not use your API Key.

        :param page: The page to request.
        :type page: int_

        :return: The page of auctions.
        :rtype: PyPixel.AuctionPage.AuctionPage"""
        url = '{0.base_url}skyblock/profiles?page={1}'.format(self, page)
        data, cached = await self._send(url, authenticate=False)
        if not data['success']:
            raise PyPixelError("Couldn't GET from {0}: {1}".format(url, data['cause']))
        return AuctionPage(data, cached, self)

    async def get_key(self, key=None) -> APIKey:
        """|coro|

        Gets information on an API Key.

        :param key: The API key you want information for.
                    Defaults to the API key you provided on initialization of the class.
        :type key: Optional[str]

        :return: The data on the API Key
        :rtype: PyPixel.Key.APIKey"""
        if key is None:
            key = self.api_key
        url = "{0.base_url}key?key={1}".format(self, key)
        try:
            data, cached = await self._send(url, authenticate=False)
        except NotFound as e:
            reason = e.data['cause'] if e.data is not None else "None"
            raise KeyNotFound(
                reason,
                e.url,
                e.data
            )
        if not data['success']:
            raise KeyNotFound(
                data['cause'],
                url,
                data
            )
        if not cached:
            await self.cache.cache(url, data)
        return APIKey(
            data['record'],
            cached,
            self
        )

    async def get_achievements(self) -> AchievementData:
        r"""|coro|

        Gets every achievement on the Hypixel Network using the ``/resources/achievements`` endpoint.

        This does not use your API Key.

        :raises PyPixel.Errors.PyPixelError: The request failed for some reason.

        :return: An object containing every achievement.
        :rtype: PyPixel.Achievements.AchievementData"""

        url = "{0}resources/achievements".format(self.base_url)
        data, cached = await self._send(url, authenticate=False)
        if not data['success']:
            raise PyPixelError("Couldn't GET from {0}: {1}".format(url, data['cause']))
        return AchievementData(data, cached)

    async def get_name(self, uuid: str) -> str:
        r"""|coro|

        Gets a player's name from their UUID. This does not use the Hypixel API.

        :param uuid: The player's UUID.
        :type uuid: str

        :raises PyPixel.Errors.PlayerNotFound: The UUID is invalid.

        :return: The player's name.
        :rtype: str"""

        url = "https://sessionserver.mojang.com/session/minecraft/profile/{0}".format(uuid)
        try:
            data, cached = await self._send(url)
        except NotFound as e:
            raise PlayerNotFound(
                "Player does not exist",
                e.url,
                e.data
            )
        try:
            return data['name']
        except:
            raise PlayerNotFound(
                "Player does not exist",
                url,
                data
            )

    async def get_uuid(self, name: str) -> str:
        r"""|coro|

        Get's a player's UUID from their name.

        :param name: The player's name.
        :type name: str

        :raises PyPixel.Errors.PlayerNotFound: The name is invalid.

        :return: The player's UUID.
        :rtype: str"""
        url = "https://api.mojang.com/users/profiles/minecraft/{0}".format(name)
        try:
            data, cached = await self._send(url)
        except NotFound as e:
            raise PlayerNotFound(
                "Player does not exist",
                e.url,
                e.data
            )
        try:
            return data['id']
        except:
            raise PlayerNotFound(
                "Player does not exist",
                url,
                data
            )

    async def _send(self, url: str, *, headers=None, authenticate: Optional[bool] = None) -> Tuple[dict, bool]:
        r"""|coro|

        Sends a request to the specified url.

        :param url: The URL the request will be sent to.
        :type url: str

        :param headers: The request headers. Defaults to an empty dict.
        :type headers: Optional[dict]

        :param authenticate: Whether or not to provide an Api-Key header with your API Key.
                            If not provided, will provide the Api-Key header based on the url the
                            request is being sent to.
        :type authenticate: Optional[bool]

        :return: The json data from the API, and a boolean value indicating
            whether or not the data was retrieved from the cache.
        :rtype: Tuple[dict, bool]"""

        if headers is None:
            headers = dict()
        data = await self.cache.getFromCache(url)
        cached = True
        if data is None:
            headers['User-Agent'] = self.user_agent
            if authenticate is None:
                if url.startswith(self.base_url):
                    headers['Api-Key'] = self.api_key
            elif authenticate:
                headers['Api-Key'] = self.api_key
            async with self.session.get(url, headers=headers) as response:
                try:
                    data = await response.json()
                except aiohttp.ClientError:
                    data = None
                if 500 <= response.status < 600:
                    raise APIError(
                        response.status,
                        "None",
                        url,
                        data
                    )
                if response.status == 404:
                    raise NotFound(
                        "None",
                        url,
                        data
                    )
                if 400 <= response.status < 500:
                    raise ClientError(
                        response.status,
                        "None",
                        url,
                        data
                    )
            cached = False
        return data, cached
