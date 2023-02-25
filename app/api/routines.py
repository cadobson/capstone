from flask import Blueprint, jsonify, session, request
from app.api.auth_routes import validation_errors_to_error_messages
from app.forms.exercise_form import CreateExerciseForm, EditExerciseForm
from app.models import db, Routine, Exercise, User
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
