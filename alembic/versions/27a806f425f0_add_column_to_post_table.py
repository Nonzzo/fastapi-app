"""add column to post table

Revision ID: 27a806f425f0
Revises: ead7a401ca44
Create Date: 2022-12-06 20:23:44.062491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27a806f425f0'
down_revision = 'ead7a401ca44'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
