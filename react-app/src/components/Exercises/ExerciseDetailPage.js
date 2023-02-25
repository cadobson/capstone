import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from "react-router-dom"
import { getExercise } from "../../store/exercise"

import defaultImg from "./no_preview_img.png"


const ExerciseDetailPage = () => {
  const id = useParams().id
  const exerciseData = useSelector(state => state.exercise)
  const [isLoaded, setIsLoaded] = useState(false)

  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(getExercise(id))
    .then(() => setIsLoaded(true))
  }, [dispatch])

  return (
    <>
      {isLoaded && (
        <>

          <div className="exercise-detail">
            <div className="exercise-detail-text">
              <h1>{exerciseData.name}</h1>
              <div className="exercise-detail-description">{exerciseData.description}</div>
            </div>
            <div className="exercise-detail-preview-img">
              <img src={exerciseData.motion_img_url || defaultImg} alt={`preview of exercise: ${exerciseData.name}`} />
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
