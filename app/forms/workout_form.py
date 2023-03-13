from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import Routine


class CreateWorkoutSessionForm(FlaskForm):
    routine_id = IntegerField('routine_id', validators=[DataRequired()])


class EditWorkoutSessionForm(FlaskForm):
    notes = StringField('notes')
