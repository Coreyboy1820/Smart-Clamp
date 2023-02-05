import { useEffect, useState } from 'react'
import { WorkoutsDTO, WorkoutsGETParametersDTO } from '../dto/workouts.dto';
import { WORKOUT_FILTERS } from '../util/constants';

export default function Workouts({ workouts }) {
  const [workoutFilters, setWorkoutFilters] = useState<WorkoutsGETParametersDTO>(WORKOUT_FILTERS);
  const [filteredWorkouts, setFilteredWorkouts] = useState<WorkoutsDTO[] | undefined>([]);
  const exercises = workouts.map((workout) => workout.exercise).filter((exercise, index, self) => self.indexOf(exercise) === index);
  const createdAtDates = workouts.map((workout) => workout.created_at.split('T')[0]).filter((created_at, index, self) => self.indexOf(created_at) === index);

  const exerciseList = exercises.map((exercise) => {
    return (
      <option key={exercise} value={exercise}>{exercise}</option>
    )
  })

  const createdAtDatesList = createdAtDates.map((createdAtDate) => {
    return (
      <option key={createdAtDate} value={createdAtDate}>{createdAtDate}</option>
    )
  })

  const workoutList = filteredWorkouts.map((workout) => {
    return (
      <div key={workout.id} className="workout-set">
        <p >{workout.reps} reps x {workout.weight}lbs</p>
      </div>
    )
  })

  function updateWorkoutFilters(e) {
    setWorkoutFilters({ ...workoutFilters, [e.target.name]: e.target.value })
  }

  useEffect(() => {
    const filteredWorkouts = workouts.filter((workout) => {
      return workout.exercise === workoutFilters.exercise && workout.created_at.split('T')[0] === workoutFilters.created_at
    })
    setFilteredWorkouts(filteredWorkouts);
  }, [workouts, workoutFilters])

  return (
    <div>
      <h2>Workouts</h2>
      <select
        name='exercise'
        value={workoutFilters.exercise}
        onChange={updateWorkoutFilters}
      >
        {exerciseList}
      </select>
      <select
        name='created_at'
        value={workoutFilters.created_at}
        onChange={updateWorkoutFilters}
      >
        {createdAtDatesList}
      </select>
      <h3>Bicep Curls</h3>
      <div>
        {workoutList}
      </div>
    </div>
  )
}
