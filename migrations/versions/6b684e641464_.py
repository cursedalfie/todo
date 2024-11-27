"""empty message

Revision ID: 6b684e641464
Revises: 2aa87798dfe0
Create Date: 2024-11-06 18:10:00.891015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b684e641464'
down_revision: Union[str, None] = '2aa87798dfe0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('is_completed', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'is_completed')
    # ### end Alembic commands ###