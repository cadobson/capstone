from flask import Blueprint, jsonify, session, request
from app.api.auth_routes import validation_errors_to_error_messages
from app.forms.exercise_form import CreateExerciseForm, EditExerciseForm
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
        print("===============================", routine_exercises)

        return_obj = routine.to_dict()
        return_obj["Routine_Exercise"] = [re.to_dict()
                                          for re in routine_exercises]
        return return_obj
    return {'errors': ['Unauthorized']}, 401
