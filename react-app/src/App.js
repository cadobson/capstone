import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import Exercises from "./components/Exercises/Exercises";
import ExerciseDetailPage from "./components/Exercises/ExerciseDetailPage";
import Routines from "./components/Routines";
import RoutineDetailPage from "./components/Routines/RoutineDetailPage";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      <div className="main-container">
        <div className="main-content">
          {isLoaded && (
            <Switch>
              <Route path="/login" >
                <LoginFormPage />
              </Route>
              <Route path="/signup">
                <SignupFormPage />
              </Route>
              <Route path="/exercises/:id">
                <ExerciseDetailPage />
              </Route>
              <Route path="/exercises">
                <Exercises />
              </Route>
              <Route path="/routines/:id">
                <RoutineDetailPage />
              </Route>
              <Route path="/routines">
                <Routines />
              </Route>
            </Switch>
          )}
        </div>

      </div>

    </>
  );
}

export default App;
