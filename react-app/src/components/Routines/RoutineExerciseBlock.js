import { useDispatch } from "react-redux"
import { Link } from "react-router-dom"
import { deleteExerciseFromRoutine } from "../../store/routine"


const RoutineExerciseBlock = ({routineExercise, enableDelete, routineId}) => {
  const {order, Exercise, exercise_id, sets_reps_array, instructions} = routineExercise
  const dispatch = useDispatch()

  const handleDeleteRoutineExercise = (e) => {
    e.preventDefault()
    dispatch(deleteExerciseFromRoutine(routineId, routineExercise.id))

  }

  return (
    <div className="routine-exercise-block">
      <div className="routine-exercise-block-left-side">
        <h2>Step {order}: {Exercise.name}</h2>
        <div><Link to={`/exercises/${exercise_id}`}>View Exercise Detail Page</Link></div>
        <div>Sets/Reps/Rest: {sets_reps_array}</div>
        {instructions && (
          <div>Instructions: {instructions}</div>
        )}
      </div>
      <div className="routine-exercise-block-right-side">
        {enableDelete && (
          <button className="routine-exercise-delete-button" onClick={handleDeleteRoutineExercise}>
          <i className="fas fa-trash" />
        </button>
        )}
      </div>




    </div>
  )
}

export default RoutineExerciseBlock
