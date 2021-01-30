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


class PyPixelError(Exception):
    r"""Base exception class for PyPixel."""


class HTTPExeption(PyPixelError):
    r"""Base exception for when the API returns a non 200 status code."""


class APIError(HTTPExeption):
    r"""Exeption that's thrown when the API returns a 500 range status code."""


class ClientError(HTTPExeption):
    r"""Exeption that's thrown when the API returns a 400 range status code."""


class NotFound(ClientError):
    r"""Exception thats thrown when the API returns a 404 status code."""


class PlayerNotFound(NotFound):
    r"""Exception thats thrown when a player couldn't be found.
    
    Parameters
    -----------
    reason: :class:`str`
        The reason the player couldn't be found."""

    def __init__(self, reason):
        self.reason = reason


class GuildNotFound(NotFound):
    r"""Exception thats thrown when a guild couldn't be found.
    
    Parameters
    -----------
    reason: :class:`str`
        The reason the guild couldn't be found."""

    def __init__(self, reason):
        self.reason = reason
