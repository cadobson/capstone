from app.models import db, Exercise, environment, SCHEMA

bench_press_description = """The bench press is a popular compound exercise that primarily targets the chest, but also engages other upper body muscles such as the shoulders and triceps. Here is a step-by-step guide on how to perform a bench press properly:

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
Vary your grip: Varying your grip can engage different muscle groups in your workout."""

dead_lift_description = """The deadlift is a compound exercise that targets multiple muscle groups, including the back, glutes, and legs. Here's a step-by-step guide on how to perform a deadlift properly:

Set up the equipment: Locate a barbell and adjust it to a comfortable height. Load the bar with an appropriate weight, and position it on the ground in front of you.

Stand in position: Stand in front of the bar with your feet shoulder-width apart. The bar should be positioned over the middle of your feet.

Grip the bar: Reach down and grip the bar with an overhand grip, with your hands slightly wider than shoulder-width apart. Your palms should be facing down.

Get in position: Bend your knees slightly, and hinge forward at the hips to lower your torso. Keep your back straight and your chest up, and engage your core muscles.

Lift the bar: Drive your hips forward and stand up straight, lifting the bar off the ground. As you lift, keep the bar close to your body and your arms straight.

Lower the bar: Lower the bar back down to the ground by reversing the movement. Hinge at the hips and bend your knees to lower the bar, keeping it close to your body and your back straight.

Repeat: Perform the desired number of repetitions, making sure to maintain proper form throughout the exercise.

Tips for a proper deadlift:

Start light: It's important to start with a light weight to learn proper form and avoid injury.
Keep your back straight: Keep your back straight throughout the movement to avoid injury and engage the correct muscles.
Engage your core: Engage your core muscles throughout the exercise to maintain proper form and stability.
Use your legs: Use your legs to drive the movement, rather than relying on your back to lift the weight.
Don't round your back: Avoid rounding your back, as this can lead to injury.
Keep the bar close: Keep the bar close to your body throughout the movement to maintain proper form and engage the correct muscles."""

squat_description = """The squat is a compound exercise that targets multiple muscle groups, including the legs, glutes, and core. Here's a step-by-step guide on how to perform a squat exercise with a barbell:

Set up the equipment: Locate a barbell and adjust it to a comfortable height on the squat rack. Load the bar with an appropriate weight, and position yourself in front of the bar.

Position yourself: Stand in front of the bar with your feet shoulder-width apart, toes pointed slightly outward. Position the bar across the back of your shoulders, resting on your traps.

Grip the bar: Reach back and grip the bar with a shoulder-width grip, palms facing forward. Squeeze your shoulder blades together to create a shelf for the bar to rest on.

Prepare to lift: Take a deep breath and brace your core muscles. Engage your glutes and legs to prepare for the lift.

Lower your body: Begin the squat by pushing your hips back and bending your knees, lowering your body towards the ground. Keep your chest up and your back straight.

Lower until thighs are parallel: Continue lowering until your thighs are parallel to the ground. Make sure your knees are in line with your toes, and your weight is evenly distributed over your feet.

Push back up: Push through your heels to lift your body back up to the starting position. Exhale as you push back up.

Repeat: Perform the desired number of repetitions, making sure to maintain proper form throughout the exercise.

Tips for a proper barbell squat:

Start with a light weight: It's important to start with a light weight to learn proper form and avoid injury.
Keep your back straight: Keep your back straight throughout the movement to avoid injury and engage the correct muscles.
Engage your core: Engage your core muscles throughout the exercise to maintain proper form and stability.
Keep your knees in line with your toes: Make sure your knees are pointing in the same direction as your toes to avoid injury.
Use your glutes and legs: Use your glutes and legs to drive the movement, rather than relying on your back to lift the weight.
Focus on form: Proper form is essential to avoid injury and engage the correct muscles."""

overhead_press_description = """The overhead press, also known as the shoulder press, is a compound exercise that targets the shoulders, triceps, and upper back. Here's a step-by-step guide on how to perform an overhead press:

Set up the equipment: Locate a barbell or dumbbells and adjust the weight to a comfortable level. If using a barbell, position it at chest height on a squat rack.

Stand in position: Stand in front of the barbell or dumbbells with your feet shoulder-width apart. If using a barbell, grip the bar with a slightly wider than shoulder-width grip, palms facing forward.

Get in position: Position the barbell or dumbbells at shoulder level, with your elbows bent and your forearms perpendicular to the ground. Engage your core muscles and maintain a neutral spine.

Lift the weight: Lift the weight overhead by extending your arms, keeping the weight close to your body. Fully extend your arms at the top of the movement, but don't lock out your elbows.

Lower the weight: Lower the weight back down to the starting position by bending your elbows and lowering the weight to shoulder level.

Repeat: Perform the desired number of repetitions, making sure to maintain proper form throughout the exercise.

Tips for a proper overhead press:

Start with a light weight: It's important to start with a light weight to learn proper form and avoid injury.
Keep your core engaged: Engage your core muscles throughout the exercise to maintain proper form and stability.
Keep your back straight: Keep your back straight and maintain a neutral spine throughout the movement to avoid injury.
Don't lock out your elbows: Avoid locking out your elbows at the top of the movement, as this can put unnecessary strain on the joints.
Keep the weight close to your body: Keep the weight close to your body throughout the movement to maintain proper form and engage the correct muscles.
Use a full range of motion: Use a full range of motion, lowering the weight to shoulder level at the bottom of the movement and fully extending your arms at the top."""

