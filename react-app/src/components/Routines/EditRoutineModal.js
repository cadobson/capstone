import {useState} from 'react'
import {useDispatch} from 'react-redux'
import {useHistory} from 'react-router-dom'
import { useModal } from '../../context/Modal'
import {editRoutine} from '../../store/routine'

const EditRoutineModal = ({routineData}) => {
  const dispatch = useDispatch()
  const history = useHistory()
  const [name, setName] = useState(routineData.name)
  const [description, setDescription] = useState(routineData.description)
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


    dispatch(editRoutine(name, description, routineData.id))
      .then(() => {history.push(`/routines/${routineData.id}`)})
      .then(() => {closeModal()})
      .catch(async (res) => {
        const data = await res.json()
        if (data && data.errors) setErrors(data.errors)
      })
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <div>
          {errors.map((error) => (
            <div>{error}</div>
          ))}
        </div>
        <div>
          <label htmlFor="name">Name</label>
          <input
            name="name"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="description">Description</label>
          <input
            name="description"
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </div>
        <button type="submit">Edit Routine</button>
      </form>
    </>
  )
}

export default EditRoutineModal
