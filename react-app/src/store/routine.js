const SET_ROUTINE = "routines/SET_ROUTINE";
const REMOVE_ROUTINE = "routines/REMOVE_ROUTINE";

const setRoutine = (routine) => ({
  type: SET_ROUTINE,
  payload: routine,
});

const removeRoutine = (routine) => ({
  type: REMOVE_ROUTINE,
  payload: routine,
});

export const getRoutine = (id) => async (dispatch) => {
  const response = await fetch(`/api/routines/${id}`);
  if (response.ok) {
    const data = await response.json();
    dispatch(setRoutine(data));
  }
  return response;
}



const routineReducer = (state = {}, action) => {
  switch (action.type) {
    case SET_ROUTINE: {
      const newState = { ...action.payload };
      return newState;
    }
    case REMOVE_ROUTINE:{
      const newState = { ...action.payload };
      return newState;
    }
    default: {
      return state;
    }
  }
}

export default routineReducer