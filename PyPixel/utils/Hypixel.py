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

from nbt.nbt import NBTFile
import io
import base64
from typing import Union, Literal
from .games import GameInfo
import re

mcformat = re.compile(r'§.')

class HypixelUtils:
    r"""General utilities relating to Hypixel."""

    @staticmethod
    def parseNBT(raw_data: Union[bytes, str]) -> NBTFile:
        r"""Parses NBT data from the API.

        :param raw_data: The raw encoded NBT data.
        :type raw_data: Union[bytes, str]

        :return: The decoded NBT data.
        :rtype: nbt.nbt.NBTFile"""

        data = NBTFile(fileobj=io.BytesIO(base64.b64decode(raw_data)))
        return data

    @staticmethod
    def getRank(data: dict) -> Literal[
        'Default', 'VIP', 'VIP+', 'MVP', 'MVP+', 'MVP++', 'YouTube', 'Helper', 'Moderator', 'Admin'
    ]:
        r"""Gets a player's rank from their raw API data.

        :param data: The player's raw API data.
        :type data: dict

        :return: The player's rank.
        :rtype: Literal['Default', 'VIP', 'VIP+', 'MVP', 'MVP+', 'MVP++', 'YouTube', 'Helper', 'Moderator', 'Admin']"""

        if "rank" in data and data["rank"] != "NORMAL":
            rank = data["rank"]
        elif "monthlyPackageRank" in data:
            if data['player']['monthlyPackageRank'] == "SUPERSTAR":
                rank = "MVP++"
            else:
                rank = "Default"
        elif "newPackageRank" in data:
            rank = data["newPackageRank"]
        elif "packageRank" in data:
            rank = data["packageRank"]
        else:
            rank = "Default"
        if rank == "VIP_PLUS":
            rank = "VIP+"
        elif rank == "MVP_PLUS":
            rank = "MVP+"
        elif rank == "YOUTUBER":
            rank = "YouTube"
        elif rank == "ADMIN":
            rank = "Admin"
        elif rank == "MODERATOR":
            rank = "Moderator"
        elif rank == "HELPER":
            rank = "Helper"
        return rank

    @staticmethod
    def guildlevel(xp: float):
        r"""Gets a guild's level from the guild's xp.

        :param xp: The guild's XP.
        :type xp: float

        :return: The guild's level.
        :rtype: int"""

        req_exp = [100000,
                   150000,
                   250000,
                   500000,
                   750000,
                   1000000,
                   1250000,
                   1500000,
                   2000000,
                   2500000,
                   2500000,
                   2500000,
                   2500000,
                   2500000,
                   3000000]
        lvl = 0
        for i in range(1000):
            if i >= len(req_exp):
                needed = req_exp[len(req_exp) - 1]
            else:
                needed = req_exp[i]
            xp -= needed
            if xp < 0:
                return int(lvl)
            lvl += 1
        return 0

    @staticmethod
    def playerLevel(xp: float) -> int:
        r"""Gets a player's network level from their network experience,
        using the equation ``(((2 * xp) + 30625) ^ (1 / 2) / 50) - 2.5``.

        :param xp: The player's network experience.
        :type xp: float

        :return: The player's network level.
        :rtype: int"""

        network_level = (((2 * xp) + 30625) ** (1 / 2) / 50) - 2.5
        level = round(network_level, 0)
        return int(level)

    @staticmethod
    def skywarsLevel(xp: float) -> int:
        r"""Gets a player's SkyWars level from their SkyWars experience.

        :param xp: The player's SkyWars experience.
        :type xp: float

        :return: The player's SkyWars level.
        :rtype: int"""

        level = 0
        xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
        if xp >= 15000:
            level = (xp - 15000) / 10000. + 12
        else:
            for i, item in enumerate(xps):
                if xp < item:
                    # noinspection PyTypeChecker
                    level = int(round(int(1 + i + float(xp - xps[i - 1]) / (item - xps[i - 1], 0))))
        return level

    @staticmethod
    def getGameName(game: Union[int, str]) -> str:
        r"""Gets the name of a Hypixel gamemode from its ID or it's name in the API.

        :param game: The game's ID/API Name.
        :type game: Union[int, str]

        :return: The game's name, or if the game is not found, the original value you provided.
        :rtype: str"""
        if isinstance(game, int):
            for game_ in GameInfo.ids:
                if GameInfo.ids[game_] == game:
                    return GameInfo.apinames[game_]
        else:
            if game in GameInfo.apinames:
                return GameInfo.apinames[game]
        if isinstance(game, str):
            if game.lower() in GameInfo.databasenames:
                return GameInfo.databasenames[game.lower()]
        return game

    @staticmethod
    def stripFormatting(text: str) -> str:
        return mcformat.sub('', text)
