import { useEffect, useState } from "react"
import { useSelector } from "react-redux"
import { useDispatch } from "react-redux"
import { getPublicExercises } from "../../store/exercises"

const Exercises = () => {
  const questionData = useSelector(state => state.exercises.questions)
  const [isLoaded, setIsLoaded] = useState(false)
  const currentSessionUser = useSelector(state => state.session.user)

  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(getPublicExercises())
    .then(() => {setIsLoaded(true)})
  }, [dispatch])


  return (
    <div>
      <h1>Exercises</h1>
    </div>
  )
}

export default Exercises
