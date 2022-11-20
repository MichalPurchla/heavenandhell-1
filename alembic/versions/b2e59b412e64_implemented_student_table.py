"""implemented_student_table

Revision ID: b2e59b412e64
Revises: 315798f12265
Create Date: 2022-11-20 11:43:45.816244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2e59b412e64'
down_revision = '315798f12265'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('students', sa.Column('first_name', sa.String(length=50), nullable=False))
    op.add_column('students', sa.Column('last_name', sa.String(length=50), nullable=False))
    op.add_column('students', sa.Column('pesel', sa.String(length=11), nullable=False))
    op.add_column('students', sa.Column('phone', sa.String(length=20), nullable=True))
    op.add_column('students', sa.Column('address', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'students', ['pesel'])


def downgrade() -> None:
    op.drop_constraint(None, 'students', type_='unique')
    op.drop_column('students', 'address')
    op.drop_column('students', 'phone')
    op.drop_column('students', 'pesel')
    op.drop_column('students', 'last_name')
    op.drop_column('students', 'first_name')
