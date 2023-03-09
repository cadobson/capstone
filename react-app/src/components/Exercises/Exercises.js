import { useEffect, useState } from "react"
import { useSelector } from "react-redux"
import { useDispatch } from "react-redux"
import { useModal } from "../../context/Modal"
import { getPrivateExercises, getPublicExercises } from "../../store/exercises"
import CreateExerciseModal from "./CreateExerciseModal"
import ExerciseBlock from "./ExerciseBlock"
import "./ExerciseBlock.css"
import "./Exercises.css"

const Exercises = () => {
  const exercisesData = useSelector(state => state.exercises)
  const [isLoaded, setIsLoaded] = useState(false)
  const currentSessionUser = useSelector(state => state.session.user)
  const [showPrivateHeader, setShowPrivateHeader] = useState(false)

  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(getPublicExercises())
    .then(() => {setIsLoaded(true)})
  }, [dispatch])

  const handleLoadPrivateExercises = () => {
    setIsLoaded(false)
    dispatch(getPrivateExercises())
    .then(() => {setIsLoaded(true)})
    setShowPrivateHeader(true)
  }

  const handleLoadPublicExercises = () => {
    setIsLoaded(false)
    dispatch(getPublicExercises())
    .then(() => {setIsLoaded(true)})
    setShowPrivateHeader(false)
  }

  const {setModalContent} = useModal()
  const handleOpenCreateExerciseModal = () => {
    // The redirect to the new exercise is inside this modal
    setModalContent(<CreateExerciseModal />)
  }

  return (
    <>
      <h1>Exercises</h1>
      <div className="load-exercises-button-container">
        <button className="load-exercises-button" onClick={handleLoadPublicExercises}>View All Public Exercises</button>
        {currentSessionUser && (
          <>
            <button className="load-exercises-button" onClick={handleLoadPrivateExercises}>View My Exercises</button>
            <button className="create-exercise-button" onClick={handleOpenCreateExerciseModal}>Create a New Exercise</button>
          </>

        )}

      </div>
      {showPrivateHeader && (
        <>
          <h2>My Exercises</h2>
          <div>Only you can see these</div>
          {isLoaded && exercisesData.length === 0 && (
            <div>
              You don't have any exercises yet. Consider creating some!
            </div>
          )}
        </>
      )}
      {!showPrivateHeader && (
        <>
          <h2>All Public Exercises</h2>
        </>
      )}
      <div className="exercises-container">
        {isLoaded && exercisesData.map((exercise) => {
          return <ExerciseBlock exercise={exercise} key={exercise.id} />
        })}
      </div>
    </>
  )
}

export default Exercises
