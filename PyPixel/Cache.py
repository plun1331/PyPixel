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

from threading import Thread
import asyncio


class Cache(Thread):
    r"""A class used for caching data returned from the api

        
    Parameters
    -----------
    clear_cache_after: :class:`int`
        How often the cache should be cleared in seconds.
    """

    def __init__(self, clear_cache_after: int):
        super().__init__()
        self.cached = {}
        self.cachedelay = clear_cache_after
        self.setDaemon(True)
        self.start()

    def run(self):
        r"""Runs a loop that refreshes the cache every so often.

        This is not meant to be called manually."""
        loop = asyncio.new_event_loop()
        while True:
            loop.run_until_complete(asyncio.sleep(self.cachedelay))
            loop.run_until_complete(self.clearCache())

    async def clearCache(self):
        r"""|coro|
        
        Clears the cache."""
        self.cached = {}

    async def getFromCache(self, url: str):
        r"""|coro|
        
        Gets the cached url from the cache.
        
        Returns
        -------
        :class:`Optional[dict]`
            The cached response. Can also be `None` if the response is not cached."""
        if url in self.cached:
            return self.cached[url]
        return None

    async def cache(self, url: str, data: dict):
        r"""|coro|
        
        Caches a response."""
        self.cached[url] = data
