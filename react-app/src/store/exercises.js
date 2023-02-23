

const SET_EXERCISES = "exercises/SET_EXERCISES";

const setExercises = (exercises) => ({
  type: SET_EXERCISES,
  payload: exercises,
});

export const getPublicExercises = () => async (dispatch) => {
  const response = await fetch("/api/exercises/public");
  if (response.ok) {
    const data = await response.json();
    dispatch(setExercises(data));
  }
  return response;
}

export const getPrivateExercises = () => async (dispatch) => {
  const response = await fetch("/api/exercises/current");
  if (response.ok) {
    const data = await response.json();
    dispatch(setExercises(data));
  }
  return response;
}




const exercisesReducer = (state = {}, action) => {
  switch (action.type) {
    case SET_EXERCISES:
      const newState = [...action.payload.Exercises];

      return newState;
    default:
      return state;
  }
}

export default exercisesReducer;
