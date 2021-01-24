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

from contextlib import suppress

class SkyBlockStats:
    def __init__(self, stats):
        with suppress(KeyError):
            self.top_crit_damage = stats['highest_crit_damage']
        with suppress(KeyError):
            self.kills = int(stats['kills'])
        with suppress(KeyError):
            self.zombie_kills = int(stats['kills_zombie'])
        with suppress(KeyError):
            self.bids = int(stats['auctions_bids'])
        with suppress(KeyError):
            self.highest_bid = stats['auctions_highest_bid']
        with suppress(KeyError):
            self.zombie_villager_kills = int(stats['kills_zombie_villager'])
        with suppress(KeyError):
            self.skeleton_kills = int(stats['kills_skeleton'])
        with suppress(KeyError):
            self.spider_kills = int(stats['kills_spider'])
        with suppress(KeyError):
            self.enderman_kills = int(stats['kills_enderman'])
        with suppress(KeyError):
            self.deaths = int(stats['deaths'])
        with suppress(KeyError):
            self.zombie_deaths = int(stats['deaths_zombie'])
        with suppress(KeyError):
            self.void_deaths = int(stats['deaths'])
        with suppress(KeyError):
            self.skeleton_deaths = int(stats['deaths_skeleton'])
        with suppress(KeyError):
            self.fire_deaths = int(stats['deaths_fire'])
        with suppress(KeyError):
            self.auctions_won = int(stats['auctions_won'])
        with suppress(KeyError):
            self.uncommon_auctions_bought = int(stats['auctions_bought_uncommon'])
        with suppress(KeyError):
            self.auctions_gold_spent = int(stats['auctions_gold_spent'])
        with suppress(KeyError):
            self.auctions_created = int(stats['auctions_created'])
        with suppress(KeyError):
            self.auction_fees_spent = int(stats['auctions_fees'])
        with suppress(KeyError):
            self.player_deaths = int(stats['deaths_player'])
        with suppress(KeyError):
            self.auctions_completed = int(stats['auctions_completed'])
        with suppress(KeyError):
            self.uncommon_auctions_sold = int(stats['auctions_sold_uncommon'])
        with suppress(KeyError):
            self.auction_gold_earned = int(stats['auctions_gold_earned'])
        with suppress(KeyError):
            self.invisible_creeper_kills = int(stats['kills_invisible_creeper'])
        with suppress(KeyError):
            self.emerald_slime_kills = int(stats['kills_emerald_slime'])
        with suppress(KeyError):
            self.diamond_zombie_kills = int(stats['kills_diamond_zombie'])
        with suppress(KeyError):
            self.diamond_skeleton_deaths = int(stats['deaths_diamond_skeleton'])
        with suppress(KeyError):
            self.diamond_zombie_deaths = int(stats['deaths_diamond_zombie'])
        with suppress(KeyError):
            self.diamond_skeleton_kills = int(stats['kills_diamond_skeleton'])
        with suppress(KeyError):
            self.lapis_zombie_kills = int(stats['kills_lapis_zombie'])
        with suppress(KeyError):
            self.emerald_slime_deaths = int(stats['deaths_emerald_slime'])
        with suppress(KeyError):
            self.redstone_pigman_kills = int(stats['kills_redstone_pigman'])
        with suppress(KeyError):
            self.redstone_pigman_deaths = int(stats['deaths_redstone_pigman'])
        with suppress(KeyError):
            self.splitter_spider_silverfish_kills = int(stats['kills_splitter_spider_silverfish'])
        with suppress(KeyError):
            self.jockey_shot_silverfish_kills = int(stats['kills_jockey_shot_silverfish'])
        with suppress(KeyError):
            self.wither_skeleton_kills = int(stats['kills_wither_skeleton'])
        with suppress(KeyError):
            self.magma_cube_kills = int(stats['kills_magma_cube'])
        with suppress(KeyError):
            self.magma_cube_fireball_kills = int(stats['kills_fireball_magma_cube'])
        with suppress(KeyError):
            self.cow_kills = int(stats['kills_cow'])
        with suppress(KeyError):
            self.pig_kills = int(stats['kills_pig'])
        with suppress(KeyError):
            self.items_fished = int(stats['items_fished'])
        with suppress(KeyError):
            self.normal_items_fished = int(stats['items_fished_normal'])
        with suppress(KeyError):
            self.treasure_items_fished = int(stats['items_fished_treasure'])
        with suppress(KeyError):
            self.common_auctions_bought = int(stats['auctions_bought_common'])
        with suppress(KeyError):
            self.witch_kills = int(stats['kills_witch'])
        with suppress(KeyError):
            self.spider_deaths = int(stats['deaths_spider'])
        with suppress(KeyError):
            self.epic_auctions_bought = int(stats['auctions_bought_epic'])
        with suppress(KeyError):
            self.magma_cube_fireball_deaths = int(stats['deaths_fireball_magma_cube'])
        with suppress(KeyError):
            self.weaver_spider_kills = int(stats['kills_weaver_spider'])
        with suppress(KeyError):
            self.splitter_spider_kills = int(stats['kills_splitter_spider'])
        with suppress(KeyError):
            self.jockey_skeleton_kills = int(stats['kills_jockey_skeleton'])
        with suppress(KeyError):
            self.spider_jockey_kills = int(stats['kills_spider_jockey'])
        with suppress(KeyError):
            self.dasher_spider_kills = int(stats['kills_dasher_spider'])
        with suppress(KeyError):
            self.spider_jockey_deaths = int(stats['deaths_spider_jockey'])
        with suppress(KeyError):
            self.dasher_spider_deaths = int(stats['deaths_dasher_spider'])
        with suppress(KeyError):
            self.jockey_shot_silverfish_deaths = int(stats['deaths_jockey_shot_silverfish'])
        with suppress(KeyError):
            self.splitter_spider_deaths = int(stats['deaths_splitter_spider'])
        with suppress(KeyError):
            self.common_auctions_sold = int(stats['auctions_sold_common'])
        with suppress(KeyError):
            self.no_bid_auctions = int(stats['auctions_no_bids'])
        with suppress(KeyError):
            self.ghast_kills = int(stats['kills_ghast'])
        with suppress(KeyError):
            self.rare_auctions_sold = int(stats['auctions_sold_rare'])
        with suppress(KeyError):
            self.epic_auctions_sold = int(stats['auctions_sold_epic'])
        with suppress(KeyError):
            self.magma_cube_boss_deaths = int(stats['deaths_magma_cube_boss'])
        with suppress(KeyError):
            self.blaze_kills = int(stats['kills_blaze'])
        with suppress(KeyError):
            self.wither_skeleton_deaths = int(stats['deaths_wither_skeleton'])
        with suppress(KeyError):
            self.magma_cube_deaths = int(stats['deaths_magma_cube'])
        with suppress(KeyError):
            self.respawning_skeleton_kills = int(stats['kills_respawning_skeleton'])
        with suppress(KeyError):
            self.fall_deaths = int(stats['deaths_fall'])
        with suppress(KeyError):
            self.rare_auctions_bought = int(stats['auctions_bought_rare'])
        with suppress(KeyError):
            self.rabbit_kills = int(stats['kills_rabbit'])
        with suppress(KeyError):
            self.sheep_kills = int(stats['kills_sheep'])
        with suppress(KeyError):
            self.pigman_kills = int(stats['kills_pigman'])
        with suppress(KeyError):
            self.player_kills = int(stats['kills_player'])
        with suppress(KeyError):
            self.ruin_wolf_kills = int(stats['kills_ruin_wolf'])
        with suppress(KeyError):
            self.night_respawning_skeleton_kills = int(stats['kills_night_respawining_skeleton'])
        with suppress(KeyError):
            self.legendary_auctions_bought = int(stats['auctions_bought_legendary'])
        with suppress(KeyError):
            self.chicken_kills = int(stats['kills_chicken'])
        with suppress(KeyError):
            self.respawning_skeleton_deaths = int(stats['deaths_respawning_skeleton'])
        with suppress(KeyError):
            self.ruin_wolf_deaths = int(stats['deaths_ruin_wolf'])
        with suppress(KeyError):
            self.unburried_zombie_deaths = int(stats['deaths_unburied_zombie'])
        with suppress(KeyError):
            self.unburried_zombie_kills = int(stats['kills_unburried_zombie'])
        with suppress(KeyError):
            self.enderman_deaths = int(stats['deaths_enderman'])
        with suppress(KeyError):
            self.endermite_deaths = int(stats['deaths_endermite'])
        with suppress(KeyError):
            self.endermite_kills = int(stats['kills_endermite'])
        with suppress(KeyError):
            self.zealot_enderman_deaths = int(stats['deaths_zealot_enderman'])
        with suppress(KeyError):
            self.wise_dragon_deaths = int(stats['deaths_wise_dragon'])
        with suppress(KeyError):
            self.watcher_deaths = int(stats['deaths_watcher'])
        with suppress(KeyError):
            self.watcher_kills = int(stats['kills_watcher'])
        with suppress(KeyError):
            self.random_slime_kills = int(stats['kills_random_slime'])
        with suppress(KeyError):
            self.voracious_spider_kills = int(stats['kills_voracious_spider'])
        with suppress(KeyError):
            self.wolf_deaths = int(stats['deaths_wolf'])
        with suppress(KeyError):
            self.old_wolf_kills = int(stats['kills_old_wolf'])
        with suppress(KeyError):
            self.olf_wolf_deaths = int(stats['deaths_old_wolf'])
        with suppress(KeyError):
            self.zealot_enderman_kills = int(stats['kills_zealot_enderman'])
        with suppress(KeyError):
            self.obsidian_wither_kills = int(stats['kills_obsidian_wither'])
        with suppress(KeyError):
            self.howling_spirit_kills = int(stats['kills_howling_spirit'])
        with suppress(KeyError):
            self.howling_spirit_deaths = int(stats['deaths_howling_spirit'])
        with suppress(KeyError):
            self.unknown_deaths = int(stats['deaths_unknown'])
        with suppress(KeyError):
            self.sea_walker_kills = int(stats['kills_sea_walker'])
        with suppress(KeyError):
            self.pond_squid_kills = int(stats['kills_pond_squid'])
        with suppress(KeyError):
            self.sea_guardian_kills = int(stats['deaths_sea_guardian'])
        with suppress(KeyError):
            self.sea_archer_kills = int(stats['kills_sea_archer'])
        with suppress(KeyError):
            self.young_dragon_deaths = int(stats['deaths_young_dragon'])
        with suppress(KeyError):
            self.zombie_deep_kills = int(stats['kills_zombie_deep'])
        with suppress(KeyError):
            self.gifts_given = int(stats['gifts_given'])
        with suppress(KeyError):
            self.gifts_recieved = int(stats['gifts_recieved'])
        with suppress(KeyError):
            self.frozen_steve_deaths = int(stats['deaths_frozen_steve'])
        with suppress(KeyError):
            self.brood_mother_spider_kills = int(stats['kills_brood_mother_spider'])
        with suppress(KeyError):
            self.brood_mother_cave_spider_kills = int(stats['kills_brood_mother_cave_spider'])
        with suppress(KeyError):
            self.foraging_race_best_time = int(stats['foraging_race_best_time'])
        with suppress(KeyError):
            self.legendary_auctions_sold = int(stats['auctions_sold_legendary'])
        with suppress(KeyError):
            self.special_auctions_sold = int(stats['auctions_sold_special'])
        with suppress(KeyError):
            self.generator_magma_cube_kills = int(stats['kills_generator_magma_cube'])
        with suppress(KeyError):
            self.bat_pinata_kills = int(stats['kills_bat_pinata'])
        with suppress(KeyError):
            self.special_auctions_bought = int(stats['auctions_bought_special'])
        with suppress(KeyError):
            self.horseman_zombie_kills = int(stats['kills_horseman_zombie'])
        with suppress(KeyError):
            self.old_dragon_deaths = int(stats['deaths_old_dragon'])
        with suppress(KeyError):
            self.liquid_hot_magma_deaths = int(stats['deaths_liquid_hot_magma'])
        with suppress(KeyError):
            self.liquid_hot_magma_kills = int(stats['kills_liquid_hot_magma'])
        with suppress(KeyError):
            self.most_winter_snowballs_hit = int(stats['most_winter_snowballs_hit'])
        with suppress(KeyError):
            self.most_winter_damage_dealt = int(stats['most_winter_damage_dealt'])
        with suppress(KeyError):
            self.most_winter_magma_damage_dealt = int(stats['most_winter_magma_damage_dealt'])
        with suppress(KeyError):
            self.ender_crystals_destroyed = int(stats['ender_crystals_destroyed'])
        with suppress(KeyError):
            self.most_winter_cannonballs_hit = int(stats['most_winter_cannonballs_hit'])
        with suppress(KeyError):
            self.slime_kills = int(stats['kills_slime'])
        with suppress(KeyError):
            self.unstable_dragon_deaths = int(stats['deaths_unstable_dragon'])
        with suppress(KeyError):
            self.superior_dragon_deaths = int(stats['deaths_superior_dragon'])
        with suppress(KeyError):
            self.forest_island_bat_kills = int(stats['kills_forest_island_bat'])
        with suppress(KeyError):
            self.strong_dragon_deaths = int(stats['deaths_strong_dragon'])
        with suppress(KeyError):
            self.pet_milestone_ores_mined = int(stats['pet_milestone_ores_mined'])
        with suppress(KeyError):
            self.pet_milestone_sea_creatures_killed = int(stats['pet_milestone_sea_creatures_killed'])
        with suppress(KeyError):
            self.chicken_deep_kills = int(stats['kills_chicken_deep'])
        with suppress(KeyError):
            self.corrupted_protector_deaths = int(stats['deaths_corrupted_protector'])
        with suppress(KeyError):
            self.pack_spirit_kills = int(stats['kills_pack_spirit'])
        with suppress(KeyError):
            self.soul_of_the_alpha_kills = int(stats['kills_soul_of_the_alpha'])
        with suppress(KeyError):
            self.frosty_the_snowman_kills = int(stats['kills_frosty_the_snowman'])
        with suppress(KeyError):
            self.frozen_steve_kills = int(stats['kills_frozen_steve'])
        with suppress(KeyError):
            self.catfish_kills = int(stats['kills_catfish'])
        # I'm not making names for these what the hell
        with suppress(KeyError):
            self.dungeon_hub_crystal_core_anything_no_return_best_time = stats['dungeon_hub_crystal_core_anything_no_return_best_time']
        with suppress(KeyError):
            self.dungeon_hub_giant_mushroom_anything_no_return_best_time = stats['dungeon_hub_giant_mushroom_anything_no_return_best_time']
        with suppress(KeyError):
            self.dungeon_hub_giant_mushroom_no_pearls_no_return_best_time = stats['dungeon_hub_giant_mushroom_no_pearls_no_return_best_time']
        with suppress(KeyError):
            self.dungeon_hub_precursor_ruins_anything_no_return_best_time = stats['dungeon_hub_precursor_ruins_anything_no_return_best_time']
        with suppress(KeyError):
            self.dungeon_hub_precursor_ruins_nothing_no_return_best_time = stats['dungeon_hub_precursor_ruins_nothing_no_return_best_time']
        with suppress(KeyError):
            self.dungeon_hub_precursor_ruins_no_pearls_no_return_best_time = stats['dungeon_hub_precursor_ruins_no_pearls_no_return_best_time']
        # Anyways
        with suppress(KeyError):
            self.crypt_lurker_kills = int(stats['kills_crypt_lurker'])
        with suppress(KeyError):
            self.dungeon_respawning_skeleton_kills = int(stats['kills_dungeon_respawning_skeleton'])
        with suppress(KeyError):
            self.scared_skeleton_kills = int(stats['kills_scared_skeleton'])
        with suppress(KeyError):
            self.skeleton_grunt_kills = int(stats['kills_skeleton_grunt'])
        with suppress(KeyError):
            self.crypt_dreadlord_kills = int(stats['kills_scared_skeleton'])
        with suppress(KeyError):
            self.crypt_souleater_kills = int(stats['kills_crypt_souleater'])
        with suppress(KeyError):
            self.crypt_tank_zombie_kills = int(stats['kills_crypt_tank_zombie'])
        with suppress(KeyError):
            self.diamond_guy_kills = int(stats['kills_diamond_guy'])
        with suppress(KeyError):
            self.zombie_grunt_kills = int(stats['kills_zombie_grunt'])
        with suppress(KeyError):
            self.crypt_lurker_deaths = int(stats['deaths_crypt_lurker'])
        with suppress(KeyError):
            self.lost_adventurer_deaths = int(stats['deaths_lost_adventurer'])
        with suppress(KeyError):
            self.watcher_summon_undead_kills = int(stats['kills_watcher_summon_undead'])
        with suppress(KeyError):
            self.skeleton_soldier_kills = int(stats['kills_skeleton_soldier'])
        with suppress(KeyError):
            self.diamond_guy_deaths = int(stats['deaths_diamond_guy'])
        with suppress(KeyError):
            self.watcher_summon_undead_deaths = int(stats['deaths_watcher_summon_undead'])
        with suppress(KeyError):
            self.bonzo_summon_undead_kills = int(stats['kills_bonzo_summon_undead'])
        with suppress(KeyError):
            self.lost_adventurer_kills = int(stats['kills_lost_adventurer'])
        with suppress(KeyError):
            self.skeleton_master_kills = int(stats['kills_skeleton_master'])
        with suppress(KeyError):
            self.sniper_skeleton_kills = int(stats['kills_sniper_skeleton'])
        with suppress(KeyError):
            self.skeleton_soldier_deaths = int(stats['deaths_skeleton_soldier'])
        with suppress(KeyError):
            self.trap_deaths = int(stats['deaths_trap'])
        with suppress(KeyError):
            self.crypt_undead_kills = int(stats['kills_crypt_undead'])
        with suppress(KeyError):
            self.skeleton_grunt_deaths = int(stats['deaths_skeleton_grunt'])
        with suppress(KeyError):
            self.scarf_warrior_deaths = int(stats['deaths_scarf_warrior'])
        with suppress(KeyError):
            self.skeleton_master_deaths = int(stats['deaths_skeleton_master'])
        with suppress(KeyError):
            self.blaze_higher_or_lower_kills = int(stats['kills_blaze_higher_or_lower'])
        with suppress(KeyError):
            self.dungeon_respawning_skeleton_deaths = int(stats['deaths_dungeon_respawning_skeleton'])
        with suppress(KeyError):
            self.scarf_deaths = int(stats['deaths_scarf'])
        with suppress(KeyError):
            self.bonzo_summon_undead_deaths = int(stats['deaths_bonzo_summon_undead'])
        with suppress(KeyError):
            self.bonzo_deaths = int(stats['deaths_bonzo'])
        with suppress(KeyError):
            self.lonely_spider_kills = int(stats['kills_lonely_spider'])
        with suppress(KeyError):
            self.parasite_kills = int(stats['kills_parasite'])
        with suppress(KeyError):
            self.cellar_spider_kills = int(stats['kills_cellar_spiders'])
        with suppress(KeyError):
            self.dungeon_secret_bat_kills = int(stats['kills_dungeon_secret_bat'])
        with suppress(KeyError):
            self.scarf_mage_kills = int(stats['kills_scarf_mage'])
        with suppress(KeyError):
            self.crypt_undead_friedrich_kills = int(stats['kills_crypt_undead_friedrich'])
        with suppress(KeyError):
            self.guardian_defender_kills = int(stats['kills_guardian_defender'])
        with suppress(KeyError):
            self.crypt_dreadlord_deaths = int(stats['deaths_crypt_dreadlord'])
        with suppress(KeyError):
            self.zombie_soldier_kills = int(stats['kills_zombie_soldier'])
        with suppress(KeyError):
            self.skeletor_deaths = int(stats['deaths_skeletor'])
        with suppress(KeyError):
            self.skeletor_kills = int(stats['kills_skeletor'])
        with suppress(KeyError):
            self.professer_mage_guardian_deaths = int(stats['deaths_professor_mage_guardian'])
        with suppress(KeyError):
            self.sea_leech_kills = int(stats['kills_sea_leech'])
        with suppress(KeyError):
            self.sea_witch_kills = int(stats['kills_sea_witch'])
        with suppress(KeyError):
            self.skeleton_emperor_kills = int(stats['kills_skeleton_emperor'])
        with suppress(KeyError):
            self.mythos_burrows_dug_next = int(stats['mythos_burrows_dug_next'])
        with suppress(KeyError):
            self.common_mythos_burrows_dug_next = int(stats['mythos_burrows_dug_next_COMMON'])
        with suppress(KeyError):
            self.mythos_burrows_dug_combat = int(stats['mythos_burrows_dug_combat'])
        with suppress(KeyError):
            self.common_mythos_burrows_dug_combat = int(stats['mythos_burrows_dug_combat_COMMON'])
        with suppress(KeyError):
            self.mythos_kills = int(stats['kills_mythos'])
        with suppress(KeyError):
            self.minos_hunter_kills = int(stats['kills_minos_hunter'])
        with suppress(KeyError):
            self.mythos_burrows_dug_treasure = int(stats['mythos_burrows_dug_treasure'])
        with suppress(KeyError):
            self.common_mythos_burrows_dug_treasure = int(stats['mythos_burrows_dug_treasure_COMMON'])
        with suppress(KeyError):
            self.siamese_lynx_kills = int(stats['kills_siamese_lynx'])
        with suppress(KeyError):
            self.mythos_burrows_chains_complete = int(stats['mythos_burrows_chains_complete'])
        with suppress(KeyError):
            self.common_mythos_burrows_chains_complete = int(stats['mythos_burrows_chains_complete_COMMON'])
        with suppress(KeyError):
            self.rare_mythos_burrows_dug_next = int(stats['mythos_burrows_dug_next_RARE'])
        with suppress(KeyError):
            self.rare_mythos_burrows_dug_combat = int(stats['mythos_burrows_dug_combat_RARE'])
        with suppress(KeyError):
            self.minotaur_deaths = int(stats['deaths_minotaur'])
        with suppress(KeyError):
            self.minotaur_kills = int(stats['kills_minotaur'])
        with suppress(KeyError):
            self.gaia_construct_kills = int(stats['kills_gaia_construct'])
        with suppress(KeyError):
            self.rare_mythos_burrows_dug_treasure = int(stats['mythos_burrows_dug_treasure_RARE'])
        with suppress(KeyError):
            self.rare_mythos_burrows_chains_complete = int(stats['mythos_burrows_chains_complete_RARE'])
        with suppress(KeyError):
            self.gaia_construct_deaths = int(stats['deaths_gaia_construct'])
        with suppress(KeyError):
            self.siamese_lynx_deaths = int(stats['deaths_siamese_lynx'])
        with suppress(KeyError):
            self.deep_sea_protector_kills = int(stats['kills_deep_sea_protector'])
        with suppress(KeyError):
            self.water_hydra_kills = int(stats['kills_water_hydra'])
        with suppress(KeyError):
            self.blue_shark_kills = int(stats['kills_blue_shark'])
        with suppress(KeyError):
            self.tiger_shark_kills = int(stats['kills_tiger_shark'])
        with suppress(KeyError):
            self.nurse_shark_kills = int(stats['kills_nurse_shark'])
        with suppress(KeyError):
            self.shadow_assassin_kills = int(stats['kills_shadow_assassin'])
        with suppress(KeyError):
            self.crypt_souleater_deaths = int(stats['deaths_crypt_souleater'])
        with suppress(KeyError):
            self.zombie_knight_kills = int(stats['kills_zombie_knight'])
        with suppress(KeyError):
            self.crypt_undead_valentin_kills = int(stats['kills_crypt_undead_valentin'])
        with suppress(KeyError):
            self.soul_of_the_alpha_deaths = int(stats['deaths_soul_of_the_alpha'])
        with suppress(KeyError):
            self.dungeon_hub_precursor_ruins_no_abilities_no_return_best_time = int(stats['dungeon_hub_precursor_ruins_no_abilities_no_return_best_time'])
        with suppress(KeyError):
            self.crypt_wither_skeleton_kills = int(stats['kills_crypt_witherskeleton'])
        with suppress(KeyError):
            self.crypt_wither_skeleton_deaths = int(stats['deaths_crypt_witherskeleton'])
        with suppress(KeyError):
            self.spirit_wolf_kills = int(stats['kills_spirit_wolf'])
        with suppress(KeyError):
            self.