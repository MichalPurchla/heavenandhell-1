"""online_course

Revision ID: 5903cb739aa6
Revises: b2e59b412e64
Create Date: 2022-11-20 11:59:55.572696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5903cb739aa6'
down_revision = 'b2e59b412e64'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'online_courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('url', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('online_courses')
