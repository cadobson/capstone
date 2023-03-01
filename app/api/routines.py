from flask import Blueprint, jsonify, session, request
from app.api.auth_routes import validation_errors_to_error_messages
from app.forms.routine_form import CreateRoutineForm, EditRoutineForm, CreateRoutineExerciseForm, EditRoutineExerciseForm
from app.models import db, Routine, RoutineExercise, Exercise, User
from sqlalchemy.orm import joinedload
from flask_login import current_user


routine_routes = Blueprint('routines', __name__)

# Get all routines belonging to the current user


@routine_routes.route('/current', methods=['GET'])
def get_routines_current_user():
    if current_user.is_authenticated:
        routines = Routine.query.filter(
            Routine.creator_id == current_user.id).all()
        return jsonify({"Routines": [routine.to_dict() for routine in routines]})
    return {'errors': ['Unauthorized']}, 401

# Get all routines which are marked public


@routine_routes.route('/public', methods=['GET'])
def get_routines_public():
    routines = Routine.query.filter(Routine.public == True).all()
    return jsonify({"Routines": [routine.to_dict() for routine in routines]})

# Get the details of a routine by id, including the exercises it contains, but only if it is public or belongs to the current user


@routine_routes.route('/<int:id>', methods=['GET'])
def get_routine(id):
    routine = Routine.query.filter(Routine.id == id).first()

    if not routine:
        return {
            'errors': ['Routine not found'],
            "statusCode": 404,
            'message': "Routine not found"
        }, 404

    if routine.public == True or routine.creator_id == current_user.id:
        routine_exercises = RoutineExercise.query.options(joinedload(RoutineExercise.exercises)).filter(
            RoutineExercise.routine_id == id).all()

        return_obj = routine.to_dict()
        return_obj["Routine_Exercise"] = [re.to_dict()
                                          for re in routine_exercises]
        return return_obj
    return {'errors': ['Unauthorized']}, 401

# Create a new routine


@routine_routes.route('/', methods=['POST'])
def create_routine():
    if not current_user.is_authenticated:
        return {'errors': ['Unauthorized']}, 401

    form = CreateRoutineForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = request.get_json()
        routine = Routine(
            name=data['name'],
            description=data['description'],
            public=False,
            creator_id=current_user.id
        )
        db.session.add(routine)
        db.session.commit()
        return routine.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

# Edit a routine


@routine_routes.route('/<int:id>', methods=['PUT'])
def edit_routine(id):
    if not current_user.is_authenticated:
        return {'errors': ['Unauthorized']}, 401

    form = EditRoutineForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = request.get_json()

        routine = Routine.query.filter(Routine.id == id).first()

        if not routine:
            return {
                'errors': ['Routine not found'],
                "statusCode": 404,
                'message': "Routine not found"
            }, 404

        if routine.creator_id == current_user.id:
            routine.name = data['name']
            routine.description = data['description']
            db.session.commit()
            return routine.to_dict()
        return {'errors': ['Unauthorized']}, 401
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

# Delete a routine and all of its routine_exercises


@routine_routes.route('/<int:id>', methods=['DELETE'])
def delete_routine(id):
    if not current_user.is_authenticated:
        return {'errors': ['Unauthorized']}, 401

    routine = Routine.query.filter(Routine.id == id).first()
    if routine.creator_id == current_user.id:
        routine_exercises = RoutineExercise.query.filter(
            RoutineExercise.routine_id == id).all()
        for routine_exercise in routine_exercises:
            db.session.delete(routine_exercise)
        db.session.delete(routine)
        db.session.commit()
        return {
            "message": "Routine deleted",
            "statusCode": 200
        }, 200
    return {'errors': ['Unauthorized']}, 401

# Add a routine_exercise to a routine


