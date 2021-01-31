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
        self.uuid = uuid
        self.last_save = datetime.datetime.fromtimestamp(
            memberdata['last_save'] / 1000) if 'last_save' in memberdata else None
        self.armour = HypixelUtils.parseNBT(memberdata['inv_armor']['data']) if 'inv_armor' in memberdata else None
        self.first_join = datetime.datetime.fromtimestamp(
            memberdata['first_join'] / 1000) if 'first_join' in memberdata else None
        self.first_join_hub = datetime.datetime.fromtimestamp(
            memberdata['first_join_hub'] / 1000) if 'first_join_hub' in memberdata else None
        self.stats = SkyBlockStats(memberdata['stats']) if 'stats' in memberdata else None
        self.objectives = [SkyBlockObjective(objective, memberdata['objectives'][
            objective]) for objective in memberdata['objectives']] if 'objectives' in memberdata else None
        self.tutorials_complete = memberdata['tutorial']
        self.quests = [SkyBlockQuest(quest, memberdata['quests'][
            quest]) for quest in memberdata['quests']] if 'quests' in memberdata else None
        self.purse = memberdata['coin_purse'] if 'coin_purse' in memberdata else None
        self.crafted_minions = memberdata['crafted_generators'] if 'crafted_generators' in memberdata else None
        self.crafted_minion_slots = SkyBlockUtils.getMinionSlots(
            memberdata['crafted_generators']) if 'crafted_generators' in memberdata else None
        self.visited_zones = memberdata['visited_zones'] if 'visited_zones' in memberdata else None
        self.collected_fairy_souls = memberdata[
            'fairy_souls_collected'] if 'fairy_souls_collected' in memberdata else None
        self.fairy_souls = memberdata['fairy_souls']
        self.fairy_soul_exchanges = memberdata['fairy_exchanges'] if 'fairy_exchanges' in memberdata else None
        self.fishing_treasure_caught = memberdata[
            'fishing_treasure_caught'] if 'fishing_treasure_caught' in memberdata else None
        self.deaths = memberdata['deaths_count'] if 'deaths_count' in memberdata else None
        self.island_types = memberdata[
            'achievement_spawned_island_types'] if 'achievement_spawned_island_types' in memberdata else None
        self.slayers = [SkyBlockSlayer(slayer, memberdata['slayer_bosses'][
            slayer]) for slayer in memberdata['slayer_bosses']] if 'slayer_bosses' in memberdata else None
        self.pets = [SkyBlockPet(pet) for pet in memberdata['pets']] if 'pets' in memberdata else None
        self.dungeons = memberdata[
            'dungeons'][
            'dungeon_types'] if 'dungeons' in memberdata and 'dungeon_types' in memberdata['dungeons'] else None
        self.dungeon_classes = memberdata[
            'dungeons'][
            'player_classes'] if 'dungeons' in memberdata and 'player_classes' in memberdata['dungeons'] else None
        self.dungeon_journals = memberdata[
            'dungeons'][
            'dungeon_journal'] if 'dungeons' in memberdata and 'dungeon_journal' in memberdata['dungeons'] else None
        self.dungeon_selected_class = memberdata[
            'dungeons'][
            'selected_dungeon_class'] if 'dungeons' in memberdata and 'selected_dungeon_class' in memberdata[
            'dungeons'] else None
        self.combat_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_combat']),
                             "xp": memberdata['experience_skill_combat']
                             } if 'experience_skill_combat' in memberdata else None
        self.mining_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_mining']),
                             "xp": memberdata['experience_skill_mining']
                             } if 'experience_skill_mining' in memberdata else None
        self.alchemy_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_alchemy']),
                              "xp": memberdata['experience_skill_alchemy']
                              } if 'experience_skill_alchemy' in memberdata else None
        self.farming_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_farming']),
                              "xp": memberdata['experience_skill_farming']
                              } if 'experience_skill_farming' in memberdata else None
        self.taming_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_taming']),
                             "xp": memberdata['experience_skill_taming']
                             } if 'experience_skill_taming' in memberdata else None
        self.enchanting_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_enchanting']),
                                 "xp": memberdata['experience_skill_enchanting']
                                 } if 'experience_skill_enchanting' in memberdata else None
        self.fishing_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_fishing']),
                              "xp": memberdata['experience_skill_fishing']
                              } if 'experience_skill_fishing' in memberdata else None
        self.foraging_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_foraging']),
                               "xp": memberdata['experience_skill_foraging']
                               } if 'experience_skill_foraging' in memberdata else None
        self.carpentry_skill = {"level": SkyBlockUtils.getSkillLevel(memberdata['experience_skill_carpentry']),
                                "xp": memberdata['experience_skill_carpentry']
                                } if 'experience_skill_carpentry' in memberdata else None
        self.runecrafting_skill = {"level": SkyBlockUtils.getSkillLevel(
            memberdata['experience_skill_runecrafting']),
            "xp": memberdata['experience_skill_runecrafting']
        } if 'experience_skill_runecrafting' in memberdata else None
        skills = [self.combat_skill,
                  self.mining_skill,
                  self.alchemy_skill,
                  self.farming_skill,
                  self.taming_skill,
                  self.enchanting_skill,
                  self.fishing_skill,
                  self.foraging_skill]
        skills = [skill['level'] for skill in skills if skill is not None]
        self.skill_average = sum(skills) / len(skills)
        self.fishing_bag = HypixelUtils.parseNBT(memberdata[
                                                     'fishing_bag']['data']) if 'fishing_bag' in memberdata else None
        self.equipped_wardrobe_slot = memberdata[
            'wardrobe_equipped_slot'] if 'wardrobe_equipped_slot' in memberdata else None
        self.combat_collection = SkyBlockUtils.combatCollection(memberdata) if 'collection' in memberdata else None
        self.mining_collection = SkyBlockUtils.miningCollection(memberdata) if 'collection' in memberdata else None
        self.fishing_collection = SkyBlockUtils.fishingCollection(memberdata) if 'collection' in memberdata else None
        self.farming_collection = SkyBlockUtils.farmingCollection(memberdata) if 'collection' in memberdata else None
        self.foraging_collection = SkyBlockUtils.foragingCollection(memberdata) if 'collection' in memberdata else None
        self.quiver = HypixelUtils.parseNBT(memberdata['quiver']['data']) if 'quiver' in memberdata else None
        self.ender_chest = HypixelUtils.parseNBT(memberdata[
                                                     'ender_chest_contents'][
                                                     'data']) if 'ender_chest_contents' in memberdata else None
        self.wardrobe = HypixelUtils.parseNBT(memberdata[
                                                  'wardrobe_contents'][
                                                  'data']) if 'wardrobe_contents' in memberdata else None
        self.potion_bag = HypixelUtils.parseNBT(memberdata[
                                                    'potion_bag']['data']) if 'potion_bag' in memberdata else None
        self.personal_vault = HypixelUtils.parseNBT(memberdata[
                                                        'personal_vault_contents'][
                                                        'data']
                                                    ) if 'personal_vault_contents' in memberdata else None
        self.inventory = HypixelUtils.parseNBT(memberdata[
                                                   'inv_contents'][
                                                   'data']) if 'inv_contents' in memberdata else None
        self.talismans = HypixelUtils.parseNBT(memberdata[
                                                   'talisman_bag'][
                                                   'data']) if 'talisman_bag' in memberdata else None
        self.candy_inventory = HypixelUtils.parseNBT(memberdata[
                                                         'candy_inventory_contents'][
                                                         'data']) if 'candy_inventory_contents' in memberdata else None

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
