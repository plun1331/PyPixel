.. _examples:

Examples
=========
The following are examples of using PyPixel

Getting a Player
*****************
.. code:: py

    # Import the Module
    import PyPixel
    # Importing asyncio so we can call coroutines
    import asyncio

    # Initialize the Hypixel class
    hypixel = PyPixel.Hypixel(api_key="API Key")

    async def main():
        # Get tha player's UUID
        uuid = await hypixel.get_uuid('awsomo28')
        # Get the player
        player = await hypixel.get_player(uuid)
        # Prints the player's rank
        print(player.rank)

    # run the above coroutine
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

Getting a Player's SkyBlock Profiles
*************************************
.. code:: py

    # Import the Module
    import PyPixel
    # Importing asyncio so we can call coroutines
    import asyncio

    # Initialize the Hypixel class
    hypixel = PyPixel.Hypixel(api_key="API Key")

    async def main():
        # Get the player's UUId
        uuid = await hypixel.get_uuid('Jacktheguy')
        # Get their profiles from the API.
        profiles = await hypixel.get_profiles(uuid)
        # Print their profile's names
        print([str(profile) for profile in profiles]])

    # run the above coroutine
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

Adding Examples
****************
If you wish to add another example, just make a pull request, I really don't mind.