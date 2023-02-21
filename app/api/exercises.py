from flask import Blueprint, jsonify, session, request
from app.api.auth_routes import validation_errors_to_error_messages
from app.forms.exercise_form import CreateExerciseForm, EditExerciseForm
from app.models import db, Exercise, User
from sqlalchemy.orm import joinedload
from flask_login import current_user


exercise_routes = Blueprint('exercises', __name__)

# Get all exercises belonging to the current user


@exercise_routes.route('/current', methods=['GET'])
def get_exercises_current_user():
    if current_user.is_authenticated:
        exercises = Exercise.query.filter(
            Exercise.creator_id == current_user.id).all()
        return jsonify([exercise.to_dict() for exercise in exercises])
    return {'errors': ['Unauthorized']}, 401

# Get all exercises which are marked public


@exercise_routes.route('/public', methods=['GET'])
def get_exercises_public():
    exercises = Exercise.query.filter(Exercise.public == True).all()
    return jsonify([exercise.to_dict() for exercise in exercises])

# Get an exercise by id, but only if it is public or belongs to the current user


@exercise_routes.route('/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.filter(Exercise.id == id).first()

    if not exercise:
        return {
            'errors': ['Exercise not found'],
            "statusCode": 404,
            'message': "Exercise not found"
        }, 404

    if exercise.public == True or exercise.creator_id == current_user.id:
        return exercise.to_dict()
    return {'errors': ['Unauthorized']}, 401

# Create a new exercise


@exercise_routes.route('/', methods=['POST'])
def create_exercise():
    if not current_user.is_authenticated:
        return {'errors': ['Unauthorized']}, 401

    form = CreateExerciseForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = request.get_json()

        exercise = Exercise(
            name=data['name'],
            description=data['description'],
            creator_id=current_user.id,
            public=False,
            motion_img_url=None
        )

        db.session.add(exercise)
        db.session.commit()
        return exercise.to_dict()

    return {
        "statusCode": 400,
        "message": "Bad request",
        'errors': validation_errors_to_error_messages(form.errors)
    }, 400

# Update an exercise


@exercise_routes.route('/<int:id>', methods=['PUT'])
def update_exercise(id):
    if not current_user.is_authenticated:
        return {'errors': ['Unauthorized']}, 401

    exercise = Exercise.query.filter(Exercise.id == id).first()

    if not exercise:
        return {
            'errors': ['Exercise not found'],
            "statusCode": 404,
            'message': "Exercise not found"
        }, 404

    if exercise.creator_id != current_user.id:
        return {'errors': ['Unauthorized']}, 401

    form = EditExerciseForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = request.get_json()

        exercise.name = data['name']
        exercise.description = data['description']
        exercise.motion_img_url = data.get('motion_img_url')

        db.session.commit()
        return exercise.to_dict()

    return {
        "statusCode": 400,
        "message": "Bad request",
        'errors': validation_errors_to_error_messages(form.errors)
    }, 400
