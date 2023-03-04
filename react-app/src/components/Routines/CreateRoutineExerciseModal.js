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
  const [setsRepsArray, setSetsRepsArray] = useState("")
  const [instructions, setInstructions] = useState("")
  const [errors, setErrors] = useState([])
  const {closeModal} = useModal()

  const handleSubmit = async (e) => {
    e.preventDefault()

    setErrors([])
    const newErrors = []
    if (exerciseId.length < 1) newErrors.push("Exercise Id must not be empty")
    if (setsRepsArray.length < 1) newErrors.push("Sets and Reps must not be empty")
    if (setsRepsArray.length > 255) newErrors.push("Sets and Reps must not be more than 255 characters")
    if (instructions.length > 9999) newErrors.push("Instructions must not be more than 10000 characters")
    if (newErrors.length > 0) {
      setErrors(newErrors)
      return
    }

    dispatch(addExerciseToRoutine(routineId, exerciseId, setsRepsArray, instructions))
      // .then((data) => {history.push(`/routines/${data.id}`)})
      .then(() => closeModal())
      .catch(async (errors) => {
        console.log("errors", errors.message)
        if (errors) setErrors([errors.message])
      })
  }

  return (
    <>
      <h1>Create a New Routine Exercise</h1>
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
          Sets and Reps:
          <input
            placeholder="Sets and Reps"
            type="text"
            value={setsRepsArray}
            onChange={(e) => setSetsRepsArray(e.target.value)}
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
            required
          />
        </label>
        <button type="submit">Create Routine Exercise</button>
      </form>
    </>
  )
}

export default CreateRoutineExerciseModal
