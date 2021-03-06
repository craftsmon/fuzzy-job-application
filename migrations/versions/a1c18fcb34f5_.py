"""empty message

Revision ID: a1c18fcb34f5
Revises: 1ba415ecfdf6
Create Date: 2017-06-06 20:27:22.028344

"""
from alembic import op
import sqlalchemy as sa
import app
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a1c18fcb34f5'
down_revision = '1ba415ecfdf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('applications_ibfk_3', 'applications', type_='foreignkey')
    op.drop_column('applications', 'skill_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('applications', sa.Column('skill_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('applications_ibfk_3', 'applications', 'skills', ['skill_id'], ['id'])
    # ### end Alembic commands ###
