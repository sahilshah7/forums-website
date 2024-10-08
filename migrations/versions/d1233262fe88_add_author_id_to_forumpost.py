"""Add author_id to ForumPost

Revision ID: d1233262fe88
Revises: 757668456b93
Create Date: 2024-09-14 16:25:27.714003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1233262fe88'
down_revision = '757668456b93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('forum_post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_forum_post_author_id_user'), 'user', ['author_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('forum_post', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_forum_post_author_id_user'), type_='foreignkey')
        batch_op.drop_column('author_id')

    # ### end Alembic commands ###
