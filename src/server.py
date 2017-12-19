
import apikey
import requests

class Server:
    def __init__(self, connected_realm_id, locale):
        self.connected_realm_id = connected_realm_id
        self.locale = locale

    def get_current_leaderboards(self):
        """
        Get the list of all current leader boards for each dungeon
        
        :return: json file with link to each leaderboard for the server
        """
        url = "https://" + self.locale + \
              ".api.battle.net/data/wow/connected-realm/" + self.connected_realm_id + \
              "/mythic-leaderboard/?namespace=dynamic-us&locale=en_US&access_token=" + apikey.access
        return requests.get(url)