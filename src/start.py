from character import Character
from server import Server

char = Character("wyrmrest-accord", "magebears", "us")
print(char.get_player().text)

server = Server("1171", "us")
print(server.get_current_leaderboards().text)