from character import Character
from server import Server
import parsers.mythic as mythic
import sys

server = Server("1171", "us")
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
            #print(memeber["profile"])
            if memeber["profile"]["name"] == "Pyroblast":
                print("W00t")