from flask.cli import AppGroup
from .users import seed_users, undo_users
from .exercises import seed_exercises, undo_exercises
from .routines import seed_routines, undo_routines
from .routines_exercises import seed_routines_exercises, undo_routines_exercises

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# # Creates the `flask seed all` command
# @seed_commands.command('all')
# def seed():
#     if environment == 'production':
#         # Before seeding in production, you want to run the seed undo
#         # command, which will  truncate all tables prefixed with
#         # the schema name (see comment in users.py undo_users function).
#         # Make sure to add all your other model's undo functions below
#         undo_users()
#     seed_users()
#     # Add other seed functions here

@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding, truncate all tables prefixed with schema name
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
        # Add a truncate command here for every table that will be seeded.
        db.session.commit()
    seed_users()
    seed_exercises()
    seed_routines()
    seed_routines_exercises()
    # Add other seed functions here

# Creates the `flask seed undo` command


@seed_commands.command('undo')
def undo():
    undo_users()
    undo_exercises()
    undo_routines()
    undo_routines_exercises()
    # Add other undo functions here
