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

import datetime
from .utils import SkyBlockUtils

types = {'zombie': SkyBlockUtils.zombieSlayer,
         'spider': SkyBlockUtils.spiderSlayer,
         'wolf': SkyBlockUtils.wolfSlayer}


class SkyBlockStats(object):
    r"""Represents a player's SkyBlock Statistics.

    :param stats: The player's stats from their memberdata retrieved from the API.
    :type stats: dict"""
    def __init__(self, stats: dict):
        self.top_crit_damage = stats['highest_crit_damage'] if 'highest_crit_damage' in stats else None
        self.kills = int(stats['kills']) if 'kills' in stats else None
        self.zombie_kills = int(stats['kills_zombie']) if 'kills_zombie' in stats else None
        self.bids = int(stats['auctions_bids']) if 'auctions_bids' in stats else None
        self.highest_bid = stats['auctions_highest_bid'] if 'auctions_highest_bid' in stats else None
        self.zombie_villager_kills = int(stats['kills_zombie_villager']) if 'kills_zombie_villager' in stats else None
        self.skeleton_kills = int(stats['kills_skeleton']) if 'kills_skeleton' in stats else None
        self.spider_kills = int(stats['kills_spider']) if 'kills_spider' in stats else None
        self.enderman_kills = int(stats['kills_enderman']) if 'kills_enderman' in stats else None
        self.deaths = int(stats['deaths']) if 'deaths' in stats else None
        self.zombie_deaths = int(stats['deaths_zombie']) if 'deaths_zombie' in stats else None
        self.void_deaths = int(stats['deaths']) if 'deaths' in stats else None
        self.skeleton_deaths = int(stats['deaths_skeleton']) if 'deaths_skeleton' in stats else None
        self.fire_deaths = int(stats['deaths_fire']) if 'deaths_fire' in stats else None
        self.auctions_won = int(stats['auctions_won']) if 'auctions_won' in stats else None
        self.uncommon_auctions_bought = int(
            stats['auctions_bought_uncommon']) if 'auctions_bought_uncommon' in stats else None
        self.auctions_gold_spent = int(stats['auctions_gold_spent']) if 'auctions_gold_spent' in stats else None
        self.auctions_created = int(stats['auctions_created']) if 'auctions_created' in stats else None
        self.auction_fees_spent = int(stats['auctions_fees']) if 'auctions_fees' in stats else None
        self.player_deaths = int(stats['deaths_player']) if 'deaths_player' in stats else None
        self.auctions_completed = int(stats['auctions_completed']) if 'auctions_completed' in stats else None
        self.uncommon_auctions_sold = int(
            stats['auctions_sold_uncommon']) if 'auctions_sold_uncommon' in stats else None
        self.auction_gold_earned = int(stats['auctions_gold_earned']) if 'auctions_gold_earned' in stats else None
        self.invisible_creeper_kills = int(
            stats['kills_invisible_creeper']) if 'kills_invisible_creeper' in stats else None
        self.emerald_slime_kills = int(stats['kills_emerald_slime']) if 'kills_emerald_slime' in stats else None
        self.diamond_zombie_kills = int(stats['kills_diamond_zombie']) if 'kills_diamond_zombie' in stats else None
        self.diamond_skeleton_deaths = int(
            stats['deaths_diamond_skeleton']) if 'deaths_diamond_skeleton' in stats else None
        self.diamond_zombie_deaths = int(stats['deaths_diamond_zombie']) if 'deaths_diamond_zombie' in stats else None
        self.diamond_skeleton_kills = int(
            stats['kills_diamond_skeleton']) if 'kills_diamond_skeleton' in stats else None
        self.lapis_zombie_kills = int(stats['kills_lapis_zombie']) if 'kills_lapis_zombie' in stats else None
        self.emerald_slime_deaths = int(stats['deaths_emerald_slime']) if 'deaths_emerald_slime' in stats else None
        self.redstone_pigman_kills = int(stats['kills_redstone_pigman']) if 'kills_redstone_pigman' in stats else None
        self.redstone_pigman_deaths = int(
            stats['deaths_redstone_pigman']) if 'deaths_redstone_pigman' in stats else None
        self.splitter_spider_silverfish_kills = int(
            stats['kills_splitter_spider_silverfish']) if 'kills_splitter_spider_silverfish' in stats else None
        self.jockey_shot_silverfish_kills = int(
            stats['kills_jockey_shot_silverfish']) if 'kills_jockey_shot_silverfish' in stats else None
        self.wither_skeleton_kills = int(stats['kills_wither_skeleton']) if 'kills_wither_skeleton' in stats else None
        self.magma_cube_kills = int(stats['kills_magma_cube']) if 'kills_magma_cube' in stats else None
        self.magma_cube_fireball_kills = int(
            stats['kills_fireball_magma_cube']) if 'kills_fireball_magma_cube' in stats else None
        self.cow_kills = int(stats['kills_cow']) if 'kills_cow' in stats else None
        self.pig_kills = int(stats['kills_pig']) if 'kills_pig' in stats else None
        self.items_fished = int(stats['items_fished']) if 'items_fished' in stats else None
        self.normal_items_fished = int(stats['items_fished_normal']) if 'items_fished_normal' in stats else None
        self.treasure_items_fished = int(stats['items_fished_treasure']) if 'items_fished_treasure' in stats else None
        self.common_auctions_bought = int(
            stats['auctions_bought_common']) if 'auctions_bought_common' in stats else None
        self.witch_kills = int(stats['kills_witch']) if 'kills_witch' in stats else None
        self.spider_deaths = int(stats['deaths_spider']) if 'deaths_spider' in stats else None
        self.epic_auctions_bought = int(stats['auctions_bought_epic']) if 'auctions_bought_epic' in stats else None
        self.magma_cube_fireball_deaths = int(
            stats['deaths_fireball_magma_cube']) if 'deaths_fireball_magma_cube' in stats else None
        self.weaver_spider_kills = int(stats['kills_weaver_spider']) if 'kills_weaver_spider' in stats else None
        self.splitter_spider_kills = int(stats['kills_splitter_spider']) if 'kills_splitter_spider' in stats else None
        self.jockey_skeleton_kills = int(stats['kills_jockey_skeleton']) if 'kills_jockey_skeleton' in stats else None
        self.spider_jockey_kills = int(stats['kills_spider_jockey']) if 'kills_spider_jockey' in stats else None
        self.dasher_spider_kills = int(stats['kills_dasher_spider']) if 'kills_dasher_spider' in stats else None
        self.spider_jockey_deaths = int(stats['deaths_spider_jockey']) if 'deaths_spider_jockey' in stats else None
        self.dasher_spider_deaths = int(stats['deaths_dasher_spider']) if 'deaths_dasher_spider' in stats else None
        self.jockey_shot_silverfish_deaths = int(
            stats['deaths_jockey_shot_silverfish']) if 'deaths_jockey_shot_silverfish' in stats else None
        self.splitter_spider_deaths = int(
            stats['deaths_splitter_spider']) if 'deaths_splitter_spider' in stats else None
        self.common_auctions_sold = int(stats['auctions_sold_common']) if 'auctions_sold_common' in stats else None
        self.no_bid_auctions = int(stats['auctions_no_bids']) if 'auctions_no_bids' in stats else None
        self.ghast_kills = int(stats['kills_ghast']) if 'kills_ghast' in stats else None
        self.rare_auctions_sold = int(stats['auctions_sold_rare']) if 'auctions_sold_rare' in stats else None
        self.epic_auctions_sold = int(stats['auctions_sold_epic']) if 'auctions_sold_epic' in stats else None
        self.magma_cube_boss_deaths = int(
            stats['deaths_magma_cube_boss']) if 'deaths_magma_cube_boss' in stats else None
        self.blaze_kills = int(stats['kills_blaze']) if 'kills_blaze' in stats else None
        self.wither_skeleton_deaths = int(
            stats['deaths_wither_skeleton']) if 'deaths_wither_skeleton' in stats else None
        self.magma_cube_deaths = int(stats['deaths_magma_cube']) if 'deaths_magma_cube' in stats else None
        self.respawning_skeleton_kills = int(
            stats['kills_respawning_skeleton']) if 'kills_respawning_skeleton' in stats else None
        self.fall_deaths = int(stats['deaths_fall']) if 'deaths_fall' in stats else None
        self.rare_auctions_bought = int(stats['auctions_bought_rare']) if 'auctions_bought_rare' in stats else None
        self.rabbit_kills = int(stats['kills_rabbit']) if 'kills_rabbit' in stats else None
        self.sheep_kills = int(stats['kills_sheep']) if 'kills_sheep' in stats else None
        self.pigman_kills = int(stats['kills_pigman']) if 'kills_pigman' in stats else None
        self.player_kills = int(stats['kills_player']) if 'kills_player' in stats else None
        self.ruin_wolf_kills = int(stats['kills_ruin_wolf']) if 'kills_ruin_wolf' in stats else None
        self.night_respawning_skeleton_kills = int(
            stats['kills_night_respawining_skeleton']) if 'kills_night_respawining_skeleton' in stats else None
        self.legendary_auctions_bought = int(
            stats['auctions_bought_legendary']) if 'auctions_bought_legendary' in stats else None
        self.chicken_kills = int(stats['kills_chicken']) if 'kills_chicken' in stats else None
        self.respawning_skeleton_deaths = int(
            stats['deaths_respawning_skeleton']) if 'deaths_respawning_skeleton' in stats else None
        self.ruin_wolf_deaths = int(stats['deaths_ruin_wolf']) if 'deaths_ruin_wolf' in stats else None
        self.unburried_zombie_deaths = int(
            stats['deaths_unburied_zombie']) if 'deaths_unburied_zombie' in stats else None
        self.unburried_zombie_kills = int(
            stats['kills_unburried_zombie']) if 'kills_unburried_zombie' in stats else None
        self.enderman_deaths = int(stats['deaths_enderman']) if 'deaths_enderman' in stats else None
        self.endermite_deaths = int(stats['deaths_endermite']) if 'deaths_endermite' in stats else None
        self.endermite_kills = int(stats['kills_endermite']) if 'kills_endermite' in stats else None
        self.zealot_enderman_deaths = int(
            stats['deaths_zealot_enderman']) if 'deaths_zealot_enderman' in stats else None
        self.wise_dragon_deaths = int(stats['deaths_wise_dragon']) if 'deaths_wise_dragon' in stats else None
        self.watcher_deaths = int(stats['deaths_watcher']) if 'deaths_watcher' in stats else None
        self.watcher_kills = int(stats['kills_watcher']) if 'kills_watcher' in stats else None
        self.random_slime_kills = int(stats['kills_random_slime']) if 'kills_random_slime' in stats else None
        self.voracious_spider_kills = int(
            stats['kills_voracious_spider']) if 'kills_voracious_spider' in stats else None
        self.wolf_deaths = int(stats['deaths_wolf']) if 'deaths_wolf' in stats else None
        self.old_wolf_kills = int(stats['kills_old_wolf']) if 'kills_old_wolf' in stats else None
        self.olf_wolf_deaths = int(stats['deaths_old_wolf']) if 'deaths_old_wolf' in stats else None
        self.zealot_enderman_kills = int(stats['kills_zealot_enderman']) if 'kills_zealot_enderman' in stats else None
        self.obsidian_wither_kills = int(stats['kills_obsidian_wither']) if 'kills_obsidian_wither' in stats else None
        self.howling_spirit_kills = int(stats['kills_howling_spirit']) if 'kills_howling_spirit' in stats else None
        self.howling_spirit_deaths = int(stats['deaths_howling_spirit']) if 'deaths_howling_spirit' in stats else None
        self.unknown_deaths = int(stats['deaths_unknown']) if 'deaths_unknown' in stats else None
        self.sea_walker_kills = int(stats['kills_sea_walker']) if 'kills_sea_walker' in stats else None
        self.pond_squid_kills = int(stats['kills_pond_squid']) if 'kills_pond_squid' in stats else None
        self.sea_guardian_kills = int(stats['deaths_sea_guardian']) if 'deaths_sea_guardian' in stats else None
        self.sea_archer_kills = int(stats['kills_sea_archer']) if 'kills_sea_archer' in stats else None
        self.young_dragon_deaths = int(stats['deaths_young_dragon']) if 'deaths_young_dragon' in stats else None
        self.zombie_deep_kills = int(stats['kills_zombie_deep']) if 'kills_zombie_deep' in stats else None
        self.gifts_given = int(stats['gifts_given']) if 'gifts_given' in stats else None
        self.gifts_recieved = int(stats['gifts_recieved']) if 'gifts_recieved' in stats else None
        self.frozen_steve_deaths = int(stats['deaths_frozen_steve']) if 'deaths_frozen_steve' in stats else None
        self.brood_mother_spider_kills = int(
            stats['kills_brood_mother_spider']) if 'kills_brood_mother_spider' in stats else None
        self.brood_mother_cave_spider_kills = int(
            stats['kills_brood_mother_cave_spider']) if 'kills_brood_mother_cave_spider' in stats else None
        self.foraging_race_best_time = int(
            stats['foraging_race_best_time']) if 'foraging_race_best_time' in stats else None
        self.legendary_auctions_sold = int(
            stats['auctions_sold_legendary']) if 'auctions_sold_legendary' in stats else None
        self.special_auctions_sold = int(stats['auctions_sold_special']) if 'auctions_sold_special' in stats else None
        self.generator_magma_cube_kills = int(
            stats['kills_generator_magma_cube']) if 'kills_generator_magma_cube' in stats else None
        self.bat_pinata_kills = int(stats['kills_bat_pinata']) if 'kills_bat_pinata' in stats else None
        self.special_auctions_bought = int(
            stats['auctions_bought_special']) if 'auctions_bought_special' in stats else None
        self.horseman_zombie_kills = int(stats['kills_horseman_zombie']) if 'kills_horseman_zombie' in stats else None
        self.old_dragon_deaths = int(stats['deaths_old_dragon']) if 'deaths_old_dragon' in stats else None
        self.liquid_hot_magma_deaths = int(
            stats['deaths_liquid_hot_magma']) if 'deaths_liquid_hot_magma' in stats else None
        self.liquid_hot_magma_kills = int(
            stats['kills_liquid_hot_magma']) if 'kills_liquid_hot_magma' in stats else None
        self.most_winter_snowballs_hit = int(
            stats['most_winter_snowballs_hit']) if 'most_winter_snowballs_hit' in stats else None
        self.most_winter_damage_dealt = int(
            stats['most_winter_damage_dealt']) if 'most_winter_damage_dealt' in stats else None
        self.most_winter_magma_damage_dealt = int(
            stats['most_winter_magma_damage_dealt']) if 'most_winter_magma_damage_dealt' in stats else None
        self.ender_crystals_destroyed = int(
            stats['ender_crystals_destroyed']) if 'ender_crystals_destroyed' in stats else None
        self.most_winter_cannonballs_hit = int(
            stats['most_winter_cannonballs_hit']) if 'most_winter_cannonballs_hit' in stats else None
        self.slime_kills = int(stats['kills_slime']) if 'kills_slime' in stats else None
        self.unstable_dragon_deaths = int(
            stats['deaths_unstable_dragon']) if 'deaths_unstable_dragon' in stats else None
        self.superior_dragon_deaths = int(
            stats['deaths_superior_dragon']) if 'deaths_superior_dragon' in stats else None
        self.forest_island_bat_kills = int(
            stats['kills_forest_island_bat']) if 'kills_forest_island_bat' in stats else None
        self.strong_dragon_deaths = int(stats['deaths_strong_dragon']) if 'deaths_strong_dragon' in stats else None
        self.pet_milestone_ores_mined = int(
            stats['pet_milestone_ores_mined']) if 'pet_milestone_ores_mined' in stats else None
        self.pet_milestone_sea_creatures_killed = int(
            stats['pet_milestone_sea_creatures_killed']) if 'pet_milestone_sea_creatures_killed' in stats else None
        self.chicken_deep_kills = int(stats['kills_chicken_deep']) if 'kills_chicken_deep' in stats else None
        self.corrupted_protector_deaths = int(
            stats['deaths_corrupted_protector']) if 'deaths_corrupted_protector' in stats else None
        self.pack_spirit_kills = int(stats['kills_pack_spirit']) if 'kills_pack_spirit' in stats else None
        self.soul_of_the_alpha_kills = int(
            stats['kills_soul_of_the_alpha']) if 'kills_soul_of_the_alpha' in stats else None
        self.frosty_the_snowman_kills = int(
            stats['kills_frosty_the_snowman']) if 'kills_frosty_the_snowman' in stats else None
        self.frozen_steve_kills = int(stats['kills_frozen_steve']) if 'kills_frozen_steve' in stats else None
        self.catfish_kills = int(stats['kills_catfish']) if 'kills_catfish' in stats else None
        self.dungeon_hub_crystal_core_anything_no_return_best_time = stats[
            'dungeon_hub_crystal_core_anything_no_return_best_time'
        ] if 'dungeon_hub_crystal_core_anything_no_return_best_time' in stats else None
        self.dungeon_hub_giant_mushroom_anything_no_return_best_time = stats[
            'dungeon_hub_giant_mushroom_anything_no_return_best_time'
        ] if 'dungeon_hub_giant_mushroom_anything_no_return_best_time' in stats else None
        self.dungeon_hub_giant_mushroom_no_pearls_no_return_best_time = stats[
            'dungeon_hub_giant_mushroom_no_pearls_no_return_best_time'
        ] if 'dungeon_hub_giant_mushroom_no_pearls_no_return_best_time' in stats else None
        self.dungeon_hub_precursor_ruins_anything_no_return_best_time = stats[
            'dungeon_hub_precursor_ruins_anything_no_return_best_time'
        ] if 'dungeon_hub_precursor_ruins_anything_no_return_best_time' in stats else None
        self.dungeon_hub_precursor_ruins_nothing_no_return_best_time = stats[
            'dungeon_hub_precursor_ruins_nothing_no_return_best_time'
        ] if 'dungeon_hub_precursor_ruins_nothing_no_return_best_time' in stats else None
        self.dungeon_hub_precursor_ruins_no_pearls_no_return_best_time = stats[
            'dungeon_hub_precursor_ruins_no_pearls_no_return_best_time'
        ] if 'dungeon_hub_precursor_ruins_no_pearls_no_return_best_time' in stats else None
        self.crypt_lurker_kills = int(stats['kills_crypt_lurker']) if 'kills_crypt_lurker' in stats else None
        self.dungeon_respawning_skeleton_kills = int(
            stats['kills_dungeon_respawning_skeleton']) if 'kills_dungeon_respawning_skeleton' in stats else None
        self.scared_skeleton_kills = int(stats['kills_scared_skeleton']) if 'kills_scared_skeleton' in stats else None
        self.skeleton_grunt_kills = int(stats['kills_skeleton_grunt']) if 'kills_skeleton_grunt' in stats else None
        self.crypt_dreadlord_kills = int(stats['kills_scared_skeleton']) if 'kills_scared_skeleton' in stats else None
        self.crypt_souleater_kills = int(stats['kills_crypt_souleater']) if 'kills_crypt_souleater' in stats else None
        self.crypt_tank_zombie_kills = int(
            stats['kills_crypt_tank_zombie']) if 'kills_crypt_tank_zombie' in stats else None
        self.diamond_guy_kills = int(stats['kills_diamond_guy']) if 'kills_diamond_guy' in stats else None
        self.zombie_grunt_kills = int(stats['kills_zombie_grunt']) if 'kills_zombie_grunt' in stats else None
        self.crypt_lurker_deaths = int(stats['deaths_crypt_lurker']) if 'deaths_crypt_lurker' in stats else None
        self.lost_adventurer_deaths = int(
            stats['deaths_lost_adventurer']) if 'deaths_lost_adventurer' in stats else None
        self.watcher_summon_undead_kills = int(
            stats['kills_watcher_summon_undead']) if 'kills_watcher_summon_undead' in stats else None
        self.skeleton_soldier_kills = int(
            stats['kills_skeleton_soldier']) if 'kills_skeleton_soldier' in stats else None
        self.diamond_guy_deaths = int(stats['deaths_diamond_guy']) if 'deaths_diamond_guy' in stats else None
        self.watcher_summon_undead_deaths = int(
            stats['deaths_watcher_summon_undead']) if 'deaths_watcher_summon_undead' in stats else None
        self.bonzo_summon_undead_kills = int(
            stats['kills_bonzo_summon_undead']) if 'kills_bonzo_summon_undead' in stats else None
        self.lost_adventurer_kills = int(stats['kills_lost_adventurer']) if 'kills_lost_adventurer' in stats else None
        self.skeleton_master_kills = int(stats['kills_skeleton_master']) if 'kills_skeleton_master' in stats else None
        self.sniper_skeleton_kills = int(stats['kills_sniper_skeleton']) if 'kills_sniper_skeleton' in stats else None
        self.skeleton_soldier_deaths = int(
            stats['deaths_skeleton_soldier']) if 'deaths_skeleton_soldier' in stats else None
        self.trap_deaths = int(stats['deaths_trap']) if 'deaths_trap' in stats else None
        self.crypt_undead_kills = int(stats['kills_crypt_undead']) if 'kills_crypt_undead' in stats else None
        self.skeleton_grunt_deaths = int(stats['deaths_skeleton_grunt']) if 'deaths_skeleton_grunt' in stats else None
        self.scarf_warrior_deaths = int(stats['deaths_scarf_warrior']) if 'deaths_scarf_warrior' in stats else None
        self.skeleton_master_deaths = int(
            stats['deaths_skeleton_master']) if 'deaths_skeleton_master' in stats else None
        self.blaze_higher_or_lower_kills = int(
            stats['kills_blaze_higher_or_lower']) if 'kills_blaze_higher_or_lower' in stats else None
        self.dungeon_respawning_skeleton_deaths = int(
            stats['deaths_dungeon_respawning_skeleton']) if 'deaths_dungeon_respawning_skeleton' in stats else None
        self.scarf_deaths = int(stats['deaths_scarf']) if 'deaths_scarf' in stats else None
        self.bonzo_summon_undead_deaths = int(
            stats['deaths_bonzo_summon_undead']) if 'deaths_bonzo_summon_undead' in stats else None
        self.bonzo_deaths = int(stats['deaths_bonzo']) if 'deaths_bonzo' in stats else None
        self.lonely_spider_kills = int(stats['kills_lonely_spider']) if 'kills_lonely_spider' in stats else None
        self.parasite_kills = int(stats['kills_parasite']) if 'kills_parasite' in stats else None
        self.cellar_spider_kills = int(stats['kills_cellar_spiders']) if 'kills_cellar_spiders' in stats else None
        self.dungeon_secret_bat_kills = int(
            stats['kills_dungeon_secret_bat']) if 'kills_dungeon_secret_bat' in stats else None
        self.scarf_mage_kills = int(stats['kills_scarf_mage']) if 'kills_scarf_mage' in stats else None
        self.crypt_undead_friedrich_kills = int(
            stats['kills_crypt_undead_friedrich']) if 'kills_crypt_undead_friedrich' in stats else None
        self.guardian_defender_kills = int(
            stats['kills_guardian_defender']) if 'kills_guardian_defender' in stats else None
        self.crypt_dreadlord_deaths = int(
            stats['deaths_crypt_dreadlord']) if 'deaths_crypt_dreadlord' in stats else None
        self.zombie_soldier_kills = int(stats['kills_zombie_soldier']) if 'kills_zombie_soldier' in stats else None
        self.skeletor_deaths = int(stats['deaths_skeletor']) if 'deaths_skeletor' in stats else None
        self.skeletor_kills = int(stats['kills_skeletor']) if 'kills_skeletor' in stats else None
        self.professer_mage_guardian_deaths = int(
            stats['deaths_professor_mage_guardian']) if 'deaths_professor_mage_guardian' in stats else None
        self.sea_leech_kills = int(stats['kills_sea_leech']) if 'kills_sea_leech' in stats else None
        self.sea_witch_kills = int(stats['kills_sea_witch']) if 'kills_sea_witch' in stats else None
        self.skeleton_emperor_kills = int(
            stats['kills_skeleton_emperor']) if 'kills_skeleton_emperor' in stats else None
        self.mythos_burrows_dug_next = int(
            stats['mythos_burrows_dug_next']) if 'mythos_burrows_dug_next' in stats else None
        self.common_mythos_burrows_dug_next = int(
            stats['mythos_burrows_dug_next_COMMON']) if 'mythos_burrows_dug_next_COMMON' in stats else None
        self.mythos_burrows_dug_combat = int(
            stats['mythos_burrows_dug_combat']) if 'mythos_burrows_dug_combat' in stats else None
        self.common_mythos_burrows_dug_combat = int(
            stats['mythos_burrows_dug_combat_COMMON']) if 'mythos_burrows_dug_combat_COMMON' in stats else None
        self.mythos_kills = int(stats['kills_mythos']) if 'kills_mythos' in stats else None
        self.minos_hunter_kills = int(stats['kills_minos_hunter']) if 'kills_minos_hunter' in stats else None
        self.mythos_burrows_dug_treasure = int(
            stats['mythos_burrows_dug_treasure']) if 'mythos_burrows_dug_treasure' in stats else None
        self.common_mythos_burrows_dug_treasure = int(
            stats['mythos_burrows_dug_treasure_COMMON']) if 'mythos_burrows_dug_treasure_COMMON' in stats else None
        self.siamese_lynx_kills = int(stats['kills_siamese_lynx']) if 'kills_siamese_lynx' in stats else None
        self.mythos_burrows_chains_complete = int(
            stats['mythos_burrows_chains_complete']) if 'mythos_burrows_chains_complete' in stats else None
        self.common_mythos_burrows_chains_complete = int(stats['mythos_burrows_chains_complete_COMMON']
                                                         ) if 'mythos_burrows_chains_complete_COMMON' in stats else None
        self.rare_mythos_burrows_dug_next = int(
            stats['mythos_burrows_dug_next_RARE']) if 'mythos_burrows_dug_next_RARE' in stats else None
        self.rare_mythos_burrows_dug_combat = int(
            stats['mythos_burrows_dug_combat_RARE']) if 'mythos_burrows_dug_combat_RARE' in stats else None
        self.minotaur_deaths = int(stats['deaths_minotaur']) if 'deaths_minotaur' in stats else None
        self.minotaur_kills = int(stats['kills_minotaur']) if 'kills_minotaur' in stats else None
        self.gaia_construct_kills = int(stats['kills_gaia_construct']) if 'kills_gaia_construct' in stats else None
        self.rare_mythos_burrows_dug_treasure = int(
            stats['mythos_burrows_dug_treasure_RARE']) if 'mythos_burrows_dug_treasure_RARE' in stats else None
        self.rare_mythos_burrows_chains_complete = int(
            stats['mythos_burrows_chains_complete_RARE']) if 'mythos_burrows_chains_complete_RARE' in stats else None
        self.gaia_construct_deaths = int(stats['deaths_gaia_construct']) if 'deaths_gaia_construct' in stats else None
        self.siamese_lynx_deaths = int(stats['deaths_siamese_lynx']) if 'deaths_siamese_lynx' in stats else None
        self.deep_sea_protector_kills = int(
            stats['kills_deep_sea_protector']) if 'kills_deep_sea_protector' in stats else None
        self.water_hydra_kills = int(stats['kills_water_hydra']) if 'kills_water_hydra' in stats else None
        self.blue_shark_kills = int(stats['kills_blue_shark']) if 'kills_blue_shark' in stats else None
        self.tiger_shark_kills = int(stats['kills_tiger_shark']) if 'kills_tiger_shark' in stats else None
        self.nurse_shark_kills = int(stats['kills_nurse_shark']) if 'kills_nurse_shark' in stats else None
        self.crypt_souleater_deaths = int(
            stats['deaths_crypt_souleater']) if 'deaths_crypt_souleater' in stats else None
        self.zombie_knight_kills = int(stats['kills_zombie_knight']) if 'kills_zombie_knight' in stats else None
        self.crypt_undead_valentin_kills = int(
            stats['kills_crypt_undead_valentin']) if 'kills_crypt_undead_valentin' in stats else None
        self.soul_of_the_alpha_deaths = int(
            stats['deaths_soul_of_the_alpha']) if 'deaths_soul_of_the_alpha' in stats else None
        self.dungeon_hub_precursor_ruins_no_abilities_no_return_best_time = stats[
            'dungeon_hub_precursor_ruins_no_abilities_no_return_best_time']
        self.crypt_wither_skeleton_kills = int(
            stats['kills_crypt_witherskeleton']) if 'kills_crypt_witherskeleton' in stats else None
        self.crypt_wither_skeleton_deaths = int(
            stats['deaths_crypt_witherskeleton']) if 'deaths_crypt_witherskeleton' in stats else None
        self.spirit_wolf_kills = int(stats['kills_spirit_wolf']) if 'kills_spirit_wolf' in stats else None
        self.spirit_sheep_kills = int(stats['kills_spirit_sheep']) if 'kills_spirit_sheep' in stats else None
        self.spirit_bull_kills = int(stats['kills_spirit_bull']) if 'kills_spirit_bull' in stats else None
        self.spirit_rabbit_kills = int(stats['kills_spirit_rabbit']) if 'kills_spirit_rabbit' in stats else None
        self.thork_kills = int(stats['kills_thorn']) if 'kills_thorn' in stats else None
        self.livid_clone_deaths = int(stats['deaths_livid_clone']) if 'deaths_livid_clone' in stats else None
        self.sniper_skeleton_deaths = int(
            stats['deaths_sniper_skeleton']) if 'deaths_sniper_skeleton' in stats else None
        self.super_tank_zombie_kills = int(
            stats['kills_super_tank_zombie']) if 'kills_super_tank_zombie' in stats else None
        self.super_archer_kills = int(stats['kills_super_archer']) if 'kills_super_archer' in stats else None
        self.tentaclees_deaths = int(stats['deaths_tentaclees']) if 'deaths_tentaclees' in stats else None
        self.corrupted_protector_kills = int(
            stats['kills_corrupted_protector']) if 'kills_corrupted_protector' in stats else None
        self.professer_guardian_summon_kills = int(
            stats['kills_professor_guardian_summon']) if 'kills_professor_guardian_summon' in stats else None
        self.unstable_dragon_kills = int(stats['kills_unstable_dragon']) if 'kills_unstable_dragon' in stats else None
        self.strong_dragon_kills = int(stats['kills_strong_dragon']) if 'kills_strong_dragon' in stats else None
        self.spirit_bat_kills = int(stats['kills_spirit_bat']) if 'kills_spirit_bat' in stats else None
        self.shadow_assassin_kills = int(stats['kills_shadow_assassin']) if 'kills_shadow_assassin' in stats else None
        self.tentaclees_kills = int(stats['kills_tentaclees']) if 'kills_tentaclees' in stats else None
        self.livid_deaths = int(stats['deaths_livid']) if 'deaths_livid' in stats else None
        self.sadan_statue_deaths = int(stats['deaths_sadan_statue']) if 'deaths_sadan_statue' in stats else None
        self.scary_jerry_kills = int(stats['kills_scary_jerry']) if 'kills_scary_jerry' in stats else None
        self.wither_gourd_kills = int(stats['kills_wither_gourd']) if 'kills_wither_gourd' in stats else None
        self.trick_or_treater_kills = int(
            stats['kills_trick_or_treater']) if 'kills_trick_or_treater' in stats else None
        self.phantom_spirit_kills = int(stats['kills_phantom_spirit']) if 'kills_phantom_spirit' in stats else None
        self.wraith_kills = int(stats['kills_wraith']) if 'kills_wraith' in stats else None
        self.batty_witch_kills = int(stats['kills_batty_witch']) if 'kills_batty_witch' in stats else None
        self.zombie_commander_kills = int(
            stats['kills_zombie_commander']) if 'kills_zombie_commander' in stats else None
        self.watcher_guardian_deaths = int(
            stats['deaths_watcher_guardian']) if 'deaths_watcher_guardian' in stats else None
        self.skeletor_prime_kills = int(stats['kills_skeletor_prime']) if 'kills_skeletor_prime' in stats else None
        self.super_tank_zombie_deaths = int(
            stats['deaths_super_tank_zombie']) if 'deaths_super_tank_zombie' in stats else None
        self.skeletor_prime_deaths = int(stats['deaths_skeletor_prime']) if 'deaths_skeletor_prime' in stats else None
        self.great_white_shark_kills = int(
            stats['kills_great_white_shark']) if 'kills_great_white_shark' in stats else None
        self.zombie_knight_deaths = int(stats['deaths_zombie_knight']) if 'deaths_zombie_knight' in stats else None
        self.suffocation_deaths = int(stats['deaths_suffocation']) if 'deaths_suffocation' in stats else None
        self.protector_dragon_deaths = int(
            stats['deaths_protector_dragon']) if 'deaths_protector_dragon' in stats else None
        self.sadan_deaths = int(stats['deaths_sadan']) if 'deaths_sadan' in stats else None
        self.sadan_golem_deaths = int(stats['deaths_sadan_golem']) if 'deaths_sadan_golem' in stats else None
        self.watcher_scarf_deaths = int(stats['deaths_watcher_scarf']) if 'deaths_watcher_scarf' in stats else None
        self.scarf_warrior_kills = int(stats['kills_scarf_warrior']) if 'kills_scarf_warrior' in stats else None
        self.crypt_undead_deaths = int(stats['deaths_crypt_undead']) if 'deaths_crypt_undead' in stats else None
        self.watcher_scarf_kills = int(stats['kills_watcher_scarf']) if 'kills_watcher_scarf' in stats else None
        self.spirit_bat_deaths = int(stats['deaths_spirit_bat']) if 'deaths_spirit_bat' in stats else None
        self.spirit_miniboss_deaths = int(
            stats['deaths_spirit_miniboss']) if 'deaths_spirit_miniboss' in stats else None
        self.spirit_chicken_deaths = int(stats['deaths_spirit_chicken']) if 'deaths_spirit_chicken' in stats else None
        self.spirit_sheep_deaths = int(stats['deaths_spirit_sheep']) if 'deaths_spirit_sheep' in stats else None
        self.crypt_undead_marius_kills = int(
            stats['kills_crypt_undead_marius']) if 'kills_crypt_undead_marius' in stats else None


