import Link from 'react-router-dom/Link'

const Homepage = () => {
  return (
    <>
      <h1>Rep Recorder</h1>
      <div>
        <h2>What is Rep Recorder?</h2>
        <p>Rep Recorder is a web application that allows you to track your exercise performance for your favorite exercises.</p>
        <p>To get started, click on <Link to="/exercises">exercises</Link> to explore exercises to add to your routine, or click on <Link to="/routines">routines</Link> to view and build a routine.</p>

      </div>
    </>
  )
}

export default Homepage
