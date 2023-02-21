import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
		<div className="nav-holder">

      <NavLink exact to="/">Home</NavLink>
      <NavLink to="/exercises">Exercises</NavLink>
      <NavLink to="/routines">Routines</NavLink>

			{isLoaded && (

        <ProfileButton user={sessionUser} />

			)}
		</div>
	);
}

export default Navigation;
