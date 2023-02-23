import { useEffect, useState } from "react"
import { useSelector } from "react-redux"
import { useDispatch } from "react-redux"
import { getPrivateExercises, getPublicExercises } from "../../store/exercises"
import ExerciseBlock from "./ExerciseBlock"
import "./ExerciseBlock.css"

const Exercises = () => {
  const exercisesData = useSelector(state => state.exercises)
  const [isLoaded, setIsLoaded] = useState(false)
  const currentSessionUser = useSelector(state => state.session.user)
  const [showPrivateHeader, setShowPrivateHeader] = useState(false)

  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(getPublicExercises())
    .then(() => {console.log("data from backend: ", exercisesData)})
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

  return (
    <>
      <h1>Exercises</h1>
      <div className="load-exercises-button-container">
        <button className="load-exercises-button" onClick={handleLoadPublicExercises}>Load Public Exercises</button>
        {currentSessionUser && <button className="load-exercises-button" onClick={handleLoadPrivateExercises}>Load Private Exercises</button>}
      </div>
      {showPrivateHeader && (
        <>
          <h2>Private Exercises</h2>
          <div>Only you can see these</div>
        </>
      )}
      {!showPrivateHeader && (
        <>
          <h2>Public Exercises</h2>
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
