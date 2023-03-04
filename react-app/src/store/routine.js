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
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      throw new Error(data.errors)
    }
  } else {
    throw new Error(["An error occured. Please try again."]);
  }
  return response;
}

export const createRoutine = (name, description) => async (dispatch) => {
  const response = await fetch("/api/routines/", {
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
    dispatch(setRoutine(data));
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

export const deleteRoutine = (id) => async (dispatch) => {
  const response = await fetch(`/api/routines/${id}`, {
    method: "DELETE",
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(removeRoutine(data));
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

const routineReducer = (state = {}, action) => {
  switch (action.type) {
    case SET_ROUTINE: {
      const newState = { ...action.payload };
      return newState;
    }
    case REMOVE_ROUTINE:{
      const newState = { ...action.payload };
      return {};
    }
    default: {
      return state;
    }
  }
}

export default routineReducer
