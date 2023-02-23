import { useState } from "react";
import defaultImg from "./no_preview_img.png"
import { Link } from "react-router-dom";

const ExerciseBlock = ({ exercise }) => {
  const { creator_id, description, id, motion_img_url, name} = exercise
  const [showFullDescription, setShowFullDescription] = useState(false)


  const truncatedDescription = description.length > 400 ? description.substring(0, 397) + "...(click to show more)" : description;
  const imgUrl = motion_img_url ? motion_img_url : defaultImg

  console.log(description)

  return (
    <div className="exercise-block">
        <div className="exercise-block-text">
          <h3>{name}</h3>
          <Link to={`/exercises/${id}`}>View Exercise Page</Link>
          <div className="exercise-block-description" onClick={() => {setShowFullDescription(!showFullDescription)}}>
            {showFullDescription ? description : truncatedDescription}
          </div>
        </div>
        <div className="exercise-block-preview-img">
          <img src={imgUrl} alt={`preview of exercise: ${name}`} />
        </div>
    </div>
  )
}

export default ExerciseBlock
