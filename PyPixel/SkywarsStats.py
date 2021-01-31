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

from .utils import Hypixel
from contextlib import suppress


class SkyWarsStats(object):
    r"""Base class for a player's SkyWars stats.
    
    :param playerstats: The raw player stats data from the API.
    :type playerstats: dict"""

    def __init__(self, playerstats: dict):
        stats = playerstats['SkyWars']
        self.raw = stats
        self.overall = self.Overall(stats)
        self.solo = self.Solo(stats)
        self.teams = self.Teams(stats)
        self.mega = self.Mega(stats)
        self.ranked = self.Ranked(stats)
        self.lab = self.Lab(stats)
        self.laboratory = self.lab
        with suppress(KeyError):
            self.experience = stats['skywars_experience']
        with suppress(KeyError):
            self.level = Hypixel.skywarsLevel(stats['skywars_experience'])

    class Overall(object):
        r"""The player's overall SkyWars stats.
    
        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict"""

        def __init__(self, stats: dict):
            with suppress(KeyError):
                self.packages = stats['packages']
            with suppress(KeyError):
                self.winstreak = stats['win_streak']
            with suppress(KeyError):
                self.survived_players = stats['survived_players']
            with suppress(KeyError):
                self.games_lost = stats['losses']
            with suppress(KeyError):
                self.blocks_broken = stats['blocks_broken']
            with suppress(KeyError):
                self.blocks_placed = stats['blocks_placed']
            with suppress(KeyError):
                self.coins = stats['coins']
            with suppress(KeyError):
                self.deaths = stats['deaths']
            with suppress(KeyError):
                self.quits = stats['quits']
            with suppress(KeyError):
                self.items_enchanted = stats['items_enchanted']
            with suppress(KeyError):
                self.souls_gathered = stats['souls_gathered']
            with suppress(KeyError):
                self.souls = stats['souls']
            with suppress(KeyError):
                self.kills = stats['kills']
            with suppress(KeyError):
                self.arrows_hit = stats['arrows_hit']
            with suppress(KeyError):
                self.arrows_shot = stats['arrows_shot']
            with suppress(KeyError):
                self.wins = stats['wins']
            with suppress(KeyError):
                self.games_played = stats['games']
            with suppress(KeyError):
                self.souls_spent = stats['paid_souls']
            with suppress(KeyError):
                self.assists = stats['assists']
            with suppress(KeyError):
                self.pearls_thrown = stats['enderpearls_thrown']
            with suppress(KeyError):
                self.eggs_thrown = stats['egg_thrown']
            with suppress(KeyError):
                self.killstreak = stats['killstreak']
            with suppress(KeyError):
                self.top_winstreak = stats['highestWinstreak']
            with suppress(KeyError):
                self.top_killstreak = stats['highestKillstreak']
            with suppress(KeyError):
                self.recently_played_mode = stats['lastMode']
            with suppress(KeyError):
                self.longest_bow_shot = stats['longest_bow_shot']
            with suppress(KeyError):
                self.chests_opened = stats['chests_opened']
            with suppress(KeyError):
                self.time_played = stats['time_played']
            with suppress(KeyError):
                self.melee_kills = stats['melee_kills']
            with suppress(KeyError):
                self.most_kills_game = stats['most_kills_game']
            with suppress(KeyError):
                self.fastest_win = stats['fastest_win']
            with suppress(KeyError):
                self.void_kills = stats['void_kills']
            with suppress(KeyError):
                self.mob_kills = stats['mob_kills']
            with suppress(KeyError):
                self.longest_bow_kill = stats['longest_bow_kill']
            with suppress(KeyError):
                self.tokens = stats['cosmetic_tokens']
            with suppress(KeyError):
                self.bow_kills = stats['bow_kills']

    class Solo(object):
        r"""The player's solo SkyWars stats.
    
        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict"""

        def __init__(self, stats: dict):
            self.normal = self.Normal(stats)
            self.insane = self.Insane(stats)
            with suppress(KeyError):
                self.kit = stats['activeKit_SOLO']
            with suppress(KeyError):
                self.losses = stats['losses_solo']
            with suppress(KeyError):
                self.deaths = stats['deaths_solo']
            with suppress(KeyError):
                self.survived_players = stats['survived_players_solo']
            with suppress(KeyError):
                self.kills = stats['kills_solo']
            with suppress(KeyError):
                self.games_played = stats['games_solo']
            with suppress(KeyError):
                self.games_played = stats['games_solo']
            with suppress(KeyError):
                self.wins = stats['wins_solo']
            with suppress(KeyError):
                self.assists = stats['assists_solo']
            with suppress(KeyError):
                self.chests_opened = stats['chests_opened_solo']
            with suppress(KeyError):
                self.time_played = stats['time_played_solo']
            with suppress(KeyError):
                self.fastest_win = stats['fastest_win_solo']
            with suppress(KeyError):
                self.melee_kills = stats['melee_kills_solo']
            with suppress(KeyError):
                self.killstreak = stats['killstreak_solo']
            with suppress(KeyError):
                self.winstreak = stats['winstreak_solo']
            with suppress(KeyError):
                self.most_kills_game = stats['most_kills_game_solo']
            with suppress(KeyError):
                self.void_kills = stats['void_kills_solo']
            with suppress(KeyError):
                self.longest_bow_shot = stats['longest_bow_shot_solo']
            with suppress(KeyError):
                self.arrows_hit = stats['arrows_hit_solo']
            with suppress(KeyError):
                self.arrows_shot = stats['arrows_shot_solo']
            with suppress(KeyError):
                self.longest_bow_kill = stats['longest_bow_kill_solo']

        class Normal(object):
            r"""The player's solo normal SkyWars stats.
    
            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict"""

            def __init__(self, stats: dict):
                with suppress(KeyError):
                    self.losses = stats['losses_solo_normal']
                with suppress(KeyError):
                    self.deaths = stats['deaths_solo_normal']
                with suppress(KeyError):
                    self.kills = stats['kills_solo_normal']
                with suppress(KeyError):
                    self.wins = stats['wins_solo_normal']

        class Insane(object):
            r"""The player's solo insane SkyWars stats.
    
            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict"""

            def __init__(self, stats: dict):
                with suppress(KeyError):
                    self.losses = stats['losses_solo_insane']
                with suppress(KeyError):
                    self.deaths = stats['deaths_solo_insane']
                with suppress(KeyError):
                    self.kills = stats['kills_solo_insane']
                with suppress(KeyError):
                    self.wins = stats['wins_solo_insane']

    class Teams(object):
        r"""The player's teams SkyWars stats.
    
        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict"""

        def __init__(self, stats: dict):
            self.normal = self.Normal(stats)
            self.insane = self.Insane(stats)
            with suppress(KeyError):
                self.kit = stats['activeKit_TEAMS']
            with suppress(KeyError):
                self.survived_players = stats['survived_players_team']
            with suppress(KeyError):
                self.deaths = stats['deaths_team']
            with suppress(KeyError):
                self.assists = stats['assists_team']
            with suppress(KeyError):
                self.kills = stats['kills_team']
            with suppress(KeyError):
                self.games_played = stats['games_team']
            with suppress(KeyError):
                self.losses = stats['losses_team']
            with suppress(KeyError):
                self.wins = stats['wins_team']
            with suppress(KeyError):
                self.chests_opened = stats['chests_opened_team']
            with suppress(KeyError):
                self.time_played = stats['time_played_team']
            with suppress(KeyError):
                self.longest_bow_shot = stats['longest_bow_shot_team']
            with suppress(KeyError):
                self.fastest_win = stats['fastest_win_team']
            with suppress(KeyError):
                self.melee_kills = stats['melee_kills_team']
            with suppress(KeyError):
                self.winstreak = stats['winstreak_team']
            with suppress(KeyError):
                self.arrows_shot = stats['arrows_shot_team']
            with suppress(KeyError):
                self.arrows_hit = stats['arrows_hit_team']
            with suppress(KeyError):
                self.killstreak = stats['killstreak_team']
            with suppress(KeyError):
                self.most_kills_game = stats['most_kills_game_team']
            with suppress(KeyError):
                self.void_kills = stats['void_kills_team']
            with suppress(KeyError):
                self.longest_bow_kill = stats['longest_bow_kill_team']
            with suppress(KeyError):
                self.bow_kills = stats['bow_kills_team']

        class Normal(object):
            r"""The player's teams normal SkyWars stats.
    
            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict"""

            def __init__(self, stats):
                with suppress(KeyError):
                    self.deaths = stats['deaths_team_normal']
                with suppress(KeyError):
                    self.losses = stats['losses_team_normal']
                with suppress(KeyError):
                    self.kills = stats['kills_team_normal']
                with suppress(KeyError):
                    self.wins = stats['wins_team_normal']

        class Insane(object):
            r"""The player's teams insane SkyWars stats.
    
            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict"""

            def __init__(self, stats):
                with suppress(KeyError):
                    self.losses = stats['losses_team_insane']
                with suppress(KeyError):
                    self.deaths = stats['deaths_team_insane']
                with suppress(KeyError):
                    self.kills = stats['kills_team_insane']
                with suppress(KeyError):
                    self.wins = stats['wins_team_insane']

    class Mega(object):
        r"""The player's mega SkyWars stats.
    
        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict"""

        def __init__(self, stats):
            with suppress(KeyError):
                self.kit = stats['activeKit_MEGA']
            with suppress(KeyError):
                self.survived_players = stats['survived_players_mega']
            with suppress(KeyError):
                self.kills = stats['kills_mega']
            with suppress(KeyError):
                self.deaths = stats['deaths_mega']
            with suppress(KeyError):
                self.assists = stats['assists_mega']
            with suppress(KeyError):
                self.wins = stats['wins_mega']
            with suppress(KeyError):
                self.games_played = stats['games_mega']
            with suppress(KeyError):
                self.longest_bow_shot = stats['longest_bow_shot_mega']
            with suppress(KeyError):
                self.chests_opened = stats['chests_opened_mega']
            with suppress(KeyError):
                self.most_kills = stats['most_kills_game_mega']
            with suppress(KeyError):
                self.melee_kills = stats['melee_kills_mega']
            with suppress(KeyError):
                self.arrows_shot = stats['arrows_shot_mega']
            with suppress(KeyError):
                self.arrows_hit = stats['arrows_hit_mega']
            with suppress(KeyError):
                self.time_played = stats['time_played_mega']
            with suppress(KeyError):
                self.fastest_win = stats['fastest_win_mega']
            with suppress(KeyError):
                self.winstreak = stats['winstreak_mega']
            with suppress(KeyError):
                self.void_kills = stats['void_kills_mega']
            with suppress(KeyError):
                self.killstreak = stats['killstreak_mega']
            with suppress(KeyError):
                self.mob_kills = stats['mob_kills_mega']

    class Ranked(object):
        r"""The player's ranked SkyWars stats.
    
        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict"""

        def __init__(self, stats):
            with suppress(KeyError):
                self.kit = stats['activeKit_RANKED']
            with suppress(KeyError):
                self.assists = stats['assists_ranked']
            with suppress(KeyError):
                self.winstreak = stats['winstreak_ranked']
            with suppress(KeyError):
                self.games_played = stats['games_ranked']
            with suppress(KeyError):
                self.wins = stats['wins_ranked']
            with suppress(KeyError):
                self.deaths = stats['deaths_ranked']
            with suppress(KeyError):
                self.losses = stats['losses_ranked']
            with suppress(KeyError):
                self.longest_bow_shot = stats['longest_bow_shot_ranked']
            with suppress(KeyError):
                self.arrows_shot = stats['arrows_shot_ranked']
            with suppress(KeyError):
                self.arrows_hit = stats['arrows_hit_ranked']
            with suppress(KeyError):
                self.chests_opened = stats['chests_opened_ranked']
            with suppress(KeyError):
                self.time_played = stats['time_played_ranked']
            with suppress(KeyError):
                self.melee_kills = stats['melee_kills_ranked']
            with suppress(KeyError):
                self.most_kills_game = stats['most_kills_game_ranked']
            with suppress(KeyError):
                self.fastest_win = stats['fastest_win_ranked']
            with suppress(KeyError):
                self.void_kills = stats['void_kills_ranked']
            with suppress(KeyError):
                self.longest_bow_kill = stats['longest_bow_kill_ranked']
            with suppress(KeyError):
                self.bow_kills = stats['bow_kills_ranked']

    class Lab(object):
        r"""The player's laboratory SkyWars stats.
    
        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict"""

        def __init__(self, stats: dict):
            self.solo = self.Solo(stats)
            self.teams = self.Teams(stats)
            with suppress(KeyError):
                self.winstreak = stats['win_streak_lab']
            with suppress(KeyError):
                self.souls_gathered = stats['souls_gathered_lab']
            with suppress(KeyError):
                self.survived_playes = stats['survived_players_lab']
            with suppress(KeyError):
                self.coins_gained = stats['coins_gained_lab']
            with suppress(KeyError):
                self.kills = stats['kills_lab']
            with suppress(KeyError):
                self.deaths = stats['deaths_lab']
            with suppress(KeyError):
                self.time_played = stats['time_played_lab']
            with suppress(KeyError):
                self.chests_opened = stats['chests_opened_lab']
            with suppress(KeyError):
                self.losses = stats['losses_lab']
            with suppress(KeyError):
                self.melee_kills = stats['melee_kills_lab']
            with suppress(KeyError):
                self.quits = stats['quits_lab']
            with suppress(KeyError):
                self.blocks_placed = stats['blocks_placed_lab']
            with suppress(KeyError):
                self.longest_bow_kill = stats['longest_bow_kill_lab']
            with suppress(KeyError):
                self.blocks_broken = stats['blocks_broken_lab']
            with suppress(KeyError):
                self.games_played = stats['games_lab']
            with suppress(KeyError):
                self.longest_bow_shot = stats['longest_bow_shot_lab']
            with suppress(KeyError):
                self.fastest_win = stats['fastest_win_lab']
            with suppress(KeyError):
                self.void_kills = stats['void_kills_lab']
            with suppress(KeyError):
                self.lucky_block_wins = stats['lab_win_lucky_blocks_lab']
            with suppress(KeyError):
                self.most_kills_game = stats['most_kills_game_lab']
            with suppress(KeyError):
                self.arrows_hit = stats['arrows_hit_lab']
            with suppress(KeyError):
                self.wins = stats['wins_lab']
            with suppress(KeyError):
                self.killstreak = stats['killstreak_lab']
            with suppress(KeyError):
                self.winstreak = stats['winstreak_lab']
            with suppress(KeyError):
                self.arrows_shot = stats['arrows_shot_lab']
            with suppress(KeyError):
                self.tnt_madness_wins = stats['lab_win_tnt_madness_lab']
            with suppress(KeyError):
                self.pearls_throws = stats['enderpearls_thrown_lab']
            with suppress(KeyError):
                self.slime_wins = stats['lab_win_slime_lab']
            with suppress(KeyError):
                self.assists = stats['assists_lab']
            with suppress(KeyError):
                self.falling_kills = stats['fall_kills_lab']
            with suppress(KeyError):
                self.eggs_thrown = stats['egg_thrown_lab']
            with suppress(KeyError):
                self.bow_kills = stats['bow_kills_lab']
            with suppress(KeyError):
                self.mob_kills = stats['mob_kills_lab']
            with suppress(KeyError):
                self.rush_wins = stats['lab_win_rush_lab']

        class Solo(object):
            r"""The player's solo lab SkyWars stats.

            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict"""
            def __init__(self, stats: dict):
                with suppress(KeyError):
                    self.survived_players = stats['survived_players_lab_solo']
                with suppress(KeyError):
                    self.chests_opened = stats['chests_opened_lab_solo']
                with suppress(KeyError):
                    self.deaths = stats['deaths_lab_solo']
                with suppress(KeyError):
                    self.time_played = stats['time_played_lab_solo']
                with suppress(KeyError):
                    self.losses = stats['losses_lab_solo']
                with suppress(KeyError):
                    self.longest_bow_kill = stats['longest_bow_kill_lab_solo']
                with suppress(KeyError):
                    self.games_played = stats['games_lab_solo']
                with suppress(KeyError):
                    self.melee_kills = stats['melee_kills_lab_solo']
                with suppress(KeyError):
                    self.kills = stats['kills_lab_solo']
                with suppress(KeyError):
                    self.fastest_win = stats['fastest_win_lab_solo']
                with suppress(KeyError):
                    self.longest_bow_shot = stats['longest_bow_shot_lab_solo']
                with suppress(KeyError):
                    self.arrows_shot = stats['arrows_shot_lab_solo']
                with suppress(KeyError):
                    self.winstreak = stats['winstreak_lab_solo']
                with suppress(KeyError):
                    self.wins = stats['wins_lab_solo']
                with suppress(KeyError):
                    self.void_kills = stats['void_kills_lab_solo']
                with suppress(KeyError):
                    self.most_kills_game = stats['most_kills_game_lab_solo']
                with suppress(KeyError):
                    self.lucky_block_wins = stats['lab_win_lucky_blocks_lab_solo']
                with suppress(KeyError):
                    self.killstreak = stats['killstreak_lab_solo']
                with suppress(KeyError):
                    self.arrows_hit = stats['arrows_hit_lab_solo']
                with suppress(KeyError):
                    self.tnt_madness_wins = stats['lab_win_tnt_madness_lab_solo']
                with suppress(KeyError):
                    self.slime_wins = stats['lab_win_slime_lab_solo']
                with suppress(KeyError):
                    self.assists = stats['assists_lab_solo']
                with suppress(KeyError):
                    self.falling_kills = stats['fall_kills_lab_solo']
                with suppress(KeyError):
                    self.mob_kills = stats['mob_kills_lab_solo']
                with suppress(KeyError):
                    self.rush_wins = stats['lab_win_rush_lab_solo']

        class Teams(object):
            r"""The player's teams lab SkyWars stats.

            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict"""
            def __init__(self, stats: dict):
                with suppress(KeyError):
                    self.survived_playes = stats['survived_players_lab_team']
                with suppress(KeyError):
                    self.losses = stats['losses_lab_team']
                with suppress(KeyError):
                    self.melee_kills = stats['melee_kills_lab_team']
                with suppress(KeyError):
                    self.kills = stats['kills_lab_team']
                with suppress(KeyError):
                    self.deaths = stats['deaths_lab_team']
                with suppress(KeyError):
                    self.chests_opened = stats['chests_opened_lab_team']
                with suppress(KeyError):
                    self.time_played = stats['time_played_lab_team']
                with suppress(KeyError):
                    self.arrows_shot = stats['arrows_shot_lab_team']
                with suppress(KeyError):
                    self.fastest_win = stats['fastest_win_lab_team']
                with suppress(KeyError):
                    self.games_played = stats['games_lab_team']
                with suppress(KeyError):
                    self.killstreak = stats['killstreak_lab_team']
                with suppress(KeyError):
                    self.slime_wins = stats['lab_win_slime_lab_team']
                with suppress(KeyError):
                    self.void_kills = stats['void_kills_lab_team']
                with suppress(KeyError):
                    self.wins = stats['wins_lab_team']
                with suppress(KeyError):
                    self.assists = stats['assists_lab_team']
                with suppress(KeyError):
                    self.lucky_block_wins = stats['lab_win_lucky_blocks_lab_team']
                with suppress(KeyError):
                    self.longest_bow_kill = stats['longest_bow_kill_lab_team']
                with suppress(KeyError):
                    self.most_kills_game = stats['most_kills_game_lab_team']
                with suppress(KeyError):
                    self.arrows_hit = stats['arrows_hit_lab_team']
                with suppress(KeyError):
                    self.longest_bow_shot = stats['longest_bow_shot_lab_team']
                with suppress(KeyError):
                    self.bow_kills = stats['bow_kills_lab_team']
                with suppress(KeyError):
                    self.falling_kills = stats['fall_kills_lab_team']
                with suppress(KeyError):
                    self.rush_wins = stats['lab_win_rush_lab_team']
