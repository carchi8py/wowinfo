from character import Character
from server import Server
from group import Group
import parsers.mythic as mythic
import sys

#TODO tie in this server class, with the servers we are finding below
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
        new_group = Group(duration, level)
        new_group.add_group()
        memebers = group["members"]
        for memeber in memebers:
            character_name = memeber["profile"]["name"]
            realm_name = memeber["profile"]["realm"]["slug"]
            faction = memeber["faction"]["type"]
            player_spec = memeber["specialization"]["id"]
            server.add_server(realm_name)
            if not character_name + "-" + realm_name in charaters:
                #TODO replace us with the vaule in side the json file
                new_charater = Character(realm_name, character_name, faction, player_spec, "us")
                new_charater.add_character()
                charaters[character_name + "-" + realm_name] = new_charater
            new_group.add_charater_to_group(charaters[character_name + '-' + realm_name])