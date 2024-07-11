"""task

Revision ID: 77bd1fbc2e12
Revises: 
Create Date: 2024-07-11 19:21:19.699088

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '77bd1fbc2e12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
        batch_op.alter_column('image',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               nullable=True,
               existing_server_default=sa.text('current_timestamp()'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('current_timestamp()'))

    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('user_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)

    # ### end Alembic commands ###
