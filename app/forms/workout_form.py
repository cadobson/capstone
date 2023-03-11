from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import Routine

class CreateRoutineForm(FlaskForm):
    routine_id = IntegerField('routine_id', validators=[DataRequired()])
