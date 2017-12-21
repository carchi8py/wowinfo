
import apikey
import requests

from sqlalchemy import exists
from database import Base, Character_DB, Server_DB
import db


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
        return requests.get(url).text

    def add_server(self, realm_name):
        # first step check to see if the server is already in the database
        if self.does_server_exists(realm_name):
            self.add_server_to_db(realm_name)


    def does_server_exists(self, realm_name):
        if not db.session.query(exists().where(Server_DB.name == realm_name)).scalar():
            return False
        return True

    def add_server_to_db(self, realm_name):
        new_server = Server_DB(name = realm_name)
        db.session.add(new_server)
        db.session.commit()



