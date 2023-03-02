

const SET_ROUTINES = "routines/SET_ROUTINES";

const setRoutines = (routines) => ({
  type: SET_ROUTINES,
  payload: routines,
});

export const getPublicRoutines = () => async (dispatch) => {
  const response = await fetch("/api/routines/public");
  if (response.ok) {
    const data = await response.json();
    dispatch(setRoutines(data));
  }
  return response;
}

export const getPrivateRoutines = () => async (dispatch) => {
  const response = await fetch("/api/routines/current");
  if (response.ok) {
    const data = await response.json();
    dispatch(setRoutines(data));
  }
  return response;
}

const routinesReducer = (state = {}, action) => {
  switch (action.type) {
    case SET_ROUTINES:
      const newState = [...action.payload.Routines];

      return newState;
    default:
      return state;
  }
}

export default routinesReducer
