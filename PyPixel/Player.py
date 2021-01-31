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
from .PlayerStats import PlayerStats
from .utils import HypixelUtils
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
        self.stats = PlayerStats(playerdata)
        self.uuid = playerdata['uuid'] if 'uuid' in playerdata else None
        self.achievements = playerdata['achievements'] if 'achievements' in playerdata else None
        self.one_time_achievements = playerdata['achievementsOneTime'] if 'achievementsOneTime' in playerdata else None
        self.auto_spawning_pet = playerdata['auto_spawn_pet'] if 'auto_spawn_pet' in playerdata else None
        self.current_chat_channel = playerdata['channel'] if 'channel' in playerdata else None
        self.display_name = playerdata['displayname'] if 'displayname' in playerdata else None
        self.fireworks = [Firework(firework) for firework in
                          playerdata['fireworkStorage']] if 'fireworkStorage' in playerdata else None
        self.firstLogin = datetime.datetime.fromtimestamp(
            playerdata['firstLogin'] / 1000.0) if 'firstLogin' in playerdata else None
        self.karma = playerdata['karma'] if 'karma' in playerdata else None
        self.aliases = playerdata['knownAliases'] if 'knownAliases' in playerdata else None
        self.lastLogin = datetime.datetime.fromtimestamp(
            playerdata['lastLogin'] / 1000.0) if 'lastLogin' in playerdata else None
        self.most_recently_thanked = playerdata[
            'mostRecentlyThankedUuid'] if 'mostRecentlyThankedUuid' in playerdata else None
        self.most_recently_tipped = playerdata[
            'mostRecentlyTippedUuid'] if 'mostRecentlyTippedUuid' in playerdata else None
        self.experience = playerdata['networkExp'] if 'networkExp' in playerdata else None
        self.level = HypixelUtils.playerLevel(playerdata['networkExp']) if 'networkExp' in playerdata else None
        self.name = playerdata['playername'] if 'playername' in playerdata else None
        self.settings = playerdata['settings'] if 'settings' in playerdata else None
        self.spectators_hidden = playerdata['spectators_invisible'] if 'spectators_invisible' in playerdata else None
        self.recieved_thanks = playerdata['thanksReceived'] if 'thanksReceived' in playerdata else None
        self.thanks_sent = playerdata['thanksSent'] if 'thanksSent' in playerdata else None
        self.version = playerdata['mcVersionRp'] if 'mcVersionRp' in playerdata else None
        self.rank_plus = playerdata['rankPlusColor'] if 'rankPlusColor' in playerdata else None
        self.last_logout = datetime.datetime.fromtimestamp(
            playerdata['lastLogout'] / 1000) if 'lastLogout' in playerdata else None
        self.cloak = playerdata['currentCloak'] if 'currentCloak' in playerdata else None
        self.achievement_points = playerdata['achievementPoints'] if 'achievementPoints' in playerdata else None
        self.click_effect = playerdata['currentClickEffect'] if 'currentClickEffect' in playerdata else None
        self.current_pet = playerdata['currentPet'] if 'currentPet' in playerdata else None
        self.social_media = playerdata['socialMedia']['links'] if 'socialMedia' in playerdata else None
        self.recently_played = playerdata['mostRecentGameType'] if 'mostRecentGameType' in playerdata else None
        self.rank = HypixelUtils.getRank(playerdata)
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
