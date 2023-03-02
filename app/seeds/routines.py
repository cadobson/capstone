from app.models import db, Routine, environment, SCHEMA


def seed_routines():
    startingstrength = Routine(
        name='Starting Strength', description='The most popular introductory strength training program in the world.', public=True, creator_id=1)
    push = Routine(
        name='Push', description='A routine for working your chest, shoulders, and triceps. "Push" refers to the pushing motions of the exercises. This routine is often paired with a Pull routine and a leg routine, performed on alternating days.', public=True, creator_id=1)

    db.session.add(startingstrength)
    db.session.add(push)
    db.session.commit()


def undo_routines():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.routines RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM routines")

    db.session.commit()