@routine_routes.route('/<int:id>', methods=['POST'])
def create_routine_exercise(id):
    if not current_user.is_authenticated:
        return {'errors': ['Unauthorized']}, 401

    form = CreateRoutineExerciseForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = request.get_json()

        # Check if the routine exists and belongs to the current user
        routine = Routine.query.filter(Routine.id == id).first()
        if not routine:
            return {
                'errors': ['Routine not found'],
                "statusCode": 404,
                'message': "Routine not found"
            }, 404

        if routine.creator_id != current_user.id:
            return {'errors': ['Unauthorized']}, 401

        # Check if the exercise exists and is either public or belongs to the current user
        proposed_exercise = Exercise.query.filter(
            Exercise.id == data['exercise_id']).first()
        if not proposed_exercise:
            return {
                'errors': ['Exercise not found'],
                "statusCode": 404,
                'message': "Exercise not found"
            }, 404
        if proposed_exercise.public == False and proposed_exercise.creator_id != current_user.id:
            return {'errors': ['Unauthorized']}, 401

        number_of_routine_exercises = RoutineExercise.query.filter(
            RoutineExercise.routine_id == id).count()
        if number_of_routine_exercises >= 20:
            return {
                'errors': ['Routine is full'],
                "statusCode": 400,
                'message': "Routine is full"
            }, 400

        routine_exercise = RoutineExercise(
            routine_id=id,
            exercise_id=data['exercise_id'],
            sets_reps_array=data['sets_reps_array'],
            instructions=data['instructions'],
            creator_id=current_user.id,
            order=number_of_routine_exercises + 1
        )
        db.session.add(routine_exercise)
        db.session.commit()
        return routine_exercise.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

# Edit the instructions or sets_reps_array of a routine_exercise


@routine_routes.route('/<int:id>/routine_exercise/<int:routine_exercise_id>', methods=['PUT'])
def edit_routine_exercise(id, routine_exercise_id):
    if not current_user.is_authenticated:
        return {'errors': ['Unauthorized']}, 401

    form = EditRoutineExerciseForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = request.get_json()
        routine_exercise = RoutineExercise.query.filter(
            RoutineExercise.routine_id == id, RoutineExercise.id == routine_exercise_id).first()

        if not routine_exercise:
            return {
                'errors': ['Routine Exercise not found'],
                "statusCode": 404,
                'message': "Routine Exercise not found"
            }, 404

        if routine_exercise.creator_id == current_user.id:
            routine_exercise.instructions = data['instructions']
            routine_exercise.sets_reps_array = data['sets_reps_array']
            db.session.commit()
            return routine_exercise.to_dict()
        return {'errors': ['Unauthorized']}, 401
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

# Delete a routine_exercise


@routine_routes.route('/<int:id>/routine_exercise/<int:routine_exercise_id>', methods=['DELETE'])
def delete_routine_exercise(id, routine_exercise_id):
    if not current_user.is_authenticated:
        return {'errors': ['Unauthorized']}, 401

    routine_exercise = RoutineExercise.query.filter(
        RoutineExercise.routine_id == id, RoutineExercise.id == routine_exercise_id).first()

    # Check to see if the routine_exercise exists
    if not routine_exercise:
        return {
            'errors': ['Routine Exercise not found'],
            "statusCode": 404,
            'message': "Routine Exercise not found"
        }, 404

    if routine_exercise.creator_id == current_user.id:
        db.session.delete(routine_exercise)
        db.session.commit()

        # Update the order of the remaining routine_exercises
        routine_exercises = RoutineExercise.query.filter(
            RoutineExercise.routine_id == id).all()
        for i in range(len(routine_exercises)):
            routine_exercises[i].order = i + 1
        db.session.commit()

        return {
            "message": "Routine Exercise deleted",
            "statusCode": 200
        }, 200
    return {'errors': ['Unauthorized']}, 401

# Copy a routine and all of its routine_exercises


@routine_routes.route('/<int:id>/copy', methods=['POST'])
def copy_routine(id):
    if not current_user.is_authenticated:
        return {'errors': ['Unauthorized']}, 401

    routine = Routine.query.filter(Routine.id == id).first()
    if not routine:
        return {
            'errors': ['Routine not found'],
            "statusCode": 404,
            'message': "Routine not found"
        }, 404

    # Check if the routine is public or belongs to the current user
    if routine.public == False and routine.creator_id != current_user.id:
        return {'errors': ['Unauthorized']}, 401

    # Create a new routine
    new_routine = Routine(
        name=routine.name,
        description=routine.description,
        public=False,
        creator_id=current_user.id
    )
    db.session.add(new_routine)
    db.session.commit()

    # Create all of the routine_exercises
    routine_exercises = RoutineExercise.query.filter(
        RoutineExercise.routine_id == id).all()
    for routine_exercise in routine_exercises:
        new_routine_exercise = RoutineExercise(
            routine_id=new_routine.id,
            exercise_id=routine_exercise.exercise_id,
            sets_reps_array=routine_exercise.sets_reps_array,
            instructions=routine_exercise.instructions,
            creator_id=current_user.id,
            order=routine_exercise.order
        )
        db.session.add(new_routine_exercise)
    db.session.commit()
    return new_routine.to_dict()

# Get all of the routines that belong to the current user
