# PyPixel

[![Discord Server Invite](https://discord.com/api/guilds/766123673425281025/embed.png)](https://discord.gg/k6fgvUn3aF)
[![PyPI version info](https://img.shields.io/pypi/v/pypixel-api.svg)](https://pypi.python.org/pypi/pypixel-api)
[![PyPI supported Python versions](https://img.shields.io/pypi/pyversions/pypixel-api.svg)](https://pypi.python.org/pypi/pypixel-api)

Discord Server Invite PyPI Version Info PyPI supported Python versions

An asynchronous wrapper for the Hypixel API.





# Installation

**Python 3.6 or higher is required**

You can install the package with the following command.

```sh
# Linux/macOS
python3 -m pip install -U pypixel-api

# Windows
py -3 -m pip install -U pypixel-api
```



# A few examples

## Getting a player.

```py
# Import the module
import PyPixel
# Importing asyncio so we can run our coroutine
import asyncio

# Initialize the Hypixel class
hypixel = PyPixel.Hypixel(api_key='YOUR_API_KEY')

async def getPlayer():
    # Gets a player by UUID. For this example, we'll use mine.
    player = await hypixel.get_player('c7b08e0c73c94750b7780841025f40d4')

    print(player.name)
    print(player.uuid)
    print(player.rank) 

# Run the above coroutine
loop = asyncio.get_event_loop()
loop.run_until_complete(getPlayer())

"""
Output:

awsomo28
c7b08e0c73c94750b7780841025f40d4
MVP+
"""
```



## Getting a guild

```py
# Import the module
import PyPixel
# Importing asyncio so we can run our coroutine
import asyncio


# Initialize the Hypixel class
hypixel = PyPixel.Hypixel(api_key='YOUR_API_KEY')

async def getGuild():
    # Gets a player by UUID. For this example, we'll use mine.
    guild = await hypixel.get_guild('SkyKings', 'name')

    print(guild.name)
    print(guild.members[0].rank)
    print(guild.level)


# Run the above coroutine
loop = asyncio.get_event_loop()
loop.run_until_complete(getGuild())


"""
Output:

SkyKings
GUILDMASTER
98
"""
```
