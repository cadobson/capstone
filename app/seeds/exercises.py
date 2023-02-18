from app.models import db, Exercise, environment, SCHEMA


# Adds a few demo exercises, which will be owned by the administrator
def seed_exercises():
    bench_press = Exercise(
        name="Bench Press", description="A standard powerlifting exercise for the chest, shoulders, and arms.", motion_img_url=None, public=True, creator_id=1)
    dead_lift = Exercise(
        name="Dead Lift", description="A standard powerlifting exercise for the back, legs, and arms.", motion_img_url=None, public=True, creator_id=1)
    squat = Exercise(
        name="Squat", description="A standard powerlifting exercise for the legs and core.", motion_img_url=None, public=True, creator_id=1)
    overhead_press = Exercise(
        name="Overhead Press", description="A standard powerlifting exercise for the shoulders and arms.", motion_img_url=None, public=True, creator_id=1)
    pull_up = Exercise(
        name="Pull Up", description="A classic, low-equpiment exercise for the back and arms.", motion_img_url=None, public=True, creator_id=1)
    push_up = Exercise(
        name="Push Up", description="A classic, zero-equpiment exercise for the chest and arms.", motion_img_url=None, public=True, creator_id=1)

    db.session.add(bench_press)
    db.session.add(dead_lift)
    db.session.add(squat)
    db.session.add(overhead_press)
    db.session.add(pull_up)
    db.session.add(push_up)
    db.session.commit()


def undo_exercises():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.exercises RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM exercises")

    db.session.commit()
