import { useState } from "react"
import { useDispatch } from "react-redux"
import { useHistory } from "react-router-dom"


const CreateRoutineModal = () => {
  const dispatch = useDispatch()
  const history = useHistory()
  
  const [name, setName] = useState()
  const [description, setDescription] = useState()


  return (
    <>
      Create Routine Modal
    </>
  )
}

export default CreateRoutineModal