"""empty message

Revision ID: af661d230724
Revises:
Create Date: 2023-03-11 17:37:16.284035

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = 'af661d230724'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(
                        length=40), nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.Column('hashed_password', sa.String(
                        length=255), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('username')
                    )
    op.create_table('exercises',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('description', sa.String(
                        length=10000), nullable=False),
                    sa.Column('motion_img_url', sa.String(
                        length=255), nullable=True),
                    sa.Column('public', sa.Boolean(), nullable=False),
                    sa.Column('creator_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('routines',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('description', sa.String(
                        length=10000), nullable=False),
                    sa.Column('public', sa.Boolean(), nullable=False),
                    sa.Column('creator_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('routine_exercises',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('routine_id', sa.Integer(), nullable=False),
                    sa.Column('exercise_id', sa.Integer(), nullable=False),
                    sa.Column('instructions', sa.String(
                        length=10000), nullable=True),
                    sa.Column('creator_id', sa.Integer(), nullable=False),
                    sa.Column('order', sa.Integer(), nullable=False),
                    sa.Column('target_sets_count',
                              sa.Integer(), nullable=False),
                    sa.Column('target_reps_count',
                              sa.Integer(), nullable=False),
                    sa.Column('rest_seconds', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], ),
                    sa.ForeignKeyConstraint(
                        ['exercise_id'], ['exercises.id'], ),
                    sa.ForeignKeyConstraint(['routine_id'], ['routines.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('workout_sessions',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('public', sa.Boolean(), nullable=False),
                    sa.Column('creator_id', sa.Integer(), nullable=False),
                    sa.Column('routine_id', sa.Integer(), nullable=False),
                    sa.Column('notes', sa.String(length=10000), nullable=True),
                    sa.Column('date', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], ),
                    sa.ForeignKeyConstraint(['routine_id'], ['routines.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('workout_session_steps',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('workout_session_id',
                              sa.Integer(), nullable=False),
                    sa.Column('exercise_id', sa.Integer(), nullable=False),
                    sa.Column('instructions', sa.String(
                        length=10000), nullable=True),
                    sa.Column('target_reps_count',
                              sa.Integer(), nullable=True),
                    sa.Column('target_sets_count',
                              sa.Integer(), nullable=True),
                    sa.Column('rest_seconds', sa.Integer(), nullable=True),
                    sa.Column('order', sa.Integer(), nullable=False),
                    sa.Column('creator_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], ),
                    sa.ForeignKeyConstraint(
                        ['exercise_id'], ['exercises.id'], ),
                    sa.ForeignKeyConstraint(['workout_session_id'], [
                        'workout_sessions.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('workout_session_step_results',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('workout_session_step_id',
                              sa.Integer(), nullable=False),
                    sa.Column('actual_reps_count',
                              sa.Integer(), nullable=True),
                    sa.Column('actual_weight', sa.Float(), nullable=True),
                    sa.Column('creator_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], ),
                    sa.ForeignKeyConstraint(['workout_session_step_id'], [
                        'workout_session_steps.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###
    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE exercises SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE routines SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE routine_exercises SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE workout_sessions SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE workout_session_steps SET SCHEMA {SCHEMA};")
        op.execute(
            f"ALTER TABLE workout_session_step_results SET SCHEMA {SCHEMA};")


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workout_session_step_results')
    op.drop_table('workout_session_steps')
    op.drop_table('workout_sessions')
    op.drop_table('routine_exercises')
    op.drop_table('routines')
    op.drop_table('exercises')
    op.drop_table('users')
    # ### end Alembic commands ###
