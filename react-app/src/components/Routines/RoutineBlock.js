import { useState } from "react";
import { Link } from "react-router-dom";


const RoutineBlock =  ({ routine }) => {
  const {creator_id, description, id, name} = routine
  const [showFullDescription, setShowFullDescription] = useState(false)

  const truncatedDescription = description.length > 200 ? description.substring(0, 197) + "...(click to show more)" : description;

  return (
    <div className="routine-block">
      <div className="routine-block-text">
        <h3>{name}</h3>
        <Link to={`/routines/${id}`}>View Routine Page</Link>
        <div className="routine-block-description" onClick={() => {setShowFullDescription(!showFullDescription)}}>
          {showFullDescription ? description : truncatedDescription}
        </div>
      </div>
    </div>
  )
}

export default RoutineBlock;
