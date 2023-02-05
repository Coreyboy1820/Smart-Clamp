export default function Workouts({ workouts, exercise }) {
  const workoutList = workouts.map((workout) => {
    return (
      <div key={workout.id} className="workout-set">
        <p >{workout.exercise} {workout.reps} reps x {workout.weight}lbs</p>
      </div>
    )
  })

  return (
    <div>
      <h2> Your {exercise.toUpperCase()} Workouts </h2>
      <div>
        {workoutList}
      </div>
    </div>
  )
}
