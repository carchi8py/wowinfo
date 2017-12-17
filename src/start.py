from character import Character
from server import Server

char = Character("wyrmrest-accord", "magebears", "us")
print(char.getCharaterInfo().text)

server = Server("1171", "us")
print(server.get_current_leader_boards().text)