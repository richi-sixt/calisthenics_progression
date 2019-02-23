"""Exercises

Revision ID: f78156f3089b
Revises: d61ecddac82f
Create Date: 2019-02-07 11:27:02.289963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f78156f3089b'
down_revision = 'd61ecddac82f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('workout_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['workout_id'], ['workout.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_exercises_title'), 'exercises', ['title'], unique=False)
    op.create_table('exercise',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('workout_id', sa.Integer(), nullable=False),
    sa.Column('exercise_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercises.id'], ),
    sa.ForeignKeyConstraint(['workout_id'], ['workout.id'], ),
    sa.PrimaryKeyConstraint('id', 'workout_id'),
    sa.UniqueConstraint('order')
    )
    op.create_table('set',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('reps', sa.Integer(), nullable=True),
    sa.Column('exercise_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercise.id'], ),
    sa.PrimaryKeyConstraint('id', 'exercise_id'),
    sa.UniqueConstraint('order')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('set')
    op.drop_table('exercise')
    op.drop_index(op.f('ix_exercises_title'), table_name='exercises')
    op.drop_table('exercises')
    # ### end Alembic commands ###