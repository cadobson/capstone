const SET_EXERCISE = "exercise/SET_EXERCISE";

const setExercise = (exercise) => ({
  type: SET_EXERCISE,
  payload: exercise,
});

export const getExercise = (id) => async (dispatch) => {
  const response = await fetch(`/api/exercises/${id}`);
  if (response.ok) {
    const data = await response.json();
    dispatch(setExercise(data));
  }
  return response;
}

export const createExercise = (name, description) => async (dispatch) => {
  const response = await fetch("/api/exercises/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name,
      description,
    }),
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(setExercise(data));
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ["An error occurred. Please try again."];
  }
};

const exerciseReducer = (state = {}, action) => {
  switch (action.type) {
    case SET_EXERCISE:
      const newState = { ...action.payload };
      return newState;
    default:
      return state;
  }
}

export default exerciseReducer;
