from character import Character
from server import Server
import parsers.mythic as mythic
import sys

server = Server("1171", "us")
charaters = {}
leaderboards = server.get_current_leaderboards()
dungeons = mythic.parse_leaderboards(leaderboards)
for dungeon in dungeons:
    dungeon_leaderboard = mythic.get_dungeon_leaderboard(dungeon)
    dungeon_name = dungeon_leaderboard["map"]["name"]["en_US"]
    leading_groups = dungeon_leaderboard["leading_groups"]
    for group in leading_groups:
        duration = group["duration"]
        level = group["keystone_level"]
        memebers = group["members"]
        for memeber in memebers:
            character_name = memeber["profile"]["name"]
            realm_name = memeber["profile"]["realm"]["slug"]
            server.add_server(realm_name)
            if not character_name + "-" + realm_name in charaters:
                #TODO replace us with the vaule in side the json file
                new_charater = Character(realm_name, character_name, "us")
                new_charater.add_character()
                charaters[character_name + "-" + realm_name] = new_charater