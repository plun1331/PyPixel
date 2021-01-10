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

import typing
from .Player import Player
from .Errors import PlayerNotFound, GuildNotFound
from .Cache import Cache
from .Other import sendRequest
from .Guild import Guild


class Hypixel:
    r"""The main class that will be used for requesting information from the Hypixel API.
    
    Parameters
    -----------
    api_key: :class:`str`
        Your Hypixel API key.
    
    base_url: Optional[:class:`str`]
        The base URL for the Hypixel API.

    clear_cache_after: Optional[:class:`int`]
        How often the cache should clear in seconds.
    """
    def __init__(self, *, api_key: str, base_url: str="https://api.hypixel.net/", clear_cache_after: int=300):
        self.api_key = str(api_key)
        self.base_url = str(base_url) if str(base_url).endswith('/') else str(base_url) + '/'
        self.cache = Cache(int(clear_cache_after))

    async def get_player(self, uuid: str) -> Player:
        r"""|coro|
        
        Gets a player from the Hypixel API using the `/player` endpoint.
        
        Parameters
        -----------
        uuid: :class:`str`
            The UUID you are requesting player data for.

        Returns
        --------
        :class:`.Player`
            The returned player.

        Raises
        --------
        :class:`.PlayerNotFound`
            The player couldn't be found. 
            This could happen for a variety of reasons."""
        url = self.base_url + 'player' + '?key=' + self.api_key + '&uuid=' + uuid
        data, cached = await sendRequest(url, self.cache)
        if not data['success']:
            raise PlayerNotFound(data['cause'])
        if not cached:
            await self.cache.cache(url, data)
        player = Player(data, cached, self)
        return player

    async def get_guild(self, arg: str, by: typing.Literal['id', 'name', 'player']) -> Guild:
        r"""|coro|
        
        Gets a guild from the Hypixel API using the `/guild` endpoint.
        
        Parameters
        -----------
        arg: :class:`str`
            The guild ID or name, or a player UUID.

        by: :class:`typing.Literal['id', 'name', 'player']`
            The type of `arg` you provided.

        Returns
        --------
        :class:`.Guild`
            The returned guild.

        Raises
        --------
        :class:`TypeError`
            An invalid `by` param was provided."""
        url = self.base_url + 'guild?key=' + self.api_key + '&'
        if by.lower() == 'id':
            url += 'id=' + arg
        elif by.lower() == 'name':
            url += 'name=' + arg
        elif by.lower() == 'player':
            url += 'player=' + arg
        else:
            raise TypeError("Invalid input: " + by)
        data, cached = await sendRequest(url, self.cache)
        if not data['success']:
            raise GuildNotFound(data['cause'])
        if not cached:
            await self.cache.cache(url, data)
        guild = Guild(data, cached, self)
        return guild
        