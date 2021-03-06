"""empty message

Revision ID: 211de0792902
Revises: None
Create Date: 2015-02-23 12:11:52.187729

"""

# revision identifiers, used by Alembic.
revision = '211de0792902'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notes')
    ### end Alembic commands ###
