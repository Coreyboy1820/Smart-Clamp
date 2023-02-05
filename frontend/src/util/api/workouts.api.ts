import { WorkoutsDTO } from "../../dto/workouts.dto";

export async function getWorkouts(username: string) {
    const request_url = `/workouts?username=${username}`;
    const response = await fetch(request_url);
    const workouts: WorkoutsDTO[] = await response.json();
    return workouts;
};