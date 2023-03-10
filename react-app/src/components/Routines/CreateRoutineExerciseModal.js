import { useState } from "react"
import { useDispatch } from "react-redux"
import { useHistory, useParams } from "react-router-dom"
import { useModal } from "../../context/Modal"
import { addExerciseToRoutine } from "../../store/routine"

const CreateRoutineExerciseModal = ({routineData}) => {
  const routineId = routineData.id
  const dispatch = useDispatch()
  const history = useHistory()

  const [exerciseId, setExerciseId] = useState(0)
  const [targetSetsCount, setTargetSetsCount] = useState(0)
  const [targetRepsCount, setTargetRepsCount] = useState(0)
  const [restSeconds, setRestSeconds] = useState(0)
  const [instructions, setInstructions] = useState("")
  const [errors, setErrors] = useState([])
  const {closeModal} = useModal()

  const handleSubmit = async (e) => {
    e.preventDefault()

    setErrors([])
    const newErrors = []
    if (exerciseId.length < 1) newErrors.push("Exercise Id must not be empty")
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

    dispatch(addExerciseToRoutine(routineId, exerciseId, instructions, targetSetsCount, targetRepsCount, restSeconds))
      .then(() => closeModal())
      .catch((errors) => {
        if (errors) setErrors(errors.message.split(","))
      })
  }

  return (
    <>
      <h1>Add a Step</h1>
      <form onSubmit={handleSubmit}>
        <ul>
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>
        <label>
          Exercise Id:
          <input
            placeholder="Exercise Id"
            type="number"
            value={exerciseId}
            onChange={(e) => setExerciseId(e.target.value)}
            required
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
        <label>
          Instructions:
          <input
            placeholder="Instructions"
            type="text"
            value={instructions}
            onChange={(e) => setInstructions(e.target.value)}
          />
        </label>
        <button type="submit">Add Step to Routine</button>
      </form>
    </>
  )
}

export default CreateRoutineExerciseModal
