from app.models import db, Exercise, environment, SCHEMA

bench_press_description = """
The bench press is a popular compound exercise that primarily targets the chest, but also engages other upper body muscles such as the shoulders and triceps. Here is a step-by-step guide on how to perform a bench press properly:

Set up the equipment: Locate a flat bench and adjust it to a comfortable height. Make sure the barbell is loaded with an appropriate weight and positioned on the rack above the bench.

Warm-up: It is important to warm up your muscles before performing any exercise. Perform a few light sets of bench press or use resistance bands to warm up your chest, shoulders, and arms.

Position yourself: Lie flat on the bench with your eyes directly under the bar. Your feet should be firmly planted on the ground, and your back should be arched slightly to create a natural curve in your spine. Grasp the bar with a shoulder-width grip and lift it off the rack, holding it directly above your chest.

Lower the bar: Slowly lower the bar towards your chest, keeping your elbows close to your body. Lower the bar until it touches your chest or comes close to it.

Push the bar back up: Push the bar back up towards the starting position, exhaling as you push. Make sure to keep your wrists straight and your elbows locked out at the top of the movement.

Repeat: Perform the desired number of repetitions, making sure to maintain proper form throughout the exercise.

Rack the bar: Once you have completed your set, carefully rack the bar back on the rack.

Tips for a proper bench press:

Use a spotter: Always have a spotter when performing heavy sets of bench press to ensure safety and prevent injury.
Keep your form correct: Keep your feet firmly planted on the ground, and your back slightly arched to maintain proper form throughout the exercise.
Breathe properly: Inhale as you lower the bar and exhale as you push it back up.
Choose appropriate weight: Select a weight that challenges you but allows you to perform the exercise with proper form.
Vary your grip: Varying your grip can engage different muscle groups and prevent boredom in your workout.
"""

# Adds a few demo exercises, which will be owned by the administrator


def seed_exercises():
    bench_press = Exercise(
        name="Bench Press", description=bench_press_description, motion_img_url=None, public=True, creator_id=1)
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
