const SET_EXERCISE = "exercise/SET_EXERCISE";
const REMOVE_EXERCISE = "exercise/REMOVE_EXERCISE";

const setExercise = (exercise) => ({
  type: SET_EXERCISE,
  payload: exercise,
});

const removeExercise = (exercise) => ({
  type: REMOVE_EXERCISE,
  payload: exercise,
})

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
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      throw new Error(data.errors)
    }
  } else {
    throw new Error(["An error occured. Please try again."]);
  }
};

export const deleteExercise = (id) => async (dispatch) => {
  const response = await fetch(`/api/exercises/${id}`, {
    method: "DELETE",
  });
  if (response.ok) {
    dispatch(removeExercise(id));
  }
  return response;
};

export const updateExercise = (name, description, id) => async (dispatch) => {
  const response = await fetch(`/api/exercises/${id}`, {
    method: "PUT",
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
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      throw new Error(data.errors)
    }
  } else {
    throw new Error(["An error occured. Please try again."]);
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
