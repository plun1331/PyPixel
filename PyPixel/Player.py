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

from .Firework import Firework
import datetime
from contextlib import suppress
from .PlayerStats import PlayerStats
from .utils import Hypixel
from .Errors import GuildNotFound


class Player(object):
    r"""Represents a Hypixel player.
    
    :param data: The raw data from the API.
    :type data: dict

    :param cached: Whether or not the data was retrieved from the cache.
    :type cached: bool

    :param hypixel: The PyPixel.Hypixel class used to make the request.
    :type hypixel: PyPixel.Hypixel.Hypixel"""

    def __init__(self, data: dict, cached: bool, hypixel):
        playerdata = data['player']
        self.raw = playerdata
        self._hypixel = hypixel  # This is done so I can call functions from the Hypixel class
        with suppress(KeyError):
            self.uuid = playerdata['uuid']
        with suppress(KeyError):
            self.achievements = playerdata['achievements']
        with suppress(KeyError):
            self.one_time_achievements = playerdata['achievementsOneTime']
        with suppress(KeyError):
            self.auto_spawning_pet = playerdata['auto_spawn_pet']
        with suppress(KeyError):
            self.current_chat_channel = playerdata['channel']
        with suppress(KeyError):
            self.display_name = playerdata['displayname']
        with suppress(KeyError):
            self.fireworks = [Firework(firework) for firework in playerdata['fireworkStorage']]
        with suppress(KeyError):
            self.firstLogin = datetime.datetime.fromtimestamp(playerdata['firstLogin'] / 1000.0)
        with suppress(KeyError):
            self.karma = playerdata['karma']
        with suppress(KeyError):
            self.aliases = playerdata['knownAliases']
        with suppress(KeyError):
            self.lastLogin = datetime.datetime.fromtimestamp(playerdata['lastLogin'] / 1000.0)
        with suppress(KeyError):
            self.most_recently_thanked = playerdata['mostRecentlyThankedUuid']
        with suppress(KeyError):
            self.most_recently_tipped = playerdata['mostRecentlyTippedUuid']
        with suppress(KeyError):
            self.experience = playerdata['networkExp']
        with suppress(KeyError):
            self.level = Hypixel.playerLevel(playerdata['networkExp'])
        with suppress(KeyError):
            self.name = playerdata['playername']
        with suppress(KeyError):
            self.settings = playerdata['settings']
        with suppress(KeyError):
            self.spectators_hidden = playerdata['spectators_invisible']
        with suppress(KeyError):
            self.stats = PlayerStats(playerdata)
        with suppress(KeyError):
            self.recieved_thanks = playerdata['thanksReceived']
        with suppress(KeyError):
            self.thanks_sent = playerdata['thanksSent']
        with suppress(KeyError):
            self.version = playerdata['mcVersionRp']
        with suppress(KeyError):
            self.rank_plus = playerdata['rankPlusColor']
        with suppress(KeyError):
            self.last_logout = datetime.datetime.fromtimestamp(playerdata['lastLogout'] / 1000)
        with suppress(KeyError):
            self.cloak = playerdata['currentCloak']
        with suppress(KeyError):
            self.achievement_points = playerdata['achievementPoints']
        with suppress(KeyError):
            self.click_effect = playerdata['currentClickEffect']
        with suppress(KeyError):
            self.current_pet = playerdata['currentPet']
        with suppress(KeyError):
            self.social_media = playerdata['socialMedia']['links']
        with suppress(KeyError):
            self.recently_played = playerdata['mostRecentGameType']
        with suppress(KeyError):
            self.rank = Hypixel.getRank(playerdata)
        with suppress(KeyError):
            self.cached = cached

    def __eq__(self, other):
        try:
            if other.uuid == self.uuid:
                return True
        except AttributeError:
            pass
        return False

    def __str__(self):
        return self.name

    async def get_guild(self):
        r"""|coro|
        
        Gets the Guild object that the player belongs to.

        :return: The player's guild.
        :rtype: PyPixel.Guild.Guild, optional"""
        try:
            return await self._hypixel.get_guild(self.uuid, 'player')
        except GuildNotFound as e:
            if e.reason == "Player {0} is not in a guild.".format(self.uuid):
                return None

    async def profiles(self):
        r"""|coro|

        Gets the player's SkyBlock profiles.

        :return: A list containing the player's SkyBlock profiles.
        :rtype: List[PyPixel.SkyBlockProfile.SkyBlockProfile]"""
        return await self._hypixel.get_profiles(self.uuid)
