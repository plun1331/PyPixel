Documentation
==============
The following section outlines the API for PyPixel.

API Reference
**************
.. _Cache:
.. py:class:: Cache(clear_cache_after)

    A class used for caching data returned from the api

    :param clear_cache_after: How often the cache should be cleared in seconds.
    :type clear_cache_after: class:`int`

    .. py:method:: run()

        Runs a loop that refreshes the cache every so often.

        .. warning::
            This is not meant to be called manually, and is invoked when the class is initialized.

    .. py:method:: clearCache()

        |coro|

        Clears the cache.

    .. py:method:: getFromCache(url)

        |coro|

        Gets the cached url from the cache.

        :return: The cached response. Can also be `None` if the response is not cached.
        :rtype: Optional[dict_]

    .. py:method:: cache(url, data)

        |coro|

        Caches a response.

        :param url: The URL the request was sent to.
        :type url: str_

        :param data: The response as a dict.
        :type data: dict_

.. _Firework:
.. py:class:: Firework(firework)

    Represents a firework. Interesting, right?

    :param firework: The raw firework data.
    :type firework: dict_

.. _Guild:
.. py:class:: Guild(data, cached, hypixel)

    Represents a Hypixel guild.

    :param data: The raw data from the API.
    :type data: dict_

    :param cached: Whether or not the data was retrieved from the cache.
    :type cached: bool_

    :param hypixel: The Hypixel class used to make the request.
    :type hypixel: :ref:`Hypixel<Hypixel>`

    .. py:method:: get_member(member)

        |coro|

        Gets a Player object from a GuildMember

        :param member: The member you want a player object from.
        :type member: :ref:`GuildMember<GuildMember>`

        :return: The retrieved player.
        :rtype: :ref:`Player<Player>`

.. _GuildMember:
.. py:class:: GuildMember(memberdata)

    Represents a Hypixel guild member.

    :param memberdata: A dict containing the member's data.
    :type memberdata: dict_

    .. py:attribute:: uuid

        The player's UUID.

    .. py:attribute:: rank

        The player's guild rank.

    .. py:attribute:: joined

        The date the player joined.

    .. py:attribute:: quest_participation

        The player's quest participation.

    .. py:attribute:: xp_history

        The player's guild XP history.

.. _GuildRank:
.. py:class:: GuildRank(rankdata)

    Represents a Hypixel guild rank.

    :param rankdata: A dict containing the rank's data.
    :type rankdata: dict

    .. py:attribute:: name

        The rank's name.

    .. py:attribute:: default

        A boolean indicating if the rank is the default rank.

    .. py:attribute:: tag

        The rank's tag.

    .. py:attribute:: created

        The date/time the rank was created.

    .. py:attribute:: priority

        The rank's priority in the guild's rank heirarchy.

