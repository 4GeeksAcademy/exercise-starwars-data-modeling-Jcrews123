import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorites(Base):
    __tablename__ = 'favorites'
    user_uid = Column(Integer, ForeignKey("user.uid"), primary_key=True, )
    people_uid = Column(Integer, ForeignKey('people.uid'))
    planets_uid = Column(Integer, ForeignKey('planets.uid'))
    species_uid = Column(Integer, ForeignKey('species.uid'))

class User(Base):
    __tablename__ = 'user'
    uid = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    created = Column(String(50))
           
class People(Base):
    __tablename__ = 'people'
    uid = Column(Integer, primary_key=True)
    _id = Column(String(50), nullable=False)
    name = Column(String(250), nullable=False)
    # height = Column(float)
    mass = Column(Integer)
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))
    birth_year = Column(String(20))
    gender = Column(String(20))
    created = Column(String(50))
    edited = Column(String(50))
    homeworld = Column(String(50), ForeignKey("planets.uid"))
    url = Column(String(50), nullable=False)
    description = Column(String(100))

class Planets(Base):
    __tablename__ = 'planets'
    uid = Column(Integer, primary_key=True)
    _id = Column(String(50), nullable=False)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(50))
    population = Column(Integer)
    climate = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(Integer)
    created = Column(String(100))
    description = Column(String(100))
    url = Column(String(50))
    
class Species(Base):
    __tablename__ = 'species'
    uid = Column(Integer, primary_key=True)
    _id = Column(String(50), nullable=False)
    name = Column(String(250), nullable=False)
    classification = Column(String(50))
    designation = Column(String(50))
    average_height = Column(Integer)
    average_lifespan = Column(Integer)
    hair_colors = Column(String(100))
    skin_colors = Column(String(100))
    eye_colors = Column(String(50))
    homeworld = Column(String(50),ForeignKey("planets.uid"))
    language = Column(String(50))
    people = Column(String(300))
    created = Column(String(50))
    edited = Column(String(50))
    url = Column(String(50))
    description = Column(String(50))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
