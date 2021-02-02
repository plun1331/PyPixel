PyPixel.utils API Reference
============================
The following section outlines the API for PyPixel.utils.

.. _HypixelUtils:
.. py:class:: HypixelUtils

    General utilities relating to Hypixel.

    .. py:staticmethod:: parseNBT(raw_data)

        Parses NBT data from the API.

        :param raw_data: The raw encoded NBT data.
        :type raw_data: Union[bytes_, str_]

        :return: The decoded NBT data.
        :rtype: nbt.nbt.NBTFile

    .. py:staticmethod:: getRank(data)

        Gets a player's rank from their raw API data.

        :param data: The player's raw API data.
        :type data: dict_

        :return: The player's rank.
        :rtype: Literal['Default', 'VIP', 'VIP+', 'MVP', 'MVP+', 'MVP++', 'YouTube', 'Helper', 'Moderator', 'Admin']

    .. py:staticmethod:: guildlevel(xp)

        Gets a guild's level from the guild's xp.

        :param xp: The guild's XP.
        :type xp: float_

        :return: The guild's level.
        :rtype: int_

    .. py:staticmethod:: playerLevel(xp)

        Gets a player's network level from their network experience,
        using the equation ``(((2 * xp) + 30625) ^ (1 / 2) / 50) - 2.5``.

        :param xp: The player's network experience.
        :type xp: float_

        :return: The player's network level.
        :rtype: int_

    .. py:staticmethod:: skywarsLevel(xp)

        Gets a player's SkyWars level from their SkyWars experience.

        :param xp: The player's SkyWars experience.
        :type xp: float_

        :return: The player's SkyWars level.
        :rtype: int_

    .. py:staticmethod:: getGameName(game)

        .. versionadded:: 0.1.9

        Gets the name of a Hypixel gamemode from its ID or it's name in the API.

        :param game: The game's ID/API Name.
        :type game: Union[int_, str_]

        :return: The game's name, or if the game is not found, the original value you provided.
        :rtype: str_


.. py:class:: SkyBlockUtils

    Utilities relating to Hypixel SkyBlock.

    .. py:staticmethod:: getItem(item, *, reverse)

        Gets an item name from an item ID.

        :param item: The item ID.
        :type item: str_

        :param reverse: Whether or not to translate an item name to an item ID.
        :type reverse: Optional[bool_]

        :return: The item name/ID.
        :rtype: str_

    .. py:staticmethod:: getMinionSlots(crafted)

        Gets the number of crafted minion slots a player has.

        :param crafted: The player's crafted minions.
        :type crafted: list_

        :return: The player's crafted minion slots.
        :rtype: int_

    .. py:staticmethod:: zombieSlayer(xp)

        Gets the level for the Zombie slayer from the slayer experience.

        :param xp: The player's Zombie slayer XP.
        :type xp: float_

        :return: The player's Zombie slayer level.
        :rtype: int_

    .. py:staticmethod:: spiderSlayer(xp)

        Gets the level for the Spider slayer from the slayer experience.

        :param xp: The player's Spider slayer XP.
        :type xp: float_

        :return: The player's Spider slayer level.
        :rtype: int_

    .. py:staticmethod:: wolfSlayer(xp)

        Gets the level for the Wolf slayer from the slayer experience.

        :param xp: The player's Wolf slayer XP.
        :type xp: float_

        :return: The player's Wolf slayer level.
        :rtype: int_

    .. py:staticmethod:: slayerLevels(data)

        Retrieves a SkyBlock player's Slayer levels from their profile data.

        :param data: The player's profile data.
        :type data: dict_

        :return: A tuple with the player's Slayer levels in the order Zombie, Spider, and Wolf.
        :retype: int_, int_, int_

    .. _getSkillLevel:
    .. py:staticmethod:: getSkillLevel(xp)

        Converts skill XP to a skill level.

        :param xp: The skill experience.
        :type xp: float_

        :return: The skill's level.
        :rtype: int_

    .. py:staticmethod:: getRunecraftLevel(xp)

        Converts runecrafting skill XP to a skill level.

        This is seperate from getSkillLevel_ because runecrafting has
        different experience requirements.

        :param xp: The runecrafting skill experience.
        :type xp: float_

        :return: The runecrafting skill's level.
        :rtype: int_

    .. py:staticmethod:: farmingCollection(data)

        Gets a player's SkyBlock Farming collection from their member data.

        :param data: The player's SkyBlock data.
        :type data: dict_

        :return: A dict of their items in the Farming collection.
        :rtype: dict_

    .. py:staticmethod:: miningCollection(data)

        Gets a player's SkyBlock Mining collection from their member data.

        :param data: The player's SkyBlock data.
        :type data: dict_

        :return: A dict of their items in the Mining collection.
        :rtype: dict_

    .. py:staticmethod:: combatCollection(data)

        Gets a player's SkyBlock Combat collection from their member data.

        :param data: The player's SkyBlock data.
        :type data: dict_

        :return: A dict of their items in the Combat collection.
        :rtype: dict_

    .. py:staticmethod:: foragingCollection(data)

        Gets a player's SkyBlock Foraging collection from their member data.

        :param data: The player's SkyBlock data.
        :type data: dict_

        :return: A dict of their items in the Foraging collection.
        :rtype: dict_

    .. py:staticmethod:: fishingCollection(data)

        Gets a player's SkyBlock Fishing collection from their member data.

        :param data: The player's SkyBlock data.
        :type data: dict_

        :return: A dict of their items in the Fishing collection.
        :rtype: dict_

    .. py:staticmethod:: getCollectionData(data, req_xp, collection, c)

        Modifies a collection's collection data.

        :param data: The raw API data.
        :type data: dict_

        :param req_xp: A list of the required XP.
        :type req_xp: list_

        :param collection: The collection to modify the dict with.
        :type collection: str_

        :param c: The dict to modify.
        :type c: dict_

        :return: The modified dict.
        :rtype: dict_

    .. py:staticmethod:: getLevel(req_xp, xp, *, subtract=True)

        Gets a level from required xp and total xp.

        :param req_xp: The required XP.
        :type req_xp: list_

        :param xp: The total XP.
        :type xp: float_

        :param subtract: Whether or not to subtract from xp. Defaults to ``True``
        :type subtract: bool_

        :return: The level.
        :rtype: int_




.. class:: Items

    A class containing all the Hypixel SkyBlock Item IDs.

    .. py:attribute:: ids

        A dict_ of every SkyBlock item ID.



.. py:class:: GameInfo

    .. versionadded:: 0.1.9

    Contains information on some games and their IDs.

    .. py:attribute:: apinames

        A dict_ containing game names and what they're referred to in the API.

    .. py:attribute:: databasenames

        A dict_ containing game names and what they're referred to in the Hypixel database (I assume).

    .. py:attribute:: ids

        A dict_ containing the game's API names and IDs.



.. |coro| replace:: This function is a coroutine_.
.. _TypeError: https://docs.python.org/3/library/exceptions.html#TypeError
.. _coroutine: https://docs.python.org/3/library/asyncio-task.html#coroutine
.. _dict: https://docs.python.org/3/library/stdtypes.html#dict
.. _str: https://docs.python.org/3/library/stdtypes.html#str
.. _bytes: https://docs.python.org/3/library/stdtypes.html#bytes
.. _int: https://docs.python.org/3/library/functions.html#int
.. _float: https://docs.python.org/3/library/functions.html#float
.. _bool: https://docs.python.org/3/library/functions.html#bool
.. _list: https://docs.python.org/3/library/functions.html#list