from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, ValidationError, URL
from app.models import Routine


def routine_exists(form, field):
    # Checking if routine exists
    name = field.data
    routine = Routine.query.filter(Routine.name == name).first()
    if routine:
        raise ValidationError('Routine name is already in use.')


class CreateRoutineForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), routine_exists])
    description = StringField('description', validators=[DataRequired()])


class EditRoutineForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])


class CreateRoutineExerciseForm(FlaskForm):
    exercise_id = IntegerField('exercise_id', validators=[DataRequired()])
    sets_reps_array = StringField(
        'sets_reps_array', validators=[DataRequired()])
    instructions = StringField('instructions')


class EditRoutineExerciseForm(FlaskForm):
    sets_reps_array = StringField(
        'sets_reps_array', validators=[DataRequired()])
    instructions = StringField('instructions')
