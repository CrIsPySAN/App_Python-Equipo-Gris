"""Add OAuth model and update User model

Revision ID: b26cedce204e
Revises: 5b7ced8cef1a
Create Date: 2025-01-28 21:02:40.550874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b26cedce204e'
down_revision = '5b7ced8cef1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flask_dance_oauth',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('provider', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('token', sa.JSON(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('facebook_id', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('google_id', sa.String(length=120), nullable=True))
        batch_op.create_unique_constraint(None, ['facebook_id'])
        batch_op.create_unique_constraint(None, ['google_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('google_id')
        batch_op.drop_column('facebook_id')

    op.drop_table('flask_dance_oauth')
    # ### end Alembic commands ###