.. _Hypixel:
.. py:class:: Hypixel(*, api_key, base_url = "https://api.hypixel.net, clear_cache_after = 300)

    The main class that will be used for requesting information from the Hypixel API.

    .. versionchanged:: 0.1.8

        Your API Key will now be validated upon initialization.


    :param api_key: Your Hypixel API key.
    :type api_key: str_

    :param base_url: The base URL for the Hypixel API. Defaults to 'https://api.hypixel.net/'.
    :type base_url: Optional[str_]

    :param clear_cache_after: How often the cache should clear in seconds.
    :type clear_cache_after: Optional[int_]

    .. py:method:: get_player(uuid)

        |coro|

        Gets a player from the Hypixel API using the `/player` endpoint.

        :param uuid: The UUID you are requesting player data for.
        :type uuid: str_

        :raises PlayerNotFound_: The player couldn't be found.

        :return: The player from the API.
        :rtype: :ref:`Player<Player>`

    .. py:method:: get_guild(arg, by)

        |coro|

        Gets a guild from the Hypixel API using the ``/guild`` endpoint.

        :param arg: The guild ID or name, or a player UUID.
        :type arg: str_

        :param by: The type of 'arg' you provided.
        :type by: Literal['id', 'name', 'player']

        :raises TypeError_: Invalid 'by' parameter.
        :raises GuildNotFound_: The guild was not found.

        :return: The guild from the API.
        :rtype: :ref:`Guild<Guild>`

    .. py:method:: get_profiles(uuid)

        |coro|

        Gets a player's SkyBlock profiles from the Hypixel API using the `/skyblock/profiles` endpoint.

        :param uuid: The player's UUID.
        :type uuid: str_

        :raises PlayerNotFound_: The player's profiles could not be found.

        :return: A list containing the player's profiles.
        :rtype: List[:ref:`SkyBlockProfile<SkyBlockProfile>`]

    .. py:method:: get_key(key=None)

        .. versionadded:: 0.1.8

        |coro|

        Gets information on an API Key.

        :param key: The API key you want information for.
                    Defaults to the API key you provided on initialization of the class.
        :type key: Optional[str_]

        :raises KeyNotFound_: The key provided does not exist.

        :return: The data on the API Key
        :rtype: :ref:`APIKey`<APIKey>`

    .. py:method:: get_name(uuid)

        |coro|

        Gets a player's name from their UUID. This does not use the Hypixel API.

        :param uuid: The player's UUID.
        :type uuid: str_

        :raises PlayerNotFound_: The UUID is invalid.

        :return: The player's name.
        :rtype: str_

    .. py:method:: get_uuid(name)

        |coro|

        Get's a player's UUID from their name.

        :param name: The player's name.
        :type name: str_

        :raises PlayerNotFound_: The name is invalid.

        :return: The player's UUID.
        :rtype: str_

    .. py:method:: _send(url)

        |coro|

        .. versionchanged:: 0.1.8

            This will now raise exceptions when a http error code is returned by the API.

        Sends a request to the specified url.

        :param url: The URL the request will be sent to.
        :type url: str_

        :raises APIError_: The API returned a ``500`` range status code.
        :raises NotFound_: The API returned a ``404`` status code.
        :raises ClientError_: The API returned a ``400`` range status code.

        :return: The json data from the API, and a boolean value indicating
            whether or not the data was retrieved from the cache.
        :rtype: dict_, bool_

.. _APIKey:
.. py:class:: APIKey(key_data, cached, hypixel):

    .. versionadded:: 0.1.8

    Represents an API Key.

    :param key_data: The raw key data from the API.
    :type key_data: dict

    :param cached: The raw key data from the API.
    :type cached: bool

    :param hypixel: The raw key data from the API.
    :type hypixel: :ref:`Hypixel<Hypixel>`

    .. py:attribute:: cached

        Indicates whether or not the data was retrieved from the cache.

    .. py:attribute:: key

        The API Key

    .. py:attribute:: owner

        The key's owner.

    .. py:attribute::: ratelimit

        The key's ratelimit in requests/min.

    .. py:attribute:: request_past_minute

        The amount of requests made with the key in the past minute.

    .. py:attribute:: total_requests

        The total amount of requests made with the key.

    .. py:method:: get_owner()

        |coro|

        Gets the owner pf the key as a Player object.

        :return: The key's owner.
        :rtype: Player_

.. _Player:
.. py:class:: Player(data, cached, hypixel)

    Represents a Hypixel player.

    :param data: The raw data from the API.
    :type data: dict_

    :param cached: Whether or not the data was retrieved from the cache.
    :type cached: bool_

    :param hypixel: The Hypixel class used to make the request.
    :type hypixel: :ref:`Hypixel<Hypixel>`

.. _PlayerStats:
.. py:class:: PlayerStats(data)

    Base class for a player's statistics.

    :param data: The raw player data from the API.
    :type data: dict_

    .. py:attribute:: skywars

        The player's SkyWars statistics.

.. _SkyBlockProfile:
.. py:class:: SkyBlockProfile(profiledata, cached, hypixel)

    Represents a SkyBlock profile.

    :param profiledata: The profile's data from the API.
    :type profiledata: dict_

    :param cached: A boolean indicating if the profile's data was retrieved from the cache.
    :type cached: bool_

    :param hypixel: The Hypixel class used to get the profile.
    :type hypixel: Hypixel_

.. _ProfileMember:
.. py:class:: Profilemember(uuid, memberdata, hypixel)

    Represents a member in a SkyBlock profile.

    :param uuid: The member's UUID.
    :type uuid: str_

    :param memberdata: The member's data in the profile.
    :type memberdata: dict_

    :param hypixel: The Hypixel class used to get the profile.
    :type hypixel: Hypixel_

    .. py:method:: get_player()

        |coro|

        Gets the member's player object.

        :raises PlayerNotFound_: The player couldn't be found for some reason.

        :return: The player from the API.
        :rtype: Player_

.. _SkyBlockStats:
.. py:class:: SkyBlockStats(stats)

    Represents a player's SkyBlock Statistics.

    :param stats: The player's stats from their memberdata retrieved from the API.
    :type stats: dict

.. _SkyBlockObjective:
.. py:class:: SkyBlockObjective(objective_name, objective_data)

    Represents a SkyBlock Objective.

    :param objective_name: The name of the objective.
    :type objective_name: str_

    :param objective_data: The objective's data.
    :type objective_data: dict_

    .. py:attribute:: name

        The name of the objective.

    .. py:attribute:: status

        The objective's status.

    .. py:attribute:: progress

        The objective's progress.

    .. py:attribute:: completed_at

        The objective's completion date/time. Can also be ``None`` if not completed.

.. _SkyBlockQuest:
.. py:class:: SkyBlockQuest(quest_name, quest_data)

    Represents a SkyBlock quest.

    :param quest_name: The name of the quest.
    :type quest_name: str_

    :param quest_data: The quest's data.
    :type quest_data: dict_

    .. py:attribute:: name

        The name of the quest.

    .. py:attribute:: status

        The quest's status.

    .. py:attribute:: activated_at

        The quest's activation date/time.

    .. py:attribute:: completed_at

        The quest's completion date/time. Can also be ``None`` if not completed.

.. _SkyBlockSlayer:
.. py:class:: SkyBlockSlayer(slayer, slayer_data)

    Represents a SkyBlock slayer.

    :param slayer: The name of the slayer.
    :type slayer: str_

    :param slayer_data: The slayer's data.
    :type slayer_data: dict_

    .. py:attribute:: slayer

        The name of the slayer.

    .. py:attribute:: claimed_levels

        The player's claimed levels for a slayer.

    .. py:attribute:: xp

        The player's slayer xp.

    .. py:attribute:: level

        The player's slayer level.

.. _SkyBlockPet:
.. py:class:: SkyBlockPet(pet_data)

    Represents a SkyBlock pet.

    :param pet_data: The pet's data.
    :type pet_data: dict_

    .. py:attribute:: uuid

        The pet's UUID, I guess.

    .. py:attribute:: type

        The pet's type.

    .. py:attribute:: xp

        The pet's XP.

    .. py:attribute:: active

        A boolean indicating whether or not the pet is active.

    .. py:attribute:: tier

        The pet's tier

    .. py:attribute:: held_item

        The item the pet is holding.

    .. py:attribute:: candy_used

        The candy used on the pet.

    .. py:attribute:: skin

        The pet's skin.

.. _SkyWarsStats:
.. py:class:: SkyWarsStats(playerstats)

    Base class for a player's SkyWars stats.

    :param playerstats: The raw player stats data from the API.
    :type playerstats: dict_

    .. py:class:: Overall(stats)

        The player's overall SkyWars stats.

        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict_

    .. py:class:: Solo(stats)

        The player's solo SkyWars stats.

        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict_

        .. py:class:: Normal(stats)

            The player's solo normal SkyWars stats.

            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict_

        .. py:class:: Insane(stats)

            The player's solo insane SkyWars stats.

            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict_

    .. py:class:: Teams(stats)

        The player's teams SkyWars stats.

        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict_

        .. py:class:: Normal(stats)

            The player's teams normal SkyWars stats.

            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict_

        .. py:class:: Insane(stats)

            The player's teams insane SkyWars stats.

            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict_

    .. py:class:: Mega(stats)

        The player's mega SkyWars stats.

        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict_

    .. py:class:: Ranked(stats)

        The player's ranked SkyWars stats.

        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict_

    .. py:class:: Lab(stats)

        The player's laboratory SkyWars stats.

        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict_

        .. py:class:: Solo(stats)

            The player's lab solo SkyWars stats.

            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict_

        .. py:class:: Teams(stats)

            The player's lab teams SkyWars stats.

            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict_


Exceptions
***********

.. versionchanged:: 0.1.8

    These exceptions are now actually used.

    Oh also the parameters changed.


.. _PyPixelError:
.. py:exception:: PyPixelError(*args)

    Base exception class for PyPixel.

.. _HTTPException:
.. py:exception:: HTTPException

    Base exception class for when the API returns an http error code.

    :param status_code: The status code returned by the API.
    :type status_code: int_

    :param reason: The reason the request failed.
    :type reason: str_

    :param url: The url the request was sent to.
    :type url: str_

    :param data: The JSON data returned from the request, if any.
    :type data: Optional[dict_]

.. _APIError:
.. py:exception:: APIError

    Exception that's thrown when the API returns a 500 range status code.

    :param status_code: The status code returned by the API.
    :type status_code: int_

    :param reason: The reason the request failed.
    :type reason: str_

    :param url: The url the request was sent to.
    :type url: str_

    :param data: The JSON data returned from the request, if any.
    :type data: Optional[dict_]

.. _ClientError:
.. py:exception:: ClientError

    Exception that's thrown when the API returns a 400 range status code.

    :param status_code: The status code returned by the API.
    :type status_code: int_

    :param reason: The reason the request failed.
    :type reason: str_

    :param url: The url the request was sent to.
    :type url: str_

    :param data: The JSON data returned from the request, if any.
    :type data: Optional[dict_]

.. _NotFound:
.. py:exception:: NotFound

    Exception thats thrown when the API returns a 404 status code.

    :param reason: The reason the request failed.
    :type reason: str_

    :param url: The url the request was sent to.
    :type url: str_

    :param data: The JSON data returned from the request, if any.
    :type data: Optional[dict_]

.. _PlayerNotFound:
.. py:exception:: PlayerNotFound(reason)

    Exception thats thrown when a player couldn't be found.

    :param reason: The reason the player couldn't be found.
    :type reason: str_

    :param url: The url the request was sent to.
    :type url: str_

    :param data: The JSON data returned from the request, if any.
    :type data: Optional[dict_]

.. _GuildNotFound:
.. py:exception:: GuildNotFound(reason)

    Exception thats thrown when a guild couldn't be found.

    :param reason: The reason the guild couldn't be found.
    :type reason: str_

    :param url: The url the request was sent to.
    :type url: str_

    :param data: The JSON data returned from the request, if any.
    :type data: Optional[dict_]

.. _KeyNotFound:
.. py:exception:: KeyNotFound(reason, url, data)

    .. versionadded:: 0.1.8

    Exception thats thrown when an API Key couldn't be found.

    :param reason: The reason the key couldn't be found.
    :type reason: str_

    :param url: The url the request was sent to.
    :type url: str_

    :param data: The JSON data returned from the request, if any.
    :type data: Optional[dict_]

.. |coro| replace:: This function is a coroutine_.
.. _TypeError: https://docs.python.org/3/library/exceptions.html#TypeError
.. _coroutine: https://docs.python.org/3/library/asyncio-task.html#coroutine
.. _dict: https://docs.python.org/3/library/stdtypes.html#dict
.. _str: https://docs.python.org/3/library/stdtypes.html#str
.. _int: https://docs.python.org/3/library/functions.html#int
.. _bool: https://docs.python.org/3/library/functions.html#bool