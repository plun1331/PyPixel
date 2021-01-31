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

from .utils import SkyBlockUtils, HypixelUtils
import datetime
from contextlib import suppress
from .SkyBlockStats import SkyBlockStats, SkyBlockObjective, SkyBlockQuest, SkyBlockSlayer, SkyBlockPet


class ProfileMember(object):
    r"""Represents a member in a SkyBlock profile.

    :param uuid: The member's UUID.
    :type uuid: str

    :param memberdata: The member's data in the profile.
    :type memberdata: dict

    :param hypixel: The Hypixel class used to get the profile.
    :type hypixel: PyPixel.Hypixel.Hypixel"""

    def __init__(self, uuid, memberdata, hypixel):
        self._hypixel = hypixel
        with suppress(KeyError):
            self.uuid = uuid
        with suppress(KeyError):
            self.last_save = datetime.datetime.fromtimestamp(memberdata['last_save'] / 1000)
        with suppress(KeyError):
            self.armour = HypixelUtils.parseNBT(memberdata['inv_armor']['data'])
        with suppress(KeyError):
            self.first_join = datetime.datetime.fromtimestamp(memberdata['first_join'] / 1000)
        with suppress(KeyError):
            self.first_join_hub = datetime.datetime.fromtimestamp(memberdata['first_join_hub'] / 1000)
        with suppress(KeyError):
            self.stats = SkyBlockStats(memberdata['stats'])
        with suppress(KeyError):
            self.objectives = [SkyBlockObjective(objective, memberdata['objectives'][
                objective]) for objective in memberdata['objectives']]
        with suppress(KeyError):
            self.tutorials_complete = memberdata['tutorial']
        with suppress(KeyError):
            self.quests = [SkyBlockQuest(quest, memberdata['quests'][
                quest]) for quest in memberdata['quests']]
        with suppress(KeyError):
            self.purse = memberdata['coin_purse']
        with suppress(KeyError):
            self.crafted_minions = memberdata['crafted_generators']
        with suppress(KeyError):
            self.crafted_minion_slots = SkyBlockUtils.getMinionSlots(memberdata['crafted_generators'])
        with suppress(KeyError):
            self.visited_zones = memberdata['visited_zones']
        with suppress(KeyError):
            self.collected_fairy_souls = memberdata['fairy_sould_collected']
        with suppress(KeyError):
            self.fairy_souls = memberdata['fairy_souls']
        with suppress(KeyError):
            self.fairy_soul_exchanges = memberdata['fairy_exchanges']
        with suppress(KeyError):
            self.fishing_treasure_caught = memberdata['fishing_treasure_caught']
        with suppress(KeyError):
            self.deaths = memberdata['deaths_count']
        with suppress(KeyError):
            self.island_types = memberdata['achievement_spawned_island_types']
        with suppress(KeyError):
            self.slayers = [SkyBlockSlayer(slayer, memberdata['slayer_bosses'][
                slayer]) for slayer in memberdata['slayer_bosses']]
        with suppress(KeyError):
            self.pets = [SkyBlockPet(pet) for pet in memberdata['pets']]
        with suppress(KeyError):
            self.dungeons = memberdata['dungeons']['dungeon_types']
        with suppress(KeyError):
            self.dungeon_classes = memberdata['dungeons']['player_classes']
        with suppress(KeyError):
            self.dungeon_journals = memberdata['dungeons']['dungeon_journal']
        with suppress(KeyError):
            self.dungeon_selected_class = memberdata['dungeons']['selected_dungeon_class']
        with suppress(KeyError):
            self.combat_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_combat']),
                                 "xp": memberdata['experience_skill_combat']}
        with suppress(KeyError):
            self.mining_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_mining']),
                                 "xp": memberdata['experience_skill_mining']}
        with suppress(KeyError):
            self.alchemy_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_alchemy']),
                                  "xp": memberdata['experience_skill_alchemy']}
        with suppress(KeyError):
            self.farming_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_farming']),
                                  "xp": memberdata['experience_skill_farming']}
        with suppress(KeyError):
            self.taming_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_taming']),
                                 "xp": memberdata['experience_skill_taming']}
        with suppress(KeyError):
            self.enchanting_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_enchanting']),
                                     "xp": memberdata['experience_skill_enchanting']}
        with suppress(KeyError):
            self.fishing_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_fishing']),
                                  "xp": memberdata['experience_skill_fishing']}
        with suppress(KeyError):
            self.foraging_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_foraging']),
                                   "xp": memberdata['experience_skill_foraging']}
        with suppress(KeyError):
            self.carpentry_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_carpentry']),
                                    "xp": memberdata['experience_skill_carpentry']}
        with suppress(KeyError):
            self.runecrafting_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_runecrafting']),
                                       "xp": memberdata['experience_skill_runecrafting']}
        with suppress(KeyError):
            skills = [SkyBlockUtils.getSkillLevel(memberdata['experience_skill_combat']),
                      SkyBlockUtils.getSkillLevel(memberdata['experience_skill_mining']),
                      SkyBlockUtils.getSkillLevel(memberdata['experience_skill_alchemy']),
                      SkyBlockUtils.getSkillLevel(memberdata['experience_skill_farming']),
                      SkyBlockUtils.getSkillLevel(memberdata['experience_skill_taming']),
                      SkyBlockUtils.getSkillLevel(memberdata['experience_skill_enchanting']),
                      SkyBlockUtils.getSkillLevel(memberdata['experience_skill_fishing']),
                      SkyBlockUtils.getSkillLevel(memberdata['experience_skill_foraging'])]
            self.skill_average = sum(skills) / len(skills)
        with suppress(KeyError):
            self.fishing_bag = HypixelUtils.parseNBT(memberdata['fishing_bag']['data'])
        with suppress(KeyError):
            self.equipped_wardrobe_slot = memberdata['wardrobe_equipped_slot']
        with suppress(KeyError):
            self.combat_collection = SkyBlockUtils.combatCollection(memberdata)
        with suppress(KeyError):
            self.mining_collection = SkyBlockUtils.miningCollection(memberdata)
        with suppress(KeyError):
            self.fishing_collection = SkyBlockUtils.fishingCollection(memberdata)
        with suppress(KeyError):
            self.farming_collection = SkyBlockUtils.farmingCollection(memberdata)
        with suppress(KeyError):
            self.foraging_collection = SkyBlockUtils.foragingCollection(memberdata)
        with suppress(KeyError):
            self.quiver = HypixelUtils.parseNBT(memberdata['quiver']['data'])
        with suppress(KeyError):
            self.ender_chest = HypixelUtils.parseNBT(memberdata['ender_chest_contents']['data'])
        with suppress(KeyError):
            self.wardrobe = HypixelUtils.parseNBT(memberdata['wardrobe_contents']['data'])
        with suppress(KeyError):
            self.potion_bag = HypixelUtils.parseNBT(memberdata['potion_bag']['data'])
        with suppress(KeyError):
            self.personal_vault = HypixelUtils.parseNBT(memberdata['personal_vault_contents']['data'])
        with suppress(KeyError):
            self.inventory = HypixelUtils.parseNBT(memberdata['inv_contents']['data'])
        with suppress(KeyError):
            self.talismans = HypixelUtils.parseNBT(memberdata['talisman_bag']['data'])
        with suppress(KeyError):
            self.candy_inventory = HypixelUtils.parseNBT(memberdata['candy_inventory_contents']['data'])

    def __eq__(self, other):
        try:
            if other.uuid == self.uuid:
                return True
        except AttributeError:
            pass
        return False

    async def get_player(self):
        r"""|coro|

        Gets the member's player object.

        :raises PyPixel.Errors.PlayerNotFound: The player couldn't be found for some reason.

        :return: The player from the API.
        :rtype: PyPixel.Player.Player"""

        return self._hypixel.get_player(self.uuid)
