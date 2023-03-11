from .db import db, add_prefix_for_prod, SCHEMA, environment


class WorkoutSession(db.Model):
    __tablename__ = 'workout_sessions'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    public = db.Column(db.Boolean, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id")), nullable=False)
    routine_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("routines.id")), nullable=False)
    notes = db.Column(db.String(10000), nullable=True)
    date = db.Column(db.DateTime, nullable=False)

    workout_session_steps = db.relationship(
        "WorkoutSessionStep", back_populates="workout_session")
    creator = db.relationship("User", back_populates="workout_sessions")
    routine = db.relationship("Routine", back_populates="workout_sessions")

    def to_dict(self):
        return {
            'id': self.id,
            'public': self.public,
            'creator_id': self.creator_id,
            'routine_id': self.routine_id,
            'creator': self.creator.to_dict(),
            'routine': self.routine.to_dict(),
            'notes': self.notes,
            'date': self.date,
        }


class WorkoutSessionStep(db.Model):
    __tablename__ = 'workout_session_steps'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    workout_session_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("workout_sessions.id")), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("exercises.id")), nullable=False)
    instructions = db.Column(db.String(10000), nullable=True)
    target_reps_count = db.Column(db.Integer, nullable=True)
    target_sets_count = db.Column(db.Integer, nullable=True)
    rest_seconds = db.Column(db.Integer, nullable=True)
    order = db.Column(db.Integer, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id")), nullable=False)

    workout_session = db.relationship(
        "WorkoutSession", back_populates="workout_session_steps")
    exercise = db.relationship(
        "Exercise", back_populates="workout_session_steps")
    workout_session_step_results = db.relationship(
        "WorkoutSessionStepResult", back_populates="workout_session_step")

    def to_dict(self):
        return {
            'id': self.id,
            'workout_session_id': self.workout_session_id,
            'exercise_id': self.exercise_id,
            'instructions': self.instructions,
            'target_reps_count': self.target_reps_count,
            'target_sets_count': self.target_sets_count,
            'rest_seconds': self.rest_seconds,
            'order': self.order,
            'creator_id': self.creator_id,
            # 'workout_session': self.workout_session.to_dict(),
            'exercise': self.exercise.to_dict_without_description()
        }


class WorkoutSessionStepResult(db.Model):
    __tablename__ = 'workout_session_step_results'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    workout_session_step_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("workout_session_steps.id")), nullable=False)
    actual_reps_count = db.Column(db.Integer, nullable=True)
    actual_weight = db.Column(db.Float, nullable=True)
    creator_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id")), nullable=False)

    workout_session_step = db.relationship(
        "WorkoutSessionStep", back_populates="workout_session_step_results")

    def to_dict(self):
        return {
            'id': self.id,
            'workout_session_step_id': self.workout_session_step_id,
            'actual_reps_count': self.actual_reps_count,
            'actual_weight': self.actual_weight,
            'creator_id': self.creator_id,
            'workout_session_step': self.workout_session_step.to_dict()
        }
