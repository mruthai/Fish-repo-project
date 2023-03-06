"""hey hey

Revision ID: c3f9908f027e
Revises: 795adbbcccba
Create Date: 2023-03-04 13:28:55.537677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3f9908f027e'
down_revision = '795adbbcccba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classification', sa.String(length=64), nullable=False),
    sa.Column('species', sa.String(length=64), nullable=False),
    sa.Column('breed', sa.String(length=64), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('amount'),
    sa.UniqueConstraint('breed'),
    sa.UniqueConstraint('classification'),
    sa.UniqueConstraint('species')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('animal')
    # ### end Alembic commands ###
