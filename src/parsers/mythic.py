import json
import requests
import apikey
import sys

def parse_leaderboards(leaderboards):
    """
    Get all the current leaderboard, and split them up by Dungeon so we can look at them one by one
    :param leaderboards:
    :return:
    """
    leaderboards = json.loads(leaderboards)
    return_dungeons = []
    for leaderboard in leaderboards["current_leaderboards"]:
        dungeons = json.dumps(leaderboard["key"]["href"])
        return_dungeons.append(dungeons)
    return return_dungeons

def get_dungeon_leaderboard(dungeon):
    """
    Return the top 100 group to complete a sepcific dungeon

    :param dungeon: The Dungeon URL
    :return: The JSON of the top 100 groups
    """
    dungeon = dungeon.split('"')[1]
    dungeon_leaderboard = requests.get(dungeon + "&access_token=" + apikey.access).text
    dungeon_leaderboard = json.loads(dungeon_leaderboard)
    return dungeon_leaderboard

def get_dungeon_name(dungeon_leaderboard):
    return dungeon_leaderboard["map"]