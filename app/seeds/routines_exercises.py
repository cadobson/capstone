from app.models import db, RoutineExercise, environment, SCHEMA


def seed_routines_exercises():
    # Starting Strength
    ss0 = RoutineExercise(
        routine_id=1, exercise_id=3, sets_reps_array="[5,5,5]", instructions="Warm up with half of your expected weight.")
    ss1 = RoutineExercise(
        routine_id=1, exercise_id=1, sets_reps_array="[5,5,5]", instructions=None)
    ss2 = RoutineExercise(
        routine_id=1, exercise_id=2, sets_reps_array="[5]", instructions=None)
    ss3 = RoutineExercise(
        routine_id=1, exercise_id=3, sets_reps_array="[5,5,5]", instructions=None)

    # Push
    push0 = RoutineExercise(
        routine_id=2, exercise_id=1, sets_reps_array="[5,5,5]", instructions="Warm up with half of your expected weight.")
    push1 = RoutineExercise(
        routine_id=2, exercise_id=4, sets_reps_array="[5,5,5,5,5]", instructions=None)
    push2 = RoutineExercise(
        routine_id=2, exercise_id=1, sets_reps_array="[5,5,5,5,5]", instructions=None)

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
