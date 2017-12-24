
import apikey
import requests
import server
import sys

from sqlalchemy import exists
from database import Base, Character_DB, Server_DB
import db

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

    def add_character(self):
        if not self.does_charater_exists():
            self.add_character_to_db()

    def does_charater_exists(self):
        for char in db.session.query(Character_DB).filter_by(name = self.name):
            if char.server.name == self.realm:
                return True
        return False

    def add_character_to_db(self):
        print("Adding charater: %s from realm: %s" % (self.name, self.realm))
        server_obj = db.session.query(Server_DB).filter_by(name = self.realm).first()
        new_character = Character_DB(name = self.name, server = server_obj)
        db.session.add(new_character)
        db.session.commit()