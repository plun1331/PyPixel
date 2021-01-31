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

from .utils import HypixelUtils


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
        self.experience = stats['skywars_experience'] if 'skywars_experience' in stats else None
        self.level = HypixelUtils.skywarsLevel(stats['skywars_experience']) if 'skywars_experience' in stats else None

    class Overall(object):
        r"""The player's overall SkyWars stats.
    
        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict"""

        def __init__(self, stats: dict):
            self.packages = stats['packages'] if 'packages' in stats else None
            self.winstreak = stats['win_streak'] if 'win_streak' in stats else None
            self.survived_players = stats['survived_players'] if 'survived_players' in stats else None
            self.games_lost = stats['losses'] if 'losses' in stats else None
            self.blocks_broken = stats['blocks_broken'] if 'blocks_broken' in stats else None
            self.blocks_placed = stats['blocks_placed'] if 'blocks_placed' in stats else None
            self.coins = stats['coins'] if 'coins' in stats else None
            self.deaths = stats['deaths'] if 'deaths' in stats else None
            self.quits = stats['quits'] if 'quits' in stats else None
            self.items_enchanted = stats['items_enchanted'] if 'items_enchanted' in stats else None
            self.souls_gathered = stats['souls_gathered'] if 'souls_gathered' in stats else None
            self.souls = stats['souls'] if 'souls' in stats else None
            self.kills = stats['kills'] if 'kills' in stats else None
            self.arrows_hit = stats['arrows_hit'] if 'arrows_hit' in stats else None
            self.arrows_shot = stats['arrows_shot'] if 'arrows_shot' in stats else None
            self.wins = stats['wins'] if 'wins' in stats else None
            self.games_played = stats['games'] if 'games' in stats else None
            self.souls_spent = stats['paid_souls'] if 'paid_souls' in stats else None
            self.assists = stats['assists'] if 'assists' in stats else None
            self.pearls_thrown = stats['enderpearls_thrown'] if 'enderpearls_thrown' in stats else None
            self.eggs_thrown = stats['egg_thrown'] if 'egg_thrown' in stats else None
            self.killstreak = stats['killstreak'] if 'killstreak' in stats else None
            self.top_winstreak = stats['highestWinstreak'] if 'highestWinstreak' in stats else None
            self.top_killstreak = stats['highestKillstreak'] if 'highestKillstreak' in stats else None
            self.recently_played_mode = stats['lastMode'] if 'lastMode' in stats else None
            self.longest_bow_shot = stats['longest_bow_shot'] if 'longest_bow_shot' in stats else None
            self.chests_opened = stats['chests_opened'] if 'chests_opened' in stats else None
            self.time_played = stats['time_played'] if 'time_played' in stats else None
            self.melee_kills = stats['melee_kills'] if 'melee_kills' in stats else None
            self.most_kills_game = stats['most_kills_game'] if 'most_kills_game' in stats else None
            self.fastest_win = stats['fastest_win'] if 'fastest_win' in stats else None
            self.void_kills = stats['void_kills'] if 'void_kills' in stats else None
            self.mob_kills = stats['mob_kills'] if 'mob_kills' in stats else None
            self.longest_bow_kill = stats['longest_bow_kill'] if 'longest_bow_kill' in stats else None
            self.tokens = stats['cosmetic_tokens'] if 'cosmetic_tokens' in stats else None
            self.bow_kills = stats['bow_kills'] if 'bow_kills' in stats else None

    class Solo(object):
        r"""The player's solo SkyWars stats.
    
        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict"""

        def __init__(self, stats: dict):
            self.normal = self.Normal(stats)
            self.insane = self.Insane(stats)
            self.kit = stats['activeKit_SOLO'] if 'activeKit_SOLO' in stats else None
            self.losses = stats['losses_solo'] if 'losses_solo' in stats else None
            self.deaths = stats['deaths_solo'] if 'deaths_solo' in stats else None
            self.survived_players = stats['survived_players_solo'] if 'survived_players_solo' in stats else None
            self.kills = stats['kills_solo'] if 'kills_solo' in stats else None
            self.games_played = stats['games_solo'] if 'games_solo' in stats else None
            self.games_played = stats['games_solo'] if 'games_solo' in stats else None
            self.wins = stats['wins_solo'] if 'wins_solo' in stats else None
            self.assists = stats['assists_solo'] if 'assists_solo' in stats else None
            self.chests_opened = stats['chests_opened_solo'] if 'chests_opened_solo' in stats else None
            self.time_played = stats['time_played_solo'] if 'time_played_solo' in stats else None
            self.fastest_win = stats['fastest_win_solo'] if 'fastest_win_solo' in stats else None
            self.melee_kills = stats['melee_kills_solo'] if 'melee_kills_solo' in stats else None
            self.killstreak = stats['killstreak_solo'] if 'killstreak_solo' in stats else None
            self.winstreak = stats['winstreak_solo'] if 'winstreak_solo' in stats else None
            self.most_kills_game = stats['most_kills_game_solo'] if 'most_kills_game_solo' in stats else None
            self.void_kills = stats['void_kills_solo'] if 'void_kills_solo' in stats else None
            self.longest_bow_shot = stats['longest_bow_shot_solo'] if 'longest_bow_shot_solo' in stats else None
            self.arrows_hit = stats['arrows_hit_solo'] if 'arrows_hit_solo' in stats else None
            self.arrows_shot = stats['arrows_shot_solo'] if 'arrows_shot_solo' in stats else None
            self.longest_bow_kill = stats['longest_bow_kill_solo'] if 'longest_bow_kill_solo' in stats else None

        class Normal(object):
            r"""The player's solo normal SkyWars stats.
    
            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict"""

            def __init__(self, stats: dict):
                self.losses = stats['losses_solo_normal'] if 'losses_solo_normal' in stats else None
                self.deaths = stats['deaths_solo_normal'] if 'deaths_solo_normal' in stats else None
                self.kills = stats['kills_solo_normal'] if 'kills_solo_normal' in stats else None
                self.wins = stats['wins_solo_normal'] if 'wins_solo_normal' in stats else None

        class Insane(object):
            r"""The player's solo insane SkyWars stats.
    
            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict"""

            def __init__(self, stats: dict):
                self.losses = stats['losses_solo_insane'] if 'losses_solo_insane' in stats else None
                self.deaths = stats['deaths_solo_insane'] if 'deaths_solo_insane' in stats else None
                self.kills = stats['kills_solo_insane'] if 'kills_solo_insane' in stats else None
                self.wins = stats['wins_solo_insane'] if 'wins_solo_insane' in stats else None

    class Teams(object):
        r"""The player's teams SkyWars stats.
    
        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict"""

        def __init__(self, stats: dict):
            self.normal = self.Normal(stats)
            self.insane = self.Insane(stats)
            self.kit = stats['activeKit_TEAMS'] if 'activeKit_TEAMS' in stats else None
            self.survived_players = stats['survived_players_team'] if 'survived_players_team' in stats else None
            self.deaths = stats['deaths_team'] if 'deaths_team' in stats else None
            self.assists = stats['assists_team'] if 'assists_team' in stats else None
            self.kills = stats['kills_team'] if 'kills_team' in stats else None
            self.games_played = stats['games_team'] if 'games_team' in stats else None
            self.losses = stats['losses_team'] if 'losses_team' in stats else None
            self.wins = stats['wins_team'] if 'wins_team' in stats else None
            self.chests_opened = stats['chests_opened_team'] if 'chests_opened_team' in stats else None
            self.time_played = stats['time_played_team'] if 'time_played_team' in stats else None
            self.longest_bow_shot = stats['longest_bow_shot_team'] if 'longest_bow_shot_team' in stats else None
            self.fastest_win = stats['fastest_win_team'] if 'fastest_win_team' in stats else None
            self.melee_kills = stats['melee_kills_team'] if 'melee_kills_team' in stats else None
            self.winstreak = stats['winstreak_team'] if 'winstreak_team' in stats else None
            self.arrows_shot = stats['arrows_shot_team'] if 'arrows_shot_team' in stats else None
            self.arrows_hit = stats['arrows_hit_team'] if 'arrows_hit_team' in stats else None
            self.killstreak = stats['killstreak_team'] if 'killstreak_team' in stats else None
            self.most_kills_game = stats['most_kills_game_team'] if 'most_kills_game_team' in stats else None
            self.void_kills = stats['void_kills_team'] if 'void_kills_team' in stats else None
            self.longest_bow_kill = stats['longest_bow_kill_team'] if 'longest_bow_kill_team' in stats else None
            self.bow_kills = stats['bow_kills_team'] if 'bow_kills_team' in stats else None

        class Normal(object):
            r"""The player's teams normal SkyWars stats.
    
            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict"""

            def __init__(self, stats):
                self.deaths = stats['deaths_team_normal'] if 'deaths_team_normal' in stats else None
                self.losses = stats['losses_team_normal'] if 'losses_team_normal' in stats else None
                self.kills = stats['kills_team_normal'] if 'kills_team_normal' in stats else None
                self.wins = stats['wins_team_normal'] if 'wins_team_normal' in stats else None

        class Insane(object):
            r"""The player's teams insane SkyWars stats.
    
            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict"""

            def __init__(self, stats):
                self.deaths = stats['deaths_team_insane'] if 'deaths_team_insane' in stats else None
                self.losses = stats['losses_team_insane'] if 'losses_team_insane' in stats else None
                self.kills = stats['kills_team_insane'] if 'kills_team_insane' in stats else None
                self.wins = stats['wins_team_insane'] if 'wins_team_insane' in stats else None

    class Mega(object):
        r"""The player's mega SkyWars stats.
    
        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict"""

        def __init__(self, stats):
            self.kit = stats['activeKit_MEGA'] if 'activeKit_MEGA' in stats else None
            self.survived_players = stats['survived_players_mega'] if 'survived_players_mega' in stats else None
            self.kills = stats['kills_mega'] if 'kills_mega' in stats else None
            self.deaths = stats['deaths_mega'] if 'deaths_mega' in stats else None
            self.assists = stats['assists_mega'] if 'assists_mega' in stats else None
            self.wins = stats['wins_mega'] if 'wins_mega' in stats else None
            self.games_played = stats['games_mega'] if 'games_mega' in stats else None
            self.longest_bow_shot = stats['longest_bow_shot_mega'] if 'longest_bow_shot_mega' in stats else None
            self.chests_opened = stats['chests_opened_mega'] if 'chests_opened_mega' in stats else None
            self.most_kills = stats['most_kills_game_mega'] if 'most_kills_game_mega' in stats else None
            self.melee_kills = stats['melee_kills_mega'] if 'melee_kills_mega' in stats else None
            self.arrows_shot = stats['arrows_shot_mega'] if 'arrows_shot_mega' in stats else None
            self.arrows_hit = stats['arrows_hit_mega'] if 'arrows_hit_mega' in stats else None
            self.time_played = stats['time_played_mega'] if 'time_played_mega' in stats else None
            self.fastest_win = stats['fastest_win_mega'] if 'fastest_win_mega' in stats else None
            self.winstreak = stats['winstreak_mega'] if 'winstreak_mega' in stats else None
            self.void_kills = stats['void_kills_mega'] if 'void_kills_mega' in stats else None
            self.killstreak = stats['killstreak_mega'] if 'killstreak_mega' in stats else None
            self.mob_kills = stats['mob_kills_mega'] if 'mob_kills_mega' in stats else None

    class Ranked(object):
        r"""The player's ranked SkyWars stats.
    
        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict"""

        def __init__(self, stats):
            self.kit = stats['activeKit_RANKED'] if 'activeKit_RANKED' in stats else None
            self.assists = stats['assists_ranked'] if 'assists_ranked' in stats else None
            self.winstreak = stats['winstreak_ranked'] if 'winstreak_ranked' in stats else None
            self.games_played = stats['games_ranked'] if 'games_ranked' in stats else None
            self.wins = stats['wins_ranked'] if 'wins_ranked' in stats else None
            self.deaths = stats['deaths_ranked'] if 'deaths_ranked' in stats else None
            self.losses = stats['losses_ranked'] if 'losses_ranked' in stats else None
            self.longest_bow_shot = stats['longest_bow_shot_ranked'] if 'longest_bow_shot_ranked' in stats else None
            self.arrows_shot = stats['arrows_shot_ranked'] if 'arrows_shot_ranked' in stats else None
            self.arrows_hit = stats['arrows_hit_ranked'] if 'arrows_hit_ranked' in stats else None
            self.chests_opened = stats['chests_opened_ranked'] if 'chests_opened_ranked' in stats else None
            self.time_played = stats['time_played_ranked'] if 'time_played_ranked' in stats else None
            self.melee_kills = stats['melee_kills_ranked'] if 'melee_kills_ranked' in stats else None
            self.most_kills_game = stats['most_kills_game_ranked'] if 'most_kills_game_ranked' in stats else None
            self.fastest_win = stats['fastest_win_ranked'] if 'fastest_win_ranked' in stats else None
            self.void_kills = stats['void_kills_ranked'] if 'void_kills_ranked' in stats else None
            self.longest_bow_kill = stats['longest_bow_kill_ranked'] if 'longest_bow_kill_ranked' in stats else None
            self.bow_kills = stats['bow_kills_ranked'] if 'bow_kills_ranked' in stats else None

    class Lab(object):
        r"""The player's laboratory SkyWars stats.
    
        :param stats: The raw SkyWars stats data from the API.
        :type stats: dict"""

        def __init__(self, stats: dict):
            self.solo = self.Solo(stats)
            self.teams = self.Teams(stats)
            self.winstreak = stats['win_streak_lab'] if 'win_streak_lab' in stats else None
            self.souls_gathered = stats['souls_gathered_lab'] if 'souls_gathered_lab' in stats else None
            self.survived_playes = stats['survived_players_lab'] if 'survived_players_lab' in stats else None
            self.coins_gained = stats['coins_gained_lab'] if 'coins_gained_lab' in stats else None
            self.kills = stats['kills_lab'] if 'kills_lab' in stats else None
            self.deaths = stats['deaths_lab'] if 'deaths_lab' in stats else None
            self.time_played = stats['time_played_lab'] if 'time_played_lab' in stats else None
            self.chests_opened = stats['chests_opened_lab'] if 'chests_opened_lab' in stats else None
            self.losses = stats['losses_lab'] if 'losses_lab' in stats else None
            self.melee_kills = stats['melee_kills_lab'] if 'melee_kills_lab' in stats else None
            self.quits = stats['quits_lab'] if 'quits_lab' in stats else None
            self.blocks_placed = stats['blocks_placed_lab'] if 'blocks_placed_lab' in stats else None
            self.longest_bow_kill = stats['longest_bow_kill_lab'] if 'longest_bow_kill_lab' in stats else None
            self.blocks_broken = stats['blocks_broken_lab'] if 'blocks_broken_lab' in stats else None
            self.games_played = stats['games_lab'] if 'games_lab' in stats else None
            self.longest_bow_shot = stats['longest_bow_shot_lab'] if 'longest_bow_shot_lab' in stats else None
            self.fastest_win = stats['fastest_win_lab'] if 'fastest_win_lab' in stats else None
            self.void_kills = stats['void_kills_lab'] if 'void_kills_lab' in stats else None
            self.lucky_block_wins = stats['lab_win_lucky_blocks_lab'] if 'lab_win_lucky_blocks_lab' in stats else None
            self.most_kills_game = stats['most_kills_game_lab'] if 'most_kills_game_lab' in stats else None
            self.arrows_hit = stats['arrows_hit_lab'] if 'arrows_hit_lab' in stats else None
            self.wins = stats['wins_lab'] if 'wins_lab' in stats else None
            self.killstreak = stats['killstreak_lab'] if 'killstreak_lab' in stats else None
            self.winstreak = stats['winstreak_lab'] if 'winstreak_lab' in stats else None
            self.arrows_shot = stats['arrows_shot_lab'] if 'arrows_shot_lab' in stats else None
            self.tnt_madness_wins = stats['lab_win_tnt_madness_lab'] if 'lab_win_tnt_madness_lab' in stats else None
            self.pearls_throws = stats['enderpearls_thrown_lab'] if 'enderpearls_thrown_lab' in stats else None
            self.slime_wins = stats['lab_win_slime_lab'] if 'lab_win_slime_lab' in stats else None
            self.assists = stats['assists_lab'] if 'assists_lab' in stats else None
            self.falling_kills = stats['fall_kills_lab'] if 'fall_kills_lab' in stats else None
            self.eggs_thrown = stats['egg_thrown_lab'] if 'egg_thrown_lab' in stats else None
            self.bow_kills = stats['bow_kills_lab'] if 'bow_kills_lab' in stats else None
            self.mob_kills = stats['mob_kills_lab'] if 'mob_kills_lab' in stats else None
            self.rush_wins = stats['lab_win_rush_lab'] if 'lab_win_rush_lab' in stats else None

        class Solo(object):
            r"""The player's solo lab SkyWars stats.

            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict"""

            def __init__(self, stats: dict):
                self.survived_players = stats[
                    'survived_players_lab_solo'] if 'survived_players_lab_solo' in stats else None
                self.chests_opened = stats['chests_opened_lab_solo'] if 'chests_opened_lab_solo' in stats else None
                self.deaths = stats['deaths_lab_solo'] if 'deaths_lab_solo' in stats else None
                self.time_played = stats['time_played_lab_solo'] if 'time_played_lab_solo' in stats else None
                self.losses = stats['losses_lab_solo'] if 'losses_lab_solo' in stats else None
                self.longest_bow_kill = stats[
                    'longest_bow_kill_lab_solo'] if 'longest_bow_kill_lab_solo' in stats else None
                self.games_played = stats['games_lab_solo'] if 'games_lab_solo' in stats else None
                self.melee_kills = stats['melee_kills_lab_solo'] if 'melee_kills_lab_solo' in stats else None
                self.kills = stats['kills_lab_solo'] if 'kills_lab_solo' in stats else None
                self.fastest_win = stats['fastest_win_lab_solo'] if 'fastest_win_lab_solo' in stats else None
                self.longest_bow_shot = stats[
                    'longest_bow_shot_lab_solo'] if 'longest_bow_shot_lab_solo' in stats else None
                self.arrows_shot = stats['arrows_shot_lab_solo'] if 'arrows_shot_lab_solo' in stats else None
                self.winstreak = stats['winstreak_lab_solo'] if 'winstreak_lab_solo' in stats else None
                self.wins = stats['wins_lab_solo'] if 'wins_lab_solo' in stats else None
                self.void_kills = stats['void_kills_lab_solo'] if 'void_kills_lab_solo' in stats else None
                self.most_kills_game = stats[
                    'most_kills_game_lab_solo'] if 'most_kills_game_lab_solo' in stats else None
                self.lucky_block_wins = stats[
                    'lab_win_lucky_blocks_lab_solo'] if 'lab_win_lucky_blocks_lab_solo' in stats else None
                self.killstreak = stats['killstreak_lab_solo'] if 'killstreak_lab_solo' in stats else None
                self.arrows_hit = stats['arrows_hit_lab_solo'] if 'arrows_hit_lab_solo' in stats else None
                self.tnt_madness_wins = stats[
                    'lab_win_tnt_madness_lab_solo'] if 'lab_win_tnt_madness_lab_solo' in stats else None
                self.slime_wins = stats['lab_win_slime_lab_solo'] if 'lab_win_slime_lab_solo' in stats else None
                self.assists = stats['assists_lab_solo'] if 'assists_lab_solo' in stats else None
                self.falling_kills = stats['fall_kills_lab_solo'] if 'fall_kills_lab_solo' in stats else None
                self.mob_kills = stats['mob_kills_lab_solo'] if 'mob_kills_lab_solo' in stats else None
                self.rush_wins = stats['lab_win_rush_lab_solo'] if 'lab_win_rush_lab_solo' in stats else None

        class Teams(object):
            r"""The player's teams lab SkyWars stats.

            :param stats: The raw SkyWars stats data from the API.
            :type stats: dict"""

            def __init__(self, stats: dict):
                self.survived_playes = stats[
                    'survived_players_lab_team'] if 'survived_players_lab_team' in stats else None
                self.losses = stats['losses_lab_team'] if 'losses_lab_team' in stats else None
                self.melee_kills = stats['melee_kills_lab_team'] if 'melee_kills_lab_team' in stats else None
                self.kills = stats['kills_lab_team'] if 'kills_lab_team' in stats else None
                self.deaths = stats['deaths_lab_team'] if 'deaths_lab_team' in stats else None
                self.chests_opened = stats['chests_opened_lab_team'] if 'chests_opened_lab_team' in stats else None
                self.time_played = stats['time_played_lab_team'] if 'time_played_lab_team' in stats else None
                self.arrows_shot = stats['arrows_shot_lab_team'] if 'arrows_shot_lab_team' in stats else None
                self.fastest_win = stats['fastest_win_lab_team'] if 'fastest_win_lab_team' in stats else None
                self.games_played = stats['games_lab_team'] if 'games_lab_team' in stats else None
                self.killstreak = stats['killstreak_lab_team'] if 'killstreak_lab_team' in stats else None
                self.slime_wins = stats['lab_win_slime_lab_team'] if 'lab_win_slime_lab_team' in stats else None
                self.void_kills = stats['void_kills_lab_team'] if 'void_kills_lab_team' in stats else None
                self.wins = stats['wins_lab_team'] if 'wins_lab_team' in stats else None
                self.assists = stats['assists_lab_team'] if 'assists_lab_team' in stats else None
                self.lucky_block_wins = stats[
                    'lab_win_lucky_blocks_lab_team'] if 'lab_win_lucky_blocks_lab_team' in stats else None
                self.longest_bow_kill = stats[
                    'longest_bow_kill_lab_team'] if 'longest_bow_kill_lab_team' in stats else None
                self.most_kills_game = stats[
                    'most_kills_game_lab_team'] if 'most_kills_game_lab_team' in stats else None
                self.arrows_hit = stats['arrows_hit_lab_team'] if 'arrows_hit_lab_team' in stats else None
                self.longest_bow_shot = stats[
                    'longest_bow_shot_lab_team'] if 'longest_bow_shot_lab_team' in stats else None
                self.bow_kills = stats['bow_kills_lab_team'] if 'bow_kills_lab_team' in stats else None
                self.falling_kills = stats['fall_kills_lab_team'] if 'fall_kills_lab_team' in stats else None
                self.rush_wins = stats['lab_win_rush_lab_team'] if 'lab_win_rush_lab_team' in stats else None
