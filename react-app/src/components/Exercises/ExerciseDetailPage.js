import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory, useParams } from "react-router-dom"
import { useModal } from "../../context/Modal"
import { deleteExercise, getExercise } from "../../store/exercise"
import EditExerciseModal from "./EditExerciseModal"

import defaultImg from "./no_preview_img.png"


const ExerciseDetailPage = () => {
  const id = useParams().id
  const exerciseData = useSelector(state => state.exercise)
  const [isLoaded, setIsLoaded] = useState(false)

  const currentSessionUser = useSelector(state => state.session.user)
  const showOwnerButtons = currentSessionUser && currentSessionUser.id === exerciseData.creator_id

  const dispatch = useDispatch()
  const history = useHistory()

  useEffect(() => {
    dispatch(getExercise(id))
    .then(() => setIsLoaded(true))
  }, [dispatch])

  const handleDeleteExercise = (e) => {
    e.preventDefault()
    dispatch(deleteExercise(id))
    .then(() => {history.push("/exercises")})
  }

  const {setModalContent} = useModal()
  const handleOpenEditExerciseModal = () => {
    setModalContent(<EditExerciseModal exerciseData={exerciseData} />)
  }

  return (
    <>
      {isLoaded && (
        <>

          <div className="exercise-detail">
            <div className="exercise-detail-text">
              <h1>{exerciseData.name}</h1>
              <div className="exercise-detail-description">{exerciseData.description}</div>
            </div>
            <div className="exercise-detail-sidebar">
              <img src={exerciseData.motion_img_url || defaultImg} alt={`preview of exercise: ${exerciseData.name}`} />
              {showOwnerButtons && (
                <>
                  <button className="delete-exercise-button" onClick={handleDeleteExercise}>Delete Exercise</button>
                  <button className="edit-exercise-button" onClick={handleOpenEditExerciseModal}>Edit Exercise</button>
                </>
              )}

            </div>
          </div>
        </>

      )}
      {!isLoaded && (
        <div>Loading...</div>
      )}
    </>
  )
}

export default ExerciseDetailPage
