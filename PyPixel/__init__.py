# -*- coding: utf-8 -*-

"""
PyPixel
~~~~~~~~~~~~~~~~~~~

An asynchronous wrapper for the Hypixel API.

:copyright: (c) 2021 plun1331
:license: MIT, see LICENSE for more details.

"""

__title__ = 'PyPixel'
__author__ = 'plun1331'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 plun1331'
__version__ = '0.2.1'

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from collections import namedtuple

from .Cache import Cache
from .Errors import *
from .Firework import Firework
from .Guild import Guild
from .GuildMember import GuildMember
from .GuildRank import GuildRank
from .Hypixel import Hypixel
from .Player import Player
from .PlayerStats import PlayerStats, SkyWarsStats
from .SkyBlockProfile import SkyBlockProfile
from .SkyBlockProfileMember import SkyBlockStats, SkyBlockObjective, SkyBlockQuest, SkyBlockSlayer, SkyBlockPet, \
    ProfileMember
from .Achievements import AchievementData, AchievementTier, Achievement, AchievementGame, Tiered, OneTime
from .AuctionPage import AuctionPage
from .Auction import Auction

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=1, micro=9, releaselevel='stable', serial=0)