class SkyBlockObjective(object):
    r"""Represents a SkyBlock Objective.

    :param objective_name: The name of the objective.
    :type objective_name: str

    :param objective_data: The objective's data.
    :type objective_data: dict"""

    def __init__(self, objective_name: str, objective_data: dict):
        self.name = objective_name
        self.status = objective_data['status']
        self.progress = objective_data['progress']
        self.completed_at = datetime.datetime.fromtimestamp(
            objective_data['completed_at'] / 1000
        ) if objective_data['completed_at'] != 0 else None


class SkyBlockQuest(object):
    r"""Represents a SkyBlock quest.

    :param quest_name: The name of the quest.
    :type quest_name: str

    :param quest_data: The quest's data.
    :type quest_data: dict"""

    def __init__(self, quest_name: str, quest_data: dict):
        self.name = quest_name
        self.status = quest_data['status']
        self.activated_at = datetime.datetime.fromtimestamp(
            quest_data['activated_at'] / 1000
        )
        self.completed_at = datetime.datetime.fromtimestamp(
            quest_data['completed_at'] / 1000
        )


class SkyBlockSlayer(object):
    r"""Represents a SkyBlock slayer.

    :param slayer: The name of the slayer.
    :type slayer: str

    :param slayer_data: The slayer's data.
    :type slayer_data: dict"""

    def __init__(self, slayer: str, slayer_data: dict):
        self.slayer = slayer
        self.claimed_levels = slayer_data['claimed_levels']
        self.xp = slayer_data['xp']
        self.level = types[slayer](slayer_data['xp'])


class SkyBlockPet(object):
    r"""Represents a SkyBlock pet.

    :param pet_data: The pet's data.
    :type pet_data: dict"""
    def __init__(self, pet_data: dict):
        self.uuid = pet_data['uuid']
        self.type = pet_data['type']
        self.xp = pet_data['exp']
        self.active = pet_data['active']
        self.tier = pet_data['tier']
        self.held_item = pet_data['heldItem']
        self.candy_used = pet_data['candyUsed']
        self.skin = pet_data['skin']


class SkyBlockSkill(object):
    r"""Represents a SkyBlock skill.

    :param name: The skill's name.
    :type name: str

    :param skill_data: The skill's data.
    :type skill_data: dict"""
    def __init__(self, name, skill_data):
        self.name = name
        self.level = skill_data['level']
        self.xp = skill_data['xp']
