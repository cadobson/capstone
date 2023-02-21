from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, ValidationError, URL
from app.models import Exercise


def exercise_exists(form, field):
    # Checking if exercise exists
    name = field.data
    exercise = Exercise.query.filter(Exercise.name == name).first()
    if exercise:
        raise ValidationError('Exercise name is already in use.')


class CreateExerciseForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), exercise_exists])
    description = StringField('description', validators=[DataRequired()])


class EditExerciseForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    motion_img_url = StringField('motion_img_url')
