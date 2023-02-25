import { useState } from "react"
import { useDispatch } from "react-redux"
import { useModal } from "../../context/Modal"
import { createExercise } from "../../store/exercise"


function CreateExerciseModal() {
  const dispatch = useDispatch()
  const [name, setName] = useState("")
  const [description, setDescription] = useState("")

  const [errors, setErrors] = useState([])
  const {closeModal} = useModal()

  const handleSubmit = async (e) => {
    e.preventDefault()
    const data = await dispatch(createExercise(name, description))
    if (data) {
      setErrors(data)
    } else {
      closeModal()
    }
  }

  return (
    <>
      <h1>Create a New Exercise</h1>
      <form onSubmit={handleSubmit}>
        <ul>
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>
        <label>
          Name
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </label>
        <label>
          Description
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </label>
        <button type="submit">Create</button>
      </form>
    </>
  )
}

export default CreateExerciseModal
