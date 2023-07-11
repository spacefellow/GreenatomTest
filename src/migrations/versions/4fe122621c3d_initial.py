"""initial

Revision ID: 4fe122621c3d
Revises: 
Create Date: 2023-07-09 18:11:27.328723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fe122621c3d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('film',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('rating', sa.Double(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_film_id'), 'film', ['id'], unique=False)
    op.create_table('review',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('text', sa.TEXT(), nullable=False),
    sa.Column('film_id', sa.UUID(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['film_id'], ['film.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_review_id'), 'review', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_review_id'), table_name='review')
    op.drop_table('review')
    op.drop_index(op.f('ix_film_id'), table_name='film')
    op.drop_table('film')
    # ### end Alembic commands ###
