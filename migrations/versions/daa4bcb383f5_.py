"""empty message

Revision ID: daa4bcb383f5
Revises: 
Create Date: 2022-06-21 18:34:54.701264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daa4bcb383f5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('urlvalues', sa.Column('company', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('urlvalues', 'company')
    # ### end Alembic commands ###
