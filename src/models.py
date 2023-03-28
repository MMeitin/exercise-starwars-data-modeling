import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    subscription_date = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    users = relationship('user')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('user')

class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    episode_id = Column(Integer, nullable=False)
    opening_crawl = Column(String(1000), nullable=False)

# La tabla de usuarios tiene una relación uno a muchos con las tablas de planetas y personajes. 
# La tabla de planetas y la tabla de personajes tienen una relación muchos a uno con la tabla de usuarios. 
# La tabla de películas no tiene relaciones con otras tablas.

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
