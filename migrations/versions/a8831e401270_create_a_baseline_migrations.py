"""Create a baseline migrations

Revision ID: a8831e401270
Revises: Foreign Key on player_info on nba_id
Create Date: 2024-01-03 20:50:22.017191

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8831e401270'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
  # Creates foreign key where player_info references players for nba_id
  op.create_foreign_key("fk_player_info", 
                      "player_info",
                      "players",
                      ["nba_id"],
                      ["nba_id"])

def downgrade() -> None:
  op.drop_constraint("fk_player_info",
                      "player_info",
                       "foreignkey")