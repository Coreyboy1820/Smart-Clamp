import { useState, useEffect } from 'react'

export default function Leaderboard({ workouts, exercise }) {
    const leaderboardList = workouts.map((workout, index) => {
        return (
            <div key={workout.id} className="workout-set">
                <h4>{index + 1} - {workout.username}</h4>
                <p>{workout.exercise} {workout.reps} reps x {workout.weight}lbs</p>
            </div>
        )
    })

    return (
        <div>
            <h2>{exercise.toUpperCase()} Leaderboard</h2>
            {leaderboardList}
        </div>
    )
}
