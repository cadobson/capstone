import { useDispatch } from "react-redux"
import { useHistory } from "react-router-dom"
import { useState } from "react"
import { editExerciseInRoutine } from "../../store/routine"
import { useModal } from "../../context/Modal"

const EditExerciseRoutineModal = ({routineExerciseData, routineId}) => {
  const dispatch = useDispatch()
  const history = useHistory()
  const [instructions, setInstructions] = useState(routineExerciseData.instructions)
  const [setsRepsArray, setSetsRepsArray] = useState(routineExerciseData.sets_reps_array)
  const [errors, setErrors] = useState([])
  const {closeModal} = useModal()

  const handleSubmit = async (e) => {
    e.preventDefault()

    setErrors([])
    const newErrors = []
    if (instructions.length < 1) newErrors.push("Instructions must not be empty")
    if (setsRepsArray.length < 1) newErrors.push("Sets and Reps must not be empty")
    if (instructions.length > 9999) newErrors.push("Instructions must not be more than 10000 characters")
    if (setsRepsArray.length > 255) newErrors.push("Sets and Reps must not be more than 255 characters")
    if (newErrors.length > 0) {
      setErrors(newErrors)
      return
    }

    dispatch(editExerciseInRoutine(routineId, routineExerciseData.id, instructions, setsRepsArray))
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
            required
          />
        </label>
        <label>
          Sets and Reps:
          <input
            placeholder="Sets and Reps"
            type="text"
            value={setsRepsArray}
            onChange={(e) => setSetsRepsArray(e.target.value)}
            required
          />
        </label>
        <button type="submit">Edit Step</button>
      </form>
    </>
  )
}

export default EditExerciseRoutineModal
