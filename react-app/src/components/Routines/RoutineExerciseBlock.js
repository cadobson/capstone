

const RoutineExerciseBlock = ({routineExercise}) => {
  const {order, Exercise, exercise_id, sets_reps_array, instructions} = routineExercise

  return (
    <div className="routine-exercise-block">
      <h2>Step {order}: {Exercise.name}</h2>
      <div>Sets/Reps/Rest: {sets_reps_array}</div>
      {instructions && (
        <div>Instructions: {instructions}</div>
      )}
      
    </div>
  )
}

export default RoutineExerciseBlock