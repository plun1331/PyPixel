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
from .GuildMember import GuildMember
from .GuildRank import GuildRank
from .utils import HypixelUtils


class Guild(object):
    r"""Represents a Hypixel guild.

    :param data: The raw data from the API.
    :type data: dict

    :param cached: Whether or not the data was retrieved from the cache.
    :type cached: bool

    :param hypixel: The Hypixel class used to make the request.
    :type hypixel: PyPixel.Hypixel.Hypixel"""

    def __init__(self, data, cached, hypixel):
        guilddata = data['guild']
        self._hypixel = hypixel  # This is done so I can call functions from the Hypixel class
        self.cached = cached
        self.raw = guilddata
        self.name = guilddata['name'] if 'name' in guilddata else None
        self.id = guilddata['_id'] if '_id' in guilddata else None
        self.coins = guilddata['coins'] if 'coins' in guilddata else None
        self.created = datetime.datetime.fromtimestamp(guilddata['created'] / 1000) if 'created' in guilddata else None
        self.members = [GuildMember(member) for member in guilddata['members']] if 'members' in guilddata else None
        self.joinable = guilddata['joinable'] if 'joinable' in guilddata else None
        self.public = guilddata['publiclyListed'] if 'publiclyListed' in guilddata else None
        self.tag = guilddata['tag'] if 'tag' in guilddata else None
        self.legacy_ranking = guilddata['legacyRanking'] if 'legacyRanking' in guilddata else None
        self.achievements = guilddata['achievements'] if 'achievements' in guilddata else None
        self.ranks = [GuildRank(rank) for rank in guilddata['ranks']] if 'ranks' in guilddata else None
        self.preferred_games = guilddata['preferredGames'] if 'preferredGames' in guilddata else None
        self.description = guilddata['description'] if 'description' in guilddata else None
        self.tag_color = guilddata['tagColor'] if 'tagColor' in guilddata else None
        self.chat_muted_since = guilddata['chatMute'] if 'chatMute' in guilddata else None
        self.level = HypixelUtils.guildlevel(guilddata['exp']) if 'exp' in guilddata else None
        self.xp = guilddata['exp'] if 'exp' in guilddata else None
        self.guild_xp_by_game = guilddata['guildExpByGameType'] if 'guildExpByGameType' in guilddata else None

    def __str__(self):
        return self.name

    async def get_member(self, member: GuildMember):
        r"""|coro|
        
        Gets a Player object from a GuildMember

        :return: The retrieved player.
        :rtype:`PyPixel.Player.Player`
            The returned player."""
        uuid = member.uuid
        return await self._hypixel.get_player(uuid)
