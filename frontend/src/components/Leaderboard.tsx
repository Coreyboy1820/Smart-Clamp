export default function Leaderboard({ workouts, exercise }) {
    const leaderboardList = workouts.map((workout, index) => {
        return (
            <div key={workout.id} className="workout">

                <p><b>{index + 1} - {workout.username}</b> {workout.reps} reps x {workout.weight}lbs</p>
            </div>
        )
    })

    return (
        <div>
            <h2>Leaderboard</h2>
            {leaderboardList}
        </div>
    )
}
