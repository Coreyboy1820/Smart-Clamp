import { useState, useEffect } from 'react';

import { getWorkouts } from './util/api/workouts.api';
import { WorkoutsDTO, WorkoutsGETParametersDTO } from './dto/workouts.dto';
import { WORKOUT_FILTERS, CURRENT_USER } from './util/constants';
import Leaderboard from './components/Leaderboard';
import Workouts from './components/Workouts';
import logo from './mini-logo.png';
import './App.css';


function App() {
  const [workoutFilters, setWorkoutFilters] = useState<WorkoutsGETParametersDTO>(WORKOUT_FILTERS);
  const [workouts, setWorkouts] = useState<WorkoutsDTO[] | undefined>([]);
  const sortedLeaderboardWorkouts = workouts?.filter(workout => workout.exercise === workoutFilters.exercise).sort((a, b) => {
    if (a.reps === 0) {
      return 1;
    }
    if (b.reps === 0) {
      return -1;
    }
    if (a.weight === b.weight) {
      return b.reps - a.reps;
    }
    return b.weight - a.weight;
  })

  const filteredUserWorkouts = workouts.filter((workout) => {
    if (workout.exercise === workoutFilters.exercise && workout.created_at.split('T')[0] === workoutFilters.created_at) {
      return workout;
    }
  })
  const user = { username: CURRENT_USER, workouts: workouts.filter(workout => workout.username === CURRENT_USER) }
  const exercises = workouts.map((workout) => workout.exercise).filter((exercise, index, self) => self.indexOf(exercise) === index);
  const exerciseOptions = exercises.map((exercise) => { return (<option key={exercise} value={exercise}>{exercise}</option>) })

  const dateOptions = workouts.map((workout) => workout.created_at.split('T')[0]).filter((created_at, index, self) => self.indexOf(created_at) === index).map((createdAtDate) => { return (<option key={createdAtDate} value={createdAtDate}>{createdAtDate}</option>) })

  useEffect(() => {
    const fetchWorkouts = async () => {
      const allWorkouts = await getWorkouts();
      setWorkouts(allWorkouts);
    }
    fetchWorkouts();
  }, [user.username]);

  return (
    <div>
      <header className="App-header">
        <h1>Smart Clamp</h1>

      </header>
      <main>
        <div className='input-group'>
          <select
            className='dropdown-selector-group'
            name='exercise'
            value={workoutFilters.exercise}
            onChange={(e) => setWorkoutFilters({ ...workoutFilters, [e.target.name]: e.target.value })}
          >
            {exerciseOptions}
          </select>
          <select
            className='dropdown-selector-group'
            name='created_at'
            value={workoutFilters.created_at}
            onChange={(e) => setWorkoutFilters({ ...workoutFilters, [e.target.name]: e.target.value })}
          >
            {dateOptions}
          </select>
        </div>
        <div className='grids'>
          <div className='grid'>
            <Workouts workouts={filteredUserWorkouts} exercise={workoutFilters.exercise} />
          </div>
          <div className='grid'>
            <Leaderboard workouts={sortedLeaderboardWorkouts} exercise={workoutFilters.exercise} />
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
