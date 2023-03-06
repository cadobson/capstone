import { useDispatch } from "react-redux"
import { Link } from "react-router-dom"
import { useModal } from "../../context/Modal"
import { deleteExerciseFromRoutine } from "../../store/routine"
import EditExerciseRoutineModal from "./EditExerciseRoutineModal"


const RoutineExerciseBlock = ({routineExercise, enableDelete, enableEdit, routineId}) => {
  const {order, Exercise, exercise_id, sets_reps_array, instructions} = routineExercise
  const dispatch = useDispatch()

  const handleDeleteRoutineExercise = (e) => {
    e.preventDefault()
    dispatch(deleteExerciseFromRoutine(routineId, routineExercise.id))
  }

  const {setModalContent} = useModal()
  const handleOpenEditRoutineExerciseModal = (e) => {
    e.preventDefault()
    setModalContent(<EditExerciseRoutineModal routineExerciseData={routineExercise} routineId={routineId} />)
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
          <button className="routine-exercise-delete-button" onClick={handleOpenEditRoutineExerciseModal}>
          <i className="fas fa-trash" />
        </button>
        )}
        {enableEdit && (
          <button className="routine-exercise-edit-button" onClick={handleOpenEditRoutineExerciseModal}>
            <i className="fas fa-edit" />
          </button>
        )}
      </div>




    </div>
  )
}

export default RoutineExerciseBlock
