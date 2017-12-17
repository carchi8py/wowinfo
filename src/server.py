
import apikey
import requests


class Server:
    def __init__(self, connected_realm_id, locale):
        self.connected_realm_id = connected_realm_id
        self.locale = locale

    def get_current_leader_boards(self):
        url = "https://" + self.locale + \
              ".api.battle.net/data/wow/connected-realm/" + self.connected_realm_id + \
              "/mythic-leaderboard/?namespace=dynamic-us&locale=en_US&access_token=" + apikey.access
        return requests.get(url)