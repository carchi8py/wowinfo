
import apikey
import requests

class Character:
    def __init__(self, realm, name, locale):
        self.realm = realm
        self.name = name
        self.locale = locale

    def get_player(self):
        """
        Get all the information about a Character

        :return:
        """
        url = "https://" + self.locale + \
            ".api.battle.net/wow/character/" + self.realm + "/" + self.name + \
              "?fields=items,quests,achievements,audit,progression,feed,professions,talents&?locale=en_US&apikey=" + \
        apikey.key
        return requests.get(url).text