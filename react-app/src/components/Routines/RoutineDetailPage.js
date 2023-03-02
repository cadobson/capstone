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
    <>
      {isLoaded && (
        <>
          <div className="routine-detail">
            <div className="routine-detail-text">
              <h1>{routineData.name}</h1>
              <div className="routine-detail-description">{routineData.description}</div>
            </div>
            <div className="routine-detail-sidebar">
              This routine was contributed by {routineData.creator.username}.
              {showOwnerButtons && (
                <>
                  <button className="delete-routine-button">Delete Routine</button>
                  <button className="edit-routine-button">Edit Routine</button>
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

export default RoutineDetailPage