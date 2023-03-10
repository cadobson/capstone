from .db import db, environment, SCHEMA, add_prefix_for_prod


class Exercise(db.Model):
    __tablename__ = 'exercises'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(10000), nullable=False)
    motion_img_url = db.Column(db.String(255), nullable=True)
    public = db.Column(db.Boolean, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id")), nullable=False)

    creator = db.relationship("User", back_populates="exercises")
    routines = db.relationship("RoutineExercise", back_populates="exercises")
    workout_session_steps = db.relationship(
        "WorkoutSessionStep", back_populates="exercise")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'motion_img_url': self.motion_img_url,
            'public': self.public,
            'creator_id': self.creator_id
        }

    def to_dict_without_description(self):
        return {
            'id': self.id,
            'name': self.name,
            'motion_img_url': self.motion_img_url,
            'public': self.public,
            'creator_id': self.creator_id
        }


class Routine(db.Model):
    __tablename__ = 'routines'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(10000), nullable=False)
    public = db.Column(db.Boolean, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id")), nullable=False)

    creator = db.relationship("User", back_populates="routines")
    exercises = db.relationship("RoutineExercise", back_populates="routines")
    workout_sessions = db.relationship("WorkoutSession",
                                       back_populates="routine", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'public': self.public,
            'creator_id': self.creator_id,
            'creator': self.creator.to_dict(),
        }


class RoutineExercise(db.Model):
    __tablename__ = 'routine_exercises'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    routine_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("routines.id")), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("exercises.id")), nullable=False)
    # sqlite3 does not support arrays, so encode as string
    # sets_reps_array = db.Column(db.String(10000), nullable=False)
    instructions = db.Column(db.String(10000), nullable=True)
    creator_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id")), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    target_sets_count = db.Column(db.Integer, nullable=False)
    target_reps_count = db.Column(db.Integer, nullable=False)
    rest_seconds = db.Column(db.Integer, nullable=False)

    routines = db.relationship("Routine", back_populates="exercises")
    exercises = db.relationship("Exercise", back_populates="routines")

    def to_dict(self):
        return {
            'id': self.id,
            'routine_id': self.routine_id,
            'exercise_id': self.exercise_id,
            # 'sets_reps_array': self.sets_reps_array,
            'instructions': self.instructions,
            'Exercise': self.exercises.to_dict(),
            'creator_id': self.creator_id,
            'order': self.order,
            'target_sets_count': self.target_sets_count,
            'target_reps_count': self.target_reps_count,
            'rest_seconds': self.rest_seconds
        }


# routine = db.relationship("Routine", back_populates="routine_exercises")
# exercise = db.relationship("Exercise", back_populates="routine_exercises")


# def to_dict(self):
#     return {
#         'id': self.id,
#         'routine_id': self.routine_id,
#         'exercise_id': self.exercise_id,
#         'order': self.order,
#         'sets': self.sets,
#         'reps': self.reps,
#         'weight': self.weight
#     }
