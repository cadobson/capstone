import { useSelector } from 'react-redux';
import { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux';
import { getPrivateRoutines, getPublicRoutines } from '../../store/routines';
import { useModal } from '../../context/Modal';
import RoutineBlock from './RoutineBlock';

const Routines = () => {
  const routinesData = useSelector((state) => state.routines);
  const [isLoaded, setIsLoaded] = useState(false);
  const currentSessionUser = useSelector((state) => state.session.user);
  const [showPrivateHeader, setShowPrivateHeader] = useState(false);

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getPublicRoutines())
    .then(() => {setIsLoaded(true)})
  }, [dispatch]);

  const handleLoadPrivateRoutines = () => {
    setIsLoaded(false);
    dispatch(getPrivateRoutines())
    .then(() => {setIsLoaded(true)})
    setShowPrivateHeader(true);
  }

  const handleLoadPublicRoutines = () => {
    setIsLoaded(false);
    dispatch(getPublicRoutines())
    .then(() => {setIsLoaded(true)})
    setShowPrivateHeader(false);
  }

  const {setModalContent} = useModal()
  const handleOpenCreateRoutineModal = () => {
    // The redirect to the new routine is inside this modal
    // setModalContent(<CreateRoutineModal />)
    // Does not exist yet
  }

  return (
    <>
      <h1>Routines</h1>
      <div className="load-routines-button-container">
        <button className="load-routines-button" onClick={handleLoadPublicRoutines}>All Public Routines</button>
        {currentSessionUser && <button className="load-routines-button" onClick={handleLoadPrivateRoutines}>My Routines</button>}
        <button className="create-routine-button" onClick={handleOpenCreateRoutineModal}>Create a New Routine</button>
      </div>
      {showPrivateHeader && (
        <>
          <h2>My Routines</h2>
          <div>Only you can see these</div>
          {isLoaded && routinesData.length === 0 && (
            <div>
              You don't have any routines yet. Consider copying an existing routine, or creating a new one!
            </div>
          )}
        </>
      )}
      {!showPrivateHeader && (
        <>
          <h2>All Public Routines</h2>
        </>
      )}
      {isLoaded && routinesData.length > 0 && (
        <div className="routines-container">
          {routinesData.map((routine) => (
            <RoutineBlock routine={routine} key={routine.id} />
          ))}
        </div>
      )}
    </>
  )
}

export default Routines
