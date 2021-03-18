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
from .utils import HypixelUtils


class Auction(object):
    def __init__(self, data: dict, cached: bool, hypixel):
        self.cached = cached
        self._hypixel = hypixel
        self.id = data['uuid']
        self.auctioneer = data['auctioneer']
        self.auctioneer_profile = data['profile_id']
        self.auctioneer_coop_members = data['coop']
        self.started = datetime.datetime.fromtimestamp(data['start'])
        self.end = datetime.datetime.fromtimestamp(data['end'])
        self.item = data['item_name']
        self.lore = data['item_lore']
        self.stripped_lore = HypixelUtils.stripFormatting(data['item_lore'])
        self.extra = data['extra']
        self.category = data['category']
        self.tier = data['tier']
        self.starting_bid = data['starting_bid']
        self.nbt_data = HypixelUtils.parseNBT(data['item_bytes'])
        self.claimed = data['claimed']
        self.claimed_bidders = data['claimed_bidders']
        self.highest_bid = data['highest_bid_amount']
        self.bin = data.get('bin', False)
        self.bids = data['bids']

    async def get_auctioneer(self):
        return await self._hypixel.get_player(self.auctioneer)
