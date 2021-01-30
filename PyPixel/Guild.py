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

from contextlib import suppress
import datetime
from .GuildMember import GuildMember
from .GuildRank import GuildRank
from .utils import Hypixel


class Guild(object):
    r"""Represents a Hypixel guild.
    
    Parameters
    -----------
    data: :class:`dict`
        The raw data from the API.

    cached: :class:`bool`
        Whether or not the data was retrieved from the cache.
        
    hypixel: :class:`.Hypixel`
        The .Hypixel class used to make the request."""

    def __init__(self, data, cached, hypixel):
        guilddata = data['guild']
        self.hypixel = hypixel  # This is done so I can call functions from the Hypixel class
        self.cached = cached
        with suppress(KeyError):
            self.raw = guilddata
        with suppress(KeyError):
            self.name = guilddata['name']
        with suppress(KeyError):
            self.id = guilddata['_id']
        with suppress(KeyError):
            self.coins = guilddata['coins']
        with suppress(KeyError):
            self.created = datetime.datetime.fromtimestamp(guilddata['created'] / 1000)
        self.members = [GuildMember(member) for member in guilddata['members']]
        with suppress(KeyError):
            self.joinable = guilddata['joinable']
        with suppress(KeyError):
            self.public = guilddata['publiclyListed']
        with suppress(KeyError):
            self.tag = guilddata['tag']
        with suppress(KeyError):
            self.legacy_ranking = guilddata['legacyRanking']
        with suppress(KeyError):
            self.achievements = guilddata['achievements']
        with suppress(KeyError):
            self.ranks = [GuildRank(rank) for rank in guilddata['ranks']]
        with suppress(KeyError):
            self.preferred_games = guilddata['preferredGames']
        with suppress(KeyError):
            self.description = guilddata['description']
        with suppress(KeyError):
            self.tag_color = guilddata['tagColor']
        with suppress(KeyError):
            self.chat_muted_since = guilddata['chatMute']
        with suppress(KeyError):
            self.level = Hypixel.guildlevel(guilddata['exp'])
        with suppress(KeyError):
            self.xp = guilddata['exp']
        with suppress(KeyError):
            self.guild_xp_by_game = guilddata['guildExpByGameType']

    async def get_member(self, member: GuildMember):
        r"""|coro|
        
        Gets a .Player object from a .GuildMember

        Returns
        --------
        :class:`.Player`
            The returned player."""
        uuid = member.uuid
        player = await self.hypixel.get_player(uuid)
        return player
