from flask import Blueprint, jsonify, request
from app.api.auth_routes import validation_errors_to_error_messages
from app.forms.workout_form import CreateWorkoutSessionForm, EditWorkoutSessionForm
from app.models import db, WorkoutSession, User, Exercise, WorkoutSessionStep, WorkoutSessionStepResult, Routine, RoutineExercise
from sqlalchemy.orm import joinedload
from flask_login import current_user
from datetime import date


workout_session_routes = Blueprint('workout_sessions', __name__)

# Get all workout sessions belonging to the current user


@workout_session_routes.route('/')
def get_workout_sessions():
    if current_user.is_authenticated:
        workout_sessions = WorkoutSession.query.filter(
            WorkoutSession.creator_id == current_user.id).all()
        return {"workout_sessions": [workout_session.to_dict() for workout_session in workout_sessions]}
    else:
        return {'errors': ['Unauthorized']}, 401

# Get a single workout session, including all of its steps and results, but only if the current user is the creator of the workout session.


@workout_session_routes.route('/<int:id>')
def get_workout_session(id):
    if current_user.is_authenticated:
        workout_session = WorkoutSession.query.options(joinedload(
            WorkoutSession.workout_session_steps).joinedload(WorkoutSessionStep.workout_session_step_results)).filter(WorkoutSession.id == id).first()

        if not workout_session:
            return {'errors': ['Workout session not found']}, 404
        if workout_session.creator_id == current_user.id:
            # return {"workout_session": workout_session.to_dict()}
            return_obj = workout_session.to_dict()
            return_obj["Workout_Session_Steps"] = [workout_session_step.to_dict(
            ) for workout_session_step in workout_session.workout_session_steps]
            return return_obj
        else:
            return {'errors': ['Unauthorized']}, 401
    else:
        return {'errors': ['Unauthorized']}, 401

# Create a new workout session based on an existing routine. This will create a new workout session and a new workout session step for each exercise in the routine. Date defaults to today's date.


@workout_session_routes.route('/', methods=['POST'])
def create_workout_session():
    if not current_user.is_authenticated:
        return {'errors': ['Unauthorized']}, 401

    form = CreateWorkoutSessionForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = request.get_json()
        # Check if the routine exists, and if the current user is the creator of the routine
        routine = Routine.query.filter(
            Routine.id == data['routine_id']).first()
        if not routine:
            return {'errors': ['Routine not found']}, 404
        if routine.creator_id != current_user.id:
            return {'errors': ['Unauthorized']}, 401

        workout_session = WorkoutSession(
            routine_id=data['routine_id'],
            notes="",
            creator_id=current_user.id,
            date=date.today(),
            public=False
        )
        db.session.add(workout_session)
        db.session.commit()
        routine_exercises = RoutineExercise.query.filter(
            RoutineExercise.routine_id == data['routine_id']).all()
        for routine_exercise in routine_exercises:
            workout_session_step = WorkoutSessionStep(
                workout_session_id=workout_session.id,
                exercise_id=routine_exercise.exercise_id,
                instructions=routine_exercise.instructions,
                target_reps_count=routine_exercise.target_reps_count,
                target_sets_count=routine_exercise.target_sets_count,
                rest_seconds=routine_exercise.rest_seconds,
                order=routine_exercise.order,
                creator_id=current_user.id
            )
            db.session.add(workout_session_step)
            db.session.commit()
        return {"workout_session": workout_session.to_dict()}
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

# Update a workout session. This will update the notes field only.


@workout_session_routes.route('/<int:id>', methods=['PUT'])
def update_workout_session(id):
    if not current_user.is_authenticated:
        return {'errors': ['Unauthorized']}, 401
    form = EditWorkoutSessionForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = request.get_json()
        workout_session = WorkoutSession.query.filter(
            WorkoutSession.id == id).first()
        if not workout_session:
            return {'errors': ['Workout session not found']}, 404
        if workout_session.creator_id != current_user.id:
            return {'errors': ['Unauthorized']}, 401
        workout_session.notes = data['notes']
        db.session.commit()
        return {"workout_session": workout_session.to_dict()}
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

# Delete a workout session. This will delete the workout session and all of its steps and results.


@workout_session_routes.route('/<int:id>', methods=['DELETE'])
def delete_workout_session(id):
    if not current_user.is_authenticated:
        return {'errors': ['Unauthorized']}, 401
    workout_session = WorkoutSession.query.filter(
        WorkoutSession.id == id).first()
    if not workout_session:
        return {'errors': ['Workout session not found']}, 404
    if workout_session.creator_id != current_user.id:
        return {'errors': ['Unauthorized']}, 401
    db.session.delete(workout_session)
    db.session.commit()
    return {"workout_session": workout_session.to_dict()}
