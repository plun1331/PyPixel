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

from .items import Items


class SkyBlock:
    """ Utilities relating to Hypixel SkyBlock """
    @staticmethod
    def getItem(item: str, *, reverse: bool = False) -> str:
        r"""Gets an item name from an item ID.

        Parameters
        -----------
        item :class:`str`
            The item ID.

        reverse :class:`Optional[bool]`
            Whether or not to translate an item name to an item ID.

        Returns
        --------
        :class:`str`
            The item name/ID."""
        if not reverse:
            if item not in Items.ids:
                return item
            return Items.ids[item]
        else:
            for id_ in Items.ids:
                if Items.ids[id_] == item:
                    return id_
            return item

    @staticmethod
    def getMinionSlots(crafted: list) -> int:
        r"""Gets the number of crafted minion slots a player has.

        Parameters
        -----------
        crafted :class:`list`
            The player's crafted minions.

        Returns
        --------
        :class:`int`
            The player's crafted minion slots."""
        slts = 5
        req_unique = [5,
                      15,
                      30,
                      50,
                      75,
                      100,
                      125,
                      150,
                      175,
                      200,
                      225,
                      250,
                      275,
                      300,
                      350,
                      400,
                      450,
                      500,
                      550]
        minions = []
        for minion in crafted:
            if minion not in minions:
                minions.append(minion)
        rexp = len(minions)
        for level in req_unique:
            if rexp >= level:
                slts += 1
            elif rexp < level:
                break
        slots = slts
        return slots

    @staticmethod
    def zombieSlayer(xp) -> int:
        r"""Gets the level for the Zombie slayer from the slayer experience.

        Parameters
        -----------
        xp :class:`float`
            The player's Zombie slayer XP.

        Returns
        --------
        :class:`int`
            The player's Zombie slayer level."""
        req_xp = [5,
                  15,
                  200,
                  1000,
                  5000,
                  20000,
                  100000,
                  400000,
                  1000000]
        lvl = 0
        for level in req_xp:
            if xp >= level:
                lvl += 1
            elif xp < level:
                break
        return lvl

    @staticmethod
    def spiderSlayer(xp) -> int:
        r"""Gets the level for the Spider slayer from the slayer experience.

        Parameters
        -----------
        xp :class:`float`
            The player's Wolf slayer XP.

        Returns
        --------
        :class:`int`
            The player's Spider slayer level."""
        req_xp = [5,
                  25,
                  200,
                  1000,
                  5000,
                  20000,
                  100000,
                  400000,
                  1000000]
        lvl = 0
        for level in req_xp:
            if xp >= level:
                lvl += 1
            elif xp < level:
                break
        return lvl

    @staticmethod
    def wolfSlayer(xp: float) -> int:
        r"""Gets the level for the Wolf slayer from the slayer experience.

        Parameters
        -----------
        xp :class:`float`
            The player's Wolf slayer XP.

        Returns
        --------
        :class:`int`
            The player's Wolf slayer level."""
        req_xp = [10,
                  30,
                  250,
                  1500,
                  5000,
                  20000,
                  100000,
                  400000,
                  1000000]
        lvl = 0
        for level in req_xp:
            if xp >= level:
                lvl += 1
            elif xp < level:
                break
        return lvl

    @staticmethod
    def slayerLevels(data: dict) -> (int, int, int):
        r""" Retrieves a SkyBlock player's Slayer levels from their profile data.

        Parameters
        -----------
        data :class`dict`
            The player's profile data.

        Returns
        --------
        :class:`(int, int, int)`
            A tuple with the player's Slayer levels in the order Zombie, Spider, and Wolf."""
        try:
            zombie = SkyBlock.zombieSlayer(data['slayer_bosses']['zombie']['xp'])
        except KeyError:
            zombie = 0
        try:
            spider = SkyBlock.spiderSlayer(data['slayer_bosses']['spider']['xp'])
        except KeyError:
            spider = 0
        try:
            wolf = SkyBlock.wolfSlayer(data['slayer_bosses']['wolf']['xp'])
        except KeyError:
            wolf = 0
        return zombie, spider, wolf

    @staticmethod
    def getSkillLevel(xp: float) -> int:
        r""" Converts skill XP to a skill level.

        Parameters
        -----------
        xp: :class:`float`
            The skill experience.

        Returns
        --------
        :class:`int`
            The skill's level."""
        prog_req_xp = [50,
                       125,
                       200,
                       300,
                       500,
                       750,
                       1000,
                       1500,
                       2000,
                       3500,
                       5000,
                       7500,
                       10000,
                       15000,
                       20000,
                       30000,
                       50000,
                       75000,
                       100000,
                       200000,
                       300000,
                       400000,
                       500000,
                       600000,
                       700000,
                       800000,
                       900000,
                       1000000,
                       1100000,
                       1200000,
                       1300000,
                       1400000,
                       1500000,
                       1600000,
                       1700000,
                       1800000,
                       1900000,
                       2000000,
                       2100000,
                       2200000,
                       2300000,
                       2400000,
                       2500000,
                       2600000,
                       2750000,
                       2900000,
                       3100000,
                       3400000,
                       3700000,
                       4000000]
        lvl = 0
        rexp = xp
        for level in prog_req_xp:
            if rexp >= level:
                rexp -= level
                lvl += 1
                pass
            elif rexp < level:
                break
        return lvl

    @staticmethod
    def getRuneCraftLevel(xp: float) -> int:
        r""" Converts runecrafting skill XP to a skill level.

        This is seperate from :function:`getSkillLevel` because runecrafting has
        different experience requirements.

        Parameters
        -----------
        xp: :class:`float`
            The runecrafting skill experience.

        Returns
        --------
        :class:`int`
            The runecrafting skill's level."""
        prog_req_xp = [50,
                       100,
                       125,
                       160,
                       200,
                       250,
                       315,
                       400,
                       500,
                       625,
                       785,
                       1000,
                       1250,
                       1600,
                       2000,
                       2465,
                       3125,
                       4000,
                       5000,
                       6200,
                       7800,
                       9800,
                       12200,
                       15300]
        lvl = 0
        rexp = xp
        for level in prog_req_xp:
            if rexp >= level:
                rexp -= level
                lvl += 1
                pass
            elif rexp < level:
                break
        return lvl

    @staticmethod
    def farmingCollection(data: dict) -> dict:
        r""" Gets a player's SkyBlock Farming collection from their member data.

        Parameters
        -----------
        data :class:`dict`
            The player's SkyBlock data.

        Returns
        --------
        :class:`dict`
            A dict of their items in the Farming collection."""
        collections = ['WHEAT',
                       'CARROT_ITEM',
                       'POTATO_ITEM',
                       'PUMPKIN',
                       'MELON',
                       'SEEDS',
                       'MUSHROOM_COLLECTION',
                       'INK_SACK:3',
                       'CACTUS',
                       'SUGAR_CANE',
                       'FEATHER',
                       'LEATHER',
                       'PORK',
                       'RAW_CHICKEN',
                       'MUTTON',
                       'RABBIT',
                       'NETHER_STALK']
        c = {}
        for collection in collections:
            if collection == 'WHEAT':
                req_xp = [50,
                          100,
                          250,
                          500,
                          1000,
                          2500,
                          10000,
                          15000,
                          25000,
                          50000]
            elif collection == 'CARROT_ITEM' or collection == 'POTATO_ITEM':
                req_xp = [100,
                          250,
                          500,
                          1750,
                          5000,
                          10000,
                          25000,
                          50000,
                          100000]
            elif collection == 'PUMPKIN':
                req_xp = [40,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'MELON':
                req_xp = [250,
                          500,
                          1200,
                          5000,
                          15500,
                          25000,
                          50000,
                          100000,
                          250000]
            elif collection == 'SEEDS':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000]
            elif collection == 'MUSHROOM_COLLECTION':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'INK_SACK:3':
                req_xp = [75,
                          200,
                          500,
                          2000,
                          5000,
                          10000,
                          20000,
                          50000,
                          100000]
            elif collection == 'CACTUS':
                req_xp = [100,
                          250,
                          500,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'SUGAR_CANE':
                req_xp = [100,
                          250,
                          500,
                          1000,
                          2000,
                          5000,
                          10000,
                          20000,
                          50000]
            elif collection == 'FEATHER':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'LEATHER':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000,
                          100000]
            elif collection == 'PORK':
                req_xp = [50,
                          100,
                          250,
                          1, 000,
                          2, 500,
                          5, 000,
                          10, 000,
                          25, 000,
                          50, 000]
            elif collection == 'RAW_CHICKEN':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'MUTTON':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'RABBIT':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'NETHER_STALK':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000,
                          75000,
                          100000]
            else:
                req_xp = []
            if len(req_xp) != 0:
                col = SkyBlock.getItem(collection)
                if collection in data['collection']:
                    next_lvl = 0
                    amount = data['collection'][collection]
                    lvl = 0
                    for level in req_xp:
                        if amount >= level:
                            lvl += 1
                            pass
                        elif amount < level:
                            next_lvl = level
                            break
                    if lvl >= len(req_xp):
                        c[col] = lvl
                    else:
                        progress = int(round(amount, 0))/next_lvl
                        c[col] = lvl + progress
                else:
                    c[col] = 0
        return c

    @staticmethod
    def miningCollection(data: dict):
        r""" Gets a player's SkyBlock Mining collection from their member data.

        Parameters
        -----------
        data :class:`dict`
            The player's SkyBlock data.

        Returns
        --------
        :class:`dict`
            A dict of their items in the Mining collection."""
        collections = ['COBBLESTONE',
                       'COAL',
                       'IRON_INGOT',
                       'GOLD_INGOT',
                       'DIAMOND',
                       'INK_SACK:4',
                       'EMERALD',
                       'REDSTONE',
                       'QUARTZ',
                       'OBSIDIAN',
                       'GLOWSTONE_DUST',
                       'GRAVEL',
                       'ICE',
                       'NETHERRACK',
                       'SAND',
                       'ENDER_STONE']
        c = {}
        for collection in collections:
            if collection == 'COBBLESTONE':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          40000,
                          70000]
            elif collection == 'COAL' or collection == 'IRON_INGOT' or collection == 'GOLD_INGOT' or collection == 'DIAMOND' or collection == 'QUARTZ' or collection == 'GLOWSTONE_DUST' or collection == 'GRAVEL':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'INK_SACK:4':
                req_xp = [250,
                          500,
                          1000,
                          2000,
                          10000,
                          25000,
                          50000,
                          100000,
                          150000,
                          250000]
            elif collection == 'EMERALD':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          5000,
                          15000,
                          30000,
                          50000,
                          100000]
            elif collection == 'REDSTONE':
                req_xp = [100,
                          250,
                          750,
                          1500,
                          3000,
                          5000,
                          10000,
                          25000,
                          50000,
                          200000,
                          400000,
                          600000,
                          800000,
                          1000000,
                          1200000]
            elif collection == 'OBSIDIAN':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000,
                          100000]
            elif collection == 'ICE':
                req_xp = [50,
                          100,
                          250,
                          500,
                          1000,
                          5000,
                          10000,
                          50000,
                          100000,
                          250000]
            elif collection == 'NETHERRACK':
                req_xp = [50,
                          250,
                          500]
            elif collection == 'SAND':
                req_xp = [50,
                          100,
                          250,
                          500,
                          1000,
                          2500,
                          5000]
            elif collection == 'ENDER_STONE':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          15000,
                          25000,
                          50000]
            else:
                req_xp = []
            if len(req_xp) != 0:
                col = SkyBlock.getItem(collection)
                if collection in data['collection']:
                    next_lvl = 0
                    amount = data['collection'][collection]
                    lvl = 0
                    for level in req_xp:
                        if amount >= level:
                            lvl += 1
                            pass
                        elif amount < level:
                            next_lvl = level
                            break
                    if lvl >= len(req_xp):
                        c[col] = lvl
                    else:
                        progress = int(round(amount, 0)) / next_lvl
                        c[col] = lvl + progress
                else:
                    c[col] = 0
            return c

    @staticmethod
    def combatCollection(data: dict) -> dict:
        r""" Gets a player's SkyBlock Combat collection from their member data.

        Parameters
        -----------
        data :class:`dict`
            The player's SkyBlock data.

        Returns
        --------
        :class:`dict`
            A dict of their items in the Combat collection."""
        collections = ['ROTTEN_FLESH',
                       'BONE',
                       'STRING',
                       'SPIDER_EYE',
                       'SULPHUR',
                       'ENDER_PEARL',
                       'GHAST_TEAR',
                       'SLIME_BALL',
                       'BLAZE_ROD',
                       'MAGMA_CREAM']
        c = {}
        for collection in collections:
            if collection == 'ROTTEN_FLESH' or collection == 'SPIDER_EYE' or collection == 'SULPHUR' or collection == 'SLIME_BALL' or collection == 'BLAZE_ROD' or collection == 'MAGMA_CREAM':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'BONE':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000,
                          150000]
            elif collection == 'STRING':
                req_xp = [60,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'ENDER_PEARL':
                req_xp = [50,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          15000,
                          25000,
                          50000]
            elif collection == 'GHAST_TEAR':
                req_xp = [20,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            else:
                req_xp = []
            if len(req_xp) != 0:
                col = SkyBlock.getItem(collection)
                if collection in data['collection']:
                    next_lvl = 0
                    amount = data['collection'][collection]
                    lvl = 0
                    for level in req_xp:
                        if amount >= level:
                            lvl += 1
                            pass
                        elif amount < level:
                            next_lvl = level
                            break
                    if lvl >= len(req_xp):
                        c[col] = lvl
                    else:
                        progress = int(round(amount, 0)) / next_lvl
                        c[col] = lvl + progress
                else:
                    c[col] = 0
            return c

    @staticmethod
    def foragingCollection(data: dict) -> dict:
        r""" Gets a player's SkyBlock Foraging collection from their member data.

        Parameters
        -----------
        data :class:`dict`
            The player's SkyBlock data.

        Returns
        --------
        :class:`dict`
            A dict of their items in the Foraging collection."""
        collections = ['LOG',
                       'LOG:1',
                       'LOG:2',
                       'LOG_2:1',
                       'LOG_2',
                       'LOG:3']
        c = {}
        for collection in collections:
            if collection == 'LOG':
                req_xp = [50,
                          100,
                          250,
                          500,
                          1000,
                          2000,
                          5000,
                          10000,
                          30000]
            elif collection == 'LOG:1':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2000,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'LOG:2':
                req_xp = [50,
                          100,
                          250,
                          500,
                          1, 000,
                          2, 000,
                          5, 000,
                          10, 000,
                          25, 000]
            elif collection == 'LOG_2:1':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'LOG_2':
                req_xp = [50,
                          100,
                          250,
                          500,
                          1000,
                          2000,
                          5000,
                          10000,
                          25000]
            elif collection == 'LOG:3':
                req_xp = [50,
                          100,
                          250,
                          500,
                          1000,
                          2000,
                          5000,
                          10000,
                          25000]
            else:
                req_xp = []
            if len(req_xp) != 0:
                col = SkyBlock.getItem(collection)
                if collection in data['collection']:
                    next_lvl = 0
                    amount = data['collection'][collection]
                    lvl = 0
                    for level in req_xp:
                        if amount >= level:
                            lvl += 1
                            pass
                        elif amount < level:
                            next_lvl = level
                            break
                    if lvl >= len(req_xp):
                        c[col] = lvl
                    else:
                        progress = int(round(amount, 0)) / next_lvl
                        c[col] = lvl + progress
                else:
                    c[col] = 0
            return c

    @staticmethod
    def fishingCollection(data: dict):
        r""" Gets a player's SkyBlock Fishing collection from their member data.

        Parameters
        -----------
        data :class:`dict`
            The player's SkyBlock data.

        Returns
        --------
        :class:`dict`
            A dict of their items in the Fishing collection."""
        collections = ['RAW_FISH',
                       'RAW_FISH:1',
                       'RAW_FISH:2',
                       'RAW_FISH:3',
                       'PRISMARINE_SHARD',
                       'PRISMARINE_CRYSTALS',
                       'CLAY_BALL',
                       'WATER_LILY',
                       'INK_SACK',
                       'SPONGE']
        c = {}
        for collection in collections:
            if collection == 'RAW_FISH':
                req_xp = [20,
                          50,
                          100,
                          250,
                          500,
                          1000,
                          2500,
                          15000,
                          30000,
                          45000,
                          60000]
            elif collection == 'RAW_FISH:1':
                req_xp = [20,
                          50,
                          100,
                          250,
                          500,
                          1000,
                          2500,
                          5000,
                          10000]
            elif collection == 'RAW_FISH:2':
                req_xp = [10,
                          25,
                          50,
                          100,
                          200,
                          400,
                          800]
            elif collection == 'RAW_FISH:3':
                req_xp = [20,
                          50,
                          100,
                          150,
                          400,
                          800,
                          2400,
                          4800,
                          9000]
            elif collection == 'PRISMARINE_SHARD':
                req_xp = [10,
                          25,
                          50,
                          100,
                          200]
            elif collection == 'PRISMARINE_CRYSTALS':
                req_xp = [10,
                          25,
                          50,
                          100,
                          200,
                          400,
                          800]
            elif collection == 'CLAY_BALL':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500]
            elif collection == 'WATER_LILY':
                req_xp = [10,
                          50,
                          100,
                          200,
                          500,
                          1500,
                          3000,
                          6000,
                          10000]
            elif collection == 'INK_SACK':
                req_xp = [20,
                          40,
                          100,
                          200,
                          400,
                          800,
                          1500,
                          2500,
                          4000]
            elif collection == 'SPONGE':
                req_xp = [20,
                          40,
                          100,
                          200,
                          400,
                          800,
                          1500,
                          2500,
                          4000]
            else:
                req_xp = []
            if len(req_xp) != 0:
                col = SkyBlock.getItem(collection)
                if collection in data['collection']:
                    next_lvl = 0
                    amount = data['collection'][collection]
                    lvl = 0
                    for level in req_xp:
                        if amount >= level:
                            lvl += 1
                            pass
                        elif amount < level:
                            next_lvl = level
                            break
                    if lvl >= len(req_xp):
                        c[col] = lvl
                    else:
                        progress = int(round(amount, 0)) / next_lvl
                        c[col] = lvl + progress
                else:
                    c[col] = 0
            return c
