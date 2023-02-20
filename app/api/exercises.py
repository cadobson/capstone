from flask import Blueprint, jsonify, session, request
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
    return {'errors': ['Unauthorized']}

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
    return {'errors': ['Unauthorized']}

# Create a new exercise


@exercise_routes.route('/', methods=['POST'])
def create_exercise():
    if current_user.is_authenticated:
        data = request.get_json()

        exercise = Exercise(
            name=data['name'],
            description=data['description'],
            creator_id=current_user.id,
            public=data['public']
        )

        db.session.add(exercise)
        db.session.commit()

        return exercise.to_dict()
    return {'errors': ['Unauthorized']}

