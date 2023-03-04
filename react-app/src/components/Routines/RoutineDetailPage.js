import { useParams, useHistory } from "react-router-dom"
import { useSelector, useDispatch } from "react-redux"
import { useState, useEffect } from "react"
import { deleteRoutine, getRoutine } from "../../store/routine"
import RoutineExerciseBlock from "./RoutineExerciseBlock"
import { useModal } from "../../context/Modal"
import EditRoutineModal from "./EditRoutineModal"
import CreateRoutineExerciseModal from "./CreateRoutineExerciseModal"

const RoutineDetailPage = () => {
  const id = useParams().id
  const routineData = useSelector(state => state.routine)
  const [isLoaded, setIsLoaded] = useState(false)
  const [display404, setDisplay404] = useState(false)

  const currentSessionUser = useSelector(state => state.session.user)
  const showOwnerButtons = currentSessionUser && currentSessionUser.id === routineData.creator_id

  const dispatch = useDispatch()
  const history = useHistory()

  useEffect(() => {
    dispatch(getRoutine(id))
    .then(() => setIsLoaded(true))
    .catch((error) => {setDisplay404(true)})
  }, [dispatch, id])

  const handleDeleteRoutine = (e) => {
    e.preventDefault()
    setIsLoaded(false)
    dispatch(deleteRoutine(id))
    .then(() => {history.push("/routines")})
  }

  const {setModalContent} = useModal()
  const handleOpenEditRoutineModal = () => {
    setModalContent(<EditRoutineModal routineData={routineData} />)
  }

  const handleOpenCreateRoutineExerciseModal = () => {
    setModalContent(<CreateRoutineExerciseModal routineData={routineData} />)
  }

  return (
    <>
      {isLoaded && (
        <>
          <div className="routine-detail">
            <div className="routine-detail-text">
              <h1>{routineData.name}</h1>
              <div className="routine-detail-description">{routineData.description}</div>
              This routine has {routineData.Routine_Exercise.length} exercises.
              {routineData.Routine_Exercise.map((routineExercise) => (
                <RoutineExerciseBlock routineExercise={routineExercise} key={routineExercise.id} />
              ))}
            </div>
            <div className="routine-detail-sidebar">
              This routine was contributed by {routineData.creator.username}.
              {showOwnerButtons && (
                <>
                  <button className="delete-routine-button" onClick={handleDeleteRoutine}>Delete Routine</button>
                  <button className="edit-routine-button" onClick={handleOpenEditRoutineModal}>Edit Routine</button>
                  <button className="create-routine-exercise-button" onClick={handleOpenCreateRoutineExerciseModal}>Add a Step</button>
                </>
              )}
            </div>
          </div>
        </>
      )}
      {!isLoaded && !display404 && (
        <div>Loading...</div>
      )}
      {display404 && (
        <div>404: Routine not found.</div>
      )}
    </>
  )
}

export default RoutineDetailPage
