import React from 'react';
import { NavLink } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import { logout } from '../../store/session';
import { useModal } from '../../context/Modal';
import LoginFormModal from '../LoginFormModal';
import SignupFormModal from '../SignupFormModal';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

  const dispatch = useDispatch();

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
  };


  const { setModalContent } = useModal();
  const handleOpenLoginModal = () => {
    setModalContent(<LoginFormModal />);
  };

  const handleOpenSingupModal = () => {
    setModalContent(<SignupFormModal />);
  };

  let sessionLinks
  if (sessionUser) {
    sessionLinks = (
      <>

        <button className="nav-session-buttons" onClick={handleLogout}>Log Out</button>

      </>
    )
  } else {
    sessionLinks = (
      <>
        <button className="nav-session-buttons" onClick={handleOpenLoginModal}>Login</button>
        <button className="nav-session-buttons" onClick={handleOpenSingupModal}>Sign Up</button>
      </>
    )
  }

	return (
		<div className="nav-holder">

      <NavLink exact to="/">Home</NavLink>
      <NavLink to="/exercises">Exercises</NavLink>
      <NavLink to="/routines">Routines</NavLink>

      {isLoaded && sessionLinks}

			{isLoaded && (
        <>

          <ProfileButton user={sessionUser} />
        </>


			)}
		</div>
	);
}

export default Navigation;
