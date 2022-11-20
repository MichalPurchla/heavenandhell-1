"""initial_revision

Revision ID: 315798f12265
Revises: 
Create Date: 2022-11-20 11:31:45.209378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '315798f12265'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'students',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('students')
