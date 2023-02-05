export default function Workouts({ workouts, exercise }) {
  const workoutList = workouts.map((workout) => {
    return (
      <div key={workout.id} className="workout">
        <p className="workout-text">{workout.reps} reps x {workout.weight}lbs</p>
      </div>
    )
  })

  return (
    <div >
      <h2> Your Workouts </h2>
      <div>
        {workoutList}
      </div>
    </div>
  )
}
