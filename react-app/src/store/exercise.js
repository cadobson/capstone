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