from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
import os
from dotenv import load_dotenv

load_dotenv() # environment variables

engine = create_engine(f"mysql+mysqlconnector://{os.environ.get('user')}:{os.environ.get('passwd')}@{os.environ.get('host')}/nbaplayers")
connection = engine.connect()

Base = declarative_base() # base class for declarative class definitions

class Player(Base):
  """
  Player Model
  """
  __tablename__ = 'players'

  nbaid = Column(Integer, primary_key=True)
  lastName = Column(String(100), nullable=False)
  firstName = Column(String(100), nullable=False)
  isActive = Column(Boolean, nullable = False)

  def __init__(self, **kwargs):
    """
    Initializes a player object
    """
    self.nbaid = kwargs.get("id")
    self.lastName = kwargs.get("lastName")
    self.firstName = kwargs.get("firstName")
    self.isActive = kwargs.get("isActive")

    def serialize(self):
      """
      Serializes a course object
      """
      return {"nbaid": self.nbaid, 
              "lastName": self.lastName, 
              "firstName": self.firstName,
              "isActive": self.isActive}
  
class PlayerInfo(Base):
  """
  PlayerInfo Model
  """
  __tablename__ = "playerInfo"

  nbaid = Column(Integer, primary_key=True)
  position = Column(String(100))
  height = Column(String(10))
  weight = Column(Integer)
  college = Column(String(100))
  country = Column(String(100))
  draftYear = Column(Integer)
  draftRound = Column(Integer)
  draftNumber = Column(Integer)
  fromYear = Column(Integer)
  toYear = Column(Integer)

  def __init__(self, **kwargs):
    """
    Initializes a player info object
    """
    self.nbaid = kwargs.get("id")
    self.position = kwargs.get("position", "")
    self.height = kwargs.get("height", "")
    self.weight = kwargs.get("weight", "")
    self.college = kwargs.get("college", "")
    self.country = kwargs.get("country", "")
    self.draftYear = kwargs.get("draftYear", "")
    self.draftRound = kwargs.get("draftRound", "")
    self.draftNumber = kwargs.get("draftNumber", "")
    self.fromYear = kwargs.get("fromYear", "")
    self.toYear = kwargs.get("toYear", "")

  def serialize(self):
    """
    Serializes a course object
    """
    return {"nbaid": self.nbaid, 
            "draftYear": self.draftYear, 
            "draftRound": self.draftRound,
            "draftNumber": self.draftNumber,
            "fromYear": self.fromYear,
            "toYear": self.toYear}

Base.metadata.create_all(engine)

# FOREIGN KEY

# Deleting a Table
# metadata = MetaData()
# metadata.reflect(bind=engine)

# players = metadata.tables['players']
# players.drop(engine)
