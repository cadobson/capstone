import { useState } from "react"
import { useDispatch } from "react-redux"
import { useHistory } from "react-router-dom"
import { useModal } from "../../context/Modal"
import { createRoutine } from "../../store/routine"


const CreateRoutineModal = () => {
  const dispatch = useDispatch()
  const history = useHistory()

  const [name, setName] = useState()
  const [description, setDescription] = useState()

  const [errors, setErrors] = useState([])
  const {closeModal} = useModal()

  const handleSubmit = async (e) => {
    e.preventDefault()

    setErrors([])
    const newErrors = []
    if (name.length < 1) newErrors.push("Name must not be empty")
    if (description.length < 1) newErrors.push("Description must not be empty")
    if (name.length > 255) newErrors.push("Name must be less than 255 characters")
    if (description.length > 9999) newErrors.push("Description must be less than 10000 characters")
    if (newErrors.length > 0) {
      setErrors(newErrors)
      return
    }

    dispatch(createRoutine(name, description))
      .then((data) => {history.push(`/routines/${data.id}`)})
      .then(() => closeModal())
      .catch((errors) => {
        if (errors) setErrors(errors.message.split(","))
      })
    }


  return (
    <>
      <h1>Create a new Routine</h1>
      <div>You might also consider copying an existing public routine</div>
      <form onSubmit={handleSubmit}>
        <ul>
        {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>
        <label>
          Name
          <input
            placeholder="Routine name"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </label>
        <label>
        Description
          <textarea
            placeholder="Routine description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </label>
        <button type="submit">Create new Routine</button>
      </form>
    </>
  )
}

export default CreateRoutineModal
