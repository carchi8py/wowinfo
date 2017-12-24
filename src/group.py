
import apikey
import requests

from sqlalchemy import exists
from database import Base, Character_DB, Server_DB, Group_DB
import db

class Group:
    def __init__(self, duration, level):
        self.duration = duration
        self.level = level

    def add_group(self):
        if not self.does_group_exists():
            self.add_group_to_db()

    def does_group_exists(self):
        if db.session.query(exists().where(Group_DB.duration == self.duration)).scalar():
            for group in db.session.query(Group_DB).filter_by(duration = self.duration):
                if group.level == self.level:
                    return True
        return False

    def add_group_to_db(self):
        print("Adding Group with %s on level %s" % (str(self.duration), str(self.level)))
        new_group = Group_DB(duration = self.duration, level = self.level)
        db.session.add(new_group)
        db.session.commit()
