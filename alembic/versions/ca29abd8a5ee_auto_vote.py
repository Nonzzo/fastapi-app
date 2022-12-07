"""auto-vote

Revision ID: ca29abd8a5ee
Revises: fa36cb9add37
Create Date: 2022-12-07 01:01:21.751437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca29abd8a5ee'
down_revision = 'fa36cb9add37'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
)
    


def downgrade() -> None:
    op.drop_table('votes')
