# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

import os
from dotenv import load_dotenv
load_dotenv()

engine = create_engine(os.environ.get('db_uri'))
connection = engine.connect()

Base = declarative_base() # base class for declarative class definitions
metadata = Base.metadata

# db = SQLAlchemy()
# metadata = db.metadata

class Player(Base):
  """
  Player Model
  """
  __tablename__ = "players"

  nba_id = Column(Integer, primary_key=True)
  last_name = Column(String(100), nullable=False)
  first_name = Column(String(100), nullable=False)
  is_active = Column(Boolean, nullable = False)

  def __init__(self, **kwargs):
    """
    Initializes a player object
    """
    self.nba_id = kwargs.get("nba_id")
    self.last_name = kwargs.get("last_name")
    self.first_name = kwargs.get("first_name")
    self.is_active = kwargs.get("is_active")

  def serialize(self):
    """
    Serializes a course object
    """
    return {"nba_id": self.nba_id, 
            "last_name": self.last_name, 
            "first_name": self.first_name,
            "is_active": self.is_active}
  
class PlayerInfo(Base):
  """
  Player_Info Model
  """
  __tablename__ = "player_info"

  nba_id = Column(Integer, primary_key=True)
  position = Column(String(100))
  height = Column(String(10))
  weight = Column(Integer)
  college = Column(String(100))
  country = Column(String(100))
  draft_year = Column(Integer)
  draft_round = Column(Integer)
  draft_number = Column(Integer)
  from_year = Column(Integer)
  to_year = Column(Integer)

  def __init__(self, **kwargs):
    """
    Initializes a player info object
    """
    self.nba_id = kwargs.get("id")
    self.position = kwargs.get("position", "")
    self.height = kwargs.get("height", "")
    self.weight = kwargs.get("weight", "")
    self.college = kwargs.get("college", "")
    self.country = kwargs.get("country", "")
    self.draft_year = kwargs.get("draft_year", "")
    self.draft_round = kwargs.get("draft_round", "")
    self.draft_number = kwargs.get("draft_number", "")
    self.from_year = kwargs.get("from_year", "")
    self.to_year = kwargs.get("to_year", "")

  def serialize(self):
    """
    Serializes a course object
    """
    return {"nba_id": self.nba_id,
            "position": self.position,
            "height": self.height,
            "weight": self.weight,
            "college": self.college,
            "country": self.country,
            "draft_year": self.draft_year, 
            "draft_round": self.draft_round,
            "draft_number": self.draft_number,
            "from_year": self.from_year,
            "to_year": self.to_year}

Base.metadata.create_all(engine)

# metadata = MetaData()
# metadata.reflect(bind=engine)

# players = metadata.tables['playerinfo']
# players.drop(engine)
