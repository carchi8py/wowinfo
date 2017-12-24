from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Character_DB(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    server_id = Column(Integer, ForeignKey('server.id'))
    server = relationship("Server_DB", back_populates="characters")

class Server_DB(Base):
    __tablename__ = 'server'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    characters = relationship("Character_DB", back_populates="server")

class Group_DB(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)

engine = create_engine('sqlite:///db.db')
Base.metadata.create_all(engine)