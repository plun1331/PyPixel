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

    def __init__(self, *args):
        super().__init__(*args)


class HTTPExeption(PyPixelError):
    r"""Base exception class for when the API returns an http error code.

    :param status_code: The status code returned by the API.
    :type status_code: int

    :param reason: The reason the request failed.
    :type reason: str

    :param url: The url the request was sent to.
    :type url: str

    :param data: The JSON data returned from the request, if any.
    :type data: Optional[dict]"""

    def __init__(self, status_code, reason, url, data):
        self.status_code = status_code
        self.reason = reason
        self.url = url
        self.data = data
        super().__init__(
            "Request to {0.url} returned a {0.status_code} status code: {0.url}".format(self)
        )


class APIError(HTTPExeption):
    r"""Exception that's thrown when the API returns a 500 range status code.

    :param status_code: The status code returned by the API.
    :type status_code: int

    :param reason: The reason the request failed.
    :type reason: str

    :param url: The url the request was sent to.
    :type url: str

    :param data: The JSON data returned from the request, if any.
    :type data: Optional[dict]"""

    def __init__(self, status_code, reason, url, data):
        self.status_code = status_code
        self.reason = reason
        self.url = url
        self.data = data
        super().__init__(
            self.status_code,
            self.reason,
            self.url,
            self.data
        )


class ClientError(HTTPExeption):
    r"""Exception that's thrown when the API returns a 400 range status code.

    :param status_code: The status code returned by the API.
    :type status_code: int

    :param reason: The reason the request failed.
    :type reason: str

    :param url: The url the request was sent to.
    :type url: str

    :param data: The JSON data returned from the request, if any.
    :type data: Optional[dict]"""

    def __init__(self, status_code, reason, url, data):
        self.status_code = status_code
        self.reason = reason
        self.url = url
        self.data = data
        super().__init__(
            self.status_code,
            self.reason,
            self.url,
            self.data
        )


class NotFound(ClientError):
    r"""Exception thats thrown when the API returns a 404 status code.

    :param reason: The reason the request failed.
    :type reason: str

    :param url: The url the request was sent to.
    :type url: str

    :param data: The JSON data returned from the request, if any.
    :type data: Optional[dict]"""

    def __init__(self, reason, url, data):
        self.status_code = 404
        self.reason = reason
        self.url = url
        self.data = data
        super().__init__(
            self.status_code,
            self.reason,
            self.url,
            self.data
        )


class PlayerNotFound(NotFound):
    r"""Exception thats thrown when a player couldn't be found.

    :param reason: The reason the player couldn't be found.
    :type reason: str

    :param url: The url the request was sent to.
    :type url: str

    :param data: The JSON data returned from the request, if any.
    :type data: Optional[dict]"""

    def __init__(self, reason, url, data):
        self.reason = reason
        self.url = url
        self.data = data
        super().__init__(
            self.reason,
            self.url,
            self.data
        )


class GuildNotFound(NotFound):
    r"""Exception thats thrown when a guild couldn't be found.
    
    :param reason: The reason the guild couldn't be found.
    :type reason: str

    :param url: The url the request was sent to.
    :type url: str

    :param data: The JSON data returned from the request, if any.
    :type data: Optional[dict]"""

    def __init__(self, reason, url, data):
        self.reason = reason
        self.url = url
        self.data = data
        super().__init__(
            self.reason,
            self.url,
            self.data
        )


class KeyNotFound(NotFound):
    r"""Exception thats thrown when an API Key couldn't be found.

    :param reason: The reason the key couldn't be found.
    :type reason: str

    :param url: The url the request was sent to.
    :type url: str

    :param data: The JSON data returned from the request, if any.
    :type data: Optional[dict]"""

    def __init__(self, reason, url, data):
        self.reason = reason
        self.url = url
        self.data = data
        super().__init__(
            self.reason,
            self.url,
            self.data
        )
