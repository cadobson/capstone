import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import session from './session'
import exercisesReducer from './exercises'
import exerciseReducer from './exercise';
import routinesReducer from './routines';
import routineReducer from './routine';

const rootReducer = combineReducers({
  session,
  exercises: exercisesReducer,
  exercise: exerciseReducer,
  routines: routinesReducer,
  routine: routineReducer,
});


let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
