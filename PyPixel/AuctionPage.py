# ################################################################################
#  MIT License                                                                   #
#                                                                                #
#  Copyright (c) 2021 plun1331                                                   #
#                                                                                #
#  Permission is hereby granted, free of charge, to any person obtaining a copy  #
#  of this software and associated documentation files (the "Software"), to deal #
#  in the Software without restriction, including without limitation the rights  #
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell     #
#  copies of the Software, and to permit persons to whom the Software is         #
#  furnished to do so, subject to the following conditions:                      #
#                                                                                #
#  The above copyright notice and this permission notice shall be included in all#
#  copies or substantial portions of the Software.                               #
#                                                                                #
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR    #
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,      #
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE   #
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER        #
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, #
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE #
#  SOFTWARE.                                                                     #
# ################################################################################

import datetime

from .Auction import Auction


class AuctionPage(object):
    r"""Represents a page of Skyblock auctions from the Hypixel API.

    :param data: The raw data from the API.
    :type data: dict

    :param cached: Whether or not the data was retrieved from the cache.
    :type cached: bool

    :param hypixel: The Hypixel class used to make the request.
    :type hypixel: PyPixel.Hypixel.Hypixel"""
    def __init__(self, data: dict, cached: bool, hypixel):
        self.raw = data
        self.page = data['page']
        self.total_pages = data['totalPages']
        self.total_auctions = data['totalAuctions']
        self.last_updated = datetime.datetime.fromtimestamp(data['lastUpdated']/1000)
        self.auctions = [Auction(auction, cached, hypixel) for auction in data['auctions']]
