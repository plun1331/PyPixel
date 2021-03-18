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

import asyncio
from time import time


class Cache(object):
    r"""A class used for caching data returned from the api

    :param clear_cache_after: How long data should stay cached for.
    :type clear_cache_after: class:`int`
    """

    def __init__(self, clear_cache_after: int):
        super().__init__()
        self.cached = {}
        self.cachedelay = clear_cache_after

    async def cleanCache(self):
        r"""|coro|
        
        Cleans the cache."""
        for url, info in self.cached.items():
            if info['timestamp'] + self.cachedelay < time():
                del self.cached[url]

    async def getFromCache(self, url: str):
        r"""|coro|
        
        Gets the cached url from the cache.

        :return: The cached response. Can also be `None` if the response is not cached.
        :rtype: Optional[dict]"""
        asyncio.create_task(self.cleanCache())
        if url in self.cached:
            return self.cached[url]['data']
        return None

    async def cache(self, url: str, data: dict):
        r"""|coro|
        
        Caches a response.

        :param url: The URL the request was sent to.
        :type url: str

        :param data: The response as a dict.
        :type data: dict"""
        await asyncio.create_task(self.cleanCache())
        self.cached[url] = {'data': data,
                            'timestamp': time()}
