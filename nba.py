from nba_api.stats.static import players
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
from db import Player

load_dotenv()

engine = create_engine(f"mysql+mysqlconnector://{os.environ.get('user')}:{os.environ.get('passwd')}@{os.environ.get('host')}/nbaplayers")

def fill_players_table():
  """
  Loads Players Table with all current and historic NBA players
  """
  Session = sessionmaker(bind=engine)
  session = Session()
  all_players = players.get_players()
  try:
    for i, row in enumerate(all_players):
      new_player = Player(nba_id = row['id'], first_name = row['first_name'], 
                        last_name = row['last_name'], is_active = row['is_active'])
      session.add(new_player)
      if i % 100 == 0: print(f'Added {i} players')
    session.commit()
    print(f'All {i} players added')
  except Exception as e:
    print(f'An error occurred: {e}')
    session.rollback()
  finally:
    session.close()

fill_players_table()