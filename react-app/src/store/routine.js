const SET_ROUTINE = "routines/SET_ROUTINE";
const REMOVE_ROUTINE = "routines/REMOVE_ROUTINE";
const ADD_EXERCISE_ROUTINE = "routines/ADD_EXERCISE_ROUTINE";

const setRoutine = (routine) => ({
  type: SET_ROUTINE,
  payload: routine,
});

const removeRoutine = (routine) => ({
  type: REMOVE_ROUTINE,
  payload: routine,
});

const addRoutineExercise = (routineExercise) => ({
  type: ADD_EXERCISE_ROUTINE,
  payload: routineExercise,
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

export const editRoutine = (name, description, id) => async (dispatch) => {
  const response = await fetch(`/api/routines/${id}`, {
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

export const addExerciseToRoutine = (routineId, exerciseId, instructions, setsRepsArray) => async (dispatch) => {
  const response = await fetch(`/api/routines/${routineId}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      exercise_id: exerciseId,
      sets_reps_array: setsRepsArray,
      instructions,
    }),
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(addRoutineExercise(data));
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
      //This has the effect of overwriting the state with the payload, but keeping data that is not overwritten by incoming data. This prevents issues with editing name & description vs routine_exercises in different routes
      const newState = {...state, ...action.payload };
      return newState;
    }
    case ADD_EXERCISE_ROUTINE: {
      const newState = { ...state };
      // This is a better option than reloading the entire routine, since it minimizes the amount of data being sent back and forth
      newState.Routine_Exercise.push(action.payload);
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
