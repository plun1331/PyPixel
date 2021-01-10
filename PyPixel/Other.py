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

import nbt
import io
import base64
import typing
from .Cache import Cache
import aiohttp

def playerLevel(xp) -> int:
    r"""Gets a player's network level from their network experience, 
    using the equation `(((2 * xp) + 30625) ** (1 / 2) / 50) - 2.5`.
        
    Parameters
    -----------
    xp: :class:`float`
        The player's network experience.

    Returns
    --------
    :class:`int`
        The player's network level.
    """
    network_level = (((2 * xp) + 30625) ** (1 / 2) / 50) - 2.5
    level = round(network_level, 0)
    return int(level)

def skywarsLevel(xp: float) -> int:
    r"""Gets a player's SkyWars level from their SkyWars experience.
        
    Parameters
    -----------
    xp: :class:`float`
        The player's SkyWars experience.

    Returns
    --------
    :class:`int`
        The player's SkyWars level.
    """
    level = 0
    xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
    if xp >= 15000:
        level = (xp - 15000) / 10000. + 12
    else:
        for i in range(len(xps)):
            if xp < xps[i]:
                level = int(round(int(1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1], 0))))
    return level



async def sendRequest(url: str, cache: Cache) -> dict:
    r"""|coro|
        
    Sends a request to the specified url.
        
    Parameters
    -----------
    url: :class:`str`
        The URL the request will be sent to.


    Returns
    --------
    :class:`dict`
        The json data from the API.

    :class:`bool`
        Whether or not the data was retrieved from the cache.
    """
    data = await cache.getFromCache(url)
    cached = True
    if data is None:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
        cached = False
    return data, cached

def getRank(data: dict) -> typing.Literal['Default', 'VIP', 'VIP+', 'MVP', 'MVP+', 'MVP++', 'YouTube', 'Helper', 'Moderator', 'Admin']:
    r"""Gets a player's rank from their raw API data.
        
    Parameters
    -----------
    data: :class:`dict`
        The player's raw API data.


    Returns
    --------
    :class:`Literal['Default', 'VIP', 'VIP+', 'MVP', 'MVP+', 'MVP++', 'YouTube', 'Helper', 'Moderator', 'Admin']`
        The player's rank.
    """
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


def parseNBT(raw_data):
    data = nbt.nbt.NBTFile(fileobj = io.BytesIO(base64.b64decode(raw_data)))
    return data

def guildlevel(xp: float):
    r"""Gets a guild's level from the guild's xp.
        
    Parameters
    -----------
    xp: :class:`float`
        The guild's XP.


    Returns
    --------
    :class:`int`
        The guild's level.
    """
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
        needed = 0
        if i >= len(req_exp):
            needed = req_exp[len(req_exp) - 1]
        else:
            needed = req_exp[i]
        xp -= needed
        if xp < 0:
            return int(lvl)
        else:
            lvl += 1
    return 0