pull_up_description = """The pull-up is a compound exercise that targets the upper back, shoulders, and biceps. Here's a step-by-step guide on how to perform a pull-up:

Find a sturdy pull-up bar: Locate a sturdy pull-up bar that can support your weight. The bar should be high enough that you can hang from it with your feet off the ground.

Grip the bar: Grip the bar with an overhand grip, hands shoulder-width apart. Your palms should be facing away from your body.

Hang from the bar: Hang from the bar with your arms fully extended and your shoulder blades pulled down and back. Engage your core muscles and maintain a neutral spine.

Pull yourself up: Pull yourself up towards the bar by squeezing your shoulder blades together and pulling your elbows down towards your sides. Continue pulling until your chin is above the bar.

Lower yourself down: Lower yourself back down to the starting position by extending your arms fully.

Repeat: Perform the desired number of repetitions, making sure to maintain proper form throughout the exercise.

Tips for a proper pull-up:

Start with assisted pull-ups: If you're new to pull-ups, you may want to start with assisted pull-ups using a resistance band or machine.
Engage your core: Engage your core muscles throughout the exercise to maintain proper form and stability.
Keep your shoulders down: Keep your shoulders down and back throughout the movement to engage the correct muscles and avoid injury.
Pull with your back, not your arms: Focus on pulling with your upper back muscles, rather than relying on your arms to do the work.
Use a full range of motion: Use a full range of motion, pulling yourself up until your chin is above the bar and fully extending your arms at the bottom of the movement.
Avoid swinging: Avoid swinging your body or using momentum to complete the movement. This can put unnecessary strain on your joints and reduce the effectiveness of the exercise."""

push_up_description = """The push-up is a bodyweight exercise that targets the chest, shoulders, triceps, and core muscles. Here's a step-by-step guide on how to perform a push-up:

Get in position: Start by getting into a plank position, with your hands slightly wider than shoulder-width apart and your feet hip-width apart. Your body should form a straight line from your head to your heels.

Engage your core: Engage your core muscles by pulling your belly button towards your spine. This will help to maintain proper form and stability throughout the exercise.

Lower your body: Lower your body towards the ground by bending your elbows, keeping them close to your sides. Lower yourself until your chest is a few inches above the ground.

Push back up: Push yourself back up to the starting position by extending your elbows and pushing your body away from the ground.

Repeat: Perform the desired number of repetitions, making sure to maintain proper form throughout the exercise.

Tips for a proper push-up:

Keep your body in a straight line: Keep your body in a straight line from your head to your heels throughout the movement.
Engage your core: Engage your core muscles to maintain proper form and stability.
Keep your elbows close to your sides: Keep your elbows close to your sides as you lower your body towards the ground to engage the correct muscles and avoid injury.
Lower your body until your chest is a few inches above the ground: Lower yourself until your chest is a few inches above the ground, rather than all the way down to the ground. This will help to maintain proper form and avoid injury.
Push yourself back up by extending your elbows: Push yourself back up to the starting position by extending your elbows, rather than using momentum or arching your back.
Don't let your hips sag: Avoid letting your hips sag towards the ground, as this can put unnecessary strain on your lower back. Keep your body in a straight line throughout the movement."""

# Adds a few demo exercises, which will be owned by the administrator


def seed_exercises():
    bench_press = Exercise(
        name="Bench Press", description=bench_press_description, motion_img_url=None, public=True, creator_id=1)
    dead_lift = Exercise(
        name="Dead Lift", description=dead_lift_description, motion_img_url=None, public=True, creator_id=1)
    squat = Exercise(
        name="Squat", description=squat_description, motion_img_url=None, public=True, creator_id=1)
    overhead_press = Exercise(
        name="Overhead Press", description=overhead_press_description, motion_img_url=None, public=True, creator_id=1)
    pull_up = Exercise(
        name="Pull Up", description=pull_up_description, motion_img_url=None, public=True, creator_id=1)
    push_up = Exercise(
        name="Push Up", description=push_up_description, motion_img_url=None, public=True, creator_id=1)

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
