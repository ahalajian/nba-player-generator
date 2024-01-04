from flask import Flask, request
import requests
import json

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.sql.functions import random

from db import Player

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('db_uri')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine(os.environ.get('db_uri'))

def success_response(data, code=200):
    """
    Success response
    """
    return json.dumps(data), code

def failure_response(message, code=400):
    """
    Failure response
    """
    return json.dumps({"error": message}), code

@app.route('/api/player/<int:id>/', methods=['GET'])
def get_player(id):
  with Session(engine) as session:
    player = session.query(Player).filter_by(nba_id=id).first()
    if player is None:
      return failure_response("Player not found.")
    return success_response(player.serialize())

@app.route('/api/random/', methods=['GET'])
def get_random_players():
  with Session(engine) as session:
    num_players = request.args.get("numplayers")
    type = request.args.get("type")
    
    if num_players is None or type is None:
      return failure_response("Missing a field")
    
    filter_conditions = {
            "all": True,
            "current": Player.is_active == True,
            "historic": Player.is_active == False
        }
    where_clause = filter_conditions.get(type)

    players = session.query(Player).where(where_clause).order_by(random()).limit(num_players).all()

    return success_response([player.serialize() for player in players])


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000, debug=True)