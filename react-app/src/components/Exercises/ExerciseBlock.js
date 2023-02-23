import defaultImg from "./no_preview_img.png"

const ExerciseBlock = ({ exercise }) => {
  const { creator_id, description, id, motion_img_url, name} = exercise
  const truncatedDescription = description.length > 100 ? description.substring(0, 97) + "..." : description;
  const imgUrl = motion_img_url ? motion_img_url : defaultImg

  return (
    <div className="exercise-block">
        <div className="exercise-block-description">
          <h3>{name}</h3>
          {truncatedDescription}
        </div>
        <div className="exercise-block-preview-img">
          <img src={imgUrl}/>
        </div>
    </div>
  )
}

export default ExerciseBlock
