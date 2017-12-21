from character import Character
from server import Server
import parsers.mythic as mythic

server = Server("1171", "us")
leaderboards = server.get_current_leaderboards()
dungeons = mythic.parse_leaderboards(leaderboards)
for dungeon in dungeons:
    leading_groups = mythic.get_dungeon_leaderboard(dungeon)
    for group in leading_groups:
        print(group)
        print("----")
        memebers = group["members"]
        for memeber in memebers:
            #print(memeber["profile"])
            if memeber["profile"]["name"] == "Magebears":
                print("W00t")