import { useState, useEffect } from 'react';

import './App.css';
import Workouts from './components/Workouts';
import { WorkoutsDTO } from './dto/workouts.dto';
import { getWorkouts } from './util/api/workouts.api';

function App() {
  const [workouts, setWorkouts] = useState<WorkoutsDTO[] | undefined>([]);
  const user = { username: 'user1' }

  useEffect(() => {
    const fetchWorkouts = async () => {
      const allWorkouts = await getWorkouts(user.username);
      setWorkouts(allWorkouts);
    }
    fetchWorkouts();
  }, [user.username]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Smart Clamp</h1>
      </header>
      <main>
        <Workouts workouts={workouts} />
      </main>
    </div>
  );
}

export default App;
