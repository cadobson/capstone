import { useDispatch } from "react-redux"
import { useHistory } from "react-router-dom"
import { useState } from "react"
import { editExerciseInRoutine } from "../../store/routine"
import { useModal } from "../../context/Modal"

const EditExerciseRoutineModal = ({routineExerciseData, routineId}) => {
  const dispatch = useDispatch()
  const history = useHistory()
  const [instructions, setInstructions] = useState(routineExerciseData.instructions || "")
  const [targetSetsCount, setTargetSetsCount] = useState(routineExerciseData.target_sets_count)
  const [targetRepsCount, setTargetRepsCount] = useState(routineExerciseData.target_reps_count)
  const [restSeconds, setRestSeconds] = useState(routineExerciseData.rest_seconds)
  const [errors, setErrors] = useState([])
  const {closeModal} = useModal()

  const handleSubmit = async (e) => {
    e.preventDefault()

    setErrors([])
    const newErrors = []
    if (instructions.length > 9999) newErrors.push("Instructions must not be more than 10000 characters")
    if (targetSetsCount < 1) newErrors.push("Target Sets Count must be greater than 0")
    if (targetRepsCount < 1) newErrors.push("Target Reps Count must be greater than 0")
    if (restSeconds < 0) newErrors.push("Rest Seconds must be greater than or equal to 0")
    if (targetSetsCount > 100) newErrors.push("Havin' yourself a giggle, mate? Target Sets Count must be less than or equal to 100")
    if (targetRepsCount > 100) newErrors.push("Consider cardiovascular exercise instead. Target Reps Count must be less than or equal to 100")
    if (newErrors.length > 0) {
      setErrors(newErrors)
      return
    }

    dispatch(editExerciseInRoutine(routineId, routineExerciseData.id, instructions, targetSetsCount, targetRepsCount, restSeconds))
      .then(() => {history.push(`/routines/${routineExerciseData.routine_id}`)})
      .then(() => {closeModal()})
      .catch((errors) => {
        if (errors) setErrors(errors.message.split(","))
      })
  }

  return (
    <>
      <h1>Edit Step</h1>
      <form onSubmit={handleSubmit}>
        <ul>
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>
        <label>
          Instructions:
          <input
            placeholder="Instructions"
            type="text"
            value={instructions}
            onChange={(e) => setInstructions(e.target.value)}
          />
        </label>
        <label>
          Target Sets Count:
          <input
            placeholder="Target Sets Count"
            type="number"
            value={targetSetsCount}
            onChange={(e) => setTargetSetsCount(e.target.value)}
            required
          />
        </label>
        <label>
          Target Reps Count:
          <input
            placeholder="Target Reps Count"
            type="number"
            value={targetRepsCount}
            onChange={(e) => setTargetRepsCount(e.target.value)}
            required
          />
        </label>
        <label>
          Rest Seconds:
          <input
            placeholder="Rest Seconds"
            type="number"
            value={restSeconds}
            onChange={(e) => setRestSeconds(e.target.value)}
            required
          />
        </label>
        <button type="submit">Edit Step</button>
      </form>
    </>
  )
}

export default EditExerciseRoutineModal
