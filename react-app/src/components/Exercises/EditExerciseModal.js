import { useState } from "react"
import { useDispatch } from "react-redux"
import { useHistory } from "react-router-dom"
import { useModal } from "../../context/Modal"
import { updateExercise } from "../../store/exercise"

const EditExerciseModal = ({exerciseData}) => {
  const dispatch = useDispatch()
  const history = useHistory()

  const [newName, setNewName] = useState(exerciseData.name)
  const [newDescription, setNewDescription] = useState(exerciseData.description)

  const [errors, setErrors] = useState([])
  const {closeModal} = useModal()

  const handleSubmit = async (e) => {
    e.preventDefault()

    setErrors([])
    const newErrors = []
    if (newName.length < 1) newErrors.push("Name must not be empty")
    if (newDescription.length < 1) newErrors.push("Description must not be empty")
    if (newName.length > 255) newErrors.push("Name must be less than 255 characters")
    if (newDescription.length > 9999) newErrors.push("Description must be less than 10000 characters")
    if (newErrors.length > 0) {
      setErrors(newErrors)
      return
    }

    dispatch(updateExercise(newName, newDescription, exerciseData.id))
      .then((data) => {history.push(`/exercises/${data.id}`)})
      .then(() => closeModal())
      .catch((errors) => {
        if (errors) setErrors(errors.message.split(","))
      })
  }

  return (
    <>
      <h1>Edit Exercise</h1>
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
            value={newName}
            onChange={(e) => setNewName(e.target.value)}
            required
          />
        </label>
        <label>
          Description
          <textarea
            value={newDescription}
            onChange={(e) => setNewDescription(e.target.value)}
            required
          />
        </label>
        <button type="submit">Edit</button>
      </form>
    </>
  )
}

export default EditExerciseModal
