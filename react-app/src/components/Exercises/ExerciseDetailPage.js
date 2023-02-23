import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from "react-router-dom"
import { getExercise } from "../../store/exercise"


const ExerciseDetailPage = () => {
    const id = useParams().id
    const exerciseData = useSelector(state => state.exercise)
    const [isLoaded, setIsLoaded] = useState(false)

    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getExercise(id))
        .then(() => setIsLoaded(true))
    }, [dispatch])

    return (
        <>
            <h1>Exercise Detail Page</h1>
            {isLoaded && (
                <div>{exerciseData.name}</div>
            )}
        </>
    )
}

export default ExerciseDetailPage