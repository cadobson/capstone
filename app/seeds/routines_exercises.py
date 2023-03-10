from app.models import db, RoutineExercise, environment, SCHEMA


def seed_routines_exercises():
    # Starting Strength
    ss0 = RoutineExercise(
        routine_id=1, exercise_id=3, instructions="Warm up with half of your expected weight.", creator_id=1, order=1, target_sets_count=3, target_reps_count=5, rest_seconds=120)
    ss1 = RoutineExercise(
        routine_id=1, exercise_id=1, instructions=None, creator_id=1, order=2, target_sets_count=3, target_reps_count=5, rest_seconds=120)
    ss2 = RoutineExercise(
        routine_id=1, exercise_id=2, instructions=None, creator_id=1, order=3, target_sets_count=1, target_reps_count=5, rest_seconds=120)
    ss3 = RoutineExercise(
        routine_id=1, exercise_id=3, instructions=None, creator_id=1, order=4, target_sets_count=3, target_reps_count=5, rest_seconds=120)

    # Push
    push0 = RoutineExercise(
        routine_id=2, exercise_id=1, instructions="Warm up with half of your expected weight.", creator_id=1, order=1, target_sets_count=3, target_reps_count=5, rest_seconds=120)
    push1 = RoutineExercise(
        routine_id=2, exercise_id=4, instructions=None, creator_id=1, order=2, target_sets_count=5, target_reps_count=5, rest_seconds=120)
    push2 = RoutineExercise(
        routine_id=2, exercise_id=1, instructions=None, creator_id=1, order=3, target_sets_count=5, target_reps_count=5, rest_seconds=120)

    db.session.add(ss0)
    db.session.add(ss1)
    db.session.add(ss2)
    db.session.add(ss3)
    db.session.add(push0)
    db.session.add(push1)
    db.session.add(push2)
    db.session.commit()


def undo_routines_exercises():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.routine_exercises RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM routine_exercises")

    db.session.commit()
