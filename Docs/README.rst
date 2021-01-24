PyPixel Documentation
----------------------

Attributes are currently undocumented, as there's a lot of them.

Also, these docs are unfinished, so please don't rely on them too much.

:code:`PyPixel.Hypixel(*, api_key, base_url, clear_cache_after)`
#################################################################

The main class that will be used for requesting information from the Hypixel API.

Parameters
***********
api_key: :code:`str`
    Your Hypixel API key.

base_url: :code:`Optional[str]`
    The base URL for the Hypixel API. Defaults to https://api.hypixel.net/.

clear_cache_after: :code:`Optional[int]`
    How often the cache should clear in seconds.

:code:`await get_player(uuid)`
*******************************

This function is a `Coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutine>`_

Gets a player from the Hypixel API using the :code:`/player` endpoint.

Parameters
~~~~~~~~~~~
uuid: :code:`str`
    The UUID you are requesting player data for.

Returns
~~~~~~~~~~~
:code:`PyPixel.Player`
    The returned player.

Raises
~~~~~~~~~~~
:code:`PyPixel.PlayerNotFound`
    The player couldn't be found.
    This could happen for a variety of reasons.


----


:code:`await get_guild(arg, by)`
**********************************

This function is a `Coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutine>`_

Gets a guild from the Hypixel API using the :code:`/guild` endpoint.

Parameters
~~~~~~~~~~~
arg: :code:`str`
    The guild ID or name, or a player UUID.

by: :code:`Literal['id', 'name', 'player']`
    The type of :code:`arg` you provided.

    :code:`'id'` for a guild ID,

    :code:`'name'` for a guild name,

    :code:`'player'` for a player UUID.

Returns
~~~~~~~~~~~
:code:`PyPixel.Guild`
    The returned guild.

Raises
~~~~~~~~~~~
:code:`TypeError`
    An invalid :code:`by` parameter was provided.

:code:`PyPixel.GuildNotFound`
    An invalid :code:`arg` was provided.

----


:code:`PyPixel.Player(data, cached, hypixel)`
##############################################
Represents a Hypixel player.

Parameters
***********
data: :code:`dict`
    The raw data from the API.

cached: :code:`bool`
    Whether or not the data was retrieved from the cache.

hypixel: :code:`PyPixel.Hypixel`
    The :code:`PyPixel.Hypixel` class used to make the request.

:code:`await get_guild()`
**************************

This function is a `Coroutine <https://docs.python.org/3/library/asyncio-task.html#coroutine>`_


