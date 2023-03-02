import { useParams, useHistory } from "react-router-dom"
import { useSelector, useDispatch } from "react-redux"
import { useState, useEffect } from "react"
import { getRoutine } from "../../store/routine"

const RoutineDetailPage = () => {
  const id = useParams().id
  const routineData = useSelector(state => state.routine)
  const [isLoaded, setIsLoaded] = useState(false)

  const currentSessionUser = useSelector(state => state.session.user)
  const showOwnerButtons = currentSessionUser && currentSessionUser.id === routineData.creator_id

  const dispatch = useDispatch()
  const history = useHistory()

  useEffect(() => {
    dispatch(getRoutine(id))
    .then(() => setIsLoaded(true))
  }, [dispatch])

  return (
    <div>
      <h1>Routine Detail Page</h1>
    </div>
  )
}

export default RoutineDetailPage